import ipAddress
import threading
import graphicAddAndUpdate
import tkinter as tk
import socket

lock = threading.Lock()

def getLock():
    return lock

def add(window,container,ipEntered,state):
    try:
        try:
            socket.inet_aton(ipEntered)
        except socket.error:
            return "Indirizzo IP non valido"
        #check if the ip is already in the list
        
        ip = ipAddress.ipAddress(ipEntered,state)
        container.append(ip)
        mainC=tk.Frame(window.ip_addresses_container,width=200,height=100,relief=tk.RAISED,borderwidth=1)
        mainC.pack(side=tk.TOP)
        label=tk.Button(mainC,text=ip.__get_ip__(),command=lambda:ip.pingMe(lock))
        label.pack(side=tk.TOP)
        label2=tk.Label(mainC,text=ip.__get_state__())
        label2.pack(side=tk.TOP)
        ip.automaticPing(window,container,graphicAddAndUpdate.getLock())
    except Exception as e:
        container.clear()
        return e

def updateList(windowContainer,container):
   
   if windowContainer != None and windowContainer.winfo_children() != None:
        #delete all the widgets in the windowContainer
        for widget in windowContainer.winfo_children():
            widget.destroy()

        
        for ip in container:
            mainC=tk.Frame(windowContainer,width=200,height=100)
            mainC.pack(side=tk.TOP)
            label=tk.Button(mainC,text=ip.__get_ip__(),command=lambda:ip.pingMe())
            label.pack(side=tk.TOP)
            label2=tk.Label(mainC,text=ip.__get_state__())
            label2.pack(side=tk.TOP)
        print("updating list")
    
    

    