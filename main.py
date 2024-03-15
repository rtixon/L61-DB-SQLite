from tkinter import *
from tkinter import messagebox, Label, Tk, ttk, filedialog, simpledialog
import tkinter as tk
from PIL import Image, ImageTk
import sqlite3
import pathlib
import os
import configparser

# config
with open("settings.ini", mode="w") as open_file:
    open_file.write("""[main]
user = "UserName"
keyuser = '2445'
			""")
config = configparser.ConfigParser()
config.read('settings.ini')
print(config["main"]["user"])
print(config["main"]["keyuser"])

# database
connection = sqlite3.connect('database\AmDB.db')
cursor = connection.cursor()

# database creating
cursor.execute('''
CREATE TABLE IF NOT EXISTS Rivers (
id INTEGER PRIMARY KEY,
name TEXT NOT NULL UNIQUE,
image BLOB NOT NULL,
description TEXT NOT NULL)''')
connection.commit()

# global variables
image_database_path = ('db_image.jpg')
image_database = Image.open(image_database_path)

def refresh_list(event=None):
    global cursor
    listbox.delete(0, END)
    cursor.execute('SELECT name FROM Rivers')
    names = cursor.fetchall()
    for name in names:
        listbox.insert(END, name)

def convert_to_binary_data(filename):
    # Преобразование данных в двоичный формат
    with open(filename, 'rb') as file:
        blob_data = file.read()
    return blob_data

def insertBLOB(id, name, photo, description):
    try:
        sqlite_insert_blob_query = """ INSERT INTO Rivers 
                                  (id, name, image, description) VALUES (?, ?, ?, ?)"""

        empPhoto = convert_to_binary_data(photo)
        data_tuple = (id, name, empPhoto, description)
        cursor.execute(sqlite_insert_blob_query, data_tuple)
    except sqlite3.Error as error:
        messagebox.showerror("Ошибка", f"Запись не была добавлена в базу данных. \nПодробнее: {error}")
    refresh_list()

