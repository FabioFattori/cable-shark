#open a new window and display the main loop
import requestError
import threading
import addIpAddressToList
import GraphicsElement
import tkinter as tk
from pinger import ping_ip

ip_addresses = []
title = "cable shark"

# Function to ping an IP address
def ping():
    ip_address = manager.getAll().entry.get()
    if ip_address == "":
        return
    
    manager.getAll().state_label.config(text="current State : "+requestError.res.get(2))
    manager.getAll().output_text.config(state=tk.NORMAL)
    manager.getAll().output_text.delete('1.0', tk.END)
    manager.getAll().output_text.insert(tk.END, "Pinging {}...\n".format(ip_address))
    manager.getAll().output_text.config(state=tk.DISABLED)
    
    # Create a thread for ping operation
    ping_thread = threading.Thread(target=perform_ping, args=(ip_address,))
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
        ping_thread = threading.Thread(target=ip.pingMe, args=())
        ping_thread.start()


manager=GraphicsElement.GraphicsManager(title=title,ip_addresses=ip_addresses,refreshAll=refreshAll,ping=ping)


manager.getAll().root.mainloop()