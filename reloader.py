# this program reloads the browser when it detects changes to the byte size of a user-supplied directory

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
        size1 = get_size(dir_path)
        time.sleep(2)
        size2 = get_size(dir_path)
        sizes_are_different = compare(size1, size2)
        if sizes_are_different:
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

def get_size(dir_path):
    dir_size = 0
    for (path, dirs, files) in os.walk(dir_path):
        for file in files:
            filename = os.path.join(path, file)
            dir_size += os.path.getsize(filename)
    return dir_size

def compare(size1, size2):
    if size1 != size2:
        return True
    else:
        return False

main()
