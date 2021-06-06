from tkinter import *
from tkinter import messagebox 
from PIL import ImageTk,Image
import pywhatkit
import sqlite3
import time
import clx.xms
import requests


F=Tk()
F.config(bg="GREEN")
F.geometry("620x700")



def f1():
	c.delete(0,END)

def f2():
	k=str(c.get())
	c.delete(0,END)
	k=k[:-1]
	f=k
	c.insert(0,k)

def f3(a):
	global p
	global m
	p=a
	m=str(c.get())
	c.delete(0,END)

def f4(b):   
	global f
	r=str(c.get())
	c.delete(0,END)
	f=r+b
	c.insert(0,f)
		
def f5():
	global p
	c.delete(0,END)
	
	if len(p)==0:
		messagebox.showwarning("hello","hello")

	
	
	elif p=="+":
		t=float(m)+float(f)
		c.insert(0,t)

	elif p=="-":
		t=float(m)-float(f)
		c.insert(0,t)
	elif p=="*":
		t=float(m)*float(f)
		c.insert(0,t)
	elif p=="/":
		t=float(m)/float(f)
		c.insert(0,t)
	p=""

def lt():
	my=sqlite3.connect('bol.db')
	c=my.cursor()
	c.execute("SELECT phone From bol where rowid=:fd",
		{
		'fd':dee.get()
		}
				)
	my.commit()

	fut=c.fetchall()
	fut=str(fut[0][0])

	intt=float(wq_e.get())
	loa=int(qq_e.get())
	ti=int(rq_e.get())
	emi=(loa*intt*((1+intt)**ti))//(((1+intt)**ti)-1)

	client = clx.xms.Client(service_plan_id='7c87612a94b94b16b0e6e9f8f3405ccf', token='746e3cb05eca403e89a4fdc27dd0a9c8')

	create = clx.xms.api.MtBatchTextSmsCreate()
	create.sender = '918999453985'
	create.recipients = {'91'+str(fut)}
	create.body = str(ye)+" you have a loan of "+str(qq_e.get())+" with the interest of "+str(wq_e.get())+" you have to give us RS"+str(emi)+" per month"
	try:
	  batch = client.create_batch(create)
	except (requests.exceptions.RequestException,
	  clx.xms.exceptions.ApiException) as ex:
	  print('Failed to communicate with XMS: %s' % str(ex))

	my.close()


def oi():
	mu=sqlite3.connect('loan.db')
	c=mu.cursor()
	c.execute("INSERT INTO loan VALUES(:a,:b,:c) ",
		{
		'a':ye,
		'b':qq_e.get(),
		'c':wq_e.get()

		}

		)
	

	mu.commit()
	mu.close()

def lon():
	k=Tk()
	k.config(bg="ORANGE")

	global qq_e,wq_e,rq_e

	qq=Label(k,text="Enter the amount loan: ",bg="YELLOW",font=('Arial',20))
	qq.grid(row=1,column=0,padx=5,pady=5)

	wq=Label(k,text="Enter Interest rate per month: ",bg="YELLOW",font=('Arial',20))
	wq.grid(row=2,column=0,padx=5,pady=5)

	rq=Label(k,text="Enter return time in month: ",bg="YELLOW",font=('Arial',20))
	rq.grid(row=3,column=0,padx=5,pady=5)

	qq_e=Entry(k,width=40,bd=10)
	qq_e.grid(row=1,column=1)

	wq_e=Entry(k,width=40,bd=10)
	wq_e.grid(row=2,column=1)

	rq_e=Entry(k,width=40,bd=10)
	rq_e.grid(row=3,column=1)

	but=Button(k,text="Ok",bg="RED",command=oi,height=5,width=10)
	but.grid(row=4,column=0,padx=5,pady=5)

	send=Button(k,text="send",bg="RED",command=lt,height=5,width=10)
	send.grid(row=4,column=1,padx=5,pady=5)

