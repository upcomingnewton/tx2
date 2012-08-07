#LogHandlers.py
ADMINS = (
    # ('Your Name', 'your_email@example.com'),
      ('thoughtxplore','thoughtxplore@gmail.com'),
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = LOG_SETTINGS = {
    'version': 1,
    'loggers':{
               'LOGGER_Security':{
                                    #'handlers':['File_Security','smtp'],
                                    'handlers':['File_Security','smtp_Security'],
                                    'level':'DEBUG',
                                },
               'LOGGER_Query':{
                                    #'handlers':['File_Query','smtp'],
                                    'handlers':['File_Query','smtp_Query'],
                                    'level':'DEBUG',
                                },
               'LOGGER_User':{
                                    #'handlers':['File_User','smtp'],
                                    'handlers':['File_User','smtp_User'],
                                    'level':'DEBUG',
                                },
               'SYSTEM_INITIALISE_LOGGER':{
                                    #'handlers':['File_User','smtp'],
                                    'handlers':['File_Initialise','smtp_Initialise'],
                                    'level':'DEBUG',
                                },
               
               'LOGGER_UserReg':{
                                    #'handlers':['File_User','smtp'],
                                    'handlers':['File_UserReg','smtp_UserReg'],
                                    'level':'DEBUG',
                                },
               
               'LOGGER_Communication':{
                                    #'handlers':['File_User','smtp'],
                                    'handlers':['File_Communcation','smtp_Communcation'],
                                    'level':'DEBUG',
                                },
               'LOGGER_UserProfile':{
                                    #'handlers':['File_User','smtp'],
                                    'handlers':['File_UserProfile','smtp_UserProfile'],
                                    'level':'DEBUG',
                                },
               'LOGGER_Adress':{
                                    #'handlers':['File_User','smtp'],
                                    'handlers':['File_Adress','smtp_Adress'],
                                    'level':'DEBUG',
                                },
               },
    'handlers': {
        'File_UserReg': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'DEBUG',
            'formatter': 'detailed',
            'filename': '/var/www/vhosts/thoughtxplore.com/uiet/tx2/logs/UserRegLogs',
            'maxBytes': 10485760,
            'backupCount': 5,
        },
        'File_Security': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'DEBUG',
            'formatter': 'detailed',
            'filename': '/var/www/vhosts/thoughtxplore.com/uiet/tx2/logs/SecurityLogs',
            'maxBytes': 10485760,
            'backupCount': 5,
        },
        'File_Query': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'DEBUG',
            'formatter': 'detailed',
            'filename': '/var/www/vhosts/thoughtxplore.com/uiet/tx2/logs/QueryLogs',
            'maxBytes': 10485760,
            'backupCount': 5,
        },
        'File_User': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'DEBUG',
            'formatter': 'detailed',
            'filename': '/var/www/vhosts/thoughtxplore.com/uiet/tx2/logs/UserLogs',
            'maxBytes': 10485760,
            'backupCount': 5,
        },
        'File_Initialise': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'DEBUG',
            'formatter': 'detailed',
            'filename': '/var/www/vhosts/thoughtxplore.com/uiet/tx2/logs/InitLogs',
            'maxBytes': 10485760,
            'backupCount': 5,
        },
        'File_Communcation': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'DEBUG',
            'formatter': 'detailed',
            'filename': '/var/www/vhosts/thoughtxplore.com/uiet/tx2/logs/CommunicationLogs',
            'maxBytes': 10485760,
            'backupCount': 5,
        },
        'File_UserProfile': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'DEBUG',
            'formatter': 'detailed',
            'filename': '/var/www/vhosts/thoughtxplore.com/uiet/tx2/logs/UserProfileLogs',
            'maxBytes': 10485760,
            'backupCount': 5,
        },
        'File_Adress': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'DEBUG',
            'formatter': 'detailed',
            'filename': '/var/www/vhosts/thoughtxplore.com/uiet/tx2/logs/Adress',
            'maxBytes': 10485760,
            'backupCount': 5,
        },
