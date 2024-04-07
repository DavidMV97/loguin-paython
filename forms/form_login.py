import tkinter as tk 
from tkinter import ttk, messagebox
from tkinter.font import BOLD
import utils.generic as utl
from forms.form_master import MasterPanel

class App:
    
    def check_user_password(self):
        user = self.user.get()
        password = self.password.get()
        
        if (user == 'root' and password == '1234'):
            self.window.destroy()
            MasterPanel()
        else:
            messagebox.showerror(message='Usuario o contraseña incorrectos', title='Mensaje')
    
    
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('Inicion de sesión')
        self.window.geometry('800x500')
        self.window.config(bg='#fcfcfc')
        self.window.resizable(0,0)
        utl.center_window(self.window, 800, 500)
        
        logo = utl.read_img('./img/logo.png', (200, 200))
        
        # frame logo
        frame_logo = tk.Frame(self.window, bd=0, width=300, relief=tk.SOLID, padx=10, pady=10, bg='#3a7ff6')
        frame_logo.pack(side='left', expand=tk.NO, fill=tk.BOTH)
        label = tk.Label(frame_logo, image=logo, bg='#3a7ff6')
        label.place(x=0, y=0, relwidth=1, relheight=1)
        
        # frame form
        frame_form = tk.Frame(self.window, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form.pack(side='right', expand=tk.YES, fill=tk.BOTH)
        
        # frame top 
        frame_form_top = tk.Frame(frame_form, height= 50, bd=0, relief=tk.SOLID, bg='black')
        frame_form_top.pack(side='top', fill=tk.X)
        title = tk.Label(frame_form_top, text='Inicio de sesión', font=('Times', 30), fg='#666a88', bg='#fcfcfc', pady=50)
        title.pack(expand=tk.YES, fill=tk.BOTH)
        
        # frame form fill
        frame_form_fill = tk.Frame(frame_form, height= 50, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form_fill.pack(side='bottom', expand=tk.YES, fill=tk.BOTH)
        
        label_user = tk.Label(frame_form_fill, text='Usuario', font=('Times', 14), fg='#666a88', bg='#fcfcfc', anchor='w')
        label_user.pack(fill=tk.X, padx=20, pady=5)
        self.user = ttk.Entry(frame_form_fill, font=('Times', 14))
        self.user.pack(fill=tk.X, padx=20, pady=10)
        
        label_password = tk.Label(frame_form_fill, text='Contraseña', font=('Times', 14), fg='#666a88', bg='#fcfcfc', anchor='w')
        label_password.pack(fill=tk.X, padx=20, pady=5)
        self.password = ttk.Entry(frame_form_fill, font=('Times', 14))
        self.password.pack(fill=tk.X, padx=20, pady=10)
        self.password.config(show='*')
        
        loguin = tk.Button(frame_form_fill, text='Iniciar sesion', font=('Times', 15, BOLD), bg='#3a7ff6', bd=0, fg='#fff', command=self.check_user_password)
        loguin.pack(fill=tk.X, padx=20, pady=20)
        loguin.bind('<Return>', (lambda event: self.check_user_password()))
        
        self.window.mainloop()

        
        
    