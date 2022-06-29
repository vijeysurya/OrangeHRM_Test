from selenium.webdriver.common.by import By


class Login:
    dropdown_myaccount_xpath="//span[@class='caret']"
    lnk_login_xpath="//a[normalize-space()='Login']"
    txt_email_xpath="//input[@id='input-email']"
    txt_password_xpath="//input[@id='input-password']"
    lnk_Actuallogin_xpath="//input[@value='Login']"

    def __init__(self,driver):
        self.driver=driver

    def myaccount(self):
        self.driver.find_element(By.XPATH,self.dropdown_myaccount_xpath).click()

    def login(self):
        self.driver.find_element(By.XPATH,self.lnk_login_xpath).click()

    def email(self,email_in):
        self.driver.find_element(By.XPATH,self.txt_email_xpath).send_keys(email_in)

    def passsword(self,password_in):
        self.driver.find_element(By.XPATH,self.txt_password_xpath).send_keys(password_in)

    def actuallogin(self):
        self.driver.find_element(By.XPATH,self.lnk_Actuallogin_xpath).click()
