from selenium import webdriver

LOGIN_URL = 'https://www.virtualmanager.com/da/login'
URL = 'https://www.virtualmanager.com/employees/search?utf8=%E2%9C%93&speciality=&country_id=&job_status=&age_min=&age_max=&search=1&commit=S%C3%B8g'

#Function for logging in
def login(credentials):
    browser = webdriver.Chrome()
    browser.get ('https://www.virtualmanager.com/da/login')
    browser.find_element_by_id('email').send_keys(credentials['email'])
    browser.find_element_by_id ('password').send_keys(credentials['password'])
    browser.find_element_by_xpath('//*[@id="content"]/div/div/form/p[4]/input').click()
    while(True):
       pass


#Function for setting email and password
def set_credentials():
    email = input("Enter email: ")
    password = input("Enter password: ")

    result = {
        'email': email,
        'password': password
    }

    return result


if __name__ == '__main__':
    credentials = set_credentials()
    login(credentials)

