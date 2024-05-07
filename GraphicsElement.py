import tkinter as tk
import time
import Resizator
import addIpAddressToList

class GraphicsManager:
    def exitProgram(self):
        self.root.destroy()
        exit(0)

    def __init__(self,title,ip_addresses,refreshAll,ping):
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry("800x600")
        self.resizator = Resizator.Resizer(toplevel=self.root,manager=self)
        self.resizator.bind_config()
        self.root.protocol("WM_DELETE_WINDOW", self.exitProgram)



        # Create a Frame for the left side of the screen
        self.lst = tk.Frame(self.root)
        self.lst.pack(side=tk.LEFT)

        # Create a Frame for the right side of the screen
        self.rst = tk.Frame(self.root)
        self.rst.pack(side=tk.RIGHT)

        #set the size of the frames
        self.lst.config(width=int(self.resizator.getWidth()/2), height=int(self.resizator.getHeight()),pady=10,padx=10)
        self.rst.config(width=int(self.resizator.getWidth()/2), height=int(self.resizator.getHeight()),pady=10,padx=10)

        # Create input field
        self.entry = tk.Entry(self.rst, width=int(self.resizator.getWidth()/20))
        self.entry.pack(pady=10, side=tk.TOP)

        # Create ping button
        self.ping_button = tk.Button(self.rst, text="Ping", command=ping)
        self.ping_button.pack(pady=10, side=tk.TOP,after=self.entry)
        self.ping_button.config(width=int(self.resizator.getWidth()/4))

        


        # Create state label
        self.state_label = tk.Label(self.rst, text="current State : unknown", font=("Helvetica", 16))
        self.state_label.pack(pady=10, side=tk.TOP,after=self.ping_button)
        # Create output text area
        self.output_text = tk.Text(self.rst, wrap=tk.WORD, state=tk.DISABLED)
        self.output_text.config(state=tk.DISABLED)
        self.output_text.pack(side=tk.TOP, pady=10,after=self.state_label)
        self.output_text.config(width=int(self.resizator.getWidth()/2),height=int(self.resizator.getHeight()/4))

        # create a container for two buttons
        self.button_container = tk.Frame(self.lst)
        self.button_container.pack(side=tk.TOP)
        self.button_container.config(width=int(self.resizator.getWidth()/2))

        # create a container list for all the ip addresses
        self.ip_addresses_container = tk.Frame(self.lst,height=int(self.resizator.getHeight()/2))
        self.ip_addresses_container.pack(side=tk.TOP,after=self.button_container,pady=10,padx=10)



        self.add_to_list_button = tk.Button(self.button_container, text="Add to list", command=lambda:addIpAddressToList.add(self,ip_addresses,self.entry.get(),self.state_label.cget("text").split(":")[1]))
        self.add_to_list_button.pack(pady=10, side=tk.TOP)
        self.add_to_list_button.config(width=int(self.resizator.getWidth()/4))

        self.refresh_all_button = tk.Button(self.button_container, text="Refresh all", command=lambda: refreshAll())
        self.refresh_all_button.pack(pady=10, side=tk.TOP)
        self.refresh_all_button.config(width=int(self.resizator.getWidth()/4))

    def run(self):
        self.root.mainloop()
    
    def getAll(self):
        #return an object containing all the widgets with the name of the widget as the key
        return self