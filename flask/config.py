#Imports
class DevelopmentConfig():
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'adminProject'
    MYSQL_PASSWORD = 'admin'
    MYSQL_DB = 'proyecto-bio'

config = {
    'development':DevelopmentConfig
}