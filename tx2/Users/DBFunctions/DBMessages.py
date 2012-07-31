from tx2.Misc.DBMessages import  db_messages


def decode(result):
    msg = ''
    result = result['result']
    rescode = result['rescode']
    if result == 1:
        msg += 'SUCCESS. '
    elif result == 2:
        msg += 'Requested object already exists. ' 
    elif result == -1:
        msg += 'Error. ' 
    elif result == 999:
        msg += 'Error in updating logs and book-keeping. '
    try:
        msg += db_messages[int(rescode)]
    except:
        pass
    return msg
    

db_messages.update({ 

                # user insert
                91:'User already exists with this emailid.',
                92: 'Error creating user in the system. Insertion failed.',
                999:'Log insertion failed.',

                # log in
                113: 'login type does not exist.',
                114: 'Login failed. Could not log down login.',
                115: 'Login sucessful.',
                
                # log out
                116: 'Logout failed. Login ID does not match.',
                117: 'Log out Type does not exist.',
                118: 'Error Logging out user. Error in Book Keeping.',

                # user update
                96:'User does not exist.',
                97: 'Updation of records failed.',

                # login type
                141: 'login type exists.',
                142: 'Error creation login type.',
})

