from tkinter import *
from tkinter import filedialog
from pdf2image import convert_from_path


def open_file_dialog():
    file_path = filedialog.askopenfilename(filetypes=[("PDF File", "*.pdf")])

    if file_path:
        pdf2toimg(file_path)
    # do something with the file path

def pdf2toimg(name:str):
    pages = convert_from_path(name, 500)
    for count, page in enumerate(pages):
        page.save(f'{count}.jpg', 'JPEG')

def main():
    root = Tk()
    root.withdraw()
    menu_bar = Menu(root)
    root.config(menu=menu_bar)
    file_menu_button = Menubutton(root, text="Select File", relief="raised", direction="below")
    file_menu_button.pack(side="left")

    file_menu_button.menu = Menu(file_menu_button)
    file_menu_button["menu"] = file_menu_button.menu

    file_menu_button.menu.add_command(label="Open", command=open_file_dialog)

    root.mainloop()
    

if __name__ == "__main__":
    main()
