### Пакетная обработка файлов Autocad
### Возможности
### 1. Замена префикса слоев чертежей dwg с 'H' на 'CF'
### 2. Пересохранение файлов dwg в другую папку
### 3. Переименование файлов dwg на нужный префикс
### 4. Изменение версии файлов с Autocad 2007 на версию Autocad 2021

# import modules
import os
import win32com.client
from tkinter import filedialog
from tkinter import *

# making interface
root = Tk()
root.withdraw()

# getting application
app = win32com.client.Dispatch("AutoCAD.Application.21")

# layers rename function
old_pref = 'H'
new_pref = 'CF'

def lay_renam(adoc, old, new):
    for i in adoc.Layers:
    	spt = (i.Name).split('.', 1)
    	if spt[0] == old and len(spt) > 1:
    		i.Name = new + '.' + spt[1]

# getting directory
directory = filedialog.askdirectory(title = 'Исходные файлы')
new_folder = filedialog.askdirectory(title = 'Новые файлы')

# getting files
files = os.listdir(directory)

# filtering dwg files
dwg_files = [(i, 'new_' + i) for i in files if i.split('.')[-1] == 'dwg']

# files processing
for j in dwg_files:

    file_path = os.path.join(directory,j[0])

    new_file_path = os.path.join(new_folder,j[1])

    app.Documents.Open(file_path)

    adoc = app.ActiveDocument

    lay_renam(adoc, old_pref, new_pref)

    adoc.SaveAs(new_file_path, 48)

    adoc.Close()

print('ok')
