'''
Created on 14-Sep-2012

@author: jivjot
'''
from tx2.Search.Classes.ByName import ByName
from tx2.Search.Classes.ByEmail import ByEmail
from tx2.Misc.MIscFunctions1 import is_integer
from tx2.DataBaseHelper import DBhelper

class Search(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.myoptions=[ByName(),ByEmail()]
        
    def getOptions(self):
      options=''
      
      for obj in self.myoptions:
        options+=obj.Option
        
      return options
    def getSearchControls(self,ControlInfo,data):
      searchControls=''
      arr=ControlInfo.split(",")
      count=0
      for a in arr:
        for obj in self.myoptions:
          if is_integer(a)and int(a)==obj.Id:
            count=count+1
            searchControls+=obj.gethtmlControl(count,data)
            break
      return searchControls
    def getSearchResults(self,ControlInfo,data):
      sqlstatement=None
      arr=ControlInfo.split(",")
      count=0
      for a in arr:
        for obj in self.myoptions:
          if is_integer(a)and int(a)==obj.Id:
            count=count+1
            sqlstatement=obj.getsqlstatement(count,data,sqlstatement)
            break
      if count==0:
        sqlstatement='Select * from "View_Student"'
      else:
        sqlstatement='Select * from "View_Student" where "Id" in (%s)'%(sqlstatement)+";"
      try:
          datareturned=DBhelper.CallSelectFunction(sqlstatement)
      except Exception, ex:
          datareturned=None
      return datareturned
      