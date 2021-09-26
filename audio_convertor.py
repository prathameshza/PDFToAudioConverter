import os
from os import close
from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
import tkinter
from tkinter.font import BOLD 
from tkinter.scrolledtext import ScrolledText
from tkinter.messagebox import showinfo
from typing import Iterable, Tuple

import pandas as pd
import PIL.ImageTk,PIL.Image
import pytesseract as pt

import pdf2image

import PyPDF2


import pyttsx3
from pyttsx3.drivers import sapi5

from tkinter.filedialog import *


sidebar = "gold"
mainbg = "black"
label_colour = "white"
button_colour = ""
light_colour = 'slate gray'
dark_colour= "azure"


voiceid=0
rate_value=150
book = None
content = None
start= None
end = None
current_value=150
#background_image=ImageTk.PhotoImage(file='name_of_the_image.extension')
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')


home_icon='house.png'
settings_icon='system.png'

root = Tk()
root.title("Audio Convertor")
root.geometry('580x400')
root.configure(bg=mainbg)



min_w = 50 # Minimum width of the frame
max_w = 130 # Maximum width of the frame
cur_width = min_w # Increasing width of the frame
expanded = False # Check if it is completely exanded
ex=False



def expand():
    global cur_width, expanded
    cur_width += 10 # Increase the width by 10
    rep = root.after(5,expand) # Repeat this func every 5 ms
    frame.config(width=cur_width) # Change the width to new increase width
    if cur_width >= max_w: # If width is greater than maximum width 
        expanded = True # Frame is expended
        root.after_cancel(rep) # Stop repeating the func
        fill()
    



def contract():
    global cur_width, expanded
    cur_width -= 10 # Reduce the width by 10 
    rep = root.after(5,contract) # Call this func every 5 ms
    frame.config(width=cur_width) # Change the width to new reduced width
    if cur_width <= min_w: # If it is back to normal width
        expanded = False # Frame is not expanded
        root.after_cancel(rep) # Stop repeating the func
        fill()



def fill():
    if expanded: # If the frame is exanded
        # Show a text, and remove the image
        home_b.config(text='Home',image='',font=(0,18),bg=sidebar,command=None)
        set_b.config(text='Settings',image='',font=(0,18),bg=sidebar,command=None)
        
    else:
        # Bring the image back
        home_b.config(image=home,font=(0,21))
        set_b.config(image=settings,font=(0,21))









#background_label =Label(root, image=background_image)
#background_label.place(x=0,y=0)






