#Imports
class DevelopmentConfig():
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'provenusr'
    MYSQL_PASSWORD = 'provenpass'
    MYSQL_DB = 'proyecto-bio'

config = {
    'development':DevelopmentConfig
}