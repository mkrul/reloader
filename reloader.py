# Reloads the "browser" when it detects changes to the byte size of a user-supplied directory

import os
import time
from selenium import webdriver

def main():
    dir_path = get_file_path()
    port = input("Port number to monitor: ")
    url = "http://localhost:{}/".format(port)
    driver = get_browser()
    driver.get(url)
    while True:
        time.sleep(2)
        driver.refresh()

def get_file_path():
    path_exists = False
    while path_exists == False:
        dir_path = input("Enter the absolute path of the directory: ")
        if os.path.exists(dir_path):
            return dir_path
        else:
            print("Invalid path!")

def get_browser():
    selection = ""
    while selection != "1" or "2":
        browser = input("Type 1 to use Chrome, or 2 to use Firefox: ")
        if browser == "1":
            return webdriver.Chrome(executable_path="./chromedriver.exe")
        elif browser == "2":
            return webdriver.Firefox(executable_path="./geckodriver.exe")
        else:
            print("Invalid choice!")

main()
