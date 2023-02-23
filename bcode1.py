from tkinter import* #tkinter is gui model toolkit

window = Tk() #initialising windows
window.geometry("420x420")#set size of window using geometry fxn
window.title("Fist python GUI")#set title bar

#icon = PhotoImage(file ='img1.avif')#icon is the naming
#window.iconphoto(True,icon)#iconphoto is a function arg1=true arg2=icon name


#config fxn

window.config(background="blue")

#creating labels - an area widget that holds text and/or an imag within tje window


window.mainloop() #to display window
