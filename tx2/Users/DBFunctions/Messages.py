def decode(res):
    msg = ''
    result = res['result']
    rescode = res['rescode']
    print result , rescode
    try:
      if int(result) == -5:
        msg += 'ERROR : ' + rescode
      elif int(result) == 2:
        msg += 'Re-Request : Object already exists in database. Operation terminated.'
      elif int(result) == -1 or int(result) == -2:
        msg += 'ERROR : ' + db_messages[int(rescode)]
      return msg
    except Exception ,ex:
      return 'ERROR : ' + str(ex)


db_messages = {
                # Check User For Permission
                501:'Requesting User does not exist in the system',
                502:'Requested Permission does not exist in the system',
                503:'Object on which Permission is requested is not valid. Either Object does not exist or Requested permission is not defined for this object.',
                504:'Requesting user does not have permission to perform this operation on requested object.',
                
                # menu update
                106:'Requested Menu Object to be updated does not exist',
                107:'Update failed on requested menu object.',
                999:'Logs insertion failed. Requested Operation terminated',
                110:'Menu Object updated sucessfully.',
                
                # menu insert
                102:'Menu insertion failed in database.',
                
                #user login 
                111:'User does not exist.',
                112:'emailid or password does not match.',
                113:'login type does not exist or has been disabled',
                114:'login error. Error generating loginid',
                115:'login sucessfull',
                
                #user insert
                91:'user exists in database',
                92:'user registration failed in database',
                
                # user update
                96:'user does not exist',
                97:'updation of user failed in database',
                99:'update sucessfull',
                
                # user logout
                116:'login id does not exist',
                117:'logout type does not exist or has been diabled',
                118:'logging our failed in database',
                120:'sucessfully logged out.'
}
