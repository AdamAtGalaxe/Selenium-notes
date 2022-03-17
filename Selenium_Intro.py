import requests
import time
from selenium import webdriver
import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

s = Service("/Users/adam/Documents/rando/chromedriver")
driver = webdriver.Chrome(service=s)



def wait():
    url = "https://demoqa.com/alerts"
    driver.get(url)
    driver.maximize_window()

    # implicit wait/between each call/fix race conditions
    driver.implicitly_wait(5)
    element = driver.find_element(By.XPATH, "//*[@id='promtButton']")
    driver.execute_script("arguments[0].scrollIntoView();", element)

    # hard sleep
    time.sleep(5)

    # explicit wait/smart wait
    w = WebDriverWait(driver, 10)
    w.until(expected_conditions.element_to_be_clickable((By.XPATH, "//*[@id='promtButton']")))
    driver.find_element(By.XPATH, "//*[@id='promtButton']").click()
    driver.switch_to.alert.send_keys('test')

def alerts():
    url = "https://demoqa.com/alerts"
    driver.get(url)
    driver.find_element(By.XPATH,"//*[@id='alertButton']").click()
    time.sleep(5)
    alert = driver.switch_to.alert
    alert.accept()
    alert.dismiss()
    time.sleep(5)

def promptBox():
    url = "https://demoqa.com/alerts"
    driver.get(url)
    element = driver.find_element(By.XPATH, "//*[@id='promtButton']")
    driver.execute_script("arguments[0].scrollIntoView();", element)
    element.click()
    time.sleep(5)
    alert2 = driver.switch_to.alert
    alert2.send_keys("test")

    #alert.send_keys('test')
    #alert.c # alert.dismiss()
    time.sleep(5)

def tabSwitch():
    url = "https://www.facebook.com"
    driver.get(url)

    for i in range(1, 6):
        driver.switch_to.new_window()

    handles = driver.window_handles
    len_handles = len(handles)

    for i in range(1,len_handles):
        driver.switch_to.window(handles[i])
        time.sleep(2)

def statusCode():
    #This is problematic..
    url = "https://www.facebook.com"
    r = requests.get(url)
    print(r.status_code)


def noRightClick():
    url = "https://www.facebook.com"
    driver.get(url)
    page_source = driver.page_source
    print(page_source)

    if "fldLoginUserID" in page_source:
        print("got element")
    else:
        print("Nope")

noRightClick()

#Will clean this up I promise!
"""
driver.find_element(By.XPATH, "//*[@id='identifierId']").send_keys("pjamfan671@gmail.com")
driver.find_element(By.XPATH, "//*[@id='identifierNext']/div/button").click()
print(driver.current_url)



page_title = driver.title
if page_title in "Gmail: Free, Private, & Secure Email | Google Workspace":
    print("You are here")
else:
    print("NOPE: " + driver.title)

# driver.quit()

# driver.find_element_by_xpath("//*[@id='email']").send_keys("adam_roberts@gmx.com")
driver.find_element(By.XPATH, "//*[@id='email']").send_keys("adam_roberts@gmx.com")
driver.find_element(By.XPATH, "//*[@id='pass']").send_keys("y$tr5rX&Du&E")
driver.find_element(By.XPATH, "//button[@name='login']").click()

# driver.find_element_by_partial_link_text("password").click()

mylist = driver.find_elements(By.XPATH, "//input")
print(len(mylist))

# for i in range(1, len(mylist)):
# driver.find_elements_by_xpath("(//input)" + [i] +"").send_keys("test")
# driver.find_element(By.XPATH, "(//input)" + [i] +"").send_keys("test")
"""
