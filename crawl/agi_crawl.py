
from selenium import webdriver
from selenium.webdriver.common.by import By
import csv

"""点击后，页面的details更新"""
def func_click_types(node_obj):
    for obj_item in node_obj:
        obj_item.click()


"""页面的信息存储"""
def info_store(plant_varieties):
    with open('agi_plant_info.csv', mode='w', newline='', encoding='utf-8') as fo:
        # 表头
        header = ['作物分类', '作物名称', '病害', '虫害', '为害症状', "发生因素", "防治方法"]
        writer = csv.DictWriter(fo, header)

        #写入表头
        writer.writeheader()

        #将数据写入文件



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
    # 获取作物分类元素
    tag_varieties = tag_treeBody.find_element(By.CSS_SELECTOR, ".treeNode.haschild")

    # 作物分类
    plant_varieties = []

    for tag_variety in tag_varieties:
        slist = tag_variety.text.splite('\n')
        print(slist)


   # print(plant_varieties)

    # 多植物夫类别 注意此时小类属于tag_variety下
    # for tag_variety in tag_varieties:
        # tag_variety_hide = tag_variety.find_elements(By.CLASS_NAME, "title")
        #
        # # 作物种类入表
        # for tag_variety_hide in tag_variety_hide:
        #     plant_varieties.append(tag_variety_hide.text)#将作物种类加入存储表中
        #
        # # 点击隐藏之后子类显示，details更新
        # for tag_variety_hide in tag_variety_hide:
        #     tag_variety_hide.click()
        #     tag_types = tag_treeBody.find_element(By.CLASS_NAME, "childrens")
        #     tag_types_treeVideBody2 = tag_types.find_element(By.ID, "treeViewBox-2")
        #     tag_types_treeBody = tag_types_treeVideBody2.find_element(By.CLASS_NAME, "treeBody")
        #     tag_types_treeNodes = tag_types_treeBody.find_elements(By.CLASS_NAME, "treeNode")
        #     func_click_types(tag_types_treeNodes)
        #
        #     # details刷新
        #     body_details = bw.find_element(By.CLASS_NAME, "details")
        #     bad_type_list = body_details.find_elements(By.CLASS_NAME, "badTypeList")
        #
        # # 右侧页面查找badItemList
        # for bad_type in bad_type_list:
        #     # 非空判断
        #     if bad_type.find_elements(By.CLASS_NAME, "badItemList"):
        #         # 加载badItemList
        #         bad_item_list = bad_type.find_elements(By.CLASS_NAME, "badItemList")
        #         for bad_item in bad_item_list:
        #             # 点击后弹窗出现
        #             bad_item.click()
        #             body_pop = bw.find_element(By.CLASS_NAME, "pop")
        #             body_pop_details = body_pop.find_element(By.CLASS_NAME, "details")
        #             body_pop_details_content = body_pop_details.find_elements(By.CLASS_NAME, "content")
        #             # pop的病害收集
        #             for item_detail in body_pop_details_content:
        #                 if item_detail.text == "为害症状":
        #                     print("为害症状")
        #                 elif item_detail.text == "发生因素":
        #                     print("发生因素")
        #                 elif item_detail.text == "防治方法":
        #                     print("防治方法")
        #                 else:
        #                     continue
        #             # 关闭弹窗
        #             body_pop_details_close = body_pop_details.find_element(By.CLASS_NAME, "close")
        #             body_pop_details_close.click()
        #             print(bad_item.text.strip())
        #     else:
        #         continue
