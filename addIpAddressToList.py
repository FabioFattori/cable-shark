import ipAddress
import threading
import tkinter as tk
def add(windowContainer,container,ipEntered,state):
    #check if the ip is already in the list
    for ip in container:
        if ip.__get_ip__() == ipEntered.split()[0] and len(ipEntered.split()[0]) != 0 and len(ipEntered.split(".")) == 4:
            return
    ip = ipAddress.ipAddress(ipEntered,state)
    container.append(ip)
    mainC=tk.Frame(windowContainer,width=200,height=100)
    mainC.pack()
    label=tk.Label(mainC,text=ip.__get_ip__())
    label.pack()
    label2=tk.Label(mainC,text=ip.__get_state__())
    label2.pack()
    ip.automaticPing()

def updateList(windowContainer,container):
    #get the windowContainer height
    height = windowContainer.winfo_height()

    #delete all the widgets in the windowContainer
    for widget in windowContainer.winfo_children():
        widget.destroy()
    # set the height of the windowContainer as fixed
    windowContainer.config(height=height)
    
    for ip in container:
        mainC=tk.Frame(windowContainer,width=200,height=100)
        mainC.pack()
        label=tk.Label(mainC,text=ip.__get_ip__())
        label.pack()
        label2=tk.Label(mainC,text=ip.__get_state__())
        label2.pack()
    # wait for 5 seconds before updating the list
    print("updating list")
    threading.Timer(5,updateList,[windowContainer,container]).start()
    