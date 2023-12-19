from tkinter import *
window = Tk()
window.geometry("400x300")
window.title("To_Do_List")
window.configure(background="lightgreen")
def fib_generator(n):
    if n <= 1:
        return n
    else:
        return (fib_generator(n-1) + fib_generator(n-2))
label_1 = Label(window,text='Welcome to Fibonacci Generator!',bg = 'lightgreen',font=('Century 15 bold',15,'bold'))
label_1.place(x = 30 ,y = 15)
label_2 = Label(window,text= 'Enter how many series you want?',bg = 'lightgreen',font=('Century 15 bold',15,'bold'))
label_2.place(x=30,y=150)
entry_1 = Entry(window,font=('Century 15 bold',15,'bold'),width= 32)
entry_1.place(x = 20 , y = 80)
butt = Button(window,text='Get',font=('Century 15 bold',13,'bold'),command = lambda : butt_pressed())
butt.place(x=170,y = 200)
l= []
def butt_pressed():
    key = int(entry_1.get())
    if key == 0 :
        return 0
    else:
        for i in range(abs(int(key))):
            l.append(fib_generator(i))
    win2 = Tk()
    win2.title('Here We Go!!!')
    label_3 = Label(win2,font=('Century 15 bold',15,'bold'),text= '')
    label_3.pack()
    label_3['text'] = str(l)
    l.clear()
window.mainloop()