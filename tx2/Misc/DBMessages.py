
def decode(result,rescode):
    if result == 1:
        return 'SUCCESS'
    elif result == 2:
        return 'Requested object already exists'
    else: 
        return db_messages[str(rescode)]

db_messages = {'-500':'Requested operation is not supported by system',
               '-501':'Requested object (user) does not exists',
               '-502':'Requested operation is not supported by system for this object',
               '500':'SUCCESS',
               '-1001':'Requested state does not exist',
               '-1002':'Requested state is not meant for this object',
               '-1003':'State concept is not defined for this object',
               '-1004':'mismatch in Requested State and State of the object',
               '1000':'SUCCESS',
               '999':'Log Entry failed',
               '-1':'Exception @ DB level',
               }