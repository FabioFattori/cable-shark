import tkinter as tk
class Resizator:
    def __init__(self, toplevel):
        self.toplevel = toplevel
        self.width, self.height = toplevel.winfo_width(), toplevel.winfo_height()
        self._func_id = None

    def bind_config(self):
        self._func_id = self.toplevel.bind("<Configure>", self.resize)

    def unbind_config(self):  # Untested.
        if self._func_id:
            self.toplevel.unbind("<Configure>", self._func_id)
            self._func_id = None

    def resize(self, event):
        if(event.widget == self.toplevel and
           (self.width != event.width or self.height != event.height)):
            print(f'{event.widget=}: {event.height=}, {event.width=}\n')
            self.width, self.height = event.width, event.height

    def getWidth(self):
        return int(self.width)
    def getHeight(self):
        return int(self.height)