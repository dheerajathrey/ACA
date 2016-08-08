import turtle

def check_braces(s): #program to check for braces
    c=0
    d=0
    for ch in s:
        if ch=="{":
            c=c+1
        elif ch=="}":
            d=d+1
        if(d>c):
            return 0
    if c!=d:
        return 0
    else:
        return 1
    
def check_keyword(s,j):
    global k
    if s=="if":
        if_part()
        k=j
    elif s=="repeat":
        repeat_part()
    elif s=="while":
        while_part()
    elif s=="else":
        else_part()
    elif s=="$":
        variable_part()
    else:
        other()

def graphics(s):
    lines=s.split("\n")
    for line in lines:
        if line=="turn":
            turtle.right(90)
        elif line=="move":
            turtle.forward(10)
    turtle.done()

def variable_part():
    global i
    j=0
    for j in range(len(line[i][1])):
        if (line[i][1][j]=='='):
            break

    s=line[i][1][0:j]
    v=line[i][1][j+1:]
    n=eval(v,dicti)
    dicti[s]=n

def other():
    global output
    global output2
    global p
    if p==0:
        output="".join([output,line[i][0],"\n"])
    else :
        output2="".join([output2,line[i][0],"\n"])
    

def while_part():
    global i
    global output
    global output2
    global p
    i=i+2
    c=""
    while line[i][0]!="}":   #stores the part to be printed for the while part
        c=c+line[i][0]+"\n"
        i=i+1
    while eval(line[i][1],dicti)==True: #evaluates the test condition for while everytime the loop is run
        if p==0:
            output="".join([output,c])
        else :
            output2="".join([output2,c])
        

def repeat_part():
    global i
    global output
    global output2
    global p
    x=eval(line[i][1],dicti)    #stores the number after repeat
    i=i+2
    c=""
    while line[i][0]!="}":  #stores the part to be repeated
        c="\n".join([c,line[i][0]])
        i=i+1
    for number in range(0,x):#stores c in output as many times s the repeat is given
        if p==0:
            output="".join([output,c])
        else :
            output2="".join([output2,c])
def else_part():
    global i
    global output
    global output2
    global p
    i=i+2
    c=""
    while line[i][0]!="}":  #stores the part to be printed if the else part gets executed
        c=c+line[i][0]+"\n"
        i=i+1
    if eval(line[k][1],dicti)==False:
        if p==0:
            output="".join([output,c])
        else :
            output2="".join([output2,c])

def if_part():
    global i
    global output
    global output2
    global p
    x=eval(line[i][1],dicti)  #evluates the expression in the if part
    i=i+2
    c=""
    while line[i][0]!="}":  #stores the part to be printed if the statement is true
        c=c+line[i][0]+"\n"
        i=i+1
    if x==True:#checks for the condition
        if p==0:
            output="".join([output,c])
        else :
            output2="".join([output2,c])
            
f=open("project1.py",'r')
s=f.read()
if check_braces(s)==0:
    print ("Syntax Error:Please recheck your code")
else:
    line=s.split("\n")        #splits the input into separate lines
    l=len(line)     #computes the number of lines
    i=0#loop variable
    p=0
    output=""   #stores the output
    dicti={}
    
    while i<l:
        line[i]=line[i].strip() #removes the spaces in the beginning and the end
        line[i]=line[i].split(" ") #splits the input into words
        i=i+1

    i=0
    while i<l:
        check_keyword(line[i][0],i)
        i=i+1


p=1
f=open("project2.py",'r')
s=f.read()
if check_braces(s)==0:
    print ("Syntax Error:Please recheck your code")
else:
    line=s.split("\n")        #splits the input into separate lines
    l=len(line)     #computes the number of lines
    i=0         #loop variable
    output2=""   #stores the output
    dicti={}
    
    while i<l:
        line[i]=line[i].strip() #removes the spaces in the beginning and the end
        line[i]=line[i].split(" ") #splits the input into words
        i=i+1

    i=0
    while i<l:
        check_keyword(line[i][0],i)
        i=i+1
    



def shoot_part1():
    c=turtle.Turtle()
    c.hideturtle()
    c.penup()
    c.shape('circle')
    c.shapesize(0.4,0.4)
    c.speed(1)
    pos=a.position()
    angle=a.heading()
    c.setposition(pos)
    c.left(angle)
    c.showturtle()
    c.fd(300)
    c.hideturtle()
def shoot_part2():
    d=turtle.Turtle()
    d.hideturtle()
    d.penup()
    d.shape('circle')
    d.shapesize(0.4,0.4)
    d.speed(1)
    pos=b.position()
    angle=b.heading()
    d.setposition(pos)
    d.left(angle)
    d.showturtle()
    d.fd(300)
    d.hideturtle()
    
    

        
import turtle
a=turtle.Turtle()
b=turtle.Turtle()
a.hideturtle()
b.hideturtle()
a.penup()
b.penup()
a.speed(1)
b.speed(1)
b.setposition(250,0)
b.left(180)
a.showturtle()
b.showturtle()

p=output.split()
q=output2.split()
num1=len(p)
num2=len(q)
if num1<num2:
    num3=num1
else :
    num3=num2
for item in range(num3):
    if p[item]=='turnleft':
        a.left(90)
    elif p[item]=='turnright':
        a.right(90)
    elif p[item]=='forward':
        a.forward(25)
    elif p[item]=='backward':
        a.back(25) 
    elif q[item]=='shoot':
        shoot_part1()
        
    if q[item]=='turnleft':
        b.left(90)
    elif q[item]=='turnright':
        b.right(90)
    elif q[item]=='forward':
        b.forward(25)
    elif q[item]=='backward':
        b.back(25) 
    elif q[item]=='shoot':
        shoot_part2()
        
f.close()
    







    




