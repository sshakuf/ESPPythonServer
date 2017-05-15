import RestEngine

def InitializeRestAPI():
    #find all functions that starts with REST in this module
    for func in dir():
        print func


def R_test(args):
    print('in R_test')
    print (args)
    content = '<html><header><title>ESP8266</title></header><body>TEST!!! ' + ", ".join(args) + '</body></html>'
    header = RestEngine.createHeader(content)
    return header, content

InitializeRestAPI()
