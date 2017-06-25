#!/usr/bin/python

import cgi
import time
# ~~~~~~~~~~~~~~~ support functions ~~~~~~~~~~~~~~~
hours=["12AM","1AM","2AM","3AM","4AM","5AM","6AM","7AM","8AM","9AM","10AM","11AM","12PM","1PM","2PM","3PM","4PM","5PM","6PM","7PM","8PM","9PM","10PM","11PM"]
def FStoD():
    '''
    Converts cgi.FieldStorage() return value into a standard dictionary
    '''
    d = {}
    formData = cgi.FieldStorage()
    for k in formData.keys():
        d[k] = formData[k].value
    return d

def descFind(d): #finds descriptions and returns them in a list
    times=timeFind(d) #gives time
    L=[]
    for i in times: #using the time, it finds the description for it and returns them in a list
        if d.has_key("D"+i):
            L.append(d["D"+i])
        else:
            L.append("")
    return L

def timeFind(d): #finds times and returns them in a list
    L=[]
    for i in hours: #checks cgi.FieldStorage() for times (checked boxes)
        if i in d:
            L.append(i)
    return L

def tablify(data): #takes data and puts it in a table
    times=data[0]
    description=data[1]
    header="""<table border="1" style='width:100%;'>
<tr>
<th>Time</th>
<th>Description</th>
</tr>"""
    middle=""
    end="</table>"
    for i in hours:
        middle+="<tr>"
        middle+="<td"
        if hours.index(i)==hours.index(displayHour()): #if time has is at the hour, highlight in red
            middle+=' style="color:red;">'
        else:
            middle+=">"
        middle+=i+"</td><td"
        if hours.index(i)==hours.index(displayHour()): #if time has is at the hour, highlight in red (highlights same row)
            middle+=' style="color:red;">'
        else:
            middle+=">"
        if i in times:
            middle+=description[times.index(i)] #if there is a time, add its description in the table as well
        middle+="</td></tr>"
    middle+="</table>"
    return header+middle+end

def dataify(timesL, descL): #takes lists of time and descriptions and writes them
    ctr=0
    for i in timesL: #writes the data until it's all written
        writeData(timesL[ctr], descL[ctr])
        ctr+=1
        
def writeData(date, desc): #writes in userdata.txt the time and description corresponding in the user's save
    ctr=0
    user=returnUser()
    if desc=="": #if there is no description to write, stop
        return
    if date=="2AM" or date== "2PM": #otherwise when you look for 2AM, you get 12AM
        date="0"+date
    f= open("userdata.txt", "r")
    fRead=f.readlines()
    f.close()
    for i in fRead: #if it is the user, find the location in userdata.txt
        if user+"|"==i[:len(user+"|")]:
            index=ctr #location of user data
        ctr+=1
    userData=fRead[index][len(user+"|"):].strip() #userdata without user and \n
    if userData.find(date)==-1: 
        a=userData+date+":"+desc+";" #if there is no data, write it
    else:
        a=userData.replace(date+":", date+":"+desc+",") #if there is data, add to it
    fRead[index:index+1]=user+"|"+a+"\n" #replace the text in userdata.txt with the new data we changed
    s=linestostring(fRead)
    openf= open("userdata.txt", "w") #save as string and write it
    openf.write(s)
    openf.close()

def dataAnalysis(): #reads userdata.txt and checks each description for the time and returns them as lists in a list
    times=[]
    desc=[]
    ctr=0
    user=returnUser()
    f= open("userdata.txt", "r")
    fRead=f.readlines()
    f.close()
    for i in fRead: #if it is the user, find the location in userdata.txt
        if user+"|"==i[:len(user+"|")]:
            index=ctr #location of user data
        ctr+=1
    userData=fRead[index][len(user+"|"):].strip() #userdata without user and \n
    splitData=userData.split(";") #separate each time and its description on the file
    while len(splitData)>1: #adds the times and descriptions to lists until you reach the last value (which is empty)
        times.append(splitData[0][:splitData[0].find(":")]) 
        desc.append(splitData[0][splitData[0].find(":")+1:])
        del splitData[0]
    if "02AM" in times:
        times[times.index("02AM")]="2AM" #turns 02AM back to 2AM, necessary to differentiate between 2AM and 12AM
    if "02PM" in times:
        times[times.index("02PM")]="2PM"
    return [times, desc]
    
def main(): #runs functions
    d=FStoD()
    times=timeFind(d)
    desc=descFind(d)
    dataify(times, desc)
    clearTable(d)
    data=dataAnalysis()
    table=tablify(data)
    return table

def clearTable(d): #if clear table is checked, clear the table
    ctr=0
    user=returnUser()
    if d.has_key("clearTable"): #checks if it is checked
        openf=open("userdata.txt","r")
        f=openf.readlines()
        openf.close()
        for i in f: #looks for location of user in userdata.txt
            if user in i:
                index=ctr 
            ctr+=1
        f[index:index+1]=user+"|"
        s=linestostring(f)
        g=open("userdata.txt", "w")
        g.write(s) #clears the data
        g.close()
            
def displayHour(): #rxeturns hour
    rawtime=int(time.ctime().split(":")[0].split(" ")[3]) #finds hour from the huge amount of time given to you
    hour= rawtime
    if hour == 0: #hours are turned from 0-23 so this converts it to normal times
        return "12"+"AM"
    elif hour<=12:
        return str(hour)+"AM"
    else:
        return str(hour-12)+"PM"

def returnUser(): #returns user
    return cgi.FieldStorage()['user'].value
        
def linestostring(L): #turns readlines into a string
    s=""
    for i in L:
        s+=i
    return s
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ========= CONTENT-TYPE LINE REQUIRED. ===========
# ======= Must be beginning of HTML string ======== 
htmlStr = "Content-Type: text/html\n\n" #NOTE there are 2 '\n's !!! 
htmlStr += "<html><head><title> To-Do </title></head></html>\n"
htmlStr += "<body>"

# ~~~~~~~~~~~~~ HTML-generating code ~~~~~~~~~~~~~~
htmlStr += "<center><h3>To Do</h3></center>"
htmlStr += "<center>"
htmlStr += str(main())
htmlStr += "</center>"
htmlStr += "<a href='page1.py?user="+cgi.FieldStorage()['user'].value+"&magicnumber="+cgi.FieldStorage()['magicnumber'].value+"'> Go Back </a>"
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

htmlStr += "</body></html>"


print htmlStr