def withdraw():
	global kg
	my=sqlite3.connect('bol.db')
	c=my.cursor()
	c.execute("SELECT Amount From bol where rowid=:fd",
		{
		'fd':dee.get()
		}
				)
	kg=c.fetchall()
	kg=int(kg[0][0])

	kg=kg-int(we.get())

	my.commit()
	my.close()

def py():
	my=sqlite3.connect('bol.db')
	c=my.cursor()
	global fu

	c.execute("""UPDATE bol SET 

		Amount=:lh where rowid=:kj""",
		{
		'lh':str(kg),
		'kj':dee.get()
		}
		)
	my.commit()
	c.execute("SELECT Amount,Phone from bol where rowid=:fi",
		{
		'fi':dee.get()
		}

		)
	f=c.fetchall()
	c=str(f[0][0])
	fu=str(f[0][1])
	



	#message="You Have RS: "+f+" in your bachatgat"
	#pywhatkit.sendwhatmsg('+91 9359831337',message,19,20)
	client = clx.xms.Client(service_plan_id='7c87612a94b94b16b0e6e9f8f3405ccf', token='746e3cb05eca403e89a4fdc27dd0a9c8')

	create = clx.xms.api.MtBatchTextSmsCreate()
	create.sender = '918999453985'
	create.recipients = {'91'+str(fu)}
	create.body = "Rs "+str(we.get())+" are added to your account Hence your total balance is "+str(c)

	try:
	  batch = client.create_batch(create)
	except (requests.exceptions.RequestException,
	  clx.xms.exceptions.ApiException) as ex:
	  print('Failed to communicate with XMS: %s' % str(ex))

	my.commit()
	my.close()

def pr():
	global kg
	my=sqlite3.connect('bol.db')
	c=my.cursor()
	c.execute("SELECT Amount From bol where rowid=:fd",
		{
		'fd':dee.get()
		}


				)
	kg=c.fetchall()
	kg=int(kg[0][0])

	kg=kg+int(we.get())

	my.commit()
	my.close()

def tr():
	global s
	global we
	global ye
	s=Toplevel()
	s.config(bg="GREEN")
	my=sqlite3.connect('bol.db')
	c=my.cursor()
	c.execute("SELECT First_name,Middle_name,Last_name From bol where rowid=:k",
		{
		'k':dee.get()
		}
		)

	f=c.fetchall()

	ye=" ".join(f[0])
	sa=StringVar()
	sa.set("")

	Ima=ImageTk.PhotoImage(Image.open("trans.jpg"))

	Imag=Label(s,image=Ima)
	Imag.grid(row=1,column=0,columnspan=3,padx=20,pady=15)

	hel=Label(s,text="Welcome "+str(ye),font=('Arial',20),bg="RED")
	hel.grid(row=0,column=0,columnspan=3)

	fra=Frame(s,padx=5,pady=5,bg="CYAN")
	fra.grid(row=2,column=0,padx=5,pady=5,columnspan=3)

	wq=Label(fra,text="Amount you want to add/withdraw:",font=('Arial',20),bg="RED")
	wq.grid(row=3,column=0,padx=5,pady=5)

	we=Entry(fra,width=50,bd=5)
	we.grid(row=3,column=2)
	
	ro=Button(fra,text="ADD",command=pr,height=5,width=10,bg="BLUE")

	ro.grid(row=4,column=0,padx=5,pady=10)

	ro=Button(fra,text="Withdraw",command=withdraw,height=5,width=10,bg="BLUE")

	ro.grid(row=4,column=2,padx=5,pady=10)

	Done=Button(fra,text="DONE",command=py,bg="BLUE",height=5,width=10)

	Done.grid(row=5,column=1,padx=5,pady=5)

	lon_l=Label(s,text="Do you want a loan: ",bg="ORANGE",font=('Arial',20))
	lon_l.grid(row=6,column=0,padx=5,pady=20)

	Loan=Button(s,text="YES",command=lon,height=5,width=10,bg="BLUE")
	Loan.grid(row=6,column=1,padx=5,pady=20)

	Loa=Button(s,text="NO",command=s.destroy,height=5,width=10,bg="BLUE")
	Loa.grid(row=6,column=2,padx=5,pady=20)

	my.commit()
	my.close()

	s.mainloop()