def insertData(event=None):
    insertBLOB(1, "Енисей", "photo\enisey.jpg",
               "Енисей - река в Тыве, Хакасии и Красноярском крае, одна из самых длинных "
               "и полноводных рек мира и России. Впадает в Карское море Северного "
               "Ледовитого океана. Длина — 3487 км, площадь водосборного "
               "бассейна — 2580000 км² (второй по величине в России), а годовой сток "
               "составляет 624,41 км³ (самая полноводная река в России).")
    insertBLOB(2, "Обь", "photo\ob.jpg",
               "Обь - река в России, протекает по Западной Сибири. Одна из крупнейших рек в мире. "
               "Длина Оби — 3650 км (от истока Иртыша — 5410 км), площадь водосборного "
               "бассейна — 2990000 км². Расход воды в 287 км от устья (у Салехарда) "
               "— 12492 м³/с. Среднемноголетний сток — 403,981 км³/год. Берёт начало при слиянии "
               "Бии и Катуни в предгорьях Алтая. В устье образует Обскую губу и впадает в Карское море.")
    insertBLOB(3, "Амур", "photo/amur.jpg",
               "Амур — река на Дальнем Востоке в Восточной Азии. Протекает по территории России и "
               "границе России и КНР. Длина — 2824 км (от слияния Шилки и Аргуни), площадь бассейна "
               "— 1856 тысяч км². Впадает в Охотское море или Японское море. Годовой сток составляет 403,66 км³.")
    insertBLOB(4, "Лена", "photo\lena.jpg",
               "Лена — река в Восточной Сибири России, впадает в море Лаптевых Северного Ледовитого "
               "океана, образуя крупнейшую в Арктике дельту. Длина вместе с дельтой — 4400 км. "
               "В некоторых случаях указывается длина 4294 км без учёта Быковской протоки (106 км) "
               "в дельте Лены. Площадь бассейна — 2,49 млн км². Среднемноголетний сток равен 530,225 км³/год.")
    insertBLOB(5, "Волга", "photo/volga.jpg", "Волга - одна из крупнейших рек на Земле и самая большая по водности, "
                                              "площади бассейна и длине в Европе, а также крупнейшая в мире река, впадающая в "
                                              "бессточный (внутренний) водоём. Длина реки составляет 3530 км (до постройки "
                                              "водохранилищ — 3690 км), а площадь водосборного бассейна — 1360 тыс.км². "
                                              "Годовой сток составляет 254 км³.")
    insertBLOB(6, "Днепр", "photo\dnepr.jpeg",
               "Днепр — четвёртая по длине река Европы после Волги, Дуная и Урала, имеет самое "
               "длинное русло в границах Украины. Длина Днепра от истока до устья в естественном "
               "состоянии составляла 2285 (2139) км, теперь (после постройки каскада водохранилищ), "
               "когда во многих местах выпрямили фарватер — 2201 км; в пределах Украины — 1121 км, "
               "в пределах Белоруссии — 595 км (115 км находятся на пограничной территории "
               "Белоруссии и Украины), в пределах России — 485 км. Площадь водосборного бассейна — "
               "504 000 км², из них в пределах Украины — 291400 км². Средний расход воды "
               "в устье — 1670 м³/с. Уклон реки — 0,09 м/км.")
    insertBLOB(7, "Печора", "photo\pechora.jpg", "Печора — река в Республике Коми и Ненецком автономном округе России. "
                                                 "Длина — 1809 км, площадь водосборного бассейна — 322 тыс. км². "
                                                 "Берёт начало на Северном Урале, в юго-восточной части Республики Коми, "
                                                 "и течёт сперва преимущественно на юго-запад. Высота истока — 675 м над уровнем моря. "
                                                 "В 1981 году у истока, найденного экспедицией Ивана Просвирнина, была "
                                                 "установлена чугунная плита с надписью «Отсюда начинается великая северная река Печора».")
    insertBLOB(8, "Урал", "photo\yral.jpg",
               "Урал — река в Восточной Европе, протекает по территории России и Казахстана, "
               "впадает в Каспийское море. Является третьей по протяжённости рекой Европы, "
               "уступает по этому показателю только Волге и Дунаю. Длина — 2428 км. "
               "Площадь водосборного бассейна — 231000 км². Средний расход воды у с. "
               "Кушум — 400 м³/с. Основное питание реки — тающий снег (60-70 %); "
               "вклад осадков относительно невелик.")
    insertBLOB(9, "Дон", "photo\don.jpeg",
               "Дон — река в Европейской части России. Длина реки — 1870 км, площадь водосборного "
               "бассейна — 422 тыс.км². Средний расход воды — 680 м³/с. Уклон реки — 0,096 м/км. "
               "Пятая по протяжённости река Европы. Исток Дона располагается в городе Новомосковске, "
               "находящемся в северной части Среднерусской возвышенности, на высоте около 180 м "
               "над уровнем моря. Исток Дона является одной из главных достопримечательностей города.")
    insertBLOB(10, "Кама", "photo\kama.jpg",
               "Кама — река в европейской части России, левый и самый крупный приток Волги. "
               "Длина Камы составляет 1805 км (до постройки Куйбышевского водохранилища была 2030 км). "
               "Река принимает 74718 притоков, площадь водосборного бассейна — более 507000 км². "
               "Уклон реки по состоянию на 1952 год — 0,11 м/км.")


#insertData()
window = Tk()
window.title("Известные реки России")
window.geometry('900x345')
window.resizable(False, False)
window.attributes("-topmost", False)

def about(event=None):
    messagebox.showinfo('О программе', 'База данных "Известные реки России"'
                                       '\n(с) Rozhkov T.A., Russia, 2024')
def content(event=None):
    NewWindow = Toplevel()
    NewWindow.title('Справка')
    NewWindow.geometry('370x175')
    NewWindow.resizable(False, False)
    label = Label(NewWindow, text='Справка, База данных <Известные реки России>'
                                   '\nПозволяет: добавлять / изменять / удалять информацию.'
                        '\nКлавиши программы:'
                        '\nF1 - Вызов справки по программе,'
                        '\nF2 - Добавить в базу данных,'
                        '\nF3 - Удалить из базы данных,'
                        '\nF4 - Изменить запись в базе данных,'
                        '\nF10- Меню программы.', justify='left', font='Arial 10')
    label.grid(sticky='n', row=0)
    button = Button(NewWindow, text="Закрыть", font=10, command=NewWindow.destroy)
    button.grid(row=1)
    NewWindow.mainloop()

