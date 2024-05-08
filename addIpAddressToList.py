import ipAddress
import addIpAddressToList
import threading
import tkinter as tk

lock = threading.Lock()

def getLock():
    return lock

def add(window,container,ipEntered,state):
    #check if the ip is already in the list
    for ip in container:
        if ip.__get_ip__() == ipEntered.split()[0] and len(ipEntered.split()[0]) != 0 and len(ipEntered.split(".")) == 4:
            return
    ip = ipAddress.ipAddress(ipEntered,state)
    container.append(ip)
    mainC=tk.Frame(window.ip_addresses_container,width=200,height=100,relief=tk.RAISED,borderwidth=1)
    mainC.pack(side=tk.TOP)
    label=tk.Button(mainC,text=ip.__get_ip__(),command=lambda:ip.pingMe())
    label.pack(side=tk.TOP)
    label2=tk.Label(mainC,text=ip.__get_state__())
    label2.pack(side=tk.TOP)
    ip.automaticPing(window,container,addIpAddressToList.getLock())

def updateList(windowContainer,container):
   
   if windowContainer != None and windowContainer.winfo_children() != None:
        #delete all the widgets in the windowContainer
        for widget in windowContainer.winfo_children():
            widget.destroy()

        #delete the content of the log.txt file
        with open("log.txt","w") as file:
            file.write("")

        print("updating list")
        
        for ip in container:
            mainC=tk.Frame(windowContainer,width=200,height=100)
            mainC.pack(side=tk.TOP)
            label=tk.Button(mainC,text=ip.__get_ip__(),command=lambda:ip.pingMe())
            label.pack(side=tk.TOP)
            label2=tk.Label(mainC,text=ip.__get_state__())
            label2.pack(side=tk.TOP)
    
    

    