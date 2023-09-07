from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import lxml

username = '' # USERNAME HERE
passwd = '' # PASSWORD HERE

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

grades = driver.find_element(By.XPATH, ('//td[2]/form/table/tbody/tr/td/p[4]/a'))
grades.click()

html = driver.page_source
soup =  BeautifulSoup(html, features='lxml')

while True:
    pass