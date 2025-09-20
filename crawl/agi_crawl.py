from codecs import BOM
from os import popen
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


if __name__ == '__main__':
    bw = webdriver.Chrome()
    bw.maximize_window()

    '''页面加载'''
    url = "https://farm.sino-eco.com/website/bingchonghai/"
    bw.get(url)
    bw.implicitly_wait(3)

    """定位父元素"""
    tag_title = bw.find_element(By.CLASS_NAME, "childrens")
    tag_treeViewBox = tag_title.find_element(By.CLASS_NAME, "treeViewBox")
    tag_treeBody = tag_treeViewBox.find_element(By.CLASS_NAME, "treeBody")
    # 使用 CSS 选择器获取同时包含两个 class 的同级元素集合
    # By.CLASS_NAME 只能接收单个 class 名，多个 class 应使用 CSS 选择器
    tag_varieties = tag_treeBody.find_elements(By.CSS_SELECTOR, ".treeNode.haschild")
    for tag in tag_varieties:
        tag.click()
        body_details = bw.find_element(By.CLASS_NAME, "details")
        bad_type_list = body_details.find_elements(By.CLASS_NAME, "badType")
        for bad_type in bad_type_list:
            if bad_type.find_element(By.CLASS_NAME, "badItemList"):
                bad_item_list = bad_type.find_elements(By.CLASS_NAME, "badItemList")
                for bad_item in bad_item_list:
                    """点击后弹窗出现"""
                    bad_item.click()
                    body_pop = bw.find_element(By.CLASS_NAME, "pop")
                    body_pop_details = body_pop.find_elements(By.CLASS_NAME, "details")
                    body_pop_details_content = body_pop_details.find_elements(By.CLASS_NAME, "content")
                    for item_detail in body_pop_details_content:
                        if item_detail.text == "为害症状":
                            print("为害症状")
                        elif item_detail.text == "发生因素":
                            print("发生因素")
                        elif item_detail.text == "防治方法":
                            print("防治方法")
                        else:
                            continue
                    body_pop_details_close = body_pop_details.find_element(By.CLASS_NAME, "close")
                    body_pop_details_close.click()
            else:
                continue

    # """在父元素中查找子元素"""
    # try:
    #     tag_varieties = tag_title.find_elements(By.ID, "crop_1")
    # except NoSuchElementException as e:
    #     print("暂未找到该元素", e)
    # else:
    #     for tag in tag_varieties:
    #         print(tag.text)






