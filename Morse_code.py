        
d = {"A":".-","B":"-...","C":"-.-.","D":"-..","E":".",
       "F":"..-.","G":"--.","H":"....","I":"..","J":".---",
       "K":"-.-","L":".-..","M":"--","N":"-.","O":"---",
       "P":".--.","Q":"--.-","R":".-.","S":"...","T":"-",
       "U":"..-","V":"...-","W":".--","X":"-..-","Y":"-.--","Z":"--..",
       " ":"....."}
d1 = {".-":"A","-...":"B","-.-.":"C","-..":"D",".":"E",
        "..-.":"F","--.":"G","....":"H","..":"I",".---":"J",
        "-.-":"K",".-..":"L","--":"M","-.":"N","---":"O",
        ".--.":"P","--.-":"Q",".-.":"R","...":"S","-":"T",
        "..-":"U","...-":"V",".--":"W","-..-":"X","-.--":"Y","--..":"Z",
        ".....":" "}
        
    
text=input("Please enter the text: ")
text=text.upper()

def Mors(text):
    text2=""
    if "." in text:
        text=text.split()
        for i in text:
             text2+=d1[i]
    else:
        for i in text:
            text2+=d[i]
    return text2
result=Mors(text)
print(result)