def register():
	r=Tk()
	r.config(bg="GREEN")
	my=sqlite3.connect('bol.db')
	c=my.cursor()
	global First_name_e,Last_name_e,Middle_name_e,Phone_e,Amount_e,Add_e

	Request=Label(r,text="PLEASE FILL FORM",font=('Arial',20),bg="RED")
	Request.grid(row=0,column=0,columnspan=2)

	First_name=Label(r,text="FIRST NAME:",bg="RED")
	First_name.grid(row=1,column=0,padx=5,pady=5)

	Middle_name=Label(r,text="MIDDLE NAME:",bg="RED")
	Middle_name.grid(row=2,column=0,padx=5,pady=5)

	Last_name=Label(r,text="LAST NAME:",bg="RED")
	Last_name.grid(row=3,column=0,padx=5,pady=5)

	Phone=Label(r,text="  PHONE :",bg="RED")
	Phone.grid(row=4,column=0,padx=5,pady=5)

	Add=Label(r,text="  ADDRESS :",bg="RED")
	Add.grid(row=5,column=0,padx=5,pady=5)

	Amount=Label(r,text="  Amount :",bg="RED")
	Amount.grid(row=6,column=0,padx=5,pady=5)

	First_name_e=Entry(r,width=50,bd=5)
	First_name_e.grid(row=1,column=1,padx=5,pady=5)

	Middle_name_e=Entry(r,width=50,bd=5)
	Middle_name_e.grid(row=2,column=1,padx=5,pady=5)

	Last_name_e=Entry(r,width=50,bd=5)
	Last_name_e.grid(row=3,column=1,padx=5,pady=5)

	Phone_e=Entry(r,width=50,bd=5)
	Phone_e.grid(row=4,column=1,padx=5,pady=5)

	Add_e=Entry(r,width=50,bd=5)
	Add_e.grid(row=5,column=1,padx=5,pady=5)

	Amount_e=Entry(r,width=50,bd=5)
	Amount_e.grid(row=6,column=1,padx=5,pady=5)

	g=Button(r,text="Enter",height=5,width=10,command=lo,bg="BLUE")
	g.grid(row=7,column=0,padx=5,pady=5,columnspan=2)

	

def li():
	
	h=Tk()
	my=sqlite3.connect('bol.db')
	c=my.cursor()

	c.execute("SELECT rowid,* FROM bol")
	f=c.fetchall()
	
	scroll_bar = Scrollbar(h) 
  
	scroll_bar.pack( side = RIGHT, 
					fill = Y ) 
	   
	mylist = Listbox(h,  
					 yscrollcommand = scroll_bar.set,width=80 ) 
	t=len(f)
	k=len(f[0])
	   
	for i in range(t): 
		e=""
		for j in range(k):
			e=e+str(f[i][j])+"   "



		mylist.insert(END, e) 
	  
	mylist.pack( side = LEFT, fill = BOTH ) 
	  
	scroll_bar.config( command = mylist.yview ) 
	   


	
	my.commit()
	my.close()

def lo():
	


	
	my=sqlite3.connect('bol.db')
	c=my.cursor()
		
	c.execute("INSERT INTO bol VALUES(:f,:m,:l,:p,:ad,:am)",
		{
		'f':First_name_e.get(),
		'm':Middle_name_e.get(),
		'l':Last_name_e.get(),
		'p':Phone_e.get(),
		'ad':Add_e.get(),
		'am':Amount_e.get()
		}
		)
	my.commit()
	my.close()


