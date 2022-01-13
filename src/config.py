class DevelopmentConfig():
    DEBUG = True
    MYSQL_HOST='localhost'
    MYSQL_PORT='33069'
    MYSQL_USER='homestead'
    MYSQL_DATABASE='homestead'
    MYSQL_PASSWORD='secret'


config = {
    'development': DevelopmentConfig
}