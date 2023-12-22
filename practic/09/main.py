import os
from pdf2docx import Converter
from docx2pdf import convert
from PIL import Image

def change_working_directory():
    new_directory = input("Введите новый рабочий каталог: ")
    os.chdir(new_directory)
    print(f"Рабочий каталог изменен на: {os.getcwd()}")

def convert_pdf_to_docx():
    pdf_file = input("Введите имя файла PDF: ")
    docx_file = input("Введите имя файла Docx для сохранения: ")

    cv = Converter(pdf_file)
    cv.convert(docx_file, start=0, end=None)
    cv.close()
    print(f"Преобразование завершено. Файл сохранен как: {docx_file}")

def convert_docx_to_pdf():
    docx_file = input("Введите имя файла Docx: ")
    pdf_file = input("Введите имя файла PDF для сохранения: ")

    convert(docx_file, pdf_file)
    print(f"Преобразование завершено. Файл сохранен как: {pdf_file}")

def compress_images():
    quality = int(input("Введите уровень качества сжатия (от 1 до 95): "))
    file_extension = input("Введите расширение файлов изображений для сжатия (например, jpg): ")
    file_list = [file for file in os.listdir() if file.endswith(f".{file_extension}")]
    
    if file_list:
        print(f"Сжимаем следующие изображения: {', '.join(file_list)}")
        for file in file_list:
            image = Image.open(file)
            image.save(file, quality=quality)
        print("Изображения успешно сжаты.")
    else:
        print(f"Изображения с расширением .{file_extension} не найдены.")

def delete_file_group():
    file_extension = input("Введите расширение файлов для удаления (например, txt): ")
    file_list = [file for file in os.listdir() if file.endswith(f".{file_extension}")]
    
    if file_list:
        print(f"Удаляем следующие файлы: {', '.join(file_list)}")
        for file in file_list:
            os.remove(file)
        print("Файлы успешно удалены.")
    else:
        print(f"Файлы с расширением .{file_extension} не найдены.")

def main():
    while True:
        print("""
        Выберите действие:
        0. Сменить рабочий каталог
        1. Преобразовать PDF в Docx
        2. Преобразовать Docх в PDF
        3. Произвести сжатие изображений
        4. Удалить группу файлов
        5. Выход
        """)

        choice = input("Введите номер действия: ")

        if choice == '0':
            change_working_directory()
        elif choice == '1':
            convert_pdf_to_docx()
        elif choice == '2':
            convert_docx_to_pdf()
        elif choice == '3':
            compress_images()
        elif choice == '4':
            delete_file_group()
        elif choice == '5':
            print("Выход из программы.")
            break
        else:
            print("Некорректный ввод. Пожалуйста, введите номер от 0 до 5.")

if __name__ == "__main__":
    main()
