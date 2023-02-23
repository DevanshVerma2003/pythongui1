from tkinter import*
def click():
    print("you clicked the button")
window =Tk()
phomto = PhotoImage(file='image2.png')

btn = Button(window,
            text="Click me!",
            command=click,   #a function/callback for the button
            font=("Comic Sans",30),
            fg="green",
            bg="black",
            activeforeground="green",
            activebackground="black",
            state=ACTIVE, #or disabled
            image=phomto,
            compound='bottom')

            #labels , buttons adjust their size according to the bigger eleement such as the image size or the text length.
            

btn.pack()





window.mainloop()