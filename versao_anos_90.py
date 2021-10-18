from tkinter import *

root = Tk()
root.title("Lista de Pessoas")
root.geometry("500x500")

my_frame = Frame(root)
my_frame.pack(pady=10)

my_list = Listbox(my_frame,
    width=25,
    height=5,
    bg="SystemButtonFace",
    bd=0,
    fg="#464646",
    highlightthickness=0,
    selectbackground="#a6a6a6",
    activestyle="none")

my_list.pack(side=LEFT, fill=BOTH)

my_scrollbar = Scrollbar(my_frame)
my_scrollbar.pack(side=RIGHT, fill=BOTH)

my_list.config(yscrollcommand=my_scrollbar)
my_scrollbar.config(command=my_list.yview)

my_entry = Entry(root)
my_entry.pack(pady=20)

# Create button frame
btn_frame = Frame(root)
btn_frame.pack(pady=20)

# LIST FUNCTIONS
def insere_pessoa():
    my_list.insert(END, my_entry.get())
    my_entry.delete(0, END)

def name_sort():
    people_tuple = my_list.get(0, END)
    people_list = []
    for i in people_tuple:
        people_list.append(i)
    people_list.sort()
    my_list.delete(0, END)
    for p in people_list:
        my_list.insert(END, p)

def age_sort():
    people_tuple = my_list.get(0, END)
    print(people_tuple)
    people_list = []
    for i in people_tuple:
        people_list.append(i.split(', '))
    print(people_list)
    people_list.sort(key=lambda x:int(x[1]))
    my_list.delete(0, END)
    for p in people_list:
        my_list.insert(END, p)

def classifica_pessoa():
    people_tuple = my_list.get(0, END)
    people_list = []
    for p in people_tuple:
        if int(p[1]) <= 12:
            people_list.append((p[0], p[1], "Criança"))
        elif int(p[1]) <= 19:
            people_list.append((p[0], p[1], "Adolescente"))
        elif int(p[1]) < 65:
            people_list.append((p[0], p[1], "Adulto"))
        else:
            people_list.append((p[0], p[1], "Idoso"))
    my_list.delete(0, END)
    for p in people_list:
        my_list.insert(END, p)

# Add buttons
add_btn = Button(btn_frame, text="Inserir pessoa", command=insere_pessoa)
sort_name_btn = Button(btn_frame, text="Ordena por nome", command=name_sort)
sort_age_btn = Button(btn_frame, text="Ordena por idade", command=age_sort)
classify_btn = Button(btn_frame, text="Classifica pessoas", command=classifica_pessoa)

add_btn.grid(row=0, column=0)
sort_name_btn.grid(row=0, column=1, padx=20)
sort_age_btn.grid(row=0, column=2)
classify_btn.grid(row=0, column=3, padx=20)

root.mainloop()