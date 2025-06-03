import tkinter as tk
from tkinter import scrolledtext
import ollama
import sys
import threading
import time

model_ver = "gemma3:4b"
my_font = "Consolas"
messages = []
loading = False

# --- ASCII art ---
ascii_banner = r"""
............................................
............................................
................############................
............####################............
....#:....########################....:#....
....#:...###*..................*###...:#....
....#.#.###......................###.#.#....
....##.###:......................:###.##....
....##.###....#####......#####....###.##....
....##.###........................###.##....
....##.###.......................:###.##....
......#.###......................###.#......
.........####..................####.........
..........########################..........
............####################............
................############................
............................................
.................conversate.................
"""

# --- GUI Setup ---
root = tk.Tk()
root.title("conversate")
root.configure(bg="black")

# Chat area (including ASCII art at the top)
chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, bg="black", fg="white", font=(my_font, 10), insertbackground='white')
chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
chat_area.tag_configure("user", foreground="white")
chat_area.tag_configure("bot", foreground="white")
chat_area.config(state=tk.NORMAL)

# Insert ASCII art at the top of chat window
chat_area.insert(tk.END, ascii_banner + "\n")
chat_area.see(tk.END)

# Status bar (for <enter> and generating...)
status_label = tk.Label(root, text="", fg="white", bg="black", font=(my_font, 10), anchor="w")
status_label.pack(fill=tk.X, padx=10)

# Input entry
entry = tk.Entry(root, bg="black", fg="white", insertbackground="white", font=(my_font, 10))
entry.pack(fill=tk.X, padx=10, pady=(0, 10))
entry.focus()

# --- Animation ---
def animate_loading():
    dots = ["", ".", "..", "..."]
    i = 0
    while loading:
        status_label.config(text=f"Generating{dots[i % 4]}")
        time.sleep(0.4)
        i += 1

# --- Main send function ---
def send_message():
    user_input = entry.get()
    if not user_input.strip():
        return

    if user_input in ("/bye", "/exit"):
        root.destroy()
        sys.exit(0)

    chat_area.insert(tk.END, f"\n\n> {user_input}\n", "user")
    chat_area.see(tk.END)
    entry.delete(0, tk.END)

    messages.append({"role": "user", "content": user_input})

    def generate_response():
        global loading
        loading = True
        threading.Thread(target=animate_loading, daemon=True).start()

        try:
            bot_reply = ""
            for chunk in ollama.chat(model=model_ver, messages=messages, stream=True):
                new_text = chunk["message"]["content"]
                bot_reply += new_text
                chat_area.insert(tk.END, new_text, "bot")
                chat_area.see(tk.END)
                chat_area.update_idletasks()
            messages.append({"role": "assistant", "content": bot_reply})
        except Exception as e:
            chat_area.insert(tk.END, f"[ERROR] {str(e)}\n", "bot")
        finally:
            loading = False
            status_label.config(text="")

    threading.Thread(target=generate_response, daemon=True).start()

entry.bind("<Return>", lambda event: send_message())

# --- Start GUI Loop ---
root.mainloop()
