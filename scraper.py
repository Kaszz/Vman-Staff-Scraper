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
    driver.find_element_by_id('password').send_keys(credentials['password'])
    driver.find_element_by_xpath('//*[@id="content"]/div/div/form/p[4]/input').click()


#Function for getting trainer parameters
def get_staff_params():
    speciality = input("Speciality [coach, scout]: ")
    job_status = input("Jobstatus | Unemployed [1] | Contracted [2]: ")
    max_age = input("Max age: ")
    youth = input("Minimum youth training skills: ")
    keeper = input("Minimum keeper training skills: ")
    outfield = input("Minimum outfield training skills: ")

    result = {
        'speciality': speciality,
        'job_status': job_status,
        'max_age': max_age,
        'youth': youth,
        'keeper': keeper,
        'outfield': outfield
    }
    return result

#Scraper functions that loops through staffers untill criteria is met
def scrape(driver, params):
    driver.get('https://www.virtualmanager.com/employees/search?utf8=%E2%9C%93&speciality=' + params['speciality'] + '&country_id=&job_status=' + params['job_status'] + '&age_min=&age_max=' + params['max_age'] + '&search=1&commit=S%C3%B8g')
    
    staff_found = False

    #Loops while no staffer is found with fitting skills
    while not staff_found:
        #Get table and loop through the rows to find relevant data
        table = driver.find_elements_by_xpath('//*[@id="content"]/div[1]/div[2]/div[1]/table/tbody/tr')
        for row in table[1:]:
            #Get skills of staffer and compare them to wants
            skillString = row.find_element_by_xpath(".//td[last()]/div/img").get_attribute('onmouseover')
            skills = skillString.split(", ")
            youth = int(skills[1])
            keeper = int(skills[2])
            outfield = int(skills[3])

            #If wants are met print link to staffer
            if ( (youth >= int(params['youth'])) and (keeper >= int(params['keeper'])) and (outfield >= int(params['outfield'])) ):
                print(row.find_element_by_xpath(".//td[2]/a").get_attribute('href'))
                staff_found = True
        
        #Goes to next page
        driver.find_element_by_class_name('next_page').click()


def main():
    driver = init_driver()

    credentials = get_credentials()
    login(driver, credentials)

    params = get_staff_params()
    scrape(driver, params)


main()