def exit_program(event=None):
    exit()

def add_data(event=None):
    def explorer(event=None):
        global filePath
        global image
        filePath = filedialog.askopenfilename(parent=NewWindow, initialdir="/", title="Select file",
                                              filetypes=(("Images", "*.jpg* *.jpeg* *.bmp* *.png*"), ("all files", "*.*")))
        if len(filePath) == 0:
            return()

        entry_path.delete(0, END)
        image = Image.open(filePath)
        resized_image = image.resize((400, 300))
        photo = ImageTk.PhotoImage(resized_image)
        image = photo
        label_image.config(image=photo, width=400, height=300)
        entry_path.config(state=NORMAL)
        entry_path.insert(END, filePath)
        entry_path.config(state=DISABLED)


    filePath = ''
    image = ''
    NewWindow = Toplevel()
    NewWindow.title('Добавление записи в базу данных')
    NewWindow.geometry('880x365')
    NewWindow.resizable(False, False)

    label_name = Label(NewWindow, text='Наименование:')
    label_name.place(x=10, y=20)
    label_ID = Label(NewWindow, text='ID элемента:')
    label_ID.place(x=10, y=50)
    label_description = Label(NewWindow, text='Описание реки:')
    label_description.place(x=10, y=80)
    label_path = Label(NewWindow, text='Путь до файла:')
    label_path.place(x=425, y=20)

    entry_name = Entry(NewWindow, font='Arial 9')
    entry_name.place(x=110, y=22, width=300, height=20)
    entry_ID = Entry(NewWindow, font='Arial 9')
    entry_ID.place(x=110, y=52, width=300, height=20)
    entry_path = Entry(NewWindow, font='Arial 9', state=DISABLED)
    entry_path.place(x=515, y=22, width=300, height=20)
    entry_description = Text(NewWindow, wrap=WORD, font='Arial 9', state=NORMAL)
    entry_description.place(x=110, y=82, width=300, height=270)

    btn_exp = Button(NewWindow, text='Обзор', command=explorer)
    btn_exp.place(x=820, y=18)
    btn_cancel = Button(NewWindow, text='Закрыть', command=NewWindow.destroy)
    btn_cancel.place(x=25, y=327)
    btn_ok = Button(NewWindow, text='Добавить')
    btn_ok.place(x=22, y=292)

    label_image = Label(NewWindow, borderwidth=2, relief="ridge", width=55, height=20, image=image)
    label_image.place(x=425, y=52)

    btn_ok.bind('<Button-1>', lambda event: insertBLOB(entry_ID.get(), entry_name.get(),
                                                                   entry_path.get(), entry_description.get("1.0",END)))
    NewWindow.mainloop()

def del_data(event=None):
    if (listbox.curselection()):
        list_name = listbox.get(listbox.curselection())
        result = messagebox.askquestion("Удаление", f"Вы уверены, что хотите удалить элемент с именем {list_name}?", icon='warning')
        if result == 'yes':
            cursor.execute('DELETE FROM Rivers WHERE name=?', list_name)
            refresh_list()
            listbox.select_set(0)
            data_refresh()
    else:
        messagebox.showinfo('Информация', 'Выберите элемент из списка для удаления')
        return ()

