from tkinter import *
from tkinter import filedialog
from win10toast import ToastNotifier
from tkinter.ttk import Combobox
import tkinter.messagebox


class window_notification:
    def __init__(self,root):
        self.root=root
        self.root.title("Windows Notification")
        self.root.iconbitmap("logo484.ico")
        self.root.geometry("500x500")
        self.root.resizable(0,0)

        heading=StringVar()
        url=StringVar()
        duration=IntVar()




        def on_enter1(e):
            but_clear['background']="black"
            but_clear['foreground']="cyan"
  
        def on_leave1(e):
            but_clear['background']="SystemButtonFace"
            but_clear['foreground']="SystemButtonText"

        def on_enter2(e):
            but_send['background']="black"
            but_send['foreground']="cyan"
  
        def on_leave2(e):
            but_send['background']="SystemButtonFace"
            but_send['foreground']="SystemButtonText"

        def on_enter3(e):
            but_browse['background']="black"
            but_browse['foreground']="cyan"
  
        def on_leave3(e):
            but_browse['background']="SystemButtonFace"
            but_browse['foreground']="SystemButtonText"

        
        def clear():
            txt.delete('1.0','end')
            heading.set("")
            url.set("")
            duration.set("Select Duration")

        def Openfile():
            file_path = filedialog.askopenfilename(title = "Select file",filetypes = (("ICon Files","*.ico"),("All files","*.*"))) 
            url.set(file_path)

        
        def send():
            if heading.get()!="":
                if url.get()!="":
                    if duration.get()!="Select Duration":
                        
                        toaster=ToastNotifier()
                        toaster.show_toast(heading.get(),
                        txt.get('1.0','end'),
                        threaded=True,
                        icon_path="{}".format(url.get()),
                        duration=duration.get())
                    else:
                        tkinter.messagebox.showerror('Error',"Please Select Duration")

                else:
                    tkinter.messagebox.showerror("Error","Please Select Icon")
            else:
                tkinter.messagebox.showerror("Error","Please Enter Heading")







#===============frame======================================#
       
        mainframe=Frame(self.root,width=500,height=500,relief="ridge",bd=4)
        mainframe.place(x=0,y=0)

        firstframe=Frame(mainframe,width=493,height=440,relief="ridge",bd=3,bg="#4287f5")
        firstframe.place(x=0,y=0)

        secondframe=Frame(mainframe,width=493,height=53,relief="ridge",bd=3,bg="brown")
        secondframe.place(x=0,y=440)

#=========================firstframe===================================#
        
        lab_Heading=Label(firstframe,text="Heading",font=('times new roman',12),bg="#4287f5",fg="white")
        lab_Heading.place(x=210,y=10)

        ent_heading=Entry(firstframe,width=29,font=('times new roman',14),relief="ridge",bd=3,textvariable=heading)
        ent_heading.place(x=110,y=40)

        lab_message=Label(firstframe,text="Enter Message",font=('times new roman',12),bg="#4287f5",fg="white")
        lab_message.place(x=200,y=80)

        txt=Text(firstframe,width=55,height=8,font=('times new roman',12),relief="ridge",bd=3)
        txt.place(x=20,y=120)

        but_browse=Button(firstframe,width=19,text="Browse",font=('times new roman',13),cursor="hand2",command=Openfile)
        but_browse.place(x=150,y=290)
        but_browse.bind("<Enter>",on_enter3)
        but_browse.bind("<Leave>",on_leave3)

        ent_url=Entry(firstframe,width=49,font=('times new roman',14),relief="ridge",bd=3,textvariable=url)
        ent_url.place(x=20,y=330)

        v=list(range(1,61))
        combo1=Combobox(firstframe,values=v,font=('arial',12),width=15,state="readonly",textvariable=duration)
        combo1.set("Select Duration")
        combo1.place(x=160,y=380)





#=========================secondframe=======================================================#
        
        but_send=Button(secondframe,width=19,text="Send",font=('times new roman',12),cursor="hand2",command=send)
        but_send.place(x=40,y=8)
        but_send.bind("<Enter>",on_enter2)
        but_send.bind("<Leave>",on_leave2)

        but_clear=Button(secondframe,width=19,text="Clear",font=('times new roman',12),cursor="hand2",command=clear)
        but_clear.place(x=260,y=8)
        but_clear.bind("<Enter>",on_enter1)
        but_clear.bind("<Leave>",on_leave1)



if __name__ == "__main__":
    root=Tk()
    app=window_notification(root)
    root.mainloop()