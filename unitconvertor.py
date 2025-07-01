
from tkinter import *
import tkinter as tk
from tkinter.ttk import Progressbar
from PIL import Image, ImageTk
from time import sleep
import webbrowser

def center(window,width,height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x= (screen_width//2)-(width//2)
    y=(screen_height//2)-(height//2)
    window.geometry(f"{width}x{height}+{x}+{y}")
'''
def convert_unit(value, from_unit, to_unit):
    conversion_factors = {
        "Meter": 1,
        "Kilometer": 1000,
        "Centimeter": 0.01,
    }
    if from_unit in conversion_factors and to_unit in conversion_factors:
        return value * conversion_factors[from_unit]/ conversion_factors[to_unit]
    else:
        return value'''
def convert_length(value, from_unit, to_unit):
    conversion_factors = {
        "Meter": 1,
        "Kilometer": 1000,
        "Centimeter": 0.01,
        "Millimeter": 0.001,
    }
    return value * conversion_factors[from_unit] / conversion_factors[to_unit]


def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    elif from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        return value + 273.15
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        return value - 273.15
    elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
        return (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
        return (value - 273.15) * 9/5 + 32
    else:
        return value
    

''''
if value in unit_categories:
    self.set_unit(unit_categories[value])
'''

class intro():
    def __init__(self,wind):
      
        wind.deiconify()   
        wind.resizable(0,0)
        wind.configure(bg="#008080") 
        wind.title("Unit Converter")
        #icon=PhotoImage(file=r"C:/Users/ommji_mttma5p/OneDrive/Desktop/python/welcome.PNG") 
        icon_img = Image.open(r"C:/Users/ommji_mttma5p/OneDrive/Desktop/python/welcome.PNG")
        icon = ImageTk.PhotoImage(icon_img)      
        wind.iconphoto(False,icon)
        center(wind,500,230) 
        
        
        entry = Label(wind,bg="#008080",fg="white",text="Welcome to  Unit Converter!",font=("Footlight MT Light",15,"bold"))
        entry.place(x=50,y=30,width=410,height=30)

        self.load = Progressbar(wind,orient=HORIZONTAL,length=250,mode='indeterminate')
        self.start=Button(wind,bg="#f5f5f5",fg="black",text="START",command=self.loading)
        self.start.place(x=200,y=90,width=80,height=30)            

        follow = Label(wind,bg="#008080",fg="white",text="Follow Me On",font=("Helvetica",12,"bold"))
        follow.place(x=186,y=150,width=104,height=20)

 
        #self.git=PhotoImage(file=r'C:/Users/ommji_mttma5p/OneDrive/Desktop/python/git.PNG')
        git_img = Image.open(r'C:/Users/ommji_mttma5p/OneDrive/Desktop/python/git.PNG')
        self.git = ImageTk.PhotoImage(git_img)
        github=Button(wind,image=self.git,bg="white",relief=FLAT,command=lambda:self.links("https://github.com/Omm-Jitesh-Mohanty"),cursor="hand2")
        github.place(x=110,y=190,width=30,height=30)

        #self.instag=PhotoImage(file=r'C:/Users/ommji_mttma5p/OneDrive/Desktop/python/ins.PNG')
        instag_img = Image.open(r'C:/Users/ommji_mttma5p/OneDrive/Desktop/python/ins.PNG')
        self.instag = ImageTk.PhotoImage(instag_img)
        insta=Button(wind,image=self.instag,bg="#008080",relief=FLAT,command=lambda:self.links("https://www.instagram.com/.omm_jitesh..s2?igsh=enFsYjZ2aXg4cG5z"),cursor="hand2")
        insta.place(x=190,y=190,width=30,height=30)

        
        #self.fcb=PhotoImage(file=r'C:/Users/ommji_mttma5p/OneDrive/Desktop/python/fb.PNG')
        fcb_img = Image.open(r'C:/Users/ommji_mttma5p/OneDrive/Desktop/python/fb.PNG')
        self.fcb = ImageTk.PhotoImage(fcb_img)
        fb=Button(wind,image=self.fcb,bg="white",relief=FLAT,command=lambda:self.links("https://www.facebook.com/share/1C9Ru8gqZf/"),cursor="hand2")
        fb.place(x=270,y=190,width=30,height=30)

        #self.tweet=PhotoImage(file=r'C:/Users/ommji_mttma5p/OneDrive/Desktop/python/ln.PNG')
        ln_img = Image.open(r'C:/Users/ommji_mttma5p/OneDrive/Desktop/python/ln.PNG')
        self.tweet = ImageTk.PhotoImage(ln_img)
        twitter=Button(wind,image=self.tweet,bg="white",relief=FLAT,command=lambda:self.links("https://www.linkedin.com/in/omm-jitesh-mohanty-045a6a320?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app"),cursor="hand2")
        twitter.place(x=350,y=190,width=30,height=30)

    def links(self,url):    
        webbrowser.get("C:/Program Files" + " (x86)/Google/Chrome/Application/chrome.exe" +" %s --incognito").open(url)

    def loading(self):
        self.start.place(x=0,y=0,width=0,height=0)  
        self.load.place(x=120,y=100)
        wind.update()        
        c=0
        while c < 100:
            self.load['value'] += 1
            wind.update()
            sleep(0.02)
            c += 1
        self.load.place_forget()  # Hide the progress bar
        wind.withdraw()  # Hide the intro window
        win.deiconify()  # Show the main converter window
        # Set default parameters (you can customize this)
        unit_data = {
            "Length": {
        "lb": ["Meter", "Kilometer", "Centimeter"],
        "para": convert_length,
        "para1": convert_length
    },
    "Temperature": {
        "lb": ["Celsius", "Fahrenheit", "Kelvin"],
        "para": convert_temperature,
        "para1": convert_temperature
    },
        }
        converter(unit_data,"Length")  # Launch the converter page
            

class converter():
    def __init__(self,unit_categories,default_key):
        self.unit_categories=unit_categories
        self.default_unit=unit_categories[default_key]
        self.current_unit=None


        win.deiconify()
        win.geometry("350x500")
        win.resizable(0,0)
        win.title("Converter")
        #icon=PhotoImage(file=r'C:/Users/ommji_mttma5p/OneDrive/Desktop/python/welcome.PNG')
        icon_img = Image.open(r'C:/Users/ommji_mttma5p/OneDrive/Desktop/python/welcome.PNG')
        icon = ImageTk.PhotoImage(icon_img)
        win.iconphoto(False,icon)
        
        self.inp_stg = StringVar()
        self.opt_stg = StringVar()

        self.lb = Listbox(win)  
        self.lb1 = Listbox(win)
        self.disp1 = Label(win)
        self.disp2 = Label(win)
        
        center(win,350,500)
        #self.unit_categories=unit_categories
        default_unit = unit_categories["Length"]
        #self.set_unit(self.default_unit)
        # Input Part of the window(Top Half).
        upr=Label(win,bg="#add8e6",width=400,height=250)
        upr.place(x=0,y=0)

        # window(Bottom Half).
        lwr=Label(win,bg="#189AB4",width=400,height=250,bd=0)
        lwr.place(x=0,y=250)

        
        self.menu_lb=Listbox(win,selectmode=SINGLE,height=0,font=("Helvetica",10))
        #self.menu_lb.bind('<>',self.option)
        self.menu_lb.bind('<<ListboxSelect>>', self.option) 
        options=["Length","Temperature", "Speed","Time","Mass"]
        
        for i in range(len(options)):
            self.menu_lb.insert(i,options[i])


        
        #self.pic=PhotoImage(file=r"C:/Users/ommji_mttma5p/OneDrive/Desktop/python/menu.PNG")
        menu_img = Image.open(r"C:/Users/ommji_mttma5p/OneDrive/Desktop/python/menu.PNG")
        self.pic = ImageTk.PhotoImage(menu_img)
        self.menu=Button(win,image=self.pic,width=35,height=30,bg="#add8e6",bd=0,command=lambda:self.select('m'))
        self.menu.place(x=0,y=0)
        
       
        self.inp_stg=StringVar()
        self.inp=Entry(win,bg="#add8e6",fg="white",font=("Helvetica",14),text=self.inp_stg,bd=1)
        self.inp.place(x=120,y=100,width=116,height=40)
        #self.inp.bind('',self.operation)
        #self.inp.bind('',self.operation)
        self.inp.bind('<KeyRelease>', self.operation)
        self.lb_menu=self.default_unit["lb"]
        self.lb=Listbox(win,selectmode=SINGLE,height=0)            
        #self.lb.bind('<>',self.option)
        self.lb.bind('<<ListboxSelect>>', self.option) 
        self.disp1=Label(win,text=self.lb_menu[0],bg="white",fg="black")
        self.disp1.place(x=120,y=160,width=100,height=20)

       
        #self.down=PhotoImage(file=r"C:/Users/ommji_mttma5p/OneDrive/Desktop/python/drop.PNG")
        drop_img = Image.open(r"C:/Users/ommji_mttma5p/OneDrive/Desktop/python/drop.PNG")
        self.down = ImageTk.PhotoImage(drop_img)
        scroll_upr=Button(win,image=self.down,width=14,height=18,bd=0,command=lambda:self.select(0))
        scroll_upr.place(x=220,y=160)
        self.opt_stg=StringVar()    
        
        self.opt=Entry(win,bg="#189AB4",fg="black",font=("Helvetica",14),text=self.opt_stg,bd=1)
        self.opt.place(x=120,y=350,width=116,height=40)
        #self.opt.bind('',self.operation)
        self.opt.bind('<KeyRelease>', self.operation)


        self.lb1=Listbox(win,selectmode=SINGLE,height=0)
        #self.lb1.bind('<>',self.option)
        self.lb1.bind('<<ListboxSelect>>', self.option)
        
        for i in range(len(self.lb_menu)):
            self.lb1.insert(i,self.lb_menu[i])
            self.lb.insert(i,self.lb_menu[i])        

        
        #self.disp1=Label(win,text=self.lb_menu[1],bg="#ffffff",fg="black")
        #self.disp1.place(x=120,y=410,width=100,height=20)
        self.disp1 = Label(win, text=self.lb_menu[0], bg="white", fg="black")
        self.disp1.place(x=120, y=160, width=100, height=20)

        self.disp2 = Label(win, text=self.lb_menu[1], bg="white", fg="black")
        self.disp2.place(x=120, y=410, width=100, height=20)
       
        scroll_dwn=Button(win,image=self.down,width=14,height=18,bd=0,command=lambda:self.select(1),bg="#f5f5f5")
        scroll_dwn.place(x=220,y=410)

        self.para=self.default_unit["para"]  
        self.para1=self.default_unit["para1"]

        self.form=StringVar()   
        self.formulae=Label(win,text="",bg="#189AB4",fg="white",font=("Helvetica",10))
        self.formulae.place(x=50,y=450,width=250,height=25)
        self.set_unit(self.default_unit)

        self.set_unit(self.default_unit)

        print(self.para,self.para1)

    def option(self, event):
        #pass
        widget = event.widget
        try:
            index = widget.curselection()[0]
            value = widget.get(index)
            if widget == self.menu_lb:
                if value in self.unit_categories:
                    #self.set_unit(unit_categories[value])
                    self.default_unit = self.unit_categories[value]
                    self.set_unit(self.default_unit)
                    self.menu_lb.place_forget()
                return

            if widget == self.lb:
                self.disp1['text'] = value
                self.lb.place_forget()
            elif widget == self.lb1:
                self.disp2['text'] = value 
                self.lb1.place_forget()
        except IndexError:
            return
        if widget == self.lb:
            self.disp1['text'] = value
            self.lb.place_forget()
        elif widget == self.lb1:
            self.disp2['text'] = value
            self.lb1.place_forget()
        elif val == 'm':
            self.menu_lb.place(x=35, y=30, height=140, width=120)

    def select(self, val):
        print(f"Scroll selected with value: {val}")
        if val == 0:
            # From unit dropdown
            self.lb.place(x=120, y=180, height=len(self.lb_menu)*20)
        elif val == 1:
            # To unit dropdown
            self.lb1.place(x=120, y=430, height=len(self.lb_menu)*20)
    
    def set_unit(self,default_unit):
        if default_unit == self.current_unit:
            return  # Stop recursion if same unit
        self.current_unit=default_unit

        


        global exp_in,exp_out
        exp_in=""   
        exp_out="" 
        
        self.inp_stg.set("") 
        self.opt_stg.set("")  
        self.unit=default_unit 
        self.lb_menu=default_unit["lb"]
        
        self.lb.delete(0,END)   
        self.lb1.delete(0,END)  
        self.lb.place(y=0,height=0)
        self.lb1.place(y=250,height=0)

       
        self.disp1['text']=self.lb_menu[0]
        self.disp1['text']=self.lb_menu[1]

        self.para=default_unit["para"]
        self.para1=default_unit["para1"]

       
        for i in range(len(self.lb_menu)):
            self.lb1.insert(END,self.lb_menu[i])
            self.lb.insert(i,self.lb_menu[i])

        #value = float(self.inp_stg.get())
        inp_value = self.inp_stg.get()

        if inp_value == '':
            value = 0.0  # or some default value
        else:
            try:
                value = float(inp_value)
            except ValueError:
                # handle invalid input
                value = 0.0  
        self.inp_unit=self.lb_menu[0]
        self.opt_unit=self.lb_menu[1]
        #self.set_unit(default_unit)
        result = self.para(value, self.inp_unit, self.opt_unit)
        self.opt_stg.set(str(result))
        self.formulae['text'] = f"Formula: {value} {self.inp_unit} → {result} {self.opt_unit}"
        #self.formulae['text'] = "Formulae: "+ operator.replace("{}","Unit")

        center(wind,500,230)
        win.update()

   
    def operation(self,event):
        try:
            inp_val = float(self.inp_stg.get())
            from_unit = self.disp1['text']
            to_unit = self.disp2['text']
            result = self.para(inp_val, from_unit, to_unit)
            self.opt_stg.set(str(result))
            self.formulae['text'] = f"{inp_val} {from_unit} = {result} {to_unit}"
        except ValueError:
            self.opt_stg.set("Invalid")
            self.formulae['text'] = "Please enter a valid number."
        except Exception as e:
            self.opt_stg.set("Error")
            self.formulae['text'] = str(e)

        '''global exp_in,operator,exp_out
        if not hasattr(self, 'disp1'):
            return  
        self.inp_unit = self.disp1['text']
        self.opt_unit = self.disp2['text']

        try:
            widget = event.widget
            if(widget == self.inp):
                win.update()
                index = self.unit[self.opt_unit][-1]
                operator = self.unit[self.inp_unit][index]

                if(event.char >= '0' and event.char <= '9'):
                    exp_in = self.inp_stg.get()
                    exp_out = str(eval(operator.format(exp_in)))
                    self.opt_stg.set(exp_out)
                
                elif((event.char=='\b') or
                     (len(self.inp_stg.get())=='0'
                      and event.char<='9')):
                    exp_out = self.opt_stg.get()
                    exp_in = str(eval(operator.format(exp_out)))
                    self.inp_stg.set(exp_in)
                    
                elif(event.char == '\b' or 
                     (len(self.opt_stg.get()) == 0)):
                    self.opt_stg.set("")
                    self.formulae['text'] = "Formulae: " + operator.replace("{}", self.inp_unit)
        except Exception as e:
            self.opt_stg.set("Error")
            self.formulae['text'] = f"Invalid input or formula: {str(e)}"'''

wind=Tk()
wind.withdraw()
intro=intro(wind)
win=Toplevel()
win.withdraw()
wind.mainloop()
