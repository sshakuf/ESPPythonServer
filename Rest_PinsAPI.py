import RestEngine
from machine import Pin

pinsNumsOutput = [0,1,2,3,4,5]
pinsNumsInput = [12,13,14,15,16]
pins = {} 




def Initialize():
    # Create the pins
    for p in pinsNumsOutput:
        pins[p] = Pin(p, Pin.OUT)
    for p in pinsNumsInput:
        pins[p] = Pin(p, Pin.IN)


def htmlPinsState():
    c = "<p> outputs: <br/> "
    for v in pinsNumsOutput:
        c += " pin " + str(v) + ": "+  str(pins[v].value())+ "  " 
    c+= "</p>"
    c += "<p> Inputs: <br/>"
    for v in pinsNumsInput:
        c += " pin " + str(v) + ": "+  str(pins[v].value())+ "  " 
    c+= "</p>"
    
    return c


def Get_pins(inProp):
    c =  " pin " + str(inProp) + ": "+  str(pins[inProp].value())+ "  "
    content = RestEngine.CreateHTML(c)
    header = RestEngine.createHeader(content)
    return header, content


def Set_pins(inProp, inVal):
    if inVal != 0:
        pins[inProp].value(1)
    else:
        pins[inProp].value(0)
    c =  " pin " + str(inProp) + ": "+  str(pins[inProp].value())+ "  "
    content = RestEngine.CreateHTML(c)
    header = RestEngine.createHeader(content)
    return header, content


def R_pins(args):
    print('in R_pins')
    print (args)
    c = htmlPinsState()
    
    
    content = RestEngine.CreateHTML(c)
    header = RestEngine.createHeader(content)
    return header, content

