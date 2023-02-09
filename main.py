from tkinter import *
import speedtest

def speedcheck():
    sp = speedtest.Speedtest()
    # SPEED MODULE SE SPEEDTEST CALLS
    sp.get_servers()
    down = str(round(sp.download()/(10**6),3)) + " Mbps "
    # BITS/SEC TO MBPS DIVIDE BY 10^6
    up = str(round(sp.upload()/(10**6),3)) + " Mbps "
    lab_down.config(text=down)
    lab_up.config(text=up)


sp=Tk()
sp.title(" Internet Speed Check ")
sp.geometry("500x500")
sp.config(bg="lightyellow")
sp.minsize(500,500)
sp.maxsize(500,500)
lab=Label(sp,text="Internet Speed Check",font=("Time New Roman",22,"bold",),bg="lightyellow",fg="red")
lab.place(x=120,y=50)

lab=Label(sp,text="Downloading Speed",font=("Time New Roman",22,"bold",),bg="yellow",fg="black")
lab.place(x=120,y=100)

lab_down=Label(sp,text="000",font=("Time New Roman",22,"bold",),bg="green",fg="red")
lab_down.place(x=180,y=140)

lab=Label(sp,text="Uploading Speed",font=("Time New Roman",22,"bold",),bg="yellow",fg="black")
lab.place(x=130,y=200)

lab_up=Label(sp,text="000",font=("Time New Roman",22,"bold",),bg="green",fg="red")
lab_up.place(x=180,y=240)


button=Button(sp,text="Run Now",font=("Time New Roman",30,"bold"),relief="raised",fg="green",command=speedcheck)
button.place(x=140,y=290)
sp.mainloop()