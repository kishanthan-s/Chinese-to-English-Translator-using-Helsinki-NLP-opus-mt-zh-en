import tkinter as tk
from tkinter import ttk, messagebox
from translator_model import get_supported_languages, load_translation_model

root = tk.Tk()
root.title("Local Translator")
root.geometry("600x400")

tk.Label(root, text="Select Language Pair:").pack()
lang_var = tk.StringVar()
lang_choices = get_supported_languages()
lang_menu = ttk.Combobox(root, textvariable=lang_var, values=lang_choices, state='readonly')
lang_menu.pack()
lang_menu.current(0)

tk.Label(root, text="Enter Text (Chinese):").pack()
input_box = tk.Text(root, height=6)
input_box.pack(fill='both', expand=True)

tk.Label(root, text="Translated Text (English):").pack()
output_box = tk.Text(root, height=6, bg="#f0f0f0")
output_box.pack(fill='both', expand=True)

def translate():
    input_text = input_box.get("1.0", tk.END).strip()
    if not input_text:
        messagebox.showwarning("Warning", "Please enter text.")
        return
    try:
        tokenizer, model = load_translation_model(lang_var.get())
        inputs = tokenizer(input_text, return_tensors="pt", padding=True)
        translated = model.generate(**inputs)
        result = tokenizer.decode(translated[0], skip_special_tokens=True)
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, result)
    except Exception as e:
        messagebox.showerror("Error", str(e))

tk.Button(root, text="Translate", command=translate).pack(pady=10)
root.mainloop()
