from tx2.Misc.DBMessages import  db_messages


def decode(result,rescode):
    msg = ''
    if result == 1:
        msg += 'SUCCESS'
    elif result == 2:
        msg += 'Requested object already exists' 
    msg += db_messages[str(rescode)]
    return msg
    
# insert function messages
db_messages.update({'601':'User registration failed. Please try again later, if problem persists, contact system administrator.',
               '602':'User registration failed. Error adding user to group. Please try again later, if problem persists, contact system administrator.',
               '603':'User registration failed. Error adding entry to logs.Please try again later, if problem persists, contact system administrator.',
               })

#login user
db_messages.update({
                    '2101':'user does not exist',
                    '2102':'user email or password is not correct',
                    '2103':'SYSTEM-ERROR.login type does not exist.Please report this error to your coordinator',
                    #2104 = insertion in login log table failed
                    '2104':'SYSTEM-ERROR. Error Generating login id.Please report this error to your coordinator',
                    })

#logout user
db_messages.update({
                    '2111':'SYSTEM ERROR. Login Id not found.Please report this error to your coordinator',
                    '2112':'SYSTEM ERROR. Logout Type not exists.Please report this error to your coordinator',
                    #2113 = updation of login log failed
                    '2113':'SYSTEM ERROR. Could not log out. Please report this error to your coordinator',
                    })


# user insert
db_messages.update({
                    '2131':'User Exists',
                    '2132':'System Error. Error in User Creation.Please report this error to your coordinator',
                    '2133':'System Error. Error in User Creation.Please report this error to your coordinator',
                    '999':'log entry failed',
                    })

# user state change single
db_messages.update({
                    '2141':'System Error. Requested Group Does not exist.Please report this error to your coordinator',
                    '2142':'System Error. Error in updation of state.Please report this error to your coordinator',
                    '2143':'System Erorr. Could not drop user from previous group.',
                    '2144':'System Error. Could not update user\'s group',
                    });
                    
                    
# create group
db_messages.update({
                    '2201':'Already Exists',
                    '2202':'Error insertion at database level',
                    });
