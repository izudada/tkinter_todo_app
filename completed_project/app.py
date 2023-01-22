import tkinter as tk  #  imports tkinter library as a variable tk
from helpers import create_todo_frame


root = tk.Tk()  # to create a root window or widget
root.title("Todo App")  #   Create a title for the root widget
 # width, height for the window
root.minsize(400, 400) 
root.maxsize(600, 600)
#   setting the geometry
root.geometry("400x400+60+60") 

#   bacgroung color
bg = "#003366"

# vertical and horizontal values
x = root.winfo_screenwidth()    
y = root.winfo_screenheight()

#   create frames
menu_frame = tk.Frame(root, width=x, height=y, bg=bg)
menu_frame.grid(row=0, column=0, sticky="nesw")

# create logo widget/image
logo_img = tk.PhotoImage(file="assets/white_logo.png")
logo_widget = tk.Label(menu_frame, image=logo_img, bg=bg)
logo_widget.image = logo_img
logo_widget.place(x=int(x/2) - 100, y=5)


create_todo_frame(tk, menu_frame, x, y, bg)

root.mainloop()
