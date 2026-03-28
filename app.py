import tkinter as tk

def main():
    window = tk.Tk()
    window.title("Hello World App")
    window.geometry("300x200")

    label = tk.Label(window, text="Hello World", font=("Arial", 12))
    label.pack(expand=True)

    window.mainloop()

if __name__ == "__main__":
    main()
