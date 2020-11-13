players=[]
player=[]
draw=False
global choice
def get_check(name=''):
  if name=='':
     name=input("Enter your username:")
  with open("loginfo.txt",'r') as c:
   words=c.read().split()
   for i in range(0,len(words),2):
    if(name == words[i]):
      print("Username Already Exists,Try other username")
      return get_check(input("Username:"))
  return name

def get_login_name():
  name=input("Username:")
  if name not in players:
     return name
  else:
    print("Already Logged in User,Please log in with another username")
    return get_login_name()     
   
def encrypt(password):
  encrypted_password=''
  notrev_list="abAO1cNdB2PMDe3EfRgLQC4hiS5Ujk6TVKlFmH7noW8GYpq9XIrZstuvJwxyz"
  rev_list=notrev_list[::-1]
  for i in range(len(password)):
     if password[i].isalnum():
      indexx=notrev_list.index(password[i])
     else:
       indexx=0
     encrypted_password=encrypted_password+rev_list[indexx]
  return encrypted_password 

def login():
  with open("loginfo.txt",'r') as f:
    username=get_login_name()
    password=input("password:")
    login_info=f.readlines()
    for i in login_info:
      splitup=i.split()
      if(username==splitup[0]):
         if(encrypt(password)==splitup[1]):
            players.append(username)
            return True
             
         else:
             print("Invalid password")
             print("Try again")  
             return login()
    print("please enter a valid username")
    login()
    
  return False    
         
def register():
  with open("loginfo.txt",'a') as f:
    with open("rank.txt","a") as f1:
     newusername=get_check()
     f.write(newusername)#name
     players.append(newusername)
     f.write(" ")
     newpassword=input("password:")
     f.write(encrypt(newpassword)) #password
     f.write(" ")
     f.write("\n")
     f1.write(newusername+" "+"0\n")
  return True
  
print("  ____________________WELCOME TO TIC-TAC-TOE 2.0____________________")
def loginpage():
  for i in range(2):
   choice=int(input("1-Register\n2:Login\nYour Choice :"))
   if not str(choice).isdigit():
     choice=int(input("1-Register\n2:Login\nYour Choice :"))

   if(choice==1):
     print(" New User ? Okay let's Sign up")
     success=register()
   else:
     print("Already Registered User? Please Login to Continue")
     success=login()
   print()
   
   
  if(success==True):
    print("_____LOGIN SUCCESS,LET'S START!!_____")
    global choice1
    import random
    choice1=random.randint(1,2)
    if choice1==1:
      cho=['x','o']
    else:
      cho=['o','x']  
    for i in range(2):
        print("  "+players[i]+"- Your alloted symbol is "+cho[i])
    print()
    return True
  else:
    print("Incorrect user name or password\nEnter again please")
    loginpage()

def getpos(sym):
     
    a=input("\nEnter where to put "+sym+": ")
    if a.isdigit():
        return int(a)
    else:
        print("Enter a Number Please\n")
        return getpos(sym)
       
    return a
def initialize(n,sym):
    if n not in list:
        list.append(n)
        if(level=="HARD"):
            if 0<n<6: a[0][n-1]=sym
            elif 6<=n<11: a[1][n-6]=sym
            elif 11<=n<16: a[2][n-11]=sym
            elif 16<=n<21: a[3][n-16]=sym
            elif 21<=n<26: a[4][n-21]=sym
            else:
                print("Enter a number between 1-25")
                intialize(getpos(sym),sym)
            
        else:
            if 1<=n<4:
                 a[0][n-1]=sym
            elif 4<=n<7:
                 a[1][n-4]=sym
            elif 7<=n<10:
                 a[2][n-7]=sym
            else:
                print("Enter a number between 1-9")
                initialize(getpos(sym),sym) 
    else:
        print("Already filled slot, Try to put",sym,"somewhere else")
        initialize(getpos(sym),sym)
