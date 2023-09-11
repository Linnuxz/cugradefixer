from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


username = ''  # USERNAME HERE
passwd = ''  # PASSWORD HERE

driver = webdriver.Chrome()

driver.get('https://programs.cu.edu.ge/cu/loginStud')

txtUsername = driver.find_element(
    By.XPATH, ('//div[@class="form-group"][2]/input'))
txtUsername.click()
txtUsername.send_keys(username)

txtPasswd = driver.find_element(
    By.XPATH, ('//div[@class="form-group last"]/input'))
txtPasswd.click()
txtPasswd.send_keys(passwd)

btnLogin = driver.find_element(
    By.XPATH, ('//button[@class="btn btn-default bd50"]'))
btnLogin.send_keys(Keys.RETURN)

profile = driver.find_element(By.XPATH, ('//a[@class="style732"][1]'))
profile.click()

gradesPage = driver.find_element(
    By.XPATH, ('//td[2]/form/table/tbody/tr/td/p[4]/a'))
gradesPage.click()

newURl = driver.window_handles[0]

driver.switch_to.window(newURl)

percentage = '100.00'
gpa = '4.00'

for i in range(2, 14):
    percentagePath = driver.find_element(
        By.XPATH, ('//tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr[' + str(i) + ']/td[5]/input'))
    gradePath = driver.find_element(
        By.XPATH, ('//tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr[' + str(i) + ']/td[6]'))
    driver.execute_script("arguments[0].innerText = 'A'", gradePath)
    percentagePath.clear()
    percentagePath.send_keys(percentage)
    gpaPath = driver.find_element(
        By.XPATH, ('//tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr[' + str(i) + ']/td[7]'))
    driver.execute_script("arguments[0].innerText = '4.00'", gpaPath)


for i in range(15, 17):
    gpaChart = driver.find_element(
        By.XPATH, ('//tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr[' + str(i) + ']/td[2]/input'))
    gpaChart.clear()
    gpaChart.send_keys(percentage)
    gpaChart = driver.find_element(
        By.XPATH, ('//tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr[' + str(i) + ']/td[3]/input'))
    gpaChart.clear()
    gpaChart.send_keys(gpa)


for i in range(17, 23):
    percentagePath = driver.find_element(
        By.XPATH, ('//tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr[' + str(i) + ']/td[5]/input'))
    gradePath = driver.find_element(
        By.XPATH, ('//tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr[' + str(i) + ']/td[6]'))
    driver.execute_script("arguments[0].innerText = 'A'", gradePath)
    percentagePath.clear()
    percentagePath.send_keys(percentage)
    gpaPath = driver.find_element(
        By.XPATH, ('//tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr[' + str(i) + ']/td[7]'))
    driver.execute_script("arguments[0].innerText = '4.00'", gpaPath)


for i in range(24, 27, 2):
    gpaChart = driver.find_element(
        By.XPATH, ('//tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr[' + str(i) + ']/td[2]/input'))
    gpaChart.clear()
    gpaChart.send_keys(percentage)
    gpaChart = driver.find_element(
        By.XPATH, ('//tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr[' + str(i) + ']/td[3]/input'))
    gpaChart.clear()
    gpaChart.send_keys(gpa)


# to keep the browser open
input()
