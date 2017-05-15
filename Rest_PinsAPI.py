import RestEngine

def InitializeRestAPI():
    #find all functions that starts with REST in this module
    for func in dir():
        print func


def R_pin(args):
    print('in R_pin')
    print (args)
    content = '<html><header><title>ESP8266</title></header><body>PINTEST!!! ' + ", ".join(args) + '</body></html>'
    header = RestEngine.createHeader(content)
    return header, content

InitializeRestAPI()
