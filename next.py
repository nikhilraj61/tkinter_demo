import tkinter

t=tkinter.Tk()
t.geometry('500x500')
t.title('next_page')
t.configure(bg='cyan')

a=tkinter.Label(text="DEMO_PAGE.PY",bg='green',fg="white",font=('bradleyhanditc' ,25,'bold'))
a.pack()
S = tkinter.Scrollbar(t)
T = tkinter.Text(t, height=4, width=50)
S.pack(side=tkinter.RIGHT, fill=tkinter.Y)
T.pack(side=tkinter.LEFT, fill=tkinter.Y)
S.config(command=T.yview)
T.config(yscrollcommand=S.set)
quote = """HAMLET: To be, or not to be--that is the question:
Whether 'tis nobler in the mind to suffer
The slings and arrows of outrageous fortune
Or to take arms against a sea of troubles
And by opposing end them. To die, to sleep--
No more--and by a sleep to say we end
The heartache, and the thousand natural shocks
That flesh is heir to. 'Tis a consummation
Devoutly to be wished."""
T.insert(tkinter.END, quote)

# Fact = """A man can be arrested in
# Italy for wearing a skirt in public."""


t.mainloop()