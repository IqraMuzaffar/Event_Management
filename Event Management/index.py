from threading import Event
from flask import Flask,render_template,request,redirect
app= Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/book")
def book():
    return render_template("book.html")

@app.route("/signup")
def index():
    return render_template('Signup.html')

@app.route("/signin")
def sign():
    return render_template("Signin.html")

import datetime

class User(): #userclass setter and getter functions
   
    def __init__(self, n, r,o,l):
        self.firstname = n
        self.lastname = r
        self.email=o
        self.password=l
    def set_username(self):
        self.username = input("enter username:")
    
    def set_email(self):
        self.email= input("enter email :")
    
    def set_password(self):
        self.password= input("enter password:")
    
    def set_contact(self):
        self.contact=input("enter contact no")
    
    
    def get_contact(self):
        return self.contact
    
    def get_username(self):
        return self.username
    
    def get_email(self):
        return self.email
    
    def get_password(self):
        return self.password
     
    def add_user(self):          #signup
        
        fh=open("register.txt","a")  #appending data
        f=open("register.txt","r+")  #reading data
        c=0
        
       # for line in f:
        #    print(line)
         #   lst=line.split(",")
          #  if self.email==lst[1]: #checks if user already exists
           #     c+=1
            #    print("user alreaddy exists")
             #   f.close()
              #  break
        
        if c==0:              #if user doesnoe exist,adds data

            fh.write(self.firstname + "," +  self.lastname +"," + self.email+ "," + self.password + "\n")
            fh.close()

   
    def login(self):   
        p=self.get_password()
        c=0
        f=open("register.txt","r+")
        for line in f:                                    
            lst=line.split(",")
            
            if self.get_email()==lst[2]: #if email exists
                loginlst=lst                     #email's data
                password=loginlst[3][:-1]   #password for that email
                c+=1
                break
    
        if c==0:
            print("User not registered!")  #not registered when email not found
    
        elif p==password: #password checking
            print("Login successful!")
            return render_template('home.html')
        else:
            print("Invalid Password")
                



class Event():
    
    def __init__(self, a,b,c,d,e,f):
        self.date = a
        self.timing=b
        self.venue=c
        self.capacity=d
        self.category=e
        self.type=f
        
        
    def set_event_category(self):
        print("Event Categories:-----\n 1: Royal \n 2: Simply Elegant ")

        self.category=input("Enter the category/ standard of event:")
        s=self.category
        cat=None
        
        if s=="1":
            cat="Royal"
        
        elif s=="2":
            cat="Simply Elegant"
        else:
            cat="Unavailable"
        
        self.category=cat
    

    
    def set_event_capacity(self):
        print("Capacity of Hall--- \n 1: 200-300 \n 2: 500-600 \n 3: 1000-1200")
        self.capacity=input("Enter the capacity of hall:")
        s=self.capacity
        cat=None
        
        if s=="1":
            cat="200-300"
        
        elif s=="2":
            cat="500-600"
        elif s=="3":
            cat="1000-1200"
        else:
            cat="No such option"
        
        self.capacity=cat
    
   

  
    def set_event_venues(self):
        print("Venues:---\n 1: Golf Garrison HAll \n 2: Topaz Marquee \n 3:Royal Palm")
        self.venue=input("Enter the venue of hall:")
        s=self.venue

        cat=None
        if s=="1":
            cat="Golf Garrison Hall"
        elif s=="2":
            cat="Topaz Marquee"
        elif s=="3":
            cat="Royal Palm"
        else:
            cat="No Such Option"
        
       
        self.venue=cat
       
        

    def set_event_timings(self):
        print("TImings:---\n 1:8am to 11am \n 2: 2pm to 5pm \n 3: 8pm to 11pm")
        self.timing=input("Enter the time of event:")
        s=self.timing
        cat=None
        if s=="1":
            cat="8am to 11am"
        elif s=="2":
            cat="2pm to 5pm"
        elif s=="3":
            cat="8pm to 11pm"
        else:
            cat="No Such Option"
        
        self.timing=cat

 
    
        
    def set_event_type(self):
        
        print("Event Type:---\n 1: Mehndi \n 2: Barat \n 3: Walima \n 4: Birthday/ Party" )
        self.type=input("Enter the type of event:")
        s=self.type
        cat=None
        if s=="1":
            cat="Mehndi"
        elif s=="2":
            cat="Barat"
        elif s=="3":
            cat="Walima"
        elif s=="4":
            cat="Birthday/ Party"
        else:
            cat="No Such Option"
        
        self.type=cat
        


    def set_event_date(self):
        print("Date format: year,month,date")
        self.date=input("Enter the date of event in the mentioned format:")
        
        lst=self.date.split(",")
        lst2=[int(i) for i in lst]
        print(lst2)
        date=datetime.date(lst2[0],lst2[1],lst2[2])
        datelst=[date.year,date.month,date.day]
        self.date="-".join(str(x)for x in datelst)
         

    
    def get_date(self):
        return self.date
    
  
    def get_category(self):
        return self.category
   
        
    def get_timings(self):
        return self.timing
    
    def get_venues(self):
        return self.venue
   
    def get_category(self):
        return self.category
        
  
    def get_capacity(self):
        return self.capacity

    def get_type(self):
        return self.type
   
    
    def book_event(self):
        user=User("","","","")  
        event=Event("","","","","","")
    
        user.set_email()
        
        event.set_event_timings()
        event.set_event_date()


        event.set_event_category()
        event.set_event_type()
        event.set_event_venues()
        event.set_event_capacity()
    
        f=open("event.txt","r+")
        
        fh=open("event.txt","a+")
        for line in f: 
            lst=line.split(",")
            if event.get_timings()==lst[1]:
                if event.get_date()==lst[2]:
                    if event.get_venues()==lst[3]:
                        print("slot and venue already booked!")
                        break
                    else:
                        fh.write(user.get_email()+ "," + event.get_timings() + "," + event.get_date() + "," + event.get_venues() +"," + event.get_type()+ "," + event.get_category() + "," + event.get_capacity() + "\n" )
        fh.close()
        f.close()


@app.route('/signup',methods=['POST'])
def Read_Signup_Values():
    first_name=request.form['first_name']
    last_name=request.form['last_name']
    email=request.form['email']
    password=request.form['password']
    confirmpassword=request.form['confirm_password']
    user=User(first_name,last_name,email,password)
    if confirmpassword==password:
        user.add_user()
    #else:
        #print('Password doesnot match!')
    
    
    return render_template('Signin.html')
 

@app.route("/signin",methods=["GET"])
def Read_Signin_Values():
    email=request.form["email"]
    password=request.form["password"]
   # user=User("","",email,password)
   # user.set_email()
   # user.set_password() 
    print("pakistan")


@app.route("/book",methods=["POST"])
def Read_event_values():
    print("helllo")
    category=request.form["category"]
    type=request.form["type"]
    date=request.form["date"]
    time=request.form["time"]
    capacity=request.form["capacity"]
    venue=request.form["venue"]
    event=Event(date,time,venue,capacity,category,type)
    event.book_event()
    return render_template("home.html")




if __name__=='__main__':
    app.run(debug=True)

