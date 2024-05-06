#open a new window and display the main loop

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import time
import threading
import os
import sys
import ipAddress
import addIpAddressToList
import pinger #import the pinger.py file



title = "cable shark"

import tkinter as tk
from pinger import ping_ip

ip_addresses = []


# Function to ping an IP address
def ping():
    ip_address = entry.get()
    output_text.config(state=tk.NORMAL)
    output_text.delete('1.0', tk.END)
    output_text.insert(tk.END, "Pinging {}...\n".format(ip_address))
    output_text.config(state=tk.DISABLED)
    
    # Create a thread for ping operation
    ping_thread = threading.Thread(target=perform_ping, args=(ip_address,))
    ping_thread.start()

def perform_ping(ip_address):
    response = ping_ip(ip_address)
    output_text.config(state=tk.NORMAL)
    output_text.delete('1.0', tk.END)
    output_text.insert(tk.END, response[1])
    state_label.config(text="current State : "+response[0])
    output_text.config(state=tk.DISABLED)

def refreshAll():
    for ip in ip_addresses:
        ping_thread = threading.Thread(target=ip.pingMe, args=())
        ping_thread.start()




# Create main window
root = tk.Tk()
root.title(title)



# Create a Frame for the left side of the screen
lst = tk.Frame(root)
lst.pack(side=tk.LEFT)

# Create a Frame for the right side of the screen
rst = tk.Frame(root)
rst.pack(side=tk.RIGHT)

#set the size of the frames
lst.config(width=300, height=400)
rst.config(width=400, height=400)

# Create input field
entry = tk.Entry(rst, width=30)
entry.pack(pady=10, side=tk.TOP)

# Create ping button
ping_button = tk.Button(rst, text="Ping", command=ping)
ping_button.pack(pady=10, side=tk.TOP,after=entry)



# Create state label
state_label = tk.Label(rst, text="current State : unknown", font=("Helvetica", 16))
state_label.pack(pady=10, side=tk.TOP,after=ping_button)
# Create output text area
output_text = tk.Text(rst, height=10, width=50)
output_text.config(state=tk.DISABLED)
output_text.pack(side=tk.TOP, pady=10,after=state_label)

# create a container for two buttons
button_container = tk.Frame(lst)
button_container.pack(side=tk.TOP)


add_to_list_button = tk.Button(button_container, text="Add to list", command=lambda:addIpAddressToList.add(lst,ip_addresses,entry.get(),state_label.cget("text").split(":")[1]))
add_to_list_button.pack(pady=10, side=tk.TOP)

refresh_all_button = tk.Button(button_container, text="Refresh all", command=lambda: refreshAll())
refresh_all_button.pack(pady=10, side=tk.TOP)
# Run the main event loop
root.mainloop()