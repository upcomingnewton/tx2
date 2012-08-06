'''
Created on Mar 3, 2012

@author: nitin
'''


from django.db import connection,transaction

def dictfetchall(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]

def CallFunction(sql):
    cursor = connection.cursor()
    cursor.execute(sql)
    transaction.commit_unless_managed()
    row = dictfetchall(cursor)
    #print row
    return row
    
if __name__=="__main__":
    CallFunction('SELECT * FROM "txUser_user";')