def so():
	n=Tk()
	n.config(bg="GREEN")

	global First_name_ed,Last_name_ed,Middle_name_ed,Phone_ed,Amount_ed,Add_ed

	Up_req=Label(n,text="Update Your Record",font=('Arial',20),bg="RED")
	Up_req.grid(row=0,column=0,columnspan=2)

	First_name=Label(n,text="FIRST NAME:",bg="RED")
	First_name.grid(row=1,column=0,padx=5,pady=5)

	Middle_name=Label(n,text="MIDDLE NAME:",bg="RED")
	Middle_name.grid(row=2,column=0,padx=5,pady=5)

	Last_name=Label(n,text="LAST NAME:",bg="RED")
	Last_name.grid(row=3,column=0,padx=5,pady=5)

	Phone=Label(n,text="  PHONE :",bg="RED")
	Phone.grid(row=4,column=0,padx=5,pady=5)

	Add=Label(n,text="  ADDRESS :",bg="RED")
	Add.grid(row=5,column=0,padx=5,pady=5)

	First_name_ed=Entry(n,width=50,bd=5)
	First_name_ed.grid(row=1,column=1,padx=5,pady=5)

	Middle_name_ed=Entry(n,width=50,bd=5)
	Middle_name_ed.grid(row=2,column=1,padx=5,pady=5)

	Last_name_ed=Entry(n,width=50,bd=5)
	Last_name_ed.grid(row=3,column=1,padx=5,pady=5)

	Phone_ed=Entry(n,width=50,bd=5)
	Phone_ed.grid(row=4,column=1,padx=5,pady=5)

	Add_ed=Entry(n,width=50,bd=5)
	Add_ed.grid(row=5,column=1,padx=5,pady=5)

	g=Button(n,text="Enter",height=5,width=10,command=qo,bg="BLUE")
	g.grid(row=7,column=0,padx=5,pady=5,columnspan=2)

def to():
	
	my=sqlite3.connect('bol.db')
	c=my.cursor()
	
	c.execute("DELETE FROM bol where rowid=:u",
		{

		'u':dee.get()
		}

		)


	my.commit()
	my.close()

def qo():

	my=sqlite3.connect('bol.db')
	c=my.cursor()

	c.execute("""UPDATE bol SET 


		First_name= :a,
		Middle_name= :b,
		Last_name= :c,
		Phone= :d,
		Address= :e
		
		 where rowid= :g""",
		 {

		 'a':First_name_ed.get(),
		 'b':Middle_name_ed.get(),
		 'c':Last_name_ed.get(),
		 'd':Phone_ed.get(),
		 'e':Add_ed.get(),
		 'g':dee.get()
		 }
		)


	
	my.commit()
	my.close()

def calu():
	r=Tk()
	r.title("Calculator")
	r.resizable(0,0)
	
	c=Entry(r,width=60,bd=5)
	c.grid(row=0,column=0,columnspan=4)

	c.insert(0,"0")


	p=""
	b1=Button(r,text="AC",command=f1,padx=48,pady=20,bg="black",fg="green")
	b2=Button(r,text="<-",command=f2,padx=50.3,pady=20,bg="black",fg="green")
	b3=Button(r,text="  ",command=f1,padx=50,pady=20,bg="black",fg="green")
	b4=Button(r,text="/ ",command=lambda:f3("/"),padx=50,pady=20,bg="black",fg="green")
	b5=Button(r,text=" 7 ",command=lambda:f4("7"),padx=50,pady=20,bg="black",fg="green")
	b6=Button(r,text=" 8 ",command=lambda:f4("8"),padx=51,pady=20,bg="black",fg="green")
	b7=Button(r,text="9",command=lambda:f4("9"),padx=50,pady=20,bg="black",fg="green")
	b8=Button(r,text="* ",command=lambda:f3("*"),padx=50,pady=20,bg="black",fg="green")
	b9=Button(r,text=" 4 ",command=lambda:f4("4"),padx=50,pady=20,bg="black",fg="green")
	b10=Button(r,text=" 5 ",command=lambda:f4("5"),padx=51,pady=20,bg="black",fg="green")
	b11=Button(r,text="6",command=lambda:f4("6"),padx=50,pady=20,bg="black",fg="green")
	b12=Button(r,text="+  ",command=lambda:f3("+"),padx=47,pady=20,bg="black",fg="green")
	b13=Button(r,text=" 1 ",command=lambda:f4("1"),padx=50,pady=20,bg="black",fg="green")
	b14=Button(r,text=" 2 ",command=lambda:f4("2"),padx=51,pady=20,bg="black",fg="green")
	b15=Button(r,text="3",command=lambda:f4("3"),padx=50,pady=20,bg="black",fg="green")
	b16=Button(r,text="- ",command=lambda:f3("-"),padx=50,pady=20,bg="black",fg="green")
	b17=Button(r,text="0 ",command=lambda:f4("0"),padx=113,pady=20,bg="black",fg="green")
	b18=Button(r,text=". ",command=lambda:f4("."),padx=50,pady=20,bg="black",fg="green")
	b19=Button(r,text="=",command=f5,padx=50,pady=20,bg="black",fg="green")

	b1.grid(row=1,column=0)
	b2.grid(row=1,column=1)
	b3.grid(row=1,column=2)
	b4.grid(row=1,column=3)
	b5.grid(row=2,column=0)
	b6.grid(row=2,column=1)
	b7.grid(row=2,column=2)
	b8.grid(row=2,column=3)
	b9.grid(row=3,column=0)
	b10.grid(row=3,column=1)
	b11.grid(row=3,column=2)
	b12.grid(row=3,column=3)
	b13.grid(row=4,column=0)
	b14.grid(row=4,column=1)
	b15.grid(row=4,column=2)
	b16.grid(row=4,column=3)
	b17.grid(row=5,column=0,columnspan=2)
	b18.grid(row=5,column=2)
	b19.grid(row=5,column=3)



global dee


Welcome=Label(F,text="Wecome Again",font=('Arial',50),bg="RED")
Welcome.grid(row=0,column=0,padx=20,pady=15,columnspan=3)

Ima=ImageTk.PhotoImage(Image.open("bac.jpg"))

Imag=Label(F,image=Ima)
Imag.grid(row=1,column=0,columnspan=3,padx=20,pady=15)

Register=Button(F,text="Register",command=register,height=5,width=10,bg="BLUE")
Register.grid(row=2,column=0,padx=5,pady=5)

cal=Button(F,text="Calc",command=calu,height=5,width=10,bg="BLUE")
cal.grid(row=2,column=1,padx=5,pady=5)

List=Button(F,text="Detail",command=li,height=5,width=10,bg="BLUE")
List.grid(row=2,column=2,padx=5,pady=5)

frame=LabelFrame(F,text="Operations",padx=10,pady=10,bd=6,bg="YELLOW")
frame.grid(row=3,column=0,columnspan=3,padx=10,pady=10)


de=Label(frame,text="Enter The ID:",font=('Times New Roman',18),bg="RED")
de.grid(row=4,column=0,padx=5,pady=5)

dee=Entry(frame,width=20,bd=5)
dee.grid(row=4,column=1)

Delete=Button(frame,text="Delete",command=to,height=5,width=10,bg="BLUE")
Delete.grid(row=5,column=1,padx=5,pady=5)

Update=Button(frame,text="Update",command=so,height=5,width=10,bg="BLUE")
Update.grid(row=5,column=0,padx=5,pady=5)

Transaction=Button(frame,text="Transaction",command=tr,height=5,width=10,bg="BLUE")
Transaction.grid(row=5,column=2,padx=5,pady=5)



F.mainloop()