# Adding Widgets....................
def win1():
    labelstart.destroy()
    labelstart1.destroy()
    butstart.destroy()
    credit.destroy()
    
    def expandbut1():
        global cur_width, ex
        cur_width += 2 # Increase the width by 2
        rep = root.after(5,expand) # Repeat this func every 5 ms
        but1.config(width=28) # Change the width to new increase width
        but1.config(height=22)
        but2.config(bg= light_colour)
        but2.config(width=20)
        but2.config(height=17)
        if cur_width >= 28: # If width is greater than maximum width 
            ex = True # Frame is expended
            root.after_cancel(rep) # Stop repeating the func
            fill()
        if cur_width <= 25: # If width is greater than maximum width 
            ex = True # Frame is expended
            root.after_cancel(rep) # Stop repeating the func
            fill()


    def contractbut1():
        global cur_width, ex
        cur_width -= 2 # Reduce the width by 10 
        rep = root.after(5,contract) # Call this func every 5 ms
        but1.config(width=25) # Change the width to new reduced width
        but1.config(height=20)
        but2.config(width=25) # Change the width to new reduced width
        but2.config(height=20)
        but2.config(bg=dark_colour)
        if cur_width <= 25: # If it is back to normal width
            ex = False # Frame is not expanded
            root.after_cancel(rep) # Stop repeating the func
            fill()
        
        if cur_width >= 28: # If width is greater than maximum width 
            ex = False # Frame is expended
            root.after_cancel(rep) # Stop repeating the func
            fill()


    def expandbut2():
        global cur_width, ex
        cur_width += 2 # Increase the width by 2
        rep = root.after(5,expand) # Repeat this func every 5 ms
        but2.config(width=28) # Change the width to new increase width
        but2.config(height=22)
        but1.config(bg=light_colour)
        but1.config(width=20)
        but1.config(height=17)
        if cur_width >= 28: # If width is greater than maximum width 
            ex = True # Frame is expended
            root.after_cancel(rep) # Stop repeating the func
            fill()
        if cur_width <= 25: # If width is greater than maximum width 
            ex = True # Frame is expended
            root.after_cancel(rep) # Stop repeating the func
            fill()


    def contractbut2():
        global cur_width, ex
        cur_width -= 2 # Reduce the width by 10 
        rep = root.after(5,contract) # Call this func every 5 ms
        but2.config(width=25) # Change the width to new reduced width
        but2.config(height=20)
        but1.config(bg=dark_colour)
        but1.config(width=25) # Change the width to new reduced width
        but1.config(height=20)
        if cur_width <= 25: # If it is back to normal width
            ex = False # Frame is not expanded
            root.after_cancel(rep) # Stop repeating the func
            fill()
        if cur_width >= 28: # If width is greater than maximum width 
            ex = False # Frame is expended
            root.after_cancel(rep) # Stop repeating the func
            fill()
        
    
    def read_through_text():
        but1.destroy()
        but2.destroy()
        label1.destroy()

        

        
        def speak():
            player = pyttsx3.init()
            audio_string = text.get('0.0',END)
            voices = player.getProperty('voices')                    
            player.setProperty('voice', voices[voiceid].id)
            player.setProperty('rate', rate_value)
            if audio_string:
                player.say(audio_string)
                player.runAndWait()
                player.stop()

        def save_aud():
            player = pyttsx3.init()
            audio_string = text.get('0.0',END)
            voices = player.getProperty('voices')                    
            player.setProperty('voice', voices[voiceid].id)
            player.setProperty('rate', rate_value)
            if audio_string:
                player.save_to_file(audio_string,asksaveasfilename(defaultextension='.mp3',filetypes=(("audio/mpeg", "*.mp3"),("All Files", "*.*"))))
                player.runAndWait()
                player.stop()

        def bac():
            label2.destroy()
            text.frame.destroy()
            listen_b.destroy()
            clear_b.destroy()
            save_b.destroy()
            win1()


        # Adding Widgets....................
        label2 = Label(root,text="Type the text below:",font=("Arial bold",18),background=mainbg,fg=label_colour)
        label2.grid(column=1,row=0,columnspan=3)

        text = ScrolledText(root,width=60,height=19,wrap = WORD,padx= 10, pady= 10,bd=5,relief = RIDGE)
        text.grid(row=1,column=2,columnspan=3)

        # Adding Buttons....................

        listen_b = ttk.Button(root,text='Listen',width=7,command=speak)
        listen_b.grid(row=2,column=2,ipadx=2)
        clear_b = ttk.Button(root,text='clear',width=7,command=lambda: text.delete('0.0',END))
        clear_b.grid(row=2,column=3,ipadx=2)
        save_b = ttk.Button(root,text='save',width=7,command=save_aud)
        save_b.grid(row=2,column=4,ipadx=2)

        
        home_b.config(image=home,font=(0,18),bg=sidebar,command=bac)
        

    def read_through_pdf():
        but1.destroy()
        but2.destroy()
        label1.destroy()
        pt.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        
        
        label3 = Label(root,text="Read through pdf :",font=("Brush Script MT",24),bg=mainbg,fg=label_colour)
        label3.grid(column=1,row=0)

        def browse():
            browse_b.destroy()
            global book,content
            book = askopenfilename()
            pdfReader = PyPDF2.PdfFileReader(book)
            no_page = pdfReader.numPages
            no_pagestr = "Selected pdf consist of "+str(no_page)+" number of pages"
            page_dis = Label(root,text=no_pagestr,font= 20,background=mainbg,foreground=label_colour)
            page_dis.grid(row=1,column=1,sticky='nw',pady=10)
            range_mess = Label(root,text='Enter the range below',background=mainbg,foreground=label_colour)
            range_mess.grid(row=1,column=1,sticky='nw',pady=40)
            st = Label(root,text='Page from where to start reading',background=mainbg,foreground=label_colour)
            st.grid(row=1,column=1,sticky=NW,pady=60)
            txt1= Entry(root,width=10)
            txt1.grid(column=1,row=1,sticky=NW,pady=60,padx=240)
            en = Label(root,text='Page from where to stop reading',background=mainbg,foreground=label_colour)
            en.grid(row=1,column=1,sticky=NW,pady=80)
            txt2= Entry(root,width=10)
            txt2.grid(column=1,row=1,sticky=NW,pady=80,padx=240)
            
            
            def all1():
                global start,end
                start = 0
                end = no_page
                allb.config(text='Selected',command=None)

            
            
            def play1():
                global start,end
                start = int(txt1.get())-1
                end = int(txt2.get())
                ren.config(text='Setted',command=None)
            

                

            ren = Button(root,text='Set Range',width=12,command=play1)
            ren.grid(row=1,column=1,ipadx=2,sticky=NW,pady=120,padx=180)
                    
            allb = Button(root,text='Select All',width=12,command=all1)
            allb.grid(row=1,column=1,ipadx=2,sticky=NW,pady=120,padx=20)
            
            
            
            
            def play_button():
                play_bu.destroy()

                

                def speak():
                    player = pyttsx3.init()
                    voices = player.getProperty('voices')                    
                    player.setProperty('voice', voices[voiceid].id)
                    player.setProperty('rate', rate_value)
                    pages = pdf2image.convert_from_path(pdf_path = book, dpi=200, size=(1654,2340))


                    
                    for i in range(start,end):

                        
                        content = pt.image_to_string(pages[i], lang='eng')
                        if content:
                            player.say(content)
                            player.runAndWait()
                            player.stop()
                           
                play_aud = Button(root,text='Play',width=12,command=speak)
                play_aud.grid(row=1,column=1,ipadx=2,sticky=NW,pady=155,padx=20)
                


                def save_aud():
                    player = pyttsx3.init()
                    voices = player.getProperty('voices')                    
                    player.setProperty('voice', voices[voiceid].id)
                    player.setProperty('rate', rate_value)
                    pages = pdf2image.convert_from_path(pdf_path = book, dpi=200, size=(1654,2340))
                    

                    for i in range(start,end):
                    
                        
                        content = pt.image_to_string(pages[i], lang='eng')
                    
                        if content:
                            player.save_to_file(content,desktop+'/AudioConvertorpage'+str(i+1)+'.mp3')
                            player.runAndWait()
                            player.stop()
                        
                save_au = Button(root,text='Save',width=12,command=save_aud)
                save_au.grid(row=1,column=1,ipadx=2,sticky=NW,pady=155,padx=180)
                def bac():
                    label3.destroy()
                    page_dis.destroy()
                    range_mess.destroy()
                    st.destroy()
                    txt1.destroy()
                    en.destroy()
                    txt2.destroy()
                    ren.destroy()
                    allb.destroy()
                    play_aud.destroy()
                    save_au.destroy()
                    play_bu.destroy()
                    win1()
                home_b.config(image=home,font=(0,18),bg=sidebar,command=bac)
            
            play_bu = Button(root,text='Next',width=12,command=play_button)
            play_bu.grid(row=1,column=1,ipadx=2,sticky=NW,pady=150,padx=100)
            
            def bac():
                label3.destroy()
                page_dis.destroy()
                range_mess.destroy()
                st.destroy()
                txt1.destroy()
                en.destroy()
                txt2.destroy()
                ren.destroy()
                allb.destroy()
                
                play_bu.destroy()
                win1()
            home_b.config(image=home,font=(0,18),bg=sidebar,command=bac)
        browse_b = ttk.Button(root,text='Browse the pdf file.',width=16,command=browse)
        browse_b.grid(row=1,column=1,ipadx=2,sticky=NW)
        def bac():
            browse_b.destroy()
            label3.destroy()
            win1()
        home_b.config(image=home,font=(0,18),bg=sidebar,command=bac)


            # Read a pdf file as image pages
            # We do not want images to be to big, dpi=200
            # All our images should have the same size (depends on dpi), width=1654 and height=2340
        

            
    Grid.rowconfigure(root,0,weight=0)
    Grid.columnconfigure(root,0,weight=0)
    
    Grid.rowconfigure(root,1,weight=1)
    Grid.columnconfigure(root,1,weight=0)


    #ku = ImageTk.PhotoImage(Image.open('ku.png'))
    label1 = Label(root,text="Choose one of the option",font=("Arial bold",18),background=mainbg,fg=label_colour)
    label1.grid(column=1,row=0,columnspan=5)
    longtext1 = '''Read 
    through 
    text'''
    but1 = Button(root,text=longtext1,width=25,height=20,command=read_through_text,bg=dark_colour)
    but1.grid(row=1,column=2,sticky= EW)
    longtext2 = '''Read 
    through 
    PDF'''
    but2 = Button(root,text=longtext2,width=25,height=20,command=read_through_pdf,bg=dark_colour)
    but2.grid(row=1,column=8,sticky=EW)
    but1.bind('<Enter>',lambda e: expandbut1())
    but1.bind('<Leave>',lambda e: contractbut1())
    but2.bind('<Enter>',lambda e: expandbut2())
    but2.bind('<Leave>',lambda e: contractbut2())


    
    def sett1():

        root1 = Tk()
        root1.geometry('580x450')
        
        root1.title("Settings")
        
        def david():
            global voiceid
            voiceid=1
            
        
        def zira():
            global voiceid
            voiceid=2 

            
            
        def bac():
            root1.destroy()
        saveb = ttk.Button(root1,text='Save',width=12,command=bac)
        saveb.grid(row=11,column=1,ipadx=2)    
        
        

        label3 = Label(root1,text="Settings:",font=("Brush Script MT",24))
        label3.grid(column=1,row=0)

        label3_1 = Label(root1,text="Voice",font=("Brush Script MT",18))
        label3_1.grid(column=0,row=1,sticky=NW)

        label3_2 = Label(root1,text="Choose the Voice you want :",font=("Times New Roman",12))
        label3_2.grid(column=1,row=2,sticky=NW)

        david_b = ttk.Button(root1,text='David(Male)',width=12,command=david)
        david_b.grid(row=3,column=1,ipadx=2,sticky=NW)

        zira_b = ttk.Button(root1,text='Zira(Female)',width=12,command=zira)
        zira_b.grid(row=3,column=3,ipadx=2,sticky=NE)




        label4 = Label(root1,text="Rate",font=("Brush Script MT",18))
        label4.grid(column=0,row=4,sticky=NW)
        label4_1 = Label(root1,text="Select the rate : ",font=("Times New Roman",12))
        label4_1.grid(column=1,row=5,sticky=NW)

        # slider current value
        
        

        def get_current_value():
            global rate_value
            global current_value
            val=int(slider.get())
            rate_value=val
            current_value=val
            

            
            return '{: .2f}'.format(val)


        def slider_changed(event):
            value_label.configure(text=get_current_value())
            


        # label for the slider
        slider_label = ttk.Label(root1,text='Slider:')
        slider_label.grid(column=0,row=6,sticky='w')
        #  slider
        slider = ttk.Scale(root1,from_=50,to=350,value=current_value,orient='horizontal', command=slider_changed)

        slider.grid(column=1,row=6,sticky='we')

        # current value label
        current_value_label = ttk.Label(root1,text='Current Value:')

        current_value_label.grid(row=7,columnspan=2,column=1,sticky='n',ipadx=10,ipady=1)

        # value label
        value_label = ttk.Label(root1,text=get_current_value())
        value_label.grid(row=7,columnspan=2,column=2,sticky=N)


        label5 = Label(root1,text="Themes",font=("Brush Script MT",18))
        label5.grid(column=0,row=8,sticky=NW)
        
        def homewarn():
            label5_1 = Label(root1,text="(Please, Return to home to update latest theme)",font=("Times New Roman",10),fg='red')
            label5_1.grid(column=1,row=8,sticky=NW)

        def theme1():
            global sidebar ,mainbg ,label_colour 
            sidebar= "sky blue"
            mainbg= "grey"
            label_colour="white"
            frame.config(bg=sidebar)
            root.config(bg=mainbg)
            home_b.config(bg=sidebar)
            set_b.config(bg=sidebar)
            label1.config(bg=mainbg)
            homewarn()


        the1 = Button(root1,text='Theme 1',width=12,height=4,command=theme1)
        the1.grid(row=9,column=1,ipadx=2,sticky=NW)
        
        def theme2():
            global sidebar ,mainbg ,label_colour 
            sidebar= "gold"
            mainbg= "black"
            label_colour="white"
            frame.config(bg=sidebar)
            root.config(bg=mainbg)
            home_b.config(bg=sidebar)
            set_b.config(bg=sidebar)
            label1.config(bg=mainbg)
            homewarn()




        the2 = Button(root1,text='Theme 2',width=12,height=4,command=theme2)
        the2.grid(row=9,column=7,ipadx=2,sticky=NE)
        
        
        def theme3():
            global sidebar ,mainbg ,label_colour 
            sidebar= "lavender"
            mainbg= "misty rose"
            label_colour="Black"
            frame.config(bg=sidebar)
            root.config(bg=mainbg)
            home_b.config(bg=sidebar)
            set_b.config(bg=sidebar)
            label1.config(bg=mainbg,fg=label_colour)
            homewarn()



        the3 = Button(root1,text='Theme 3',width=12,height=4,command=theme3)
        the3.grid(row=10,column=1,ipadx=2,sticky=SW)
        def theme4():
            global sidebar ,mainbg ,label_colour 
            sidebar= "indigo"
            mainbg= "steel blue"
            label_colour="white"
            frame.config(bg=sidebar)
            root.config(bg=mainbg)
            home_b.config(bg=sidebar)
            set_b.config(bg=sidebar)
            label1.config(bg=mainbg,fg=label_colour)
            homewarn()
            
        the4 = Button(root1,text='Theme 4',width=12,height=4,command=theme4)
        the4.grid(row=10,column=7,ipadx=2,sticky=SE)

        root1.columnconfigure(0, weight=1)
        root1.columnconfigure(1, weight=3)

        root1.mainloop()
    set_b.config(image=settings,font=(0,18),bg=sidebar,command=sett1)

