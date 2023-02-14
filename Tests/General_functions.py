import datetime
import json  # working with json dicts
import logging
import pprint
import time
import urllib.request
from datetime import date
import pytest
import requests
from requests.structures import CaseInsensitiveDict
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_location = '/Users/alexdezho/Documents/Personal/chromedriver'

# Items dictionary
item = {
    "Ring": "jewelry-itemType-1",
    "Earrings": "jewelry-itemType-2",
    "Bracelet": "jewelry-itemType-3",
    "Necklace": "jewelry-itemType-4",
    "Watch": "jewelry-itemType-5",
    "Pendant": "jewelry-itemType-6",
    "Chain": "jewelry-itemType-7",
    "Other": "jewelry-itemType-8",
    "Loose stone": "jewelry-itemType-9",
    "Brooch": "jewelry-itemType-10"
}


def soapUI(url, body):
    url = "http://jmtsvc04.jewelersnt.local/ExternalPaymentService/ExternalPayment.svc?singleWsdl"
    headers = {"SOAPAction": "http://tempuri.org/IExternalPayment/PaymentNotification",
               "Content-Type": "text/xml; charset=UTF-8"}
    data = """
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tem="http://tempuri.org/" xmlns:ns="http://jewelersmutual.com/externalpayment/2016/01">
       <soapenv:Header/>
       <soapenv:Body>
          <tem:PaymentNotification>
             <!--Optional:-->
             <tem:request>
                <!--Optional:-->
                <ns:AccountNumber>3000000013</ns:AccountNumber>
                <!--Optional:-->
                <ns:Amount>254.00</ns:Amount>
                <!--Optional:-->
                <ns:ApplicationName>NEW_BUSINESS</ns:ApplicationName>
                <!--Optional:-->
                <ns:AuthorizationCode>123958783</ns:AuthorizationCode>
                <!--Optional:-->
                <ns:CardInfo>
                   <!--Optional:-->
                   <ns:AutoPay>false</ns:AutoPay>
                 
                   <ns:CreditCardExpDate>2018-04-01T00:00:00</ns:CreditCardExpDate>
                   <!--Optional:-->
                   <ns:CreditCardIssuer>Mastercard</ns:CreditCardIssuer>
                   <!--Optional:-->
                   <ns:IsActive>true</ns:IsActive>
                   <!--Optional:-->
                   <ns:LastFourDigits>5454</ns:LastFourDigits>
                </ns:CardInfo>
                <!--Optional:-->
                <ns:PayeeContactInfo>
                   <!--Optional:-->
                   <ns:AddressLine1>safv</ns:AddressLine1>
                   <!--Optional:-->
                   <ns:AddressLine2>vsdavfsad</ns:AddressLine2>
                   <!--Optional:-->
                   <ns:BillingPostalCode>54956</ns:BillingPostalCode>
                   <!--Optional:-->
                   <ns:City>Neenah</ns:City>
                   <!--Optional:-->
                   <ns:Country>US</ns:Country>
                   <!--Optional:-->
                   <!--Optional:-->
                   <ns:EmailAddress>test@test.com</ns:EmailAddress>
                   <!--Optional:-->
                   <ns:FirstName>TEST</ns:FirstName>
                   <!--Optional:-->
                   <ns:LastName>TEST</ns:LastName>
                   <!--Optional:-->
                   <ns:PayeeName>TEST</ns:PayeeName>
                   <!--Optional:-->
                   <ns:PhoneNumber>470-424-7194</ns:PhoneNumber>
                   <!--Optional:-->
                   <ns:State>WI</ns:State>
                </ns:PayeeContactInfo>
                <!--Optional:-->
                <ns:PaymentStatus>ACCEPTED</ns:PaymentStatus>
                <!--Optional:-->
                <ns:ReferenceNumber>578b456A5S3AKKA35965</ns:ReferenceNumber>
                <!--Optional:-->
                <ns:TxnRefNumber>538D85F6J0v5KKK83</ns:TxnRefNumber>
             </tem:request>
          </tem:PaymentNotification>
       </soapenv:Body>
     </soapenv:Envelope>
    """
    resp = requests.post(url, headers=headers, data=data)
    print(resp.status_code)
    print(resp.text)
    return resp.text


