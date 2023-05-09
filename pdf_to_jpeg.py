from tkinter import *
from tkinter import filedialog
from pdf2image import convert_from_path
import customtkinter


file_path = ''


def open_file_dialog():
    global file_path
    file_path = filedialog.askopenfilename(filetypes=[("PDF File", "*.pdf")])
    print(file_path)


def create():
    selected_option = var.get()
    pdf2toimg(name=file_path, type=selected_option)


def pdf2toimg(name, type):
    pages = convert_from_path(name, 500)
    for count, page in enumerate(pages):
        page.save(f'{name}_{count}.{type}')
        print('page added')


def main():
    customtkinter.set_appearance_mode('dark')
    customtkinter.set_appearance_mode('dark-blue')
    root = customtkinter.CTk()
    root.geometry('500x350')
    frame = customtkinter.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill='both', expand=True)
    global var
    var = customtkinter.StringVar()

    button = customtkinter.CTkButton(
        master=frame, text='Select a file', command=open_file_dialog)
    button.pack(pady=20, padx=20)

    make = customtkinter.CTkButton(
        master=frame, text='Create a file', command=create)
    make.pack(pady=20, padx=20)

    label = customtkinter.CTkLabel(master=frame, text='Choose a type of image')
    label.pack(pady=10, padx=20)

    OPTIONS = ['JPG', 'PNG']
    for option in OPTIONS:
        type = customtkinter.CTkRadioButton(
            root, text=option, variable=var, value=option.lower())
        type.pack(pady=10, padx=20)
    root.mainloop()


if __name__ == "__main__":
    main()
