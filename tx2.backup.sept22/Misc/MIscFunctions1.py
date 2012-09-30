from tx2.CONFIG import SESSION_MESSAGE
from tx2.DataBaseHelper import DBhelper
import os
import re


def replaceContentUrls(content, typeReturn='ANCHOR'):
        urls= re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', content)
        
        if(typeReturn=='ANCHOR'):
            for i in urls:
                k="<a href='"+i+"' target='new' >"+i+"</a>"
                content=content.replace(i,k)
        return content

def AppendMessageList(HttpRequest):
    msglist = []
    try:
      if SESSION_MESSAGE in HttpRequest.session.keys():
        msglist = HttpRequest.session[SESSION_MESSAGE]
    except:
      pass
    return msglist
def is_integer(s):
    try:
        int(s)
        return True
    except :
      print "Hi"
        
def executeAllStoredProcedures(path):
  try:
    temp=os.listdir(path)
    print temp
    for subdir in temp:
      temp2=os.path.join(path,subdir)
      if os.path.isfile(temp2):
        try:
          
          f=open(temp2,'r')
          sql=f.read()
          DBhelper.CallFunction(sql)
        except Exception as ex:
          print ex
        continue
      executeAllStoredProcedures(temp2)
  except Exception as ex:
    print ex
  return 0;

if __name__=='__main__':
  executeAllStoredProcedures(os.path.realpath('../../sp'))
