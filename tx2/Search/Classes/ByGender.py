'''
Created on 14-Sep-2012

@author: jivjot
'''

class ByGender(object):
    '''
    classdocs
    '''

    
    def __init__(self):
        '''
        Constructor
        '''
        self.Id=3
        self.Option='<option value="%s">Search By Gender</option>'%(self.Id)
    def gethtmlControl(self,count,data):
      name='Control%s'%(count)
      nameor='ControlOr%s'%(count)
      value=''
      checked=''
      if name in data:
        value=data[name]
      if nameor in data:
        checked="checked='checked'"
      options=['M','F']
      htmloption=''
      for obj in options:
        if obj==value:
          htmloption+='<option value="%s" selected="selected">%s</option>'%(obj,obj)
        else:
          htmloption+='<option value="%s">%s</option>'%(obj,obj)
      html="Select Gender:<select name='%s'/>%s</select> <input type='checkbox' name='%s' %s/> OR DATA<br/>"%(name,htmloption,nameor,checked)
      
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
      sqlstatement=sqlstatement+('"UserGender" = %s'%( "'"+value+"'"))
      return sqlstatement
      