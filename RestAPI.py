import RestEngine


def R_test(args):
    print('in R_test')
    print (args)
    content = '<html><header><title>ESP8266</title></header><body> ' + ", ".join(args) + '</body></html>'
    header = RestEngine.createHeader(content)
    return header, content


