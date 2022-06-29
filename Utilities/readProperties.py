import configparser

config = configparser.RawConfigParser()
config.read("/Users/vijeysurya/PycharmProjects/pythonProject1/OrangeHRM_Test/Configurations/config.ini")
class Config:
    @staticmethod
    def email_config():
        email=config.get('common info','email')
        return email

    @staticmethod
    def password_config():
        password=config.get('common info','password')
        return password

    @staticmethod
    def baseurl_config():
        baseurl=config.get('common info','baseurl')
        return baseurl
