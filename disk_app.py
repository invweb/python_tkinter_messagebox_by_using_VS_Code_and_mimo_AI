import tkinter as tk
from tkinter import filedialog, messagebox
import os
import shutil


class DiskApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Disk Info")
        self.root.geometry("400x250")

        tk.Label(root, text="Текст:").pack(pady=(10, 0))
        self.text_entry = tk.Entry(root, width=40)
        self.text_entry.pack(pady=5)

        tk.Label(root, text="Путь к папке:").pack(pady=(10, 0))
        self.path_entry = tk.Entry(root, width=40)
        self.path_entry.pack(pady=5)

        tk.Button(root, text="Обзор", command=self.browse_folder).pack(pady=2)
        tk.Button(root, text="Показать информацию", command=self.show_info).pack(pady=10)

    def browse_folder(self):
        path = filedialog.askdirectory()
        if path:
            self.path_entry.delete(0, tk.END)
            self.path_entry.insert(0, path)

    def show_info(self):
        text = self.text_entry.get()
        path = self.path_entry.get()

        if not path or not os.path.exists(path):
            messagebox.showerror("Ошибка", "Укажите существующий путь к папке")
            return

        items = os.listdir(path)
        total_size = sum(
            os.path.getsize(os.path.join(path, f))
            for f in items
            if os.path.isfile(os.path.join(path, f))
        )
        folders = sum(1 for f in items if os.path.isdir(os.path.join(path, f)))
        files = sum(1 for f in items if os.path.isfile(os.path.join(path, f)))

        info = (
            f"Текст: {text or '(пусто)'}\n\n"
            f"Путь: {path}\n"
            f"Папок: {folders}\n"
            f"Файлов: {files}\n"
            f"Общий размер файлов: {total_size / 1024:.1f} КБ"
        )
        messagebox.showinfo("Информация", info)


if __name__ == "__main__":
    root = tk.Tk()
    app = DiskApp(root)
    root.mainloop()
