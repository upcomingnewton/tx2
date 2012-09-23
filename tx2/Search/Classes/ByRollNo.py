'''
Created on 14-Sep-2012

@author: jivjot
'''

class ByRollNo(object):
    '''
    classdocs
    '''

    
    def __init__(self):
        '''
        Constructor
        '''
        self.Id=5
        self.Option='<option value="%s">Search By RollNo</option>'%(self.Id)
    def gethtmlControl(self,count,data):
      name='Control%s'%(count)
      nameor='ControlOr%s'%(count)
      value=''
      checked=''
      if name in data:
        value=data[name]
      if nameor in data:
        checked="checked='checked'"
      html="Enter RollNo:<input type='text' name='%s' value='%s'/> <input type='checkbox' name='%s' %s/> OR DATA<br/>"%(name,value,nameor,checked)
      return html
    def getsqlstatement(self,count,data,sqlstatement):
      name='Control%s'%(count)
      nameor='ControlOr%s'%(count)
      value=''
      if name in data:
        value=data[name]
      if sqlstatement==None:
        sqlstatement='Select "User_id" from "UserProfile_studentdetails" where '
      else :
        sqlstatement='Select "User_id" from "UserProfile_studentdetails" where "User_id" in (%s)'%(sqlstatement)
        if nameor in data:
          sqlstatement=sqlstatement+' or '
        else:
          sqlstatement=sqlstatement+' and '
      sqlstatement=sqlstatement+'lower("RollNo") like lower(%s)'%( "'%%"+value+"%%'")
      return sqlstatement