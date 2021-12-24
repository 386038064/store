from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Chrome()
driver.get("http://suning.com")

driver.find_element_by_id('searchKeywords').send_keys('钥匙链')

a=driver.find_element_by_name('utf-8_homepagev8_126605238632_word02')
ActionChains(driver).move_to_element(a).perform()#鼠标移动到目标元素
time.sleep(5)#怕网卡没法显示出鼠标悬停

driver.find_element_by_id('searchSubmit').click()

a=driver.window_handles#获取窗口元素
driver.switch_to.window(a[-1])

try:
    driver.find_element_by_class_name('ltrbl').click()
except:
    print('找不到商品进入点')

a=driver.window_handles
driver.switch_to.window(a[-1])
try:
    driver.find_element_by_id('addCart').click()
except:
    print('可能找不到加入购物车')
else:
    print('加入购物车成功')

time.sleep(10)
driver.quit()