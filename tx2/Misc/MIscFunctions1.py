from tx2.CONFIG import SESSION_MESSAGE

def AppendMessageList(HttpRequest):
    msglist = []
    if SESSION_MESSAGE in HttpRequest.session.keys():
        msglist = HttpRequest.session[SESSION_MESSAGE]
    return msglist