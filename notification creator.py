#codebyte156 r2 project 1 CSE-FY



from tkinter import *
from plyer import notification
from tkinter import messagebox
from PIL import Image, ImageTk
import time

t = Tk()
t.title('Notifier')
t.geometry("600x300")
img = Image.open("notifmain-lable.png")
tkimage = ImageTk.PhotoImage(img)

# get details :D
def get_details():
    get_title = title.get()
    get_msg = msg.get()
    get_time = time1.get()
#print(get_title,get_msg, tt) ref

    if get_title == "" or get_msg == "" or get_time == "":
        messagebox.showerror("Alert", "Please fill all the fields!")
    else:
        int_time = int(float(get_time))
        min_to_sec = int_time * 60
        messagebox.showinfo("SET NOTIFICATION", "Do you want to set notification?")
        t.destroy()
        time.sleep(min_to_sec)

        notification.notify(title = get_title,
                            message = get_msg,
                            app_name = "Notification Creator",
                            app_icon = "codebyte156.ico",
                            toast = True,
                            timeout = 10)

img_label = Label(t, image=tkimage).grid()

#1 Label for Title
t_label = Label(t, text="Title to Notify",font=("Mvboli", 10))
t_label.place(x=12, y=70)

#2 ENTRY - Title
title = Entry(t, width="25",font=("Mvboli", 13))
title.place(x=123, y=70)

#3 Label - Message
m_label = Label(t, text="Display Message", font=("Mvboli", 10))
m_label.place(x=12, y=120)

#4 ENTRY - Message
msg = Entry(t, width="40", font=("Mvboli", 13))
msg.place(x=123,height=30, y=120)

#5 Label - Time
time_label = Label(t, text="Set Time", font=("Mvboli", 10))
time_label.place(x=12, y=175)

#6 ENTRY - Time
time1 = Entry(t, width="5", font=("Mvboli", 13))
time1.place(x=123, y=175)

#7 Label - min
time_min_label = Label(t, text="min", font=("Mvboli", 10))
time_min_label.place(x=175, y=180)

#8 Button
but = Button(t, text="SET NOTIFICATION", font=("Mvboli", 10, "bold"), fg="#ffffff", bg="#528DFF", width=20,
             relief="raised",
             command=get_details)
but.place(x=170, y=230)
#but.place(x=170, y=230)
t.resizable(0,0)
t.mainloop()


#You can also create your own GUI from this code, just edit the valuse given to the code
