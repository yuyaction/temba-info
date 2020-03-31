# coding: UTF-8
import time,datetime
from selenium import webdriver


login_id = 'hogehoge@gmail.com'
pas = '********'

#Headless mode
options = webdriver.chrome.options.Options()
options.add_argument('--headless')
options.add_argument('--lang=ja-JP')
#local mode
#driver = webdriver.Chrome(executable_path='./chromedriver' , chrome_options = options)
#heroku mode
driver = webdriver.Chrome(executable_path='./.chromedriver/bin/chromedriver', chrome_options = options)

#google login
driver.get('https://accounts.google.com')
time.sleep(1.5)
driver.find_element_by_xpath("//*[@id='identifierId'] | //*[@id='Email']").send_keys(login_id)
driver.find_element_by_xpath("//*[@id='identifierNext'] | //*[@id='next']").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='password'] | //*[@id='Passwd']").send_keys(pas)
driver.find_element_by_xpath("//*[@id='passwordNext'] | //*[@id='signIn']").click()
time.sleep(10)

#Mymap
driver.get('--- URL of Mymap ---')
time.sleep(10)
element = driver.find_element_by_id("map-action-add-layer")
element.click()
time.sleep(10)
element = driver.find_element_by_id("ly1-layerview-import-link")
element.click()

iframe = driver.find_element_by_class_name('fFW7wc-OEVmcd')
driver.switch_to_frame(iframe)
time.sleep(5)

element = driver.find_element_by_xpath("//*[text()='Google ドライブ']")
element.click()
time.sleep(2)
element = driver.find_element_by_xpath("//*[text()='Mymap作成用']")
element.click()
time.sleep(2)
element = driver.find_element_by_id("picker:ap:2")
element.click()
time.sleep(3)
driver.switch_to.default_content()

element = driver.find_element_by_xpath('//*[@id="upload-checkbox-1"]/span/div')
element.click()
time.sleep(2)
element = driver.find_element_by_xpath('/html/body/div[9]/div[3]/button[1]')
element.click()
time.sleep(2)
element = driver.find_element_by_xpath('//*[@id="upload-radio-0"]/div/span[1]')
element.click()
time.sleep(2)
element = driver.find_element_by_xpath('/html/body/div[7]/div[3]/button[1]')
element.click()
time.sleep(10)

#delete old layer
element = driver.find_element_by_xpath('//*[@id="ly0-layer-header"]/div[3]')
element.click()
time.sleep(2)
element = driver.find_element_by_xpath('//*[text()="このレイヤを削除"]')
element.click()
time.sleep(2)
element = driver.find_element_by_xpath('//*[@id="cannot-undo-dialog"]/div[3]/button[1]')
element.click()
time.sleep(5)

#change the name of the new layer 
element = driver.find_element_by_xpath('//*[@id="ly1-layer-header"]/div[3]')
element.click()
time.sleep(2)
element = driver.find_element_by_xpath('//*[text()="このレイヤの名前を変更"]')
element.click()
time.sleep(2)
time_now = datetime.datetime.now()
time_now = '{0:%Y/%m/%d %H:%M}'.format(time_now)
driver.find_element_by_xpath('//*[@id="update-layer-name"]/div[2]/input').send_keys(time_now)
element = driver.find_element_by_xpath('//*[@id="update-layer-name"]/div[3]/button[1]')
element.click()
time.sleep(2)


time.sleep(8)
#driver.quit()
