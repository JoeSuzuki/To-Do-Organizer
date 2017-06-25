#!/usr/bin/python
import random
import cgi,os

#the field storage is a global variable.
#Since your page has exactly one, you can
#just acccess it from anywhere in the program.
form = cgi.FieldStorage()

html="""
<html>
<head>
<title>To-Do</title>
<style>
body{
        background-color:azure;
    } 
    h1 {
        color:black;
        font-size: 30px;
    }
    p {
        color:black;
    }
    input[type=text], select {
    width: 100%;
    padding: 12px 20px;
    margin: 4px 0;
    border: 1px solid #ccc;
    border-radius: 4px;
    box-sizing: border-box;
}
    input[type=submit] {
    width: 100%;
    background-color: azure;
    border: 1px solid #ccc;
    color:black ;
    padding: 7px;
    margin: 8px 0;
    border-radius: 4px;
    cursor: pointer;
}
    input[type=checkbox] {
        cursor: pointer;    
    }
</style>
</head>
<body>
<div style="background-color:white;border-radius: 25px;box-shadow: 3px 3px 3px 3px lightblue;"> 
    <center> <h1>Welcome to the To-do Organizer!</h1>
    <p>Insert any text, and it will build you a table of your schedule...</p>
</center>
</div>
<div style="width:50%;float:left;"> <form  name="input" method="GET" action="To-Do.py" >
    <input type="checkbox" name="12AM" checked> 12AM
    <input type="text" name="D12AM"  style="height:20px;width:80%;font-size:14pt;"  ><br>
	<input type="checkbox" name="1AM"> 1AM
    <input type="text" name="D1AM"  style="height:20px;width:80%;font-size:14pt;"  ><br>
    <input type="checkbox" name="2AM"> 2AM
    <input type="text" name="D2AM"  style="height:20px;width:80%;font-size:14pt;"  ><br>
    <input type="checkbox" name="3AM"> 3AM
    <input type="text" name="D3AM"  style="height:20px;width:80%;font-size:14pt;"  ><br>
    <input type="checkbox" name="4AM"> 4AM
    <input type="text" name="D4AM"  style="height:20px;width:80%;font-size:14pt;"  ><br>
    <input type="checkbox" name="5AM"> 5AM
    <input type="text" name="D5AM"  style="height:20px;width:80%;font-size:14pt;"  ><br>
    <input type="checkbox" name="6AM"> 6AM
    <input type="text" name="D6AM"  style="height:20px;width:80%;font-size:14pt;"  ><br>
    <input type="checkbox" name="7AM"> 7AM
    <input type="text" name="D7AM"  style="height:20px;width:80%;font-size:14pt;"  ><br>
    <input type="checkbox" name="8AM"> 8AM
    <input type="text" name="D8AM"  style="height:20px;width:80%;font-size:14pt;"  ><br>
    <input type="checkbox" name="9AM"> 9AM
    <input type="text" name="D9AM"  style="height:20px;width:80%;font-size:14pt;"  ><br>
    <input type="checkbox" name="10AM"> 10AM
    <input type="text" name="D10AM"  style="height:20px;width:80%;font-size:14pt;"  ><br>
    <input type="checkbox" name="11AM"> 11AM
    <input type="text" name="D11AM"  style="height:20px;width:80%;font-size:14pt;"  ><br>
    <input type="checkbox" name="12PM"> 12PM
    <input type="text" name="D12PM"  style="height:20px;width:80%;font-size:14pt;"  ><br>
    <input type="checkbox" name="1PM"> 1PM
    <input type="text" name="D1PM"  style="height:20px;width:80%;font-size:14pt;"  ><br>
    <input type="checkbox" name="2PM"> 2PM
    <input type="text" name="D2PM"  style="height:20px;width:80%;font-size:14pt;"  ><br>
    <input type="checkbox" name="3PM"> 3PM
    <input type="text" name="D3PM"  style="height:20px;width:80%;font-size:14pt;"  ><br>
    <input type="checkbox" name="4PM"> 4PM
    <input type="text" name="D4PM"  style="height:20px;width:80%;font-size:14pt;"  ><br>
    <input type="checkbox" name="5PM"> 5PM
    <input type="text" name="D5PM"  style="height:20px;width:80%;font-size:14pt;"  ><br>
    <input type="checkbox" name="6PM"> 6PM
    <input type="text" name="D6PM"  style="height:20px;width:80%;font-size:14pt;"  ><br>
    <input type="checkbox" name="7PM"> 7PM
    <input type="text" name="D7PM"  style="height:20px;width:80%;font-size:14pt;"  ><br>
    <input type="checkbox" name="8PM"> 8PM
   <input type="text" name="D8PM"  style="height:20px;width:80%;font-size:14pt;"  > <br>
    <input type="checkbox" name="9PM"> 9PM
    <input type="text" name="D9PM"  style="height:20px;width:80%;font-size:14pt;"  ><br>
    <input type="checkbox" name="10PM"> 10PM
    <input type="text" name="D10PM"  style="height:20px;width:80%;font-size:14pt;"  ><br>
    <input type="checkbox" name="11PM"> 11PM
    <input type="text" name="D11PM"  style="height:20px;width:80%;font-size:14pt;"  ><br>
	<input type="checkbox" name="clearTable"> Clear Table <br>"""
	

