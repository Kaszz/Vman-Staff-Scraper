from selenium import webdriver


def init_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('log-level=3')
    driver = webdriver.Chrome(options=options)
    return driver

#Function for getting email and password
def get_credentials():
    email = input("Enter email: ")
    password = input("Enter password: ")

    result = {
        'email': email,
        'password': password
    }
    return result

#Function for logging in
def login(driver, credentials):
    driver.get('https://www.virtualmanager.com/da/login')
    driver.find_element_by_id('email').send_keys(credentials['email'])
    driver.find_element_by_id ('password').send_keys(credentials['password'])
    driver.find_element_by_xpath('//*[@id="content"]/div/div/form/p[4]/input').click()


#Function for getting trainer parameters
def get_staff_params():
    speciality = input("Speciality [coach, scout]: ")
    job_status = input("Jobstatus | Unemployed [1] | Contracted [2]: ")
    max_age = input("Max age: ")

    result = {
        'speciality': speciality,
        'job_status': job_status,
        'max_age': max_age
    }
    return result


def scrape(driver, params):
    driver.get('https://www.virtualmanager.com/employees/search?utf8=%E2%9C%93&speciality=' + params['speciality'] + '&country_id=&job_status=' + params['job_status'] + '&age_min=&age_max=' + params['max_age'] + '&search=1&commit=S%C3%B8g')
    


if __name__ == '__main__':
    driver = init_driver()

    credentials = get_credentials()
    login(driver, credentials)

    params = get_staff_params()
    scrape(driver, params)

    while(True):
        pass

