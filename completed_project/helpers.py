def create_todo_frame(tk, frame, x, y, bg):
    frame_width = int(x/3)
    # create frame and list frames
    create_todo_frame = tk.Frame(frame, width=frame_width, height=y, bg='#ffffff')
    create_todo_frame.place(x=5, y=100)

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
                Note: Only title input is needed to create todo.
                    ID input alone is needed to delete and update todo.
                    Both fields are needed to update a todo.
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
            command=lambda:create_todo()
        ).place(x=20, y=int(y/3)-50)

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
        ).place(x=200, y=int(y/3)-50) 
