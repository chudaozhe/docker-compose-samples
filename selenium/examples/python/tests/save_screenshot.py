from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")  #以无头模式运行Chrome
chrome_options.add_argument("--no-sandbox")  #取消沙盒模式
chrome_options.add_argument('lang=zh_CN.UTF-8')
chrome_options.add_argument('--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36') #替换User-Agent

driver = webdriver.Remote(
    command_executor='http://localhost:4444',
    options=chrome_options
)

print(driver.execute_script("return navigator.userAgent")) #打印当前的userAgent

driver.get("https://www.sogo.com/")
sleep(1)
element = driver.find_element(By.ID, "query") #定位输入框
element.send_keys("自动化测试haha11", Keys.ENTER) #输入内容并回车
sleep(1)
driver.save_screenshot("sogo.png")
sleep(2)

driver.quit()
