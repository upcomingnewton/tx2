'''
Created on 14-Sep-2012

@author: jivjot
'''
from tx2.Misc.MIscFunctions1 import is_integer

class ByAge(object):
    '''
    classdocs
    '''

    
    def __init__(self):
        '''
        Constructor
        '''
        self.Id=4
        self.Option='<option value="%s">Search By Age</option>'%(self.Id)
    def gethtmlControl(self,count,data):
      name='Control%s'%(count)
      nameor='ControlOr%s'%(count)
      nameoper='ControlOper%s'%(count)
      value=''
      checked=''
      oper='='
      if name in data:
        value=data[name]
      if nameoper in data:
        oper=data[nameoper]
      if nameor in data:
        checked="checked='checked'"
      optionarray=['=','>','<','>=','<=']
      option=''
      for obj in optionarray:
        if obj==oper:
          option=option+'<option value="%s" selected="selected">%s</option>'%(obj,obj)
        else:
          option=option+'<option value="%s" >%s</option>'%(obj,obj)
        
      htmloper='<select name="%s">%s</select>'%(nameoper,option)
      html="Enter Age:<input type='text' name='%s' value='%s'/>%s <input type='checkbox' name='%s' %s/> OR DATA<br/>"%(name,value,htmloper,nameor,checked)
      return html
    def getsqlstatement(self,count,data,sqlstatement):
      name='Control%s'%(count)
      nameor='ControlOr%s'%(count)
      value='0'
      nameoper='ControlOper%s'%(count)
      oper='='
      if nameoper in data:
        
        oper=data[nameoper]
      
      if name in data:
        if is_integer(data[name]):
          value=data[name]
      if sqlstatement==None:
        sqlstatement='Select "Id" from "View_Student" where'
      else :
        sqlstatement='Select "Id" from "View_Student" where id in (%s)'%(sqlstatement)
        if nameor in data:
          sqlstatement=sqlstatement+' or '
        else:
          sqlstatement=sqlstatement+' and '
      sqlstatement=sqlstatement+' cast("Age" as integer) %s %s'%(oper,value)
      return sqlstatement