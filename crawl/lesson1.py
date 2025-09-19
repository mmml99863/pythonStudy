from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait#等待页面加载
from selenium.webdriver.support import expected_conditions as EC

#异常报错问题
#from selenium.common.exceptions import NoSuchElementException

if __name__ == '__main__':
    # """提速网页加载"""
    # options = webdriver.ChromeOptions()# 创建一个ChromeOptions对象，用来控制浏览器的启动
    # '''prefs字典，内里数值表示：1代表启动，2代表禁止[禁止：图、表、javascript]'''
    # prefs = {
    #     'profile.default_content_setting_values': {
    #         'images': 2,
    #         'permissions.default_stylesheets': 2,
    #         'javascript': 2
    #     }
    # }
    # options.add_experimental_option('prefs', prefs)#
    # bw = webdriver.Chrome(options=options)

    '''加载网页'''
    bw = webdriver.Chrome()
    bw.maximize_window()# 最大化窗口
    #bw.minimize_window() 最小化窗口
    wait = WebDriverWait(bw, 10)#显示等待:指定等待某个标签加载完成
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "btn-primary")))
    #wait1 = bw.implicitly_wait(10)#隐式等待:等待所有标签加载完成


    url = 'https://www.bilibili.com/v/popular/all?spm_id_from=333.1007.0.0'
    bw.get(url)

    """    
    BY.参数类型
    ID = "id"
    XPATH = "xpath"
    LINK_TEXT = "link text"
    PARTIAL_LINK_TEXT = "partial link text"
    NAME = "name"
    TAG_NAME = "tag name"
    CLASS_NAME = "class name"
    CSS_SELECTOR = "css selector
    """
    data = bw.find_elements( By.CLASS_NAME, 'video-card')
    for item in data:
        print(item.text)