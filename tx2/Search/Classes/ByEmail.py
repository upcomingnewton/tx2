'''
Created on 14-Sep-2012

@author: jivjot
'''

class ByEmail(object):
    '''
    classdocs
    '''

    
    def __init__(self):
        '''
        Constructor
        '''
        self.Id=2
        self.Option='<option value="%s">Search By Email</option>'%(self.Id)
    def gethtmlControl(self,count,data):
      name='Control%s'%(count)
      nameor='ControlOr%s'%(count)
      value=''
      checked=''
      if name in data:
        value=data[name]
      if nameor in data:
        checked="checked='checked'"
      html="Enter Email:<input type='text' name='%s' value='%s'/> <input type='checkbox' name='%s' %s/> OR DATA<br/>"%(name,value,nameor,checked)
      
      return html
    def getsqlstatement(self,count,data,sqlstatement):
      name='Control%s'%(count)
      nameor='ControlOr%s'%(count)
      value=''
      if name in data:
        value=data[name]
      if sqlstatement==None:
        sqlstatement='Select id from "Users_user" where '
      else :
        sqlstatement='Select id from "Users_user" where id in (%s)'%(sqlstatement)
        if nameor in data:
          sqlstatement=sqlstatement+' or '
        else:
          sqlstatement=sqlstatement+' and '
      sqlstatement=sqlstatement+('"UserEmail" like %s'%( "'%%"+value+"%%'"))
      return sqlstatement
      