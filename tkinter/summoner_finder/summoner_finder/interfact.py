from tkinter import  Tk
from tkinter import *
import pyglet

class Application(Tk):
    def __init__(self):
        super().__init__()
        self.title('Summoner_finder')
        self.geometry("1124x632")
        self.img = PhotoImage(file="C:/Users/karolx/Desktop/tkinter/summoner_finder/summoner_finder/data/background.png")
        self.background_theme()
        self.region_input()
        self.adds_title()
        self.username_input()
        self.button()
        self.mainloop()
    
    #Adds background to gui
    def background_theme(self):
        label = Label(self, 
                        image= self.img
                        )
        label.place(relx=0.5, rely=0.5, anchor='center')
    
    def adds_title(self):
        main_title = Label(self, text='Summoner Finder', font=('main_font'))
        main_title.place(relx=0.5, rely=0.5, anchor='center')
        pass

    def region_input(self):
        region = Entry(self, font=('Helvetica',24),  width=15, bg='#7F766D' ,  bd=1)
        region.place(relx=0.25, rely=0.75, anchor='center')

    def username_input(self):
        username = Entry(self, font=('Helvetica',24),  width=15, bg='#7F766D' ,  bd=1)
        username.place(relx=0.75, rely=0.75, anchor='center')
    
    def button(self):
        Enter_button = Button(self,
                                  text='Results',
                                  width=20, 
                                  height=2, 
                                  bg='grey', 
                                  bd=2,
                                  )
        Enter_button.place(relx=0.5, rely=0.9, anchor='center')