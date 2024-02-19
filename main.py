import tkinter as tk
from tkinter import ttk

class App():
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.geometry('400x250')
        self.root.resizable(False, False)
        self.root.title('Reverse word(s) App')

        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(0, minsize=300)

        self.mainframe = tk.Frame(self.root, background='white')
        self.mainframe.pack(fill='both',expand=True)

        self.text = ttk.Label(self.mainframe, text="Hello World", anchor='center', background='white', font=('Brass Mono', 30))
        self.text.grid(row=0, column=1)
        # self.text.place(relx=0.5, rely=0, anchor='n')

        # input area
        self.set_text_field= ttk.Entry(self.mainframe)
        self.set_text_field.grid(row=2,column=1, pady=10, sticky='NWES')
        # self.set_text_field.place(relx=0.3, rely=0.2, width=150, anchor='w')

        # Set text button to press
        set_text_button = ttk.Button(self.mainframe, text='Set Text', command=self.set_text)
        set_text_button.grid(row=2, column=2, pady=10)
        # set_text_button.place(relx=0.45, rely=0.2, width=60,anchor='e')

        # shows a list of font colors for users select 
        color_options = ['red','blue','green','black']
        self.set_color_field = ttk.Combobox(self.mainframe, values=color_options)
        self.set_color_field.grid(row=3,column=1, sticky='NWES', pady=10)
        # self.set_color_field.place(relx=0, rely=0.4, width=150, anchor='w' )

        # button for color select
        set_color_button = ttk.Button(self.mainframe, text='Set color', command=self.set_color)
        set_color_button.grid(row=3, column=2, pady=10)
        # set_color_button.place(relx= 0.45, rely=0.4, width=60, anchor='e')

        self.reverse_text = ttk.Button(self.mainframe, text='Reverse Text', command=self.reverse)
        self.reverse_text.grid(row=4, column=1, sticky='NWES', pady=10)
        # self.reverse_text.place(relx=0.45, rely=0.5, width=100, anchor='center')

        self.root.mainloop()

        return
    
    def set_text(self):
        newtext = self.set_text_field.get()
        self.text.config(text=newtext)

    def set_color(self):
        newcolor = self.set_color_field.get()
        self.text.config(foreground=newcolor)

    def reverse(self):
        newtext = self.text.cget('text')
        reserved = newtext[::-1]
        self.text.config(text=reserved)
    

if __name__ == '__main__':
    App()