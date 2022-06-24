# package: https://github.com/sivel/speedtest-cli

from enum import auto
import speedtest
from tkinter import *

def speedcheck():
    st = speedtest.Speedtest()
    st.get_servers()
    upload = str(round(st.upload()/(10**6), 2)) + ' Mbps'
    download = str(round(st.download()/(10**6), 2)) + ' Mbps'
    label_up.config(text=upload)
    label_down.config(text=download)

isc = Tk()
isc.title('Internet Speed Check')
isc.resizable(False, False)
isc.geometry('300x400')
isc.config(bg='#FFDA6E')

label = Label(isc, text='Internet Speeed', fg='#000', bg='#FFDA6E', font=('Arial', '20', 'bold'))
label.place(x=50, y=25, height=25, width=200)

label = Label(isc, text='Download Speeed', fg='#000', bg='#FFDA6E', font=('Arial', '16'))
label.place(x=50, y=75, height=25, width=200)

label_down = Label(isc, text='00', fg='Green', bg='#FFDA6E', font=('Arial', '14'))
label_down.place(x=50, y=125, height=25, width=200)

label = Label(isc, text='Upload Speeed', fg='#000', bg='#FFDA6E', font=('Arial', '16'))
label.place(x=50, y=200, height=25, width=200)

label_up = Label(isc, text='00', fg='Red', bg='#FFDA6E', font=('Arial', '14'))
label_up.place(x=50, y=250, height=25, width=200)

speed_btn = Button(isc, text="Check", bg='#DF9E00', font=('Arial', '16'), relief=RAISED,command=speedcheck)
speed_btn.place(x=50, y=300, height=50, width=200)

isc.mainloop()


