from settings import GLOBAL_STATICFILES_DIRS, GLOBAL_TEMPLATE_DIRS
UserPath = "/var/www/vhosts/thoughtxplore.com/uiet/"

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    #"/home/nitin/tx2/static",
    #"/home/nitin/workspace/tx2/static",
    UserPath + GLOBAL_STATICFILES_DIRS,
)

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    #"/home/nitin/tx2/templates",
    #"/home/nitin/workspace/tx2/templates",
    UserPath + GLOBAL_TEMPLATE_DIRS,
)


# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.  smtp_AlumniLogger
LOGGING = LOG_SETTINGS = {
    'version': 1,
    'loggers':{
               'AlumniLogger':{
                                    #'handlers':['File_Security','smtp'],
                                    'handlers':['File_Alumni','smtp_AlumniLogger'],
                                    'level':'DEBUG',
                                },
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
                                    'handlers':['File_Initialise'],
                                    'level':'DEBUG',
                                },
               
               'LOGGER_UserReg':{
                                    #'handlers':['File_User','smtp'],
                                    'handlers':['File_UserReg','smtp_UserReg'],
                                    'level':'DEBUG',
                                },
               
               'LOGGER_Communication':{
                                    #'handlers':['File_User','smtp'],
                                    'handlers':['File_Communcation','smtp'],
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
        'File_Alumni': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'DEBUG',
            'formatter': 'detailed',
            'filename': UserPath + 'tx2/logs/AlumniLogs',
            'maxBytes': 10485760,
            'backupCount': 5,
        },
        'File_UserReg': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'DEBUG',
            'formatter': 'detailed',
            'filename': UserPath + 'tx2/logs/UserRegLogs',
            'maxBytes': 10485760,
            'backupCount': 5,
        },
        'File_Security': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'DEBUG',
            'formatter': 'detailed',
            'filename': UserPath + 'tx2/logs/SecurityLogs',
            'maxBytes': 10485760,
            'backupCount': 5,
        },
        'File_Query': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'DEBUG',
            'formatter': 'detailed',
            'filename': UserPath + 'tx2/logs/QueryLogs',
            'maxBytes': 10485760,
            'backupCount': 5,
        },
        'File_User': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'DEBUG',
            'formatter': 'detailed',
            'filename': UserPath + 'tx2/logs/UserLogs',
            'maxBytes': 10485760,
            'backupCount': 5,
        },
        'File_Initialise': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'DEBUG',
            'formatter': 'detailed',
            'filename': UserPath + 'tx2/logs/InitLogs',
            'maxBytes': 10485760,
            'backupCount': 5,
        },
        'File_Communcation': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'DEBUG',
            'formatter': 'detailed',
            'filename': UserPath + 'tx2/logs/CommunicationLogs',
            'maxBytes': 10485760,
            'backupCount': 5,
        },
        'File_UserProfile': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'DEBUG',
            'formatter': 'detailed',
            'filename': UserPath + 'tx2/logs/UserProfileLogs',
            'maxBytes': 10485760,
            'backupCount': 5,
        },
        'File_Adress': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'DEBUG',
            'formatter': 'detailed',
            'filename': UserPath + 'tx2/logs/Adress',
            'maxBytes': 10485760,
            'backupCount': 5,
        },
#######################################
        'smtp_AlumniLogger': {
            'class': 'logging.handlers.SMTPHandler',
            'level': 'ERROR',
            'formatter': 'email',
            'mailhost': 'localhost',
            'fromaddr': 'no-reply@thoughtxplore.com',
            'toaddrs': ['thoughtxplore@gmail.com'],
            'subject': '[ThoughtXplore-Error] Alumni',
        },
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
