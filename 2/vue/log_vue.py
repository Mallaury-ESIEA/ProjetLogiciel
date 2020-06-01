import  tkinter as tk 
from PIL import ImageTk,Image
    
class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title('AeroManagement')
        self.iconbitmap("./res/logo.ico")
        self._frame = None
        self.switch_frame(log_vue)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class log_vue(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        
        Frame1 = tk.Frame(self, borderwidth=2, relief=tk.GROOVE)
        Frame1.pack(side=tk.LEFT)
        
        my_img=ImageTk.PhotoImage(Image.open("./res/fond_log.png"))
        my_label= tk.Label(Frame1,image=my_img)
        my_label.image = my_img
        my_label.pack()
        
        
        
        # login
        valueLogin = tk.StringVar() 
        valueLogin.set("Login")
        entreeLogin = tk.Entry(Frame1, textvariable=valueLogin, width=30)
        entreeLogin.pack()
        
        # Password
        valuePassword = tk.StringVar() 
        valuePassword.set("Password")
        entreePassword = tk.Entry(Frame1, textvariable=valuePassword, width=30)
        entreePassword.pack()
        
        tk.Button(Frame1, text="Log in",
                  command=lambda: master.switch_frame(manage_planes_vue)).pack()
        
        

class manage_planes_vue(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg='blue')
        tk.Label(self, text="Page one", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Go back to start page",
                  command=lambda: master.switch_frame(log_vue)).pack()


class manage_people_vue(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg='blue')
        tk.Label(self, text="Page one", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Go back to start page",
                  command=lambda: master.switch_frame(log_vue)).pack()


class financial_report_vue(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg='blue')
        tk.Label(self, text="Page one", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Go back to start page",
                  command=lambda: master.switch_frame(log_vue)).pack()
        
        
class take_plane_vue(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg='blue')
        tk.Label(self, text="Page one", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Go back to start page",
                  command=lambda: master.switch_frame(log_vue)).pack()


class history_vue(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg='blue')
        tk.Label(self, text="Page one", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Go back to start page",
                  command=lambda: master.switch_frame(log_vue)).pack()
        
class solde_report_vue(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg='blue')
        tk.Label(self, text="Page one", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Go back to start page",
                  command=lambda: master.switch_frame(log_vue)).pack()