labelstart=Label(root,text='Welcome to',font=('Times new roman',22),fg=label_colour,bg=mainbg)
labelstart.grid(row=1,column=1,padx=130)
labelstart1=Label(root,text='Audio Convertor',font=('Brush Script MT',34),fg=label_colour,bg=mainbg)
labelstart1.grid(row=2,column=1,padx=130)

butstart = Button(root,text='Start', width=25,command=win1)
butstart.grid(row=4,column=1,padx=150)
def crie():
    cre = Tk()
    cre.title("Credits")
    cre.geometry("580x400")
    backg="sky blue"
    cre.config(bg=backg)



    label_head = Label(cre,text='Credits',font=("Standard", 50, UNDERLINE,BOLD),anchor=CENTER,fg='dark green',bg=backg)
    label_head.pack()


    label_name1= Label(cre,text='Prathmesh Zade',font=("Standard",20,BOLD),fg='dark green',bg=backg)
    label_name1.pack()

    label_name2= Label(cre,text='Kushal Sathe',font=("Standard",20,BOLD),fg='dark green',bg=backg)
    label_name2.pack()

    label_name6=Label(cre,text='Vridhi Sachdev',font=("Standard",20,BOLD),fg='dark green',bg=backg)
    label_name6.pack()

    label_name3=Label(cre,text='Subodh Dhoke',font=("Standard",20,BOLD),fg='dark green',bg=backg)
    label_name3.pack()

    label_name4=Label(cre,text='Vaishnavi Kale',font=("Standard",20,BOLD),fg='dark green',bg=backg)
    label_name4.pack()

    label_name5=Label(cre,text='Sanskruti Shelar',font=("Standard",20,BOLD),fg='dark green',bg=backg)
    label_name5.pack()
    
    label_name6=Label(cre,text='Sonal Singh',font=("Standard",20,BOLD),fg='dark green',bg=backg)
    label_name6.pack()

    label_name7=Label(cre,text='Hrushikesh Urde',font=("Standard",20,BOLD),fg='dark green',bg=backg)
    label_name7.pack()

    cre.mainloop()
credit= Button(root,text='i',width=2,command=crie)
credit.grid(row=0,column=5,sticky=NE)

home = PIL.ImageTk.PhotoImage(PIL.Image.open(home_icon).resize((40,40),PIL.Image.ANTIALIAS))
settings = PIL.ImageTk.PhotoImage(PIL.Image.open(settings_icon).resize((40,40),PIL.Image.ANTIALIAS))


root.update() # For the width to get updated
frame = Frame(root,bg=sidebar,width=55,height=400)
frame.grid(row=0,column=0,rowspan=11,sticky=NS) 

# Make the buttons with the icons to be shown
home_b = Button(frame,image=home,bg=sidebar,relief='flat')
set_b = Button(frame,image=settings,bg=sidebar,relief='flat')

# Put them on the frame
home_b.grid(row=0,column=0,pady=10)
set_b.grid(row=1,column=0,pady=50)

# Bind to the frame, if entered or left
frame.bind('<Enter>',lambda e: expand())
frame.bind('<Leave>',lambda e: contract())

# So that it does not depend on the widgets inside the frame
frame.grid_propagate(False)

root.mainloop()