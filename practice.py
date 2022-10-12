from selenium import webdriver
from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


serv_obj = Service("C:\\DRIVERS\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome()
driver.get("https://demoblaze.com/index.html")

driver.maximize_window()

login = driver.find_element(By.ID, 'login2').click()

driver.implicitly_wait(10)
# driver.find_element(By.XPATH, './/*[@id="logInModal"]/div/div').click()
username = driver.find_element(By.ID, 'loginusername').send_keys('sctqaautomation@grr.la')
time.sleep(5)
password = driver.find_element(By.ID, 'loginpassword').send_keys("Spring@123")

button = driver.find_element(By.XPATH, "//button[normalize-space()='Log in']").click()

wait = WebDriverWait(driver,10,ignored_exceptions=StaleElementReferenceException)
driver.refresh()
phone = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='list-group']/a[2]"))).click()

#add samsung phone
samsungPhone = driver.find_element(By.XPATH, "//*[@id='tbodyid']/div[1]/div/div/h4/a").click()

addcart = driver.find_element(By.XPATH, "//*[@id='tbodyid']/div[2]/div/a").click()
time.sleep(5)
Alert(driver).accept()

#add laptop
home_menu = driver.find_element(By.XPATH, "//*[@id='navbarExample']/ul/li[1]/a").click()
wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='list-group']/a[3]"))).click()
time.sleep(5)
laptop = driver.find_element(By.XPATH, "//*[@id='tbodyid']/div[4]/div/a").click()
addcart2 = driver.find_element(By.XPATH, "//*[@id='tbodyid']/div[2]/div/a").click()
time.sleep(5)
Alert(driver).accept()

#add monitor
home_menu2 = driver.find_element(By.XPATH, "//*[@id='navbarExample']/ul/li[1]/a").click()
monitors = driver.find_element(By.XPATH, "//div[@class='list-group']/a[4]").click()
asusfullhd = driver.find_element(By.XPATH, "//a[normalize-space()='ASUS Full HD']").click()
addcart3 = driver.find_element(By.XPATH, "//*[@id='tbodyid']/div[2]/div/a").click()
time.sleep(5)
Alert(driver).accept()

#navigate to cart
cart = driver.find_element(By.XPATH, "//*[@id='cartur']").click()

#total order
totalOrder = driver.find_elements(By.XPATH, "//*[@id='tbodyid']/tr")
print('total order:',len(totalOrder))


text_contents = [el.text for el in driver.find_elements(By.XPATH, "//*[@id='tbodyid']/tr")]
# Print text
for txt in text_contents:
    print(txt)

totalPrice = driver.find_element(By.XPATH,"//*[@id='totalp']")
val = totalPrice.get_attribute('value')
print("total price:", val)
#place order
placeOrder = driver.find_element(By.XPATH,"//*[@id='page-wrapper']/div/div[2]/button").click()

name = driver.find_element(By.ID,"name").send_keys("suraj")
country = driver.find_element(By.ID,"country").send_keys("india")
city = driver.find_element(By.ID,"city").send_keys("pune")
creditCart = driver.find_element(By.ID,"card").send_keys("123489")
month = driver.find_element(By.ID,"month").send_keys("april")
year = driver.find_element(By.ID,"year").send_keys("2022")
time.sleep(5)
purchase = driver.find_element(By.XPATH, "//*[@id='orderModal']/div/div/div[3]/button[2]").click()
time.sleep(5)
okbtn = driver.find_element(By.XPATH, "//button[normalize-space()='OK']").click()

driver.quit()


#driver.find_element(By.LINK_TEXT, "Samsung galaxy s6").click()
#homae_menu = driver.find_element(By.XPATH, "//*[@id='navbarExample']/ul/li[1]/a").click()
