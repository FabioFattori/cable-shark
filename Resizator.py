import tkinter as tk
class Resizer:
    def __init__(self, toplevel,manager):
        self.toplevel = toplevel
        self.width, self.height = toplevel.winfo_width(), toplevel.winfo_height()
        self._func_id = None
        self.manager = manager

    def bind_config(self):
        self._func_id = self.toplevel.bind("<Configure>", self.resize)

    def resize(self, event):
        if(event.widget == self.toplevel and
           (self.width != event.width or self.height != event.height)):
            print(f'{event.widget=}: {event.height=}, {event.width=}\n')
            self.width, self.height = event.width, event.height
            #resize all widgets 
            self.manager.getAll().lst.config(width=int(self.width/2), height=int(self.height),pady=10,padx=10)
            self.manager.getAll().rst.config(width=int(self.width/2), height=int(self.height),pady=10,padx=10)
            self.manager.getAll().entry.config(width=int(self.width/20))
            self.manager.getAll().ip_addresses_container.config(height=int(self.height/2))
            self.manager.getAll().output_text.config(width=int(self.width/2),height=int(self.height/4))
            #self.manager.getAll().button_container.config(windth=int(self.width/2))
            #self.manager.getAll().ping_button.config(width=int(self.width/4))
            #self.manager.getAll().add_to_list_button.config(windth=int(self.width/4))
            #self.manager.getAll().refresh_all_button.config(windth=int(self.width/4))


    def getWidth(self):
        return int(self.width)
    def getHeight(self):
        return int(self.height)
    