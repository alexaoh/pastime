from selenium import webdriver
from os import environ

# Could open firefox headlessly also, using Options. 
from selenium.webdriver.firefox.options import Options

# Check environment variables. 
if 'FUSER' not in environ.keys():
    raise Exception("No feide username found. Create env var: FUSER")

if 'FPASSWORD' not in environ.keys():
    raise Exception("No feide username found. Create env var: FPASSWORD")

USERNAME = environ['FUSER'] # Feide username.
PASSWORD = environ['FPASSWORD'] # Feide PASSWORD.

driver = webdriver.Firefox() # Make a firefox driver. 

driver.get("""https://idp.feide.no/simplesaml/module.php/feide/login?org=ntnu.no&AuthState=_
e2893b9b4ae7a5284839db546276190147699475df%3Ahttps%3A%2F%2Fidp.feide.no%2Fsimplesaml%2Fsaml2%
2Fidp%2FSSOService.php%3Fspentityid%3Durn%253Amace%253Afeide.no%253Aservices%253Ano.ntnu.inns
ida%26RelayState%3Dhttps%253A%252F%252Finnsida.ntnu.no%26cookieTime%3D1597334754""") # Get the url (innsida login)

# Get input fields and submit button. 
username_field = driver.find_element_by_xpath('//*[@id="username"]')
password_field = driver.find_element_by_xpath('//*[@id="password"]')
submit_btn = driver.find_element_by_xpath('/html/body/div/article/section[2]/div[1]/form/button')


# Send username, password and click submit. 
username_field.send_keys(USERNAME)
password_field.send_keys(password)
submit_btn.click()

driver.close() # Close the firefox-window when finished logging in. 
