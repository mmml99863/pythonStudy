import os
import csv
import time
import random
import re
from urllib.parse import urlparse
from urllib.request import Request, urlopen


def ensure_dir(path: str):
    os.makedirs(path, exist_ok=True)


def sanitize_filename(name: str) -> str:
    """移除 Windows 非法字符并做简单裁剪。"""
    name = re.sub(r'[\\/:*?"<>|]', '_', name)
    return name[:80] if len(name) > 80 else name


def guess_ext_from_url_and_headers(url: str, content_type: str | None) -> str:
    """根据 URL 和响应头推断扩展名，默认 .jpg。"""
    path = urlparse(url).path
    _, ext = os.path.splitext(path)
    if ext and len(ext) <= 5:
        return ext.lower()
    ct = (content_type or '').lower()
    if 'image/png' in ct:
        return '.png'
    if 'image/webp' in ct:
        return '.webp'
    if 'image/gif' in ct:
        return '.gif'
    return '.jpg'


def download_images_from_csv(csv_path: str = 'animals/cat_dog.csv', out_dir: str = 'animals/images'):
    """按“类别+i”命名从 CSV 批量下载图片。CSV 需为两列：uri,animal_type。
    保存目录默认为 animals/images。"""
    ensure_dir(out_dir)

    # 读取 CSV
    rows = []
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader, None)
        # 兼容可能没有表头或顺序颠倒的情况
        has_header = header and len(header) >= 2 and header[0].lower() == 'uri'
        if not has_header:
            # 第一行也作为数据行处理
            if header:
                rows.append(header)
        for r in reader:
            if len(r) >= 2:
                rows.append([r[0].strip(), r[1].strip()])

    # 逐类别计数命名
    counters: dict[str, int] = {}
    ok, fail = 0, 0
    samples_saved: list[str] = []

    for url, animal in rows:
        if not url:
            fail += 1
            continue
        if url.startswith('//'):
            url = 'https:' + url

        # 递增序号
        key = animal or '未知类别'
        counters[key] = counters.get(key, 0) + 1
        idx = counters[key]

        # 发送请求
        req = Request(url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36'
        })
        try:
            with urlopen(req, timeout=30) as resp:
                data = resp.read()
                content_type = resp.headers.get('Content-Type')
        except Exception:
            fail += 1
            # 遇到错误不阻塞，继续下一个
            continue

        ext = guess_ext_from_url_and_headers(url, content_type)
        base_name = sanitize_filename(f"{key}{idx}")
        file_path = os.path.join(out_dir, base_name + ext)

        # 若文件已存在，递增直到可用
        while os.path.exists(file_path):
            idx += 1
            counters[key] = idx
            base_name = sanitize_filename(f"{key}{idx}")
            file_path = os.path.join(out_dir, base_name + ext)

        try:
            with open(file_path, 'wb') as wf:
                wf.write(data)
            ok += 1
            if len(samples_saved) < 5:
                samples_saved.append(os.path.basename(file_path))
        except Exception:
            fail += 1
            continue

        time.sleep(random.uniform(0.2, 0.6))

    # 总结输出
    print(f"下载完成：成功 {ok}，失败 {fail}。保存目录：{os.path.abspath(out_dir)}")
    if samples_saved:
        print("示例已保存文件：")
        for i, name in enumerate(samples_saved, 1):
            print(f"  {i}. {name}")


if __name__ == '__main__':
    download_images_from_csv()