def application(driver, value, zipcode, rand_name, rand_name_last, addr, city, phone, email, itemtest):
    time.sleep(2)
    print('Start new application')
    driver.find_element_by_id('QuoteZipCode').click()
    time.sleep(1)
    driver.find_element_by_id('QuoteZipCode').send_keys(zipcode)
    time.sleep(1)
    driver.find_element_by_id(itemtest).click()
    time.sleep(2)
    print('Value & Item')
    driver.find_element_by_xpath('//*[@id="jewelry-itemType-1"]/option[2]').click()
    time.sleep(2)
    driver.find_element_by_id('jewelry-itemValue-1').click()
    time.sleep(1)
    driver.find_element_by_id('jewelry-itemValue-1').send_keys(value)
    time.sleep(2)
    driver.find_element_by_id('quoteInfoNext').click()
    try:
        driver.find_element_by_id('quoteInfoNext').click()
    except:
        print('button not found')
    time.sleep(3)
    driver.find_element_by_id('quoteResultsNext').click()
    time.sleep(3)
    driver.find_element_by_id('noThanks').click()
    time.sleep(2)
    driver.find_element_by_id('customerNext').click()
    time.sleep(3)
    print(rand_name)
    print(rand_name_last)
    driver.find_element_by_id('ApplicantFirstName').click()
    driver.find_element_by_id('ApplicantFirstName').send_keys(rand_name)
    time.sleep(1)
    driver.find_element_by_id('ApplicantLastName').click()
    driver.find_element_by_id('ApplicantLastName').send_keys(rand_name_last)
    time.sleep(1)
    driver.find_element_by_id('ApplicantAddress').click()
    driver.find_element_by_id('ApplicantAddress').send_keys(addr)
    time.sleep(1)
    driver.find_element_by_id('ApplicantCity').click()
    driver.find_element_by_id('ApplicantCity').send_keys(city)
    time.sleep(1)
    driver.find_element_by_id('ApplicantState').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="ApplicantState"]/option[51]').click()
    time.sleep(1)
    driver.find_element_by_id('ApplicantPhoneNumber').click()
    driver.find_element_by_id('ApplicantPhoneNumber').send_keys(phone)
    time.sleep(1)
    driver.find_element_by_id('ApplicantEmailAddress').click()
    driver.find_element_by_id('ApplicantEmailAddress').send_keys(email)
    time.sleep(1)
    driver.find_element_by_id('applicantDOBMonth').click()
    driver.find_element_by_xpath('//*[@id="applicantDOBMonth"]/option[6]').click()
    time.sleep(1)
    driver.find_element_by_id('applicantDOBDay').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="applicantDOBDay"]/option[2]').click()
    time.sleep(1)
    driver.find_element_by_id('applicantDOBYear').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="applicantDOBYear"]/option[28]').click()
    time.sleep(1)
    driver.find_element_by_id('ApplicantGender-Female').click()
    time.sleep(1)
    driver.find_element_by_xpath(
        '//*[@id="mainform"]/div[2]/div[2]/div/div[2]/div/div[1]/div/div/div/label[1]/i').click()
    time.sleep(3)
    print('start of application completed')


def section3(driver):
    print('section 3')
    driver.find_element_by_id('ConvictedOfCrime-Misdemeanor').click()
    time.sleep(1)
    driver.find_element_by_id('SentenceCompletionDate').click()
    time.sleep(1)
    today = date.today()
    d1 = today.strftime("%m/%d/2014")
    print(d1)
    driver.find_element_by_id('SentenceCompletionDate').send_keys(d1)
    time.sleep(3)
    driver.find_element_by_id('ConvictionType').click()
    driver.find_element_by_xpath('//*[@id="ConvictionType"]/option[2]').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="mainform"]/div[3]/div[2]/div[2]/div/div[1]/div/label[1]/i').click()
    time.sleep(1)
    driver.find_element_by_id('HasAgreedToTerms').click()
    time.sleep(100)
    driver.find_element_by_id('applicantNext').click()
    time.sleep(3)

    print('Jewelry Details')
    driver.find_element_by_xpath(
        '//*[@id="jmnfJewelryDetailsForm"]/div[1]/div[2]/div[1]/div/div/div/label[2]/i').click()
    time.sleep(1)
    driver.find_element_by_xpath(
        '//*[@id="jmnfJewelryDetailsForm"]/div[1]/div[2]/div[2]/div/div/div/label[1]/i').click()
    time.sleep(1)
    driver.find_element_by_id('AppraisalDate-JI-1').click()
    driver.find_element_by_id('AppraisalDate-JI-1').send_keys('11/11/2021')
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="HasAlarm-No"]').click()
    time.sleep(1)
    print('The effective date is the current date')
    driver.find_element_by_id('EffectiveDate').click()
    driver.find_element_by_id('EffectiveDate').send_keys(d1)
    time.sleep(1)
    driver.find_element_by_id('jewelryDetailsNext').click()
    time.sleep(3)
    app_num = ""


def body_homepage(driver):
    print('verifying homepage_Body containers')
    time.sleep(3)
    image_whatourpolicyholderssay = driver.find_element_by_id('image-container-8266').is_displayed()
    print(image_whatourpolicyholderssay, " Image is displayed")
    customercareicon = driver.find_element_by_xpath('//img[@alt="customer care graphic"]').is_displayed()
    print(customercareicon, "Icon customer care is displayed")
    print(driver.find_element_by_id('title-46').text)
    print(driver.find_element_by_id('info-grid-8871').text)
    print(driver.find_element_by_id('quote-widget-6401').text)
    print(driver.find_element_by_id('title-151').text)
    print(driver.find_element_by_id('info-grid-136').text)
    print(driver.find_element_by_id('image-container-8251').text)
    print(driver.find_element_by_id('feature-row-141').text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'hero__content hero__content-align-left')]").text)
    time.sleep(3)
    print('homepage_Body - verified')
    return True






