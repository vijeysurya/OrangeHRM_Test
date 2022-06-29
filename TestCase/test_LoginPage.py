import time

import pytest
from PageObject.LoginPage import Login
from Utilities.readProperties import Config
from Utilities.log import LogGen

class Test_loginPage:
    email=Config.email_config()
    password=Config.password_config()
    basurl=Config.baseurl_config()
    logger=LogGen.loggen()

    def test_tc001_homepagetitle(self,setup):
        self.logger.info("**** test_tc001_homepagetitle started ****")
        driver=setup
        driver.get(self.basurl)
        act_homepagetitle=driver.title
        self.logger.info("**** Verifying homepage title started ****")
        if act_homepagetitle=="Your Store":
            self.logger.info("**** Homepage title matched****")
            driver.close()
            assert True
        else:
            self.logger.info("**** Homepage title not matched****")
            driver.save_screenshot("/Users/vijeysurya/PycharmProjects/pythonProject1/OrangeHRM_Test/Screenshots/test_tc001_homepagetitle.png")
            driver.close()
            assert False
        self.logger.info("**** Verifying homepage title completed ****")
        self.logger.info("**** test_tc001_homepagetitle completed ****")
    def test_tc002_login(self,setup):
        self.logger.info("**** test_tc002_login started ****")
        driver=setup
        driver.get(self.basurl)
        lc=Login(driver)
        lc.myaccount()
        lc.login()
        act_logintitle=driver.title
        if act_logintitle=="Account Login":
            assert True
            lc.email(self.email)
            lc.passsword(self.password)
            lc.actuallogin()
            act_loginlandingtitle=driver.title
            if act_loginlandingtitle=="My Account":
                assert True
                driver.close()
            else:
                driver.save_screenshot("/Users/vijeysurya/PycharmProjects/pythonProject1/OrangeHRM_Test/Screenshots/test_tc002_loginlandingtitle.png")
                driver.close()
                assert False
        else:
            driver.save_screenshot("/Users/vijeysurya/PycharmProjects/pythonProject1/OrangeHRM_Test/Screenshots/test_tc002_loginlandingtitle.png")
            driver.close()
            assert False
        self.logger.info("**** test_tc002_login completed ****")