def footer(): #makes the code keep the user and magicnumber as you use the table
    header=html
    header+='<input type="hidden" name="user" value="'+form['user'].value+'">'
    header+='<input type="hidden" name="magicnumber" value="'+form['magicnumber'].value+'">'
    header+="""<center> <input type="submit" value="Submit" style=" background-color:white;"> </center>
  </form>"""
    header+='<a href="/logout.py?user='+form['user'].value+"&magicnumber="+form['magicnumber'].value+ '">Log Out</a>'
    header+="""</div>
    <div style="height:80%;width:50%;float:right;"> """
    header+='<iframe src="To-Do.py?D1AM=&D2AM=&D3AM=&D4AM=&D5AM=&D6AM=&D7AM=&D8AM=&D9AM=&D10AM=&D11AM=&D12AM=&D1PM=&D2PM=&D3PM=&D4PM=&D5PM=&D6PM=&D7PM=&D8PM=&D9PM=&D10PM=&D11PM=&D12PM=&user='+form['user'].value+"&magicnumber="+form['magicnumber'].value+'" style="height:50em;width:100%;"></iframe></div>'
    header+="</body></html>"
    return header

def authenticate():
    if 'user' in form and 'magicnumber' in form:
        #get the data from form, and IP from user.
        user = form['user'].value
        magicnumber = form['magicnumber'].value
        IP = 'NULL'
        if 'REMOTE_ADDR' in os.environ:
            IP = os.environ["REMOTE_ADDR"]
        #compare with file
        text = open('loggedin.txt').readlines()
        for line in text:
            line = line.strip().split(",")
            if line[0]==user:#when you find the right user name
                if line[1]==magicnumber and line[2]==IP:
                    return True
                else:
                    return False
        return False#in case user not found
    return False #no/missing fields passed into field storage


#either returns ?user=__&magicnumber=__  or an empty string.
def securefields():
    if 'user' in form and 'magicnumber' in form:
        user = form['user'].value
        magicnumber = form['magicnumber'].value
        return "?user="+user+"&magicnumber="+magicnumber
    return ""

#makes a link, link will include secure features if the user is logged in
def makeLink(page, text):
    return '<a href="'+page+securefields()+'">'+text+'</a><br>'

def notLoggedIn():
    return "You must be logged in!<br>\n"


def main():
        #determine if the user is properly logged in once. 
    isLoggedIn = authenticate()

    #use this to determine if you want to show "logged in " stuff, or regular stuff
    if isLoggedIn:
        print "Content-Type: text/html\n\n" + footer()
    else:
        print "Content-Type: text/html\n\n" + notLoggedIn()

main()

