import customtkinter
from customtkinter import filedialog, END
from PIL import Image

def image_converter_jpg():
    """ Converts Image File Into JPG And Saves the converted image"""
    try:
        image = filedialog.askopenfilename()
        img_file = Image.open(image)
        edited_file = img_file.convert('RGB')
        edited_file.save(f"C:/Users/Stark/Desktop/y3krats-CODEBASE/Photo_Editor/{entry.get()}.jpg")
        entry.delete(0, END)
        created_file = customtkinter.CTkLabel(master=frame, text="File was created!")
        created_file.pack(pady=12, padx=10)
    except ValueError:
        error_label = customtkinter.CTkLabel(master=frame, text="Enter a new file name!")
        error_label.pack(pady=12, padx=10)
    except AttributeError:
        no_file = customtkinter.CTkLabel(master=frame, text="No file was selected.")
        no_file.pack(pady=12, padx=10)


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
root = customtkinter.CTk()
root.geometry("350x250")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="PNG to JPG Converter")
label.pack(pady=12, padx=10)

entry = customtkinter.CTkEntry(master=frame, placeholder_text="Enter new filename.")
entry.pack(pady=12, padx=10)

button_1 = customtkinter.CTkButton(master=frame, text="Select File", command=image_converter_jpg)
button_1.pack(pady=12, padx=10)


if __name__ == "__main__":
    root.mainloop()