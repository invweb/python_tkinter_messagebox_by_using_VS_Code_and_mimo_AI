import tkinter as tk
from tkinter import messagebox


class ConcatApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Объединение текста")
        self.root.geometry("500x250")
        self.root.configure(bg="white")

        tk.Label(root, text="Поле 1:", bg="white").pack(pady=(15, 0))
        self.field1 = tk.Entry(root, width=40, bg="#e0f0ff", fg="black", font=("Arial", 11))
        self.field1.pack(pady=5)

        tk.Label(root, text="Поле 2:", bg="white").pack(pady=(5, 0))
        self.field2 = tk.Entry(root, width=40, bg="#e0f0ff", fg="black", font=("Arial", 11))
        self.field2.pack(pady=5)

        tk.Button(root, text="Объединить", command=self.concat).pack(pady=10)

        self.result = tk.Label(root, text="", font=("Arial", 12), fg="blue",
                               bg="white", wraplength=450, justify="left", padx=20)
        self.result.pack(fill="x", padx=20)

    def concat(self):
        if not self.field1.get().strip() or not self.field2.get().strip():
            messagebox.showwarning("Внимание", "Оба поля должны быть заполнены!")
            return
        text = self.field1.get() + self.field2.get()
        self.result.config(text=text)


if __name__ == "__main__":
    root = tk.Tk()
    app = ConcatApp(root)
    root.mainloop()
