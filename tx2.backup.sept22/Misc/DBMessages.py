
def decode(result,rescode):
    if result == 1:
        return 'SUCCESS'
    elif result == 2:
        return 'Requested object already exists'
    else: 
        return db_messages[str(rescode)]

db_messages = {504:'User Does Not have permission to insert in this table',}
