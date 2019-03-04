# reloader
Don't want to go through the trouble of configuring build tools?  Reloader is a simple live reloading solution.  It works by polling a user-supplied directory every 2 seconds, generating an md5 hash of the directory, and comparing the checksum with the value that it calculated 2 seconds prior.  If the checksums are different, the selenium driver reloads the browser window for you.

# How to use:
1) download the repository to your local machine
3) install the following python packages:
    - selenium
    - checksumdir
2) grant execute permissions on the following files inside of /reloader:
    - geckodriver.exe
    - chromedriver.exe
    - geckodriver-linux
    - chromedriver-linux
3) now you may run the program
4) when prompted, enter the absolute path to the directory you want to monitor
5) enter the port number that you wish to use
6) select an operating system (TODO: add support for mac OS)
7) selenium webdriver should boot up and begin monitoring the directory
