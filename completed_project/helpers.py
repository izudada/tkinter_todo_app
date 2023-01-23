import tkinter as tk
import sqlite3
import tkinter.messagebox as MessageBox


def create_todo_frame(frame, x, y, bg):
    frame_width = int(x/3)
    # create frame and list frames
    create_todo_frame = tk.Frame(frame, width=frame_width, height=y, bg='#ffffff')
    create_todo_frame.place(x=5, y=200)

    #   labels
    note= tk.Label(create_todo_frame, text="Create Todo", font=('bold', 20), bg='#ffffff', fg=bg)
    note.place(x=int(frame_width/2)-80, y=2)

    todo_id = tk.Label(create_todo_frame, text="ID", font=('bold', 10), bg='#ffffff', fg=bg)
    todo_id.place(x=20, y=50)

    title= tk.Label(create_todo_frame, text="Title", font=('bold', 10), bg='#ffffff', fg=bg)
    title.place(x=20, y=90)

    #   inputs
    id_entry = tk.Entry(create_todo_frame)
    id_entry.place(x=100, y=50)

    title_entry = tk.Entry(create_todo_frame)
    title_entry.place(x=100, y=90)

    #  warning label
    message = """
                Note: - Only title input is needed to create todo.

                    - ID input alone is needed to delete and update todo.

                    - Both fields are needed to update a todo.
                    
                    - You get a todo with its ID, before edtiting the todo.
            """
    warning= tk.Label(create_todo_frame, text=message, font=('bold', 8), bg='#ffffff', fg=bg)
    warning.place(x=5, y=110)

    #   create todo button
    tk.Button(
            create_todo_frame,
            text="Create Todo",
            font=("TkHeadingFont", 16),
            bg=bg,
            fg="#ffffff",
            activebackground="#ffffff",
            activeforeground="#000000",
            cursor="hand1",
            command=lambda:create_todo(id_entry, title_entry)
        ).place(x=20, y=int(y/3))

    #   get todo button
    tk.Button(
            create_todo_frame,
            text="Get Todo",
            font=("TkHeadingFont", 16),
            bg="#000000",
            fg="#ffffff",
            activebackground=bg,
            activeforeground="white",
            cursor="hand1",
            command=lambda:get_todo()
        ).place(x=200, y=int(y/3)) 

    #   edit todo button
    tk.Button(
            create_todo_frame,
            text="Update Todo",
            font=("TkHeadingFont", 16),
            bg="#cce6ff",
            fg="#000000",
            activebackground=bg,
            activeforeground="white",
            cursor="hand1",
            command=lambda:update_todo()
        ).place(x=20, y=int(y/3)+100) 

    all_todo(frame, x, y, bg)


def create_todo(id_entry, title_entry):
    """
        A function that creates
        a todo entry
    """
    #   create db connection
    con = sqlite3.connect('todo.db')
    cur = con.cursor()

    #   get input value
    title = title_entry.get();

    #   check if title input is empty
    if title == "":
        MessageBox.showinfo("Form Error","Title input box must not be empty")
    else:
        try:
            #   insert into database
            cur.execute("INSERT INTO todo_info(title) VALUES(?);", [title])
            con.commit()
            con.close()

            #   clear form
            id_entry.delete(0, 'end')
            title_entry.delete(0, 'end')
            MessageBox.showinfo("Success","Todo Created Sucessfully")
        except Exception as e:
            print(e)
            MessageBox.showinfo("Invalid ID","Enter a valid ID")


def all_todo( frame, x, y, bg):
    all_todo_frame = tk.Frame(frame, width=int(x/2), height=y, bg="#cce6ff")
    all_todo_frame.place(x=int(x/3)+300, y=200)

    #   create db connection
    con = sqlite3.connect('todo.db')
    cursor = con.cursor()
    #   pull data from database
    cursor.execute("select * from todo_info ORDER BY id DESC")
    result = cursor.fetchall()
    con.close()
    print(result)
 
    list_box= tk.Listbox(all_todo_frame, width=int(x/2), height=30, bg=bg, fg="#ffffff", font=('normal', 10))
    list_box.place(x=2, y=5)
    #   fetch each record
    for item in range(len(result)):
        completed = "Not Completed"
        if result[item][2] == 1:
            completed = "Completed"

        data =  f"{result[item][0]}   |   {result[item][1]}   |   {completed}"
        list_box.insert(list_box.size()+2, data)


