from tkinter import *
from tkinter import ttk,filedialog
import random
import pyttsx3
import os

e=pyttsx3.init()

root=Tk()
root.geometry("1280x720")
root.title('textTospeech')

count=1
def slider():
    global count
    if (count==1):
        slider_lebel.configure(image=p1)
    elif(count==2):
        slider_lebel.configure(image=p2)
    else:
        slider_lebel.configure(image=p3)
        count=0
    count+=1
    slider_lebel.after(1000,slider)

def blind():
    color=['pink','yellow','red','blue','green']
    a=random.choice(color)
    lbl_title.configure(bg=a)
    lbl_title.after(200,blind)

def talk():
    def check_voice():
        if (gender == 'Male'):
            e.setProperty('voice', v[0].id)
            e.setProperty('volume', (volume_) / 100)
            e.say(text)
            e.runAndWait()
        else:
            e.setProperty('voice', v[1].id)
            e.setProperty('volume', (volume_) / 100)
            e.say(text)
            e.runAndWait()

    text = txt_area.get(1.0, END)
    gender = gender_combo.get()
    speed = speed_combo.get()
    volume_ = scale_level.get()
    v = e.getProperty('voices')
    if (text):
        if (speed == 'Fast'):
            e.setProperty('rate', 300)
            check_voice()
        elif (speed == 'Normal'):
            e.setProperty('rate', 150)
            check_voice()
        else:
            e.setProperty('rate', 50)
            check_voice()


def download():
    def check_voice():
        if (gender == 'Male'):
            e.setProperty('voice', v[0].id)
            e.setProperty('volume', (volumes) / 100)
            path=filedialog.askdirectory()
            os.chdir(path)
            e.save_to_file(text,'music.mp3')
            e.runAndWait()
        else:
            e.setProperty('voice', v[1].id)
            e.setProperty('volume', (volumes) / 100)
            path = filedialog.askdirectory()
            os.chdir(path)
            e.save_to_file(text, 'music.mp3')
            e.runAndWait()

    text=txt_area.get(1.0,END)
    gender=gender_combo.get()
    speed=speed_combo.get()
    volumes=scale_level.get()
    v=e.getProperty('voices')
    if(text):
        if(speed=='Fast'):
            e.setProperty('rate',300)
            check_voice()
        elif(speed=='Normal'):
            e.setProperty('rate',150)
            check_voice()
        else:
            e.setProperty('rate',50)
            check_voice()



#==========================title====================
lbl_title=Label(root,text="Text to Speech",font='arial 50 bold')
lbl_title.place(x=0,y=0,relwidth=1)

f1=Frame(root,relief=GROOVE,bd=5)
f1.place(x=10,y=100,width=600,height=300)

scrol_bar=Scrollbar(f1,orient=VERTICAL)
scrol_bar.pack(side=RIGHT,fill=Y)
txt_area=Text(f1,font=('times new rommon',15,'bold'),bg='grey99',yscrollcommand=scrol_bar.set,wrap=WORD)
txt_area.pack(fill=BOTH)

scrol_bar.config(command=txt_area.yview)
gender_lbl=Label(root,text='Gender',font='Impack 25 bold',width=10,bg='yellow',fg='red')
gender_lbl.place(x=10,y=410)

speed_lbl=Label(root,text='Speed',font='Impack 25 bold',width=10,bg='yellow',fg='red')
speed_lbl.place(x=230,y=410)

volume_lbl=Label(root,text='Volume',font='Impack 25 bold',width=10,bg='yellow',fg='red')
volume_lbl.place(x=450,y=410)

#===================combo box====================
gender_combo=ttk.Combobox(root,values=['Male','Female'],font='arial 12 bold',state='r')
gender_combo.place(x=10,y=500)
gender_combo.set('Male')

speed_combo=ttk.Combobox(root,values=['Fast','Normal','slow'],font='arial 12 bold',state='r')
speed_combo.place(x=230,y=500)
speed_combo.set('Fast')

scale_level=Scale(root,from_=0,to=100,orient=HORIZONTAL,length=160)
scale_level.place(x=450,y=480)
scale_level.set(50)

#===================buttons======================
play_btn=Button(root,text='Play',font='arial 25 bold',width=10,bg='lime',activebackground='yellow',relief=SUNKEN,bd=10,command=talk)


play_btn.place(x=100,y=600)
d_btn=Button(root,text='Download',width=10,font='arial 25 bold ',relief=SUNKEN,bg='lime',activebackground='yellow',bd=10,command=download)
d_btn.place(x=400,y=600)

#=========================
p1=PhotoImage(file='1.PNG')
p2=PhotoImage(file='2.PNG')
p3=PhotoImage(file='3.PNG')

slider_lebel=Label(root,bd=0,image=p1)
slider_lebel.place(x=700,y=100)

root.configure(bg='powderblue')
blind()
slider()
root.mainloop()