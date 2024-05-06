import ipAddress
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