def decode(result):
    msg = ''
    result = result['result']
    rescode = result['rescode']



db_messages = {
                106:'Requested Menu Object to be updated does not exist',
                107:'Update failed on requested menu object.'
                999:'Logs insertion failed. Requested Operation terminated'
                110:'Menu Object updated sucessfully.'
}
