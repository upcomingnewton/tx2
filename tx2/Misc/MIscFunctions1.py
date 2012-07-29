from tx2.CONFIG import SESSION_MESSAGE

def AppendMessageList(HttpRequest):
    msglist = []
    try:
	    if SESSION_MESSAGE in HttpRequest.session.keys():
		msglist = HttpRequest.session[SESSION_MESSAGE]
		print '=== message list appended'
    except:
   	pass
    print '||msglist||' + str(msglist)
    return msglist
def is_integer(s):
    try:
        int(s)
        return True
    except :
        return False