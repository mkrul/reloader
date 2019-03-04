# this program reloads the browser when it detects changes to the byte size of a user-supplied directory

import os
import time
from selenium import webdriver
from checksumdir import dirhash

def main():
    dir_path = get_file_path()
    port = input("Port number to monitor: ")
    url = "http://localhost:{}/".format(port)
    browser = get_browser()
    driver = get_os(browser)
    driver.get(url)
    while True:
        hash1 = dirhash(dir_path, "md5")
        time.sleep(2)
        hash2 = dirhash(dir_path, "md5")
        hashes_are_different = compare(hash1, hash2)
        if hashes_are_different:
            driver.refresh()

def get_file_path():
    path_exists = False
    while path_exists == False:
        dir_path = input("Enter the absolute path of the directory: ")
        print(dir_path)
        if os.path.exists(dir_path):
            return dir_path
        else:
            print("Invalid path!")

def get_browser():
    selection = ""
    while selection != "1" or "2":
        browser = input("Type 1 to use Chrome, or 2 to use Firefox: ")
        if browser == "1":
            return "1"
        elif browser == "2":
            return "2"
        else:
            print("Invalid choice!")

def get_os(browser):
    selection = ""
    if browser == "1":
        while selection != "1" or "2":
            operating_system = input("Type 1 if you are using Windows, or 2 for Linux: ")
            if operating_system == "1":
                return webdriver.Chrome(executable_path="./chromedriver.exe")
            elif operating_system == "2":
                return webdriver.Chrome(executable_path="./chromedriver-linux")
            else:
                print("Invalid choice!")
    if browser == "2":
        while selection != "1" or "2":
            operating_system = input("Type 1 if you are using Windows, or 2 for Linux: ")
            if operating_system == "1":
                return webdriver.Firefox(executable_path="./geckodriver.exe")
            elif operating_system == "2":
                return webdriver.Firefox(executable_path="./geckodriver-linux")
            else:
                print("Invalid choice!")

def compare(hash1, hash2):
    if hash1 != hash2:
        return True
    else:
        return False

main()
