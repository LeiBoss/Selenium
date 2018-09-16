from selenium import webdriver

import time

driver = webdriver.PhantomJS()
#driver = webdriver.Chrome()

driver.get('https://news.baidu.com')
driver.maximize_window()

body_size = driver.find_element_by_tag_name('body').size
print(body_size['height'])

height = body_size['height']

js= 'window.scrollTo(0,10000)'

driver.execute_script(js)
time.sleep(1)
body_size1= driver.find_element_by_tag_name('body').size
print(body_size1['height'])
height1=body_size1['height']
while (height < height1):
    height = height1
    driver.execute_script(js)
    time.sleep(1)
    body_size2=driver.find_element_by_tag_name('body').size
    height1=body_size2['height']
    print(height)
    print(height1)

print(height)
print(height1)

driver.save_screenshot('test.png')

driver.quit()

