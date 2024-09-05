import os
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox

# Function to convert flac to mp3
def convert_flac_to_mp3(input_path, output_folder):
    if os.path.isdir(input_path):
        files = [os.path.join(input_path, f) for f in os.listdir(input_path) if f.endswith('.flac')]
    elif os.path.isfile(input_path) and input_path.endswith('.flac'):
        files = [input_path]
    else:
        messagebox.showerror("Error", "Invalid file or folder.")
        return

    os.makedirs(output_folder, exist_ok=True)

    for file in files:
        output_file = os.path.join(output_folder, os.path.splitext(os.path.basename(file))[0] + '.mp3')
        command = ['ffmpeg', '-i', file, '-b:a', '320k', output_file]
        subprocess.run(command)

    messagebox.showinfo("Conversion Complete", f"Files have been converted and saved to {output_folder}")

# GUI setup
def browse_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        set_destination_and_convert(folder_path)

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("FLAC files", "*.flac")])
    if file_path:
        set_destination_and_convert(file_path)

def set_destination_and_convert(input_path):
    output_folder = filedialog.askdirectory(title="Select Destination Folder")
    if output_folder:
        convert_flac_to_mp3(input_path, output_folder)

root = tk.Tk()
root.title("FLAC to MP3 Converter")

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

folder_btn = tk.Button(frame, text="Convert Folder", command=browse_folder)
folder_btn.pack(side=tk.LEFT, padx=10)

file_btn = tk.Button(frame, text="Convert File", command=browse_file)
file_btn.pack(side=tk.LEFT, padx=10)

root.mainloop()
