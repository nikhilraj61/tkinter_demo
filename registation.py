import tkinter
import tkinter . messagebox
from PIL import ImageTk, Image
from subprocess import call


t=tkinter.Tk()
t.title("reg_form")
t.geometry("500x500")
t.configure(bg="black")

p=Image.open('one.jpg')#image and location
p=p.resize((500,500))#resize
p=ImageTk.PhotoImage(p)

pic=tkinter.Label(t,image=p)#converting image ito alabel
pic.place(x=0,y=0)

#heading
a=tkinter.Label(text="profile_creation",bg='green',fg="white",font=('bradleyhanditc' ,25,'bold'))
a.place(x=90,y=0)

b=tkinter.Label(text='Name:',bg='blue',fg='white',font=('ariel',25,'italic'))
b.place(x=50,y=120)
ab=tkinter.Entry(width=30)
ab.place(x=200,y=130)

# c=tkinter.Entry(width=30)
d=tkinter.Label(text='Location:',bg='blue',fg='white',font=('ariel',25,'italic'))
d.place(x=50,y=190)
e=tkinter.Entry(width=30)
e.place(x=200,y=200)

f=tkinter.Label(text='email:',bg='blue',fg='white',font=('ariel',25,'italic'))
f.place(x=50,y=265)
g=tkinter.Entry(width=30)
g.place(x=200,y=275)

h=tkinter.Label(text='age:',bg='blue',fg='white',font=('ariel',25,'italic'))
h.place(x=50,y=340)
i=tkinter.Entry(width=30)
i.place(x=200,y=355)



def abcd():
    name=ab.get()
    location=e.get()
    email=g.get()
    age=i.get()
    
    

    if (name=="" or age==""):
        tkinter.messagebox.showerror('error??','please complete the feilds')
    else:
        import pymysql
        x=pymysql.connect(host='localhost',user='root',password='dedsec',db='mango')
        cur=x.cursor()
        cur.execute("insert into ruff values('"+name+"','"+location+"','"+email+"','"+age+"')")
        x.commit()
        x.close()
        tkinter.messagebox.showinfo('Succes','the data stored succesfully')
        t.destroy()

        call(['python','next.py'])

j=tkinter.Button(text="SUBMIT",bg='red',fg="white",height= 1, width=10,command=abcd)
j.place(x=300,y=420)


t.mainloop()
   
