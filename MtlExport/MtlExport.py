import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def extract_materials(mtl_file_path, output_file_path, selected_game):
    if selected_game == "Select Game":
        messagebox.showerror('Error', 'Please select a valid game!')
        return
    materials = []
    with open(mtl_file_path, 'r', encoding='utf-8') as mtl_file:
        for line in mtl_file:
            line = line.strip()
            if line.startswith("newmtl "):
                material_name = line[len("newmtl "):]
                materials.append(f"MATERIAL {selected_game} {material_name}\n")

    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.writelines(materials)

def open_mtl_file():
    file_path = filedialog.askopenfilename(filetypes=[("MTL Files", "*.mtl")])
    mtl_entry.delete(0, tk.END)
    mtl_entry.insert(0, file_path)

def open_output_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    output_entry.delete(0, tk.END)
    output_entry.insert(0, file_path)

def process_mtl():
    mtl_file_path = mtl_entry.get()
    output_file_path = output_entry.get()
    selected_game = game_var.get()
    extract_materials(mtl_file_path, output_file_path, selected_game)
    status_label.config(text="Materials extracted successfully!")
    status_label.configure(bg='black', fg='')

# GUI oluşturma
root = tk.Tk()
root.title("MtlExport")
root.iconbitmap("mtlexport.ico")


frame = tk.Frame(root, padx=10, pady=10)
frame.pack()
frame.configure(background='black')

mtl_label = tk.Label(frame, text="MTL File:")
mtl_label.grid(row=0, column=0, sticky="e")
mtl_label.configure(fg='green', bg='black')

mtl_entry = tk.Entry(frame, width=40)
mtl_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
mtl_entry.configure(fg='green', bg='black')

mtl_button = tk.Button(frame, text="Browse", command=open_mtl_file)
mtl_button.grid(row=0, column=2, padx=5, pady=5)
mtl_button.configure(fg='green', bg='black')

output_label = tk.Label(frame, text="Output File:")
output_label.grid(row=1, column=0, sticky="e")
output_label.configure(fg='green', bg='black')

output_entry = tk.Entry(frame, width=40)
output_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
output_entry.configure(fg='green', bg='black')

output_button = tk.Button(frame, text="Browse", command=open_output_file)
output_button.grid(row=1, column=2, padx=5, pady=5)
output_button.configure(fg='green', bg='black')

game_var = tk.StringVar()
game_var.set("Select Game")
game_menu = tk.OptionMenu(frame, game_var, "Select Game", "MW", "C", "PS", "U1", "U2", "UC", "W")
game_menu.grid(row=2, column=1, padx=5, pady=5, sticky="ew")
game_menu.configure(fg='green', bg='black')


process_button = tk.Button(frame, text="Extract Materials", command=process_mtl)
process_button.grid(row=3, column=1, padx=5, pady=10, sticky="ew")
process_button.configure(fg='green', bg='black')

status_label = tk.Label(frame, text="", fg="green", bg="black")
status_label.grid(row=4, columnspan=3)

root.mainloop()
