import os, random, sys, time
from selenium import webdriver
from bs4 import BeautifulSoup as bs
from pprint import pprint
import csv
import time

def builder_data(builder_name):
    
    # builder_name = "pultegroup"
    browser.get(f'https://www.linkedin.com/company/{builder_name}/about')
    company_name = browser.find_element_by_class_name('org-top-card-summary__title').text
    company_description = browser.find_element_by_class_name('break-words').text
    company_URL = browser.find_element_by_class_name("org-page-details__definition-text").text
    company_industry = browser.find_elements_by_class_name("org-page-details__definition-text")[1].text
    company_size = browser.find_element_by_class_name("org-about-company-module__company-size-definition-text").text
    company_headquarters = browser.find_elements_by_class_name("org-page-details__definition-text")[2].text
    company_type = browser.find_elements_by_class_name("org-page-details__definition-text")[3].text
    company_founded = browser.find_elements_by_class_name("org-page-details__definition-text")[4].text
    company_specialties = browser.find_elements_by_class_name("org-page-details__definition-text")[5].text

    company_dict = {
        "Name": company_name,
        "Description": company_description,
        "URL": company_URL,
        "Industry": company_industry,
        "Size": company_size,
        "Headquarters": company_headquarters,
        "Type": company_type,
        "Founded": company_founded,
        "Specialties": company_specialties
    }
    return company_dict

browser = webdriver.Chrome("chromedriver.exe")
browser.get('https://linkedin.com/uas/login')

file = open('config.txt')
lines = file.readlines()
username = lines[0]
password = lines[1]

elementID = browser.find_element_by_id('username')
elementID.send_keys(username)

elementID = browser.find_element_by_id('password')
elementID.send_keys(password)

elementID.submit()

csv_columns = ['Name', 'URL', 'Founded', 'Headquarters', 'Size', 'Type', 'Specialties', 'Industry', 'Description']
dict_data = []
with open('testdata.csv') as csvfilein:
    readCSV = csv.reader(csvfilein, delimiter=',')
    next(readCSV, None)
    for row in readCSV:
        if row[1]:
            print(row[1])
            time.sleep(2)
            try:
                dict_data.append(builder_data(row[1]))
            except:
                continue


pprint(dict_data)
csv_outfile = "search.csv"
try:
    with open(csv_outfile, 'w+', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in dict_data:
            writer.writerow(data)
except IOError:
    print("I/O error")