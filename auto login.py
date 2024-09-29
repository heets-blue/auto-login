from selenium import webdriver

browser = webdriver.Chrome('C:\\Users\\USER\\Desktop\\chromedriver_win32\\chromedriver.exe')

browser.get('https://psbacademyedu.blackboard.com/')

browser.implicitly_wait(3)

agree = browser.find_element_by_class_name('button-1')
agree.click()



id = browser.find_element_by_id('user_id')
id.send_keys('your id')

id = browser.find_element_by_id('password')
id.send_keys('your password')

sign_up = browser.find_element_by_class_name('button.expand.inverse.outline')
sign_up.click()

browser.implicitly_wait(5)

browser.get('https://psbacademyedu.blackboard.com/ultra/course')

#courses = browser.find_element_by_class_name('base-navigation-button-content themed-background-primary-alt-fill-only theme-border-left-active')
#courses.click()
browser.implicitly_wait(3)

crypto = browser.find_element_by_id('course-link-_2893_1')
crypto.click()

browser.implicitly_wait(3)

join1 = browser.find_element_by_id('sessions-list-dropdown')
join1.click()

joinfianl = browser.find_element_by_id('sessions-list')
joinfianl.click()
