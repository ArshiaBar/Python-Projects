from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

ops=webdriver.ChromeOptions()
ops.add_experimental_option('detach',True)
driver=webdriver.Chrome(options=ops) #executable_path arg
driver.get("https://orteil.dashnet.org/experiments/cookie/")
#print(driver.title)

#find_elements too
#selement=driver.find_element(By.CLASS_NAME,"something") #find_element_by_class_name
#selement=driver.find_element(By.NAME,"something") #name as attribute
#selement=driver.find_element(By.CSS_SELECTOR,".something a") #imagine u see <... class="something"
#selement=driver.find_element(By.ID,"something")
#selement=driver.find_element(By.LINK_TEXT,"something")
#selement=driver.find_element(By.XPATH,'//*[@id="nav-xshop"]/a[4]')
#selement.text
#selement.get_attribute("href")
#selement.size
#selement.click()
#selement.send_keys("blah")
#selement.send_keys("blah",Keys.ENTER)
#selement.send_keys(Keys.ENTER)

cselement=driver.find_element(By.ID, "cookie")

operation_start=int(time.time())
op_start=int(time.time())
while True:
    cselement.click()
    if int(time.time())==operation_start+5:
        money=int(driver.find_element(By.ID,"money").text.replace(",",""))
        aselement = driver.find_elements(By.CSS_SELECTOR, "#store b")
        available=[x for x in aselement if money>=(int(x.text.split(" - ")[1].replace(",","")) if x.text!='' else float("inf"))]
        print(available)
        if available:
            available[-1].click()
        operation_start = int(time.time())
    if int(time.time())==op_start+5*60:
        break

"""
#2 list into a dict example (keys are nums here)
dictt={}

for _ in range(len(list)):
    dictt[_]={"time":list1[_],"title":list2[_]}
"""

#driver.close() #tab
#driver.quit() #browser



#reject_button = driver.find_element(by=By.CSS_SELECTOR, value='button[action-type="DENY"]')

#for recaptcha
#input("Press Enter when you have solved the Captcha")
#hang here and then next lines of code
#another note is sometimes u need to sleep() for loading pages

#phone = driver.find_element(by=By.CSS_SELECTOR, value="input[id*=phoneNumber]") # * means like id could be user_phoneNumber. "phoneNumber" should just be there


'''
#new window
driver.switch_to.window(driver.window_handles[1])
#revert
driver.switch_to.window(driver.window_handles[0])
#the list can have a lot
'''

"""
cookie_warning = self.driver.find_elements(By.XPATH, decline_cookies_xpath)
        if cookie_warning:
            # Dismiss the cookie warning by clicking an element or button
            cookie_warning[0].click()
"""

"""
save_login_prompt = self.driver.find_element(by=By.XPATH, value="//div[contains(text(), 'Not now')]")

handling different xpath with each access
"""

#scrolling down something named modal
#self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
