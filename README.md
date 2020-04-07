Peapod Available Delivery Finder - Selenium

Purpose: Find open slots for peapod delivery and get email notification when they're available. Useful really only when all the slots are full like they are now during coronavirus outbreak.

Instructions (not exhaustive instructions, previous experience with python, terminal, etc required):

Feel free to contribute and create a pull request

Download Selenium Python SDK and choice of driver (I used Chrome), https://pypi.org/project/selenium/

Allow less secure app access your gmail account: https://support.google.com/accounts/answer/6010255 to use smtplib

fill in email and password info in peapod.py

in terminal run: python3 peapod0.py. This starts a browser and prints out two strings needed in peapod.py.

use your credentials to login to peapod and add at least one item. keep this tab open and remain logged in.

in terminal run to test: python3 peapod.py

add cron job as described in that file

common errors:

some browser elements are named by class which change when browser window size changes (i.e a button labeled med might be labled small if window is shrunk). In this case the script won't find the button and it won't be clicked. solution: change the window size to match the correct button name, or make my script more robust and do a pull request.

screensaver, energy effient mode, sleep mode stops the cron jobs. Solution: adjust your settings and keep your device plugged in
