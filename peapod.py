#!/usr/bin/env python3
import time
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

import json
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

#BROWSER DRIVER
def attach_to_session(executor_url, session_id):
    original_execute = WebDriver.execute
    def new_command_execute(self, command, params=None):
        if command == "newSession":
            # Mock the response
            return {'success': 0, 'value': None, 'sessionId': session_id}
        else:
            return original_execute(self, command, params)
    # Patch the function before creating the driver object
    WebDriver.execute = new_command_execute
    driver = webdriver.Remote(command_executor=executor_url, desired_capabilities={})
    driver.session_id = session_id
    # Replace the patched function with original function
    WebDriver.execute = original_execute
    return driver

browser = attach_to_session('http://127.0.0.1:64565', '0f7d33f41ad136eca53619564dd0ce81')

browser.get('https://www.peapod.com/')

browser.implicitly_wait(2)

exitButton = browser.find_element_by_class_name('optly-modal-close')
exitButton.click()

cart = browser.find_element_by_class_name('cart-button-content')
cart.click()

checkout = browser.find_element_by_xpath("//button[contains(.,'Checkout')]")
checkout.click()

delivery = browser.find_element_by_xpath("//button[contains(.,'Select')]")
delivery.click()
dates = browser.find_elements_by_class_name("box_date")
checked = [dates[0].text, dates[1].text]

#EMAIL
def sendEmail(date):
    msg = MIMEMultipart()
    message = 'Peapod delivery available on' + date
    msg["Subject"] = "Peapod Availability Alert"
    msg["From"] = "first.last@domain.com"
    msg["To"] = "first.last@domain.com"
    password = "32SD32sdsfn33!sd"
    msg.attach(MIMEText(message, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com: 587')
    server.starttls()
    server.login(msg['From'], password)
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()

#CHECK AND SEND EMAIL

def checkAndSendEmail(dates):
    for date in dates:
        myText = date.text
        if myText not in checked:
            checked.append(myText)
            date.click()
            slots = browser.find_elements_by_class_name('slot_select')
            for slot in slots:
                try:
                    name = slot.text
                    if name != 'Sold Out' and name != '' and name != 'Holiday':
                        print('name')
                        print(name)
                        print('date')
                        print(myText)
                        sendEmail(myText)
                        return
                except:
                    continue
            time.sleep(1)
            print("No time slot on " + myText + ", check next date.")
            checkAndSendEmail(browser.find_elements_by_class_name("box_date"))
            return

checkAndSendEmail(dates)
