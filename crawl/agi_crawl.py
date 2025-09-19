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
    tag_title = bw.find_element(By.CLASS_NAME, "title")
    """在父元素中查找子元素"""
    try:
        tag_varieties = tag_title.find_elements(By.CLASS_NAME, "treeBody")
    except NoSuchElementException as e:
        print("暂未找到该元素", e)
    else:
        print("下一步")






