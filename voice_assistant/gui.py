import tkinter as tk
from tkinter import scrolledtext
from .assistant import start_assistant, weather_info

def create_gui():
    root = tk.Tk()
    root.title("Voice Assistant")
    root.geometry("500x500")
    root.configure(bg="lightblue")

    label = tk.Label(root, text="Welcome to Voice Assistant", font=("Arial", 20), bg="lightblue")
    label.pack(pady=20)

    description_label = tk.Label(root, text="Voice Assistant Description:", font=("Arial", 12), bg="lightblue")
    description_label.pack()

    description_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10)
    description_area.pack()

    description_text = (
        "This Voice Assistant can perform various tasks:\n"
        "- Open YouTube and Google\n"
        "- Play music\n"
        "- Provide the current time\n"
        "- Check Weather\n"
        "- Respond to general queries\n"
    )

    description_area.insert(tk.INSERT, description_text)
    description_area.configure(state="disabled")

    button_frame = tk.Frame(root, bg="lightblue")
    button_frame.pack(pady=20)

    start_button = tk.Button(
        button_frame,
        text="Start Assistant",
        command=start_assistant,
        font=("Arial", 14),
        bg="green",
        fg="white",
    )
    start_button.grid(row=0, column=0, padx=10, pady=10)

    weather_button = tk.Button(
        button_frame,
        text="Check Weather",
        command=weather_info,
        font=("Arial", 14),
        bg="blue",
        fg="white",
    )
    weather_button.grid(row=0, column=1, padx=10, pady=10)

    root.mainloop()
