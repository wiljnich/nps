import urllib.request, json 
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
import time

fp = webdriver.FirefoxProfile()
fp.set_preference("browser.download.folderList", 2)
fp.set_preference("browser.download.dir", "C:\\Users\\YOURNAME\\YOURFOLDER");
fp.set_preference("browser.download.manager.showWhenStarting", False)
fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

def get_park_names():
    with urllib.request.urlopen("https://irma.nps.gov/NPSpecies/Lookup/GetAllUnits") as url:
        data = json.loads(url.read().decode())
    park_names = []
    for x in data:
        park_names.append(x['FullName'])

def get_park_files():
    for park in park_names:
        driver = webdriver.Firefox(firefox_profile=fp)
        driver.get("https://irma.nps.gov/NPSpecies/Search/SpeciesList")
        inputElement = driver.find_element_by_id("nps-npspecies-ux-filterparkcombobox-1011-inputEl")
        inputElement.send_keys(park)
        time.sleep(5)
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB * 7)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        time.sleep(5)
        inputElement = driver.find_element_by_id("button-1058")
        inputElement.click()
        time.sleep(5)
        driver.close()
        
get_park_names()
get_park_files()