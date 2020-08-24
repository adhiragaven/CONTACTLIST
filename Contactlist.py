from tkinter import *

def details():
    def save():
        txt=n1.get()
        txt1=num1.get()
        txt2=mail1.get()
        with open("Docu.txt","a+") as file:
            file.write("-Name:"+txt+"\n"+"Ph.no:"+txt1+"\n"+"Email:"+txt2+"-"+"\n\n")
        d.destroy()
    
    d=Tk()
    d.title("Details")
    name=Label(d, text="Name:")
    n1=Entry(d, width=25)
    num=Label(d, text="Ph.no:")
    num.grid(row=2,column=0)
    num1=Entry(d, width=25)
    num1.grid(row=2,column=1)
    mail=Label(d, text="Email:")
    mail.grid(row=3,column=0)
    mail1=Entry(d, width=25)
    mail1.grid(row=3,column=1)
    name.grid(row=1,column=0)
    n1.grid(row=1, column=1)
    s=Button(d, text="Save", width=15, command=save)
    s.grid(row=4,column=1)
    d.mainloop()
def search():
    #searc=Entry(con, textvariable=var, width=35)
    s=new.get()
    with open('Docu.txt','r+') as file:
        txt=file.read()
        txt=txt.split("-")
        for i in txt:
            if s in i:
                new2.delete(1.0, END)
                new2.insert(END,i)
        
def Display():
    with open('Docu.txt','r+') as file:
        txt=file.read()
        txt=txt.split("-")
        new2.delete(1.0, END)
        for i in txt:
            new2.insert(END, i)
        
def Delete():
    def confirm():
        p=se.get()
        o=[]
        with open('Docu.txt','r+') as f:
            content=f.read()
            content=content.split("-")
            k=""
            c=[]
            for i in content:
                k="-"+i+"-"
                c.append(k)
            for i in c:
                if p in i:
                    o.append("--")
                    o.append(i)
                    o.append("-\n\n-")
            f.seek(0)
            for i in c:
                if not any(j in i  for j in o):
                    f.write(i)
                    f.write("\n\n")
        
            f.truncate()
        l.destroy()
    

    def delet():
        s=se.get()
        with open('Docu.txt','r+') as file:
            txt=file.read()
            txt=txt.split("-")
            new3.delete(1.0,END)
            for i in txt:
                if s in i:
                    #new3.delete(1.0, END)
                    new3.insert(END,i)

        conf=Button(l, text="Confirm Delete", width=20, command=confirm)
        conf.pack()
        new3.pack()
    l=Tk()
    l.geometry("200x250")
    l.title("Delete")
    en=Label(l, text="Enter the name of contact to delete:")
    se=Entry(l, width=35)
    cd=Button(l, text="Delete", width=20, command=delet)
    new3=Text(l, height=10, width=35)
    en.pack()
    se.pack()
    cd.pack()
    l.mainloop()
con=Tk()
con.geometry("400x300")
con.title('Contact list')
f=Frame(con)
f.pack()
var=StringVar()
new2=Text(con, height=10, width=35)
new=Entry(con, width=35)
add=Button(f, text="Add", command=details)
add.pack(side=LEFT)
# add.grid(row=1,column=0)
sear=Button(f, text="Search", command=search)
sear.pack(side=LEFT)
new1=Label(con, text="Enter name or contact to search")
new1.pack()
dis=Button(f, text="Display", command=Display)
dis.pack(side=LEFT)
dele=Button(f, text="Delete", command=Delete)
dele.pack(side=LEFT)
#new2.delete(1.0, END)
#Dis=Text(con, width=30)
#Dis.pack()
#sear.grid(row=1,column=1)
new.pack()
new2.pack()
 #new.grid(row=2,column=1)
con.mainloop()