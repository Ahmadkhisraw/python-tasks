import os
from pdf2docx import Converter
from docx2pdf import convert
from PIL import Image
import PySimpleGUI as sg

def change_working_directory(new_directory):
    os.chdir(new_directory)
    window["-OUTPUT-"].update(f"Рабочий каталог изменен на: {os.getcwd()}")

def convert_pdf_to_docx(pdf_file, docx_file):
    cv = Converter(pdf_file)
    cv.convert(docx_file, start=0, end=None)
    cv.close()
    window["-OUTPUT-"].update(f"Преобразование завершено. Файл сохранен как: {docx_file}")

def convert_docx_to_pdf(docx_file, pdf_file):
    convert(docx_file, pdf_file)
    window["-OUTPUT-"].update(f"Преобразование завершено. Файл сохранен как: {pdf_file}")

def compress_images(quality, file_extension):
    file_list = [file for file in os.listdir() if file.endswith(f".{file_extension}")]
    
    if file_list:
        for file in file_list:
            image = Image.open(file)
            image.save(file, quality=quality)
        window["-OUTPUT-"].update("Изображения успешно сжаты.")
    else:
        window["-OUTPUT-"].update(f"Изображения с расширением .{file_extension} не найдены.")

def delete_file_group(file_extension):
    file_list = [file for file in os.listdir() if file.endswith(f".{file_extension}")]
    
    if file_list:
        for file in file_list:
            os.remove(file)
        window["-OUTPUT-"].update("Файлы успешно удалены.")
    else:
        window["-OUTPUT-"].update(f"Файлы с расширением .{file_extension} не найдены.")

# Define the layout
layout = [
    [sg.Text("Текущий рабочий каталог:"), sg.Text(os.getcwd(), key="-CURRENT_DIR-", size=(40, 1))],
    [sg.Button("Сменить рабочий каталог")],
    [sg.Button("Преобразовать PDF в Docx"), sg.InputText(key="-PDF_FILE-"), sg.InputText(key="-DOCX_FILE-")],
    [sg.Button("Преобразовать Docх в PDF"), sg.InputText(key="-DOCX_FILE2-"), sg.InputText(key="-PDF_FILE2-")],
    [sg.Button("Произвести сжатие изображений"), sg.InputText(key="-QUALITY-", size=(5, 1)), sg.InputText(key="-FILE_EXTENSION-", size=(10, 1))],
    [sg.Button("Удалить группу файлов"), sg.InputText(key="-FILE_EXTENSION2-", size=(10, 1))],
    [sg.Output(size=(60, 10), key="-OUTPUT-")],
    [sg.Button("Выход")]
]

window = sg.Window("Image Compression Tool", layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == "Выход":
        break
    elif event == "Сменить рабочий каталог":
        new_directory = sg.popup_get_folder("Выберите новый рабочий каталог")
        if new_directory:
            change_working_directory(new_directory)
            window["-CURRENT_DIR-"].update(os.getcwd())
    elif event == "Преобразовать PDF в Docx":
        convert_pdf_to_docx(values["-PDF_FILE-"], values["-DOCX_FILE-"])
    elif event == "Преобразовать Docх в PDF":
        convert_docx_to_pdf(values["-DOCX_FILE2-"], values["-PDF_FILE2-"])
    elif event == "Произвести сжатие изображений":
        compress_images(int(values["-QUALITY-"]), values["-FILE_EXTENSION-"])
    elif event == "Удалить группу файлов":
        delete_file_group(values["-FILE_EXTENSION2-"])

window.close()
