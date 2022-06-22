from tkinter import *
# import tkinter
import os

sd = Tk()
sd.title('Allahhuakbar')
sd.geometry('500x430')
sd.resizable(False, False)
sd.config(bg='Green')


def restart():
    os.system('shutdown /r /t 1')

def restart_time():
    os.system('shutdown /r /t 20')

def log_out():
    os.system('shutdown -1')

def shut_down():
    os.system('shutdown /s /t 1')

restart_btn = Button(sd, text="Restart", font=('Arial', '20', 'bold'), relief=RAISED, cursor='plus', command=restart)
restart_btn.place(x=150, y=70, height=50, width=200)

restart_btn_time = Button(sd, text="Restart Time", font=('Arial', '20', 'bold'), relief=RAISED, cursor='plus', command=restart_time)
restart_btn_time.place(x=150, y=150, height=50, width=200)

log_out_btn = Button(sd, text="Log Out", font=('Arial', '20', 'bold'), relief=RAISED, cursor='plus', command=log_out)
log_out_btn.place(x=150, y=230, height=50, width=200)

shutdown_btn = Button(sd, text="Shut Down", font=('Arial', '20', 'bold'), relief=RAISED, cursor='plus',command=shut_down)
shutdown_btn.place(x=150, y=310, height=50, width=200)



sd.mainloop()


# print(dir(sd))

# Executing a shell command
# os.system() 

# cwd = os.getcwd() 
      
# # Print the current working 
# # directory (CWD) 
# print("Current working directory:", cwd) 
