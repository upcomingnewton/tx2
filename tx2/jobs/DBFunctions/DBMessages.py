from tx2.Misc.DBMessages import  db_messages


def decode(res):
    msg = ''
    result = res['result']
    rescode = res['rescode']
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
    except Exception , e:
        msg = 'EXCEPTION : ' + str(e)
    return msg
    

db_messages.update({ 
                161:'Already exists in database',
                
                201:'Requested city is already present in the database.',
                202:'Failed to add requested city in database.',
                206:'Requested state is already present in the database.',
                207:'Failed to add requested city in database.',
                211:'Requested country is already present in the database.',
                212:'Failed to add requested country in database.',
                216:'Failed to add adress to database.',
                221:'Requested Adress Object does not exist in the system.',
                222:'Failed to update adress in database.',
                225:'Sucessfully updated adress in database',
                231:'Record already exists for this user in contact information table. Please use update operation.',
                232:'Failed to add contact information to database.',
                236:'Requested Contact Information does not exist in the system.',
                237:'Failed to update Contact Information in database.',
                240:'Sucessfully updated Contact Information in database',
})

