import os
import csv
import time
import random
from typing import List
from urllib.parse import quote

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 使用真实浏览器指纹，无需自定义 headers

def build_driver(headless: bool = False) -> webdriver.Chrome:
    """构建并返回一个 Chrome WebDriver。默认界面化(headless=False)。"""
    chrome_options = Options()
    if headless:
        chrome_options.add_argument('--headless=new')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
    chrome_options.add_experimental_option('useAutomationExtension', False)

    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    return driver


def ensure_dir(path: str):
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
    except Exception:
        pass


def write_rows(dic_path: str, file_name: str, rows: list):
    """追加写入到 CSV；文件不存在或为空时写入表头。
    与现有文件头保持一致：`uri,animal_type`，并按该顺序写入。
    """
    os.makedirs(dic_path, exist_ok=True)
    data_file = os.path.join(dic_path, file_name)
    need_header = not os.path.exists(data_file) or os.path.getsize(data_file) == 0
    with open(data_file, 'a', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        if need_header:
            w.writerow(['uri', 'animal_type'])
        for st, url in rows:
            w.writerow([url, st])


def random_sleep(min_s: float = 1.2, max_s: float = 3.0):
    time.sleep(random.uniform(min_s, max_s))

def print_samples(title: str, items: List[str], limit: int = 3):
    """打印若干条示例数据以便快速验证。"""
    print(f'{title} 示例（最多{limit}条）:')
    for i, it in enumerate(items[:limit], 1):
        print(f'  {i}. {it}')


def print_csv_tail(dic_path: str, file_name: str, tail_lines: int = 3):
    """打印 CSV 文件尾部若干行，便于确认写入结果。"""
    data_file = os.path.join(dic_path, file_name)
    try:
        with open(data_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        tail = lines[-tail_lines:] if len(lines) >= tail_lines else lines
        print('CSV 尾部示例:')
        for ln in tail:
            print('  ' + ln.strip())
    except FileNotFoundError:
        print('CSV 文件尚不存在，暂时无法打印尾部。')


def parse_image_srcs_from_dom(driver) -> List[str]:
    """提取 a 标签下 img 的图片链接（src/data-lazy/srcset）。
    - 主选择器：`a[class^="link--"] img`
    - 回退选择器：`.row-masonry-cell-inner img`
    """
    urls: List[str] = []
    try:
        imgs = driver.find_elements(By.CSS_SELECTOR, 'a[class^="link--"] img')
    except Exception:
        imgs = []
    if not imgs:
        imgs = driver.find_elements(By.CSS_SELECTOR, '.row-masonry-cell-inner img')
    if not imgs:
        imgs = driver.find_elements(By.TAG_NAME, 'img')
    for img in imgs:
        u = img.get_attribute('data-lazy') or img.get_attribute('src')
        if not u:
            srcset = img.get_attribute('srcset') or ''
            parts = [p.strip() for p in srcset.split(',') if p.strip()]
            if parts:
                u = parts[0].split(' ')[0]
        if not u:
            continue
        if u.startswith('//'):
            u = 'https:' + u
        urls.append(u)
    return list(dict.fromkeys(urls))


def crawl_keyword(driver, keyword: str, start_page: int, page_count: int) -> List[str]:
    """为指定关键词抓取若干分页的图片 URL。"""
    origin = 'https://pixabay.com/zh/photos/search/'
    encoded = quote(keyword, safe='')
    all_urls: List[str] = []
    for i in range(start_page, start_page + page_count):
        url = f'{origin}{encoded}/?pagi={i}&'
        print(f'访问: {url}')
        driver.get(url)
        try:
            WebDriverWait(driver, 15).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'a[class^="link--"] img'))
            )
        except Exception:
            pass
        random_sleep(0.8, 2.0)
        page_imgs = parse_image_srcs_from_dom(driver)
        print(f'第 {i} 页提取 {len(page_imgs)} 条图片 src')
        print_samples(f'第 {i} 页', page_imgs, limit=3)
        all_urls.extend(page_imgs)
        random_sleep(1.0, 3.0)
    # 去重
    return list(dict.fromkeys(all_urls))


def crawl():
    # 关键词列表（保持不变）
    search_types = [
        '英短蓝猫', '孟加拉猫', '橘猫', '暹罗猫', '美国短毛猫', '斯芬克斯猫', '缅因猫',
        '比熊犬', '泰迪犬', '雪纳瑞', '巴哥犬', '博美犬', '哈士奇', '萨摩耶', '边境牧羊犬', '柴犬', '金毛寻回犬'
    ]

    # 起始页交互，若失败则默认 1
    try:
        start_page = int(input('请输入开始页码:').strip())
    except Exception:
        start_page = 1

    pages_per_keyword = 3
    driver = build_driver(headless=False)
    try:
        # 预热首页（此处可登录，提升抓取稳定性与额度）
        driver.get('https://pixabay.com/zh/')
        print('已打开首页，你可以在此登录账号以提升抓取稳定性。等待 5 秒…')
        time.sleep(5)

        for st in search_types:
            urls = crawl_keyword(driver, st, start_page, pages_per_keyword)
            print_samples(f'{st} 汇总', urls, limit=5)
            write_rows('animals', 'cat_dog.csv', [(st, u) for u in urls])
            print_csv_tail('animals', 'cat_dog.csv', tail_lines=3)
            print(f'{st}: 收集到 {len(urls)} 条图片 src 并写入 CSV')
    finally:
        try:
            driver.quit()
        except Exception:
            pass


if __name__ == '__main__':
    crawl()


