import RestEngine
from machine import Pin

pinsNumsOutput = [0,1,2,3,4,5]
pinsNumsInput = [12,13,14,15,16]
pins = {} 


def intTryParse(value):
    try:
        return int(value), True
    except ValueError:
        return value, False


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
    return " pin " + str(inProp) + ": "+  str(pins[inProp].value())+ "  "

def Set_pins(inProp, inVal):
    if inVal != 0:
        pins[inProp].value(1)
    else:
        pins[inProp].value(0)
    return  " pin " + str(inProp) + ": "+  str(pins[inProp].value())+ "  "

def R_pins(args):
    print('in R_pins')
    print (args)
    c = htmlPinsState()
    if len(args) == 1:
        #check that we have a valid pin number
        pinnum, success = intTryParse(args[0])
        if success:
            #return onth the state of this pecific pin
            c = Get_pins(pinnum)
    if len(args) == 2:
        pinnum, success = intTryParse(args[0])
        if success:
            pinval, success = intTryParse(args[1])
            if success:
                c = Set_pins(pinnum, pinval) 
                
    
    
    content = RestEngine.CreateHTML(c)
    header = RestEngine.createHeader(content)
    return header, content

