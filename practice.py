from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

import time


serv_obj = Service("C:\\DRIVERS\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://demoblaze.com/index.html")

driver.maximize_window()

login = driver.find_element(By.ID, 'login2')
login.click()
driver.implicitly_wait(10)

username = driver.find_element(By.ID, 'loginusername')
username.send_keys('sctqaautomation@grr.la')
time.sleep(5)
password = driver.find_element(By.ID, 'loginpassword')
password.send_keys("Spring@123")

button = driver.find_element(By.XPATH, "//button[normalize-space()='Log in']")
button.click()

time.sleep(10)
phone = driver.find_element(By.XPATH, "//div[@class='list-group']/a[2]")
phone.click()

# add samsung phone
samsungPhone = driver.find_element(By.XPATH, "//*[@id='tbodyid']/div[1]/div/div/h4/a")
samsungPhone.click()
addCart = driver.find_element(By.XPATH, "//*[@id='tbodyid']/div[2]/div/a")
addCart.click()
time.sleep(10)
Alert(driver).accept()

# add laptop
home_menu = driver.find_element(By.XPATH, "//*[@id='navbarExample']/ul/li[1]/a")
home_menu.click()
laptops = driver.find_element(By.XPATH, "//div[@class='list-group']/a[3]")
laptops.click()
time.sleep(5)
laptop = driver.find_element(By.XPATH, "//*[@id='tbodyid']/div[4]/div/a")
laptop.click()
addCart2 = driver.find_element(By.XPATH, "//*[@id='tbodyid']/div[2]/div/a")
addCart2.click()
time.sleep(5)
Alert(driver).accept()

# add monitor
home_menu2 = driver.find_element(By.XPATH, "//*[@id='navbarExample']/ul/li[1]/a")
home_menu2.click()
time.sleep(5)
monitors = driver.find_element(By.XPATH, "//div[@class='list-group']/a[4]")
monitors.click()
asusFullhd = driver.find_element(By.XPATH, "//a[normalize-space()='ASUS Full HD']")
asusFullhd.click()
addCart3 = driver.find_element(By.XPATH, "//*[@id='tbodyid']/div[2]/div/a")
addCart3.click()
time.sleep(5)
Alert(driver).accept()

# navigate to cart
cart = driver.find_element(By.XPATH, "//*[@id='cartur']")
cart.click()

# total order
totalOrder = driver.find_elements(By.XPATH, "//*[@id='tbodyid']/tr")
print('total order:', len(totalOrder))

# sorted list
text_name = [el.text for el in driver.find_elements(By.XPATH, "//*[@id='tbodyid']/tr/td[3]")]
text_name1 = sorted(text_name)
print("sorted list:", text_name1)

text_contents = [el.text for el in driver.find_elements(By.XPATH, "//*[@id='tbodyid']/tr/td[3]")]


# Print text
total = 0
for ele in range(0, len(text_contents)):
    total = total + int(text_contents[ele])

print("total", total)

exp_value = driver.find_element(By.XPATH, "//*[@id='totalp']")

print("expected value:", exp_value.text)
time.sleep(5)
if int(total) == int(exp_value.text):
    print("total matched")
else:
    print("total not matched")

# printing total value
print("Sum of all elements in given list: ", total)

# place order
placeOrder = driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div/div[2]/button")
placeOrder.click()

name = driver.find_element(By.ID, "name")
name.send_keys("suraj")
country = driver.find_element(By.ID, "country")
country.send_keys("india")
city = driver.find_element(By.ID, "city")
city.send_keys("pune")
time.sleep(3)
creditCart = driver.find_element(By.ID, "card")
creditCart.send_keys("123489")
month = driver.find_element(By.ID, "month")
month.send_keys("april")
year = driver.find_element(By.ID, "year")
year.send_keys("2022")
time.sleep(5)
purchase = driver.find_element(By.XPATH, "//*[@id='orderModal']/div/div/div[3]/button[2]")
purchase.click()
time.sleep(5)

ids = driver.find_element(By.XPATH, "/html/body/div[10]/p").text
idList = ids.split(":")[0:3]
idJoin = ":".join(idList).strip("\nCard Number")
print("id and amount:", idJoin)

time.sleep(5)
okBtn = driver.find_element(By.XPATH, "//button[normalize-space()='OK']")
okBtn.click()

driver.quit()

