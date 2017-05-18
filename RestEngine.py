
commands = {}


def CreateHTML(inBody):
    return '<html><header><title>ESP8266</title></header><body> ' + inBody + '</body></html>'


def AddRestEndPoint(inCommand, inHandler):
    commands[inCommand] = inHandler

def Gethandler(inCommand):
    if inCommand in commands:
        return commands[inCommand]
    return None


def createHeader(content, contectType='text', fileext='html'):
    header = ''
    header += 'HTTP/1.1 200 OK\r\n'
    # header += 'Date: ' + time.localtime(time.time())
    header += 'Content-Type: ' + contectType +'/' + fileext + '\r\n'
    header += 'Content-Length: ' + str(len(content)) + '\r\n'
    header += '\r\n'
    return header



