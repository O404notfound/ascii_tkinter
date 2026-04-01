import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

ASCII_CHARS = ["@", "#", "M", "%", "?", "*", "+", ";", ":", ",", "."]

def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio * 0.5) 
    return image.resize((new_width, new_height))

def convert_to_ascii():
    file_path = file_label.cget("text")
    if not file_path or file_path == "photo found":
        messagebox.showwarning("Error", "Not found photo")
        return

    try:
        width = int(width_entry.get())
        img = Image.open(file_path)
        
        img = resize_image(img, width).convert("L")
        pixels = img.getdata()
        
        characters = "".join([ASCII_CHARS[pixel // 25] for pixel in pixels])
        pixel_count = len(characters)
        ascii_img = "\n".join([characters[index:(index+width)] for index in range(0, pixel_count, width)])
        
        text_output.delete('1.0', tk.END)
        text_output.insert(tk.END, ascii_img)
        
    except Exception as e:
        messagebox.showerror("Error:", e)

def select_file():
    path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp")])
    if path:
        file_label.config(text=path)

# Интерфейс 
root = tk.Tk()
root.title("ascii")
root.geometry("900x700")
root.configure(bg="#2c3e50")

frame = tk.Frame(root, bg="#34495e", bd=5)
frame.pack(side=tk.TOP, fill=tk.X)

btn_select = tk.Button(frame, text="select photo", command=select_file, bg="#e67e22", fg="white", font=("Arial", 10, "bold"))
btn_select.pack(side=tk.LEFT, padx=10, pady=10)

file_label = tk.Label(frame, text="the phote not select", bg="#34495e", fg="#ecf0f1", width=40, anchor="w")
file_label.pack(side=tk.LEFT, padx=10)

tk.Label(frame, text="width:", bg="#34495e", fg="white").pack(side=tk.LEFT, padx=5)
width_entry = tk.Entry(frame, width=5)
width_entry.insert(0, "100")
width_entry.pack(side=tk.LEFT, padx=5)

btn_convert = tk.Button(frame, text="start", command=convert_to_ascii, bg="#27ae60", fg="white", font=("Arial", 10, "bold"))
btn_convert.pack(side=tk.LEFT, padx=20)

text_frame = tk.Frame(root, bg="black")
text_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

scrollbar = tk.Scrollbar(text_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

text_output = tk.Text(text_frame, bg="black", fg="#00ff00", font=("Courier", 8), 
                      wrap=tk.NONE, yscrollcommand=scrollbar.set)
text_output.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.config(command=text_output.yview)

root.mainloop()