def check(sym):
    if(level=="HARD"):
        num=5
    else:
        num=3
    Continue=True
    
    
    for i in range(num):
        for j in range(num-2):
                 
            if a[i][j]==a[i][j+1]==a[i][j+2]==sym:
               a[i][j],a[i][j+1],a[i][j+2]=sym.upper()*3
               printans(sym)
               Continue=False
               return
            elif (a[j][i]==a[j+1][i]==a[j+2][i]==sym):
                a[j][i],a[j+1][i],a[j+2][i]=sym.upper()*3
                printans(sym)
                Continue=False
                return           
     
       
    if(Continue):
        num=num-2
        for i in range(num):
            for j in range(num):
                if a[i][j]==a[i+1][j+1]==a[i+2][j+2]==sym:
                    a[i][j],a[i+1][j+1],a[i+2][j+2]=sym.upper()*3
                    printans(sym)
                    Continue=False
                    return

                elif (a[i][j+2]==a[i+1][j+1]==a[i+2][j]==sym):
                    a[i][j+2],a[i+1][j+1],a[i+2][j]=sym.upper()*3
                    printans(sym)
                    Continue=False
                    return
                  
    if Continue:
     draw1()
     if draw==True:
       return   
    printtab()
    
def draw1():
  global level
  global draw
  if level=="EASY":
    order_mat=3
  elif level=="HARD":
    order_mat=5

  draw=True
  for i in range(order_mat):
    for j in range(order_mat):
      if(str(a[i][j]).isdigit()):
          draw=False
  if(draw==True):
         print("_____MATCH TIED !!_____\n  ")
         End=True
         return    
def printtab():
    for i in range(len(a)):
        print("\t",end='')
        for j in range(len(a[0])):
            space=" "           
            if (str(a[i][j])=='x') or (str(a[i][j])=='o'):
                space=" "
            elif(str(a[i][j]).isdigit()):
               if int(a[i][j])>9:
                space=""
            elif a[i][j]=="":
                space="  "
            else:
              space=" "
            print("|"+str(a[i][j])+space,end="")
        print()        
      
def printans(sym):
    global End
    global player
    global choice1
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j]!=sym.upper():
                a[i][j]=''
    if((sym=='o' and choice1==1) or(choice1==2 and sym=='x')):
      player=players[::-1]
    else:
      player=players[::]
    print("    ________WINNER________\n\t   ",player[0],"\nWINNER WINNER CHICKEN DINNER,"+player[0].upper())
    print("   YOU TOO PLAYED WELL "+player[1].upper())
    End=True
    printtab()
    
def chooselevel(level):
    if level=="1":
        print("I really thought you would play HARD MODE")
        print("_____EASY GAMEPLAY_____")
        return 3,"EASY"
    elif level=="2":
        print("That's the spirit!")
        print("_____HARD GAMEPLAY_____")
        return 5,"HARD"
    else:
        print("There is no legend level, Please select 1 or 2")


def order():
 with open("rank.txt","r") as f:
  words=[[word for word in lines.split()]for lines in f.readlines()]
  n=len(words)-1
  if not draw :
   for i in range(n+1):
    if words[i][0]==player[0]:
       words[i][1]=str(int(words[i][1])+1)
    elif words[i][0]==player[1]:
       words[i][1]=str(int(words[i][1])-1)    
   for i in range(n):
     for j in range(n-i):     
      if int(words[j][1])<int(words[j+1][1]):
         words[j],words[j+1]=words[j+1],words[j]
  copywords=words[:]

 with open("rank.txt","w") as f:
   for i in copywords:
      for j in i:
        f.write(j)
        f.write(" ")
      f.write("\n")

 with open("rank.txt","r") as f:
    print("\n _____RANK LIST_____")
    lines_list=f.readlines() 
    for i in range (len(lines_list)):
      line=lines_list[i].split()
      print(str(i+1)+"."+line[0]+" Points: "+line[1]+"\n")


                                      # __main__

from time import sleep
                             
loginpage()
print("Enter the Game Mode")
n,level=chooselevel(input("1:EASY,2:HARD\n"))
print("\t PLEASE WAIT,THE GAME IS LOADING........")
print("\n")
sleep(5)
print("\t\tLET'S START")
End=False
i=0
count=1
list=[]
a=[[x for x in range(n)]for i in range(n)]
for i in range(n):
    for j in range(n):
        a[i][j]=count                   
        count=count+1
printtab()

while(not End):     
    initialize(getpos('x'),'x')
    print()
    check('x')
    if draw==True:
      break
    if not End:
        initialize(getpos('o'),'o')
        check('o')
order()

print("Thanks for Playing...")
sleep(15)
  
      
        
                   
             
