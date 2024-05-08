#open a new window and display the main loop
import requestResponsens
import threading
import addIpAddressToList
import GraphicsElement
import tkinter as tk
import os
from pinger import ping_ip

ip_addresses = []
title = "cable shark"

# if log.txt file doesn't exists create it if exists do nothing
if not os.path.isfile('log.txt'):
    with open('log.txt', 'w') as f:
        pass


# Function to ping an IP address
def ping():
    ip_address = manager.getAll().entry.get()
    if ip_address == "":
        manager.getAll().output_text.delete('1.0', tk.END)
        manager.getAll().output_text.insert(tk.END, "insert a valid IP address ...")
        return
    
    manager.getAll().state_label.config(text="current State : "+requestResponsens.res.get(2))
    manager.getAll().output_text.config(state=tk.NORMAL)
    manager.getAll().output_text.delete('1.0', tk.END)
    manager.getAll().output_text.insert(tk.END, "Pinging {}...\n".format(ip_address))
    manager.getAll().output_text.config(state=tk.DISABLED)
    
    # Create a thread for ping operation
    ping_thread = threading.Thread(target=perform_ping, args=(ip_address,))
    with addIpAddressToList.getLock():
        ping_thread.start()

def perform_ping(ip_address):
    response = ping_ip(ip_address)
    manager.getAll().output_text.config(state=tk.NORMAL)
    manager.getAll().output_text.delete('1.0', tk.END)
    manager.getAll().output_text.insert(tk.END, response[1])
    manager.getAll().state_label.config(text="current State : "+response[0])
    manager.getAll().output_text.config(state=tk.DISABLED)

def refreshAll():
    for ip in ip_addresses:
        ping_thread = threading.Thread(target=ip.pingMe, args=[addIpAddressToList.getLock()])
        ping_thread.start()


manager=GraphicsElement.GraphicsManager(title=title,ip_addresses=ip_addresses,refreshAll=refreshAll,ping=ping)


manager.getAll().root.mainloop()