def change_data(event=None):
    def updateNote(old_name, id, new_name, photo, description):
        str_new_name = ", ".join(new_name)
        str_old_name = ", ".join(old_name)
        id_old = cursor.execute("""SELECT id FROM Rivers WHERE name=?""", (str_old_name,))
        id_old_new = cursor.fetchone()
        id_old = (id_old_new[0])
        try:
            if len(id) != 0:
                data_id = (id, str_old_name)
                print(data_id)
                cursor.execute("""UPDATE Rivers SET id =? WHERE name =?""", data_id)
                id_old = id
                print(id_old)

            if len(photo) != 0:
                empPhoto = convert_to_binary_data(photo)
                data_photo = (empPhoto, str_old_name)
                cursor.execute("""UPDATE Rivers SET image=? WHERE name=?""", data_photo)

            if len(description) != 0:
                data_description = (description, str_old_name)
                cursor.execute("""UPDATE Rivers SET description=? WHERE name=?""", data_description)

            if len(str_new_name) != 0:
                data_new_name = (new_name, id_old)
                cursor.execute("""UPDATE Rivers SET name=? WHERE id=?""", data_new_name)

            NewWindow.destroy()
            connection.commit()
        except sqlite3.Error as error:
            messagebox.showerror("Ошибка", f"Запись не была добавлена в базу данных. \nПодробнее: {error}")
        refresh_list()
        listbox.select_set(0)
        data_refresh()

    def explorer(event=None):
        global filePath
        global image
        filePath = filedialog.askopenfilename(parent=NewWindow, initialdir="/", title="Select file",
                                              filetypes=(("Images", "*.jpg* *.jpeg* *.bmp* *.png*"), ("all files", "*.*")))
        print(filePath)
        entry_path.delete(0, END)
        image = Image.open(filePath)
        resized_image = image.resize((400, 300))
        photo = ImageTk.PhotoImage(resized_image)
        image = photo
        label_image.config(image=photo, width=400, height=300)
        entry_path.config(state=NORMAL)
        entry_path.insert(END, filePath)
        entry_path.config(state=DISABLED)
    filePath = ''
    image = ''
    list_name = ''
    if (listbox.curselection()):
        list_name = listbox.get(listbox.curselection())
    if len(list_name) == 0:
        messagebox.showinfo('Информация', 'Выберите элемент из списка для изменения')
        return()

    NewWindow = Toplevel()
    NewWindow.title('Изменение записи в базе данных')
    NewWindow.geometry('880x365')
    NewWindow.resizable(False, False)

    label_name = Label(NewWindow, text='Наименование:')
    label_name.place(x=10, y=20)
    label_ID = Label(NewWindow, text='ID элемента:')
    label_ID.place(x=10, y=50)
    label_description = Label(NewWindow, text='Описание реки:')
    label_description.place(x=10, y=80)
    label_path = Label(NewWindow, text='Путь до файла:')
    label_path.place(x=425, y=20)

    entry_name = Entry(NewWindow, font='Arial 9')
    entry_name.place(x=110, y=22, width=300, height=20)
    entry_ID = Entry(NewWindow, font='Arial 9')
    entry_ID.place(x=110, y=52, width=300, height=20)
    entry_path = Entry(NewWindow, font='Arial 9', state=DISABLED)
    entry_path.place(x=515, y=22, width=300, height=20)
    entry_description = Text(NewWindow, wrap=WORD, font='Arial 9', state=NORMAL)
    entry_description.place(x=110, y=82, width=300, height=270)

    btn_exp = Button(NewWindow, text='Обзор', command=explorer)
    btn_exp.place(x=820, y=18)
    btn_cancel = Button(NewWindow, text='Закрыть', command=NewWindow.destroy)
    btn_cancel.place(x=25, y=327)
    btn_ok = Button(NewWindow, text='Изменить')
    btn_ok.place(x=22, y=292)

    label_image = Label(NewWindow, borderwidth=2, relief="ridge", width=55, height=20, image=image)
    label_image.place(x=425, y=52)
    btn_ok.bind('<Button-1>', lambda event: updateNote(list_name, entry_ID.get(), entry_name.get(),
                                                                   entry_path.get(), entry_description.get("1.0", "end-1c")))
    NewWindow.mainloop()

def find_data(event=None):
    search_query = simpledialog.askstring("Найти элемент'", "Введите название реки для поиска:")
    search_query = str(search_query)
    if search_query:
        global cursor
        cursor.execute('SELECT name FROM Rivers')
        names = cursor.fetchall()
        for index, name in enumerate(names):
            name = str(name)
            if search_query.lower() in name.lower():
                listbox.select_clear(0, END)
                listbox.select_set(index)
                data_refresh()
                return()
        else:
            messagebox.showinfo("Поиск", "Элемент не найден.")

# Menubar
menu = Menu(window)
new_item_fund = Menu(menu, tearoff=0)
new_item_fund.add_command(label='Найти...', command=find_data)
new_item_fund.add_separator()
new_item_fund.add_command(label='Добавить', command=add_data, accelerator='F2')
new_item_fund.add_command(label='Удалить', command=del_data, accelerator='F3')
new_item_fund.add_command(label='Изменить', command=change_data, accelerator='F4')
new_item_fund.add_separator()
new_item_fund.add_command(label='Выход', command=exit_program, accelerator='Ctrl + X')
new_item_ref = Menu(menu, tearoff=0)
new_item_ref.add_command(label='Содержание', command=content)
new_item_ref.add_separator()
new_item_ref.add_command(label='О программе', command=about)
menu.add_cascade(label='Фонд', menu=new_item_fund)
menu.add_cascade(label='Справка', menu=new_item_ref)

# Objects
window.columnconfigure(index=1, weight=3)
window.columnconfigure(index=2, weight=3)
window.columnconfigure(index=3, weight=40)
window.rowconfigure(index=1, weight=1)
listbox = Listbox(window)
listbox.grid(row=1, column=1, sticky="news", ipadx=1, ipady=1, padx=0, pady=0)
resized_image = image_database.resize((400, 300))
photo = ImageTk.PhotoImage(resized_image)
image_database = photo
T = Text(window, width=10, wrap=WORD, font='Arial 10', state=NORMAL)
label_image = Label(window, borderwidth=2, relief="ridge", image=image_database)
label_text = Label(window, borderwidth=2, relief="ridge", text='Описание',width=12)
canvas = Canvas(window, width=800, height=30, bg="lightblue")
canvas.create_text(450, 17, text="F1  -  Справка   |   F2  -  Добавить   |   F3  -  Удалить   |   "
                                 "F4  -  Изменить   |   F10  -  Меню", fill="black", font=("Arial 10"))
canvas.grid(row=2, column=1, columnspan=3, sticky="NSEW")
label_image.grid(row=1, column=2, sticky="n", ipadx=1, ipady=1, padx=0, pady=0)
T.grid(row=1, column=3, sticky = 'NSEW', ipadx=3, ipady=3, padx=3, pady=3)
T.insert(END, 'Нажмите на название реки в левом столбце для отображения ее описания...')
T.config(state=DISABLED)
refresh_list()

def convert_data(data, file_name):
    # Convert binary format to
    # images or files data
    with open(file_name, 'wb') as file:
        file.write(data)
    img = Image.open(file_name)

def data_refresh(event=None):
    if (listbox.curselection()):
        list_name = listbox.get(listbox.curselection())
        cursor.execute('SELECT description FROM Rivers WHERE name=?', list_name)
        elements = cursor.fetchall()
        for text in elements:
            str_text = ", ".join(text)
        T.config(state=NORMAL)
        T.delete(1.0, END)
        T.insert(END, str_text)
        T.config(state=DISABLED)
        cursor.execute('SELECT image FROM Rivers WHERE name=?', list_name)
        images = cursor.fetchall()
        for row in images:
            blob_image = row[0]
        global image_database_path
        global image_database
        path = image_database_path
        convert_data(blob_image, image_database_path)
        image_database = Image.open(image_database_path)
        resized_new_image = image_database.resize((400, 300))
        image_database = ImageTk.PhotoImage(resized_new_image)
        label_image.config(image=image_database)
        window.update()

#insertData()
window.bind('<Button-1>', data_refresh)
window.bind('<F1>', content)
window.bind('<F2>', add_data)
window.bind('<F3>', del_data)
window.bind('<F4>', change_data)
window.bind('<Control-x>', exit_program)
window.bind('<F10>', content)
window.config(menu=menu)
window.mainloop()

connection.commit()
connection.close()
