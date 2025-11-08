def  decode(chrStr):
    msg = ""
    badCharLoc = 0
    origStr = chrStr
    
    while len(chrStr) > 0:
        twoDig = int(chrStr[:2]) #spaces, integers 0-9, A-Z, a-c are all two digit chr() values
        threeDig = int(chrStr[:3]) #d-z are three digit chr() values

        if twoDig == 32: #checks for a space character
            msg, chrStr = recode(msg, chrStr, twoDig)
        elif twoDig >= 48 and twoDig <= 57: #checks for the integers 0-9
            msg, chrStr = recode(msg, chrStr, twoDig)
        elif twoDig >= 65 and twoDig <= 90: #checks for A-Z
            msg, chrStr = recode(msg, chrStr, twoDig)
        elif twoDig >= 97 and twoDig <= 99: #checks for a-c
            msg, chrStr = recode(msg, chrStr, twoDig)
        elif threeDig >= 100 and threeDig <= 122: #checks for d-z
            msg, chrStr = recode(msg, chrStr, threeDig)            
        else:
            msg = ""
            badCharLoc = len(origStr) - len(chrStr) + 1
            break

    return msg, badCharLoc
    
def recode(msg, chrStr, chrSet):
    msg = msg + chr(chrSet)
    chrStr = chrStr[len(str(chrSet)):]

    return msg, chrStr

def encode(msg):
    codeStr = ""
    while len(msg) > 0:
        codeStr = codeStr + str(ord(msg[:1]))
        msg = msg[1:]
    
    return codeStr
    
def displayRes(codedMsg, msg, badCharLoc):
    if msg == "":
        print(f"We're going to need a better code breaker.\nThe code {codedMsg} contained an unrecognized character.\nThe unrecognized character started at position {badCharLoc}.\n")
    else:
        print(f'The code {codedMsg} contained this message: {msg}\n')
    

codedMsg = "10010511599111114100"
msg, badCharLoc = decode(codedMsg)
displayRes(codedMsg, msg, badCharLoc)

codedMsg = "10010521599111114100"
msg, badCharLoc = decode(codedMsg)
displayRes(codedMsg, msg, badCharLoc)

"""newMsg = "Not exactly the Enigma machine"
print(f'The new coded message is: {encode(newMsg)}.')

codedMsg = "7811111632101120979911610812132116104101326911010510310997321099799104105110101"
msg, badCharLoc = decode(codedMsg)
displayRes(codedMsg, msg, badCharLoc)"""