#######################################
        'smtp_UserReg': {
            'class': 'logging.handlers.SMTPHandler',
            'level': 'ERROR',
            'formatter': 'email',
            'mailhost': 'localhost',
            'fromaddr': 'no-reply@thoughtxplore.com',
            'toaddrs': ['thoughtxplore@gmail.com'],
            'subject': '[ThoughtXplore-Error] UserReg',
        },
        'smtp_Security': {
            'class': 'logging.handlers.SMTPHandler',
            'level': 'ERROR',
            'formatter': 'email',
            'mailhost': 'localhost',
            'fromaddr': 'no-reply@thoughtxplore.com',
            'toaddrs': ['thoughtxplore@gmail.com'],
            'subject': '[ThoughtXplore-Error] Security',
        },
        'smtp_Query': {
            'class': 'logging.handlers.SMTPHandler',
            'level': 'ERROR',
            'formatter': 'email',
            'mailhost': 'localhost',
            'fromaddr': 'no-reply@thoughtxplore.com',
            'toaddrs': ['thoughtxplore@gmail.com'],
            'subject': '[ThoughtXplore-Error] Query',
        },
        'smtp_User': {
            'class': 'logging.handlers.SMTPHandler',
            'level': 'ERROR',
            'formatter': 'email',
            'mailhost': 'localhost',
            'fromaddr': 'no-reply@thoughtxplore.com',
            'toaddrs': ['thoughtxplore@gmail.com'],
            'subject': '[ThoughtXplore-Error] User',
        },
        'smtp_Initialise': {
            'class': 'logging.handlers.SMTPHandler',
            'level': 'ERROR',
            'formatter': 'email',
            'mailhost': 'localhost',
            'fromaddr': 'no-reply@thoughtxplore.com',
            'toaddrs': ['thoughtxplore@gmail.com'],
            'subject': '[ThoughtXplore-Error] Initialise',
        },
        'smtp_Communcation': {
            'class': 'logging.handlers.SMTPHandler',
            'level': 'ERROR',
            'formatter': 'email',
            'mailhost': 'localhost',
            'fromaddr': 'no-reply@thoughtxplore.com',
            'toaddrs': ['thoughtxplore@gmail.com'],
            'subject': '[ThoughtXplore-Error] Communcation',
        },
        'smtp_UserProfile': {
            'class': 'logging.handlers.SMTPHandler',
            'level': 'ERROR',
            'formatter': 'email',
            'mailhost': 'localhost',
            'fromaddr': 'no-reply@thoughtxplore.com',
            'toaddrs': ['thoughtxplore@gmail.com'],
            'subject': '[ThoughtXplore-Error] UserProfile',
        },
        'smtp_Adress': {
            'class': 'logging.handlers.SMTPHandler',
            'level': 'ERROR',
            'formatter': 'email',
            'mailhost': 'localhost',
            'fromaddr': 'no-reply@thoughtxplore.com',
            'toaddrs': ['thoughtxplore@gmail.com'],
            'subject': '[ThoughtXplore-Error] Adress',
        },
        'smtp': {
            'class': 'logging.handlers.SMTPHandler',
            'level': 'ERROR',
            'formatter': 'email',
            'mailhost': 'localhost',
            'fromaddr': 'no-reply@thoughtxplore.com',
            'toaddrs': ['upcomingnewton@gmail.com', 'sarvpriye98@gmail.com'],
            'subject': '[ThoughtXplore] Error encountered.',
        },
#######################################
    },
    'formatters': {
        'detailed': {
            'format': '%(asctime)s %(module)-17s line:%(lineno)-4d ' \
            '%(levelname)-8s %(message)s',
        },
        'email': {
            'format': 'Timestamp: %(asctime)s\nModule: %(module)s\n' \
            'Line: %(lineno)d\nMessage: %(message)s',
        },
    },
}
