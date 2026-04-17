from PIL import Image, ImageTk
import tkinter as tk

root = tk.Tk()
root.attributes("-fullscreen", True)
root.configure(bg="black")

label = tk.Label(root, bg="black", fg="white", font=("Arial", 24))
label.pack(expand=True)

def show_idle():
    label.config(text="Listo\nPresiona el botón", image="", compound="none")

def show_message(text):
    label.config(text=text, image="", compound="none")
    root.update()

def show_screen(image_path):
    img = Image.open(image_path)
    img = img.resize((800, 480))
    photo = ImageTk.PhotoImage(img)
    label.config(image=photo, text="")
    label.image = photo
    root.update()
