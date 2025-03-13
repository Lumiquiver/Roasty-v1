import tkinter as tk
from tkinter import scrolledtext
from roastedbyai import Conversation, Style

class RoastyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Roasty - AI Roast Master")
        self.root.geometry("500x600")
        self.convo = Conversation(Style.default)
        
        # Chat Display
        self.chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, state='disabled', height=20)
        self.chat_display.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        # Input Field
        self.input_frame = tk.Frame(root)
        self.input_frame.pack(fill=tk.X, padx=10, pady=5)
        
        self.user_input = tk.Entry(self.input_frame, width=50)
        self.user_input.pack(side=tk.LEFT, padx=5, pady=5, expand=True, fill=tk.X)
        self.user_input.bind("<Return>", self.send_message)
        
        self.send_button = tk.Button(self.input_frame, text="Roast!", command=self.send_message)
        self.send_button.pack(side=tk.RIGHT)
        
    def send_message(self, event=None):
        user_text = self.user_input.get().strip()
        if not user_text:
            return
        
        self.display_message("You", user_text)
        response = self.convo.send(user_text)
        self.display_message("Roasty", response)
        
        self.user_input.delete(0, tk.END)
        
    def display_message(self, sender, message):
        self.chat_display.config(state='normal')
        self.chat_display.insert(tk.END, f"{sender}: {message}\n", 'tag_bold' if sender == "Roasty" else 'tag_normal')
        self.chat_display.config(state='disabled')
        self.chat_display.yview(tk.END)
        
    def on_close(self):
        self.convo.kill()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = RoastyApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_close)
    root.mainloop()
