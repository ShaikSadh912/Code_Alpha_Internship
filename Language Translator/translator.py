from tkinter import *
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator
import pyttsx3

# -----------------------------
# Language Dictionary
# -----------------------------
languages = {
    "English": "en",
    "French": "fr",
    "Hindi": "hi",
    "Tamil": "ta",
    "Telugu": "te",
    "Kannada": "kn",
    "Spanish": "es",
    "German": "de",
    "Japanese": "ja",
    "Chinese": "zh-CN"
}

# -----------------------------
# Translate Function
# -----------------------------
def translate_text():
    text = input_text.get("1.0", END).strip()

    if not text:
        messagebox.showwarning(
            "Warning",
            "Please enter some text to translate."
        )
        return

    source = languages[source_lang.get()]
    target = languages[target_lang.get()]

    try:
        translated = GoogleTranslator(
            source=source,
            target=target
        ).translate(text)

        output_text.delete("1.0", END)
        output_text.insert(END, translated)

    except Exception as e:
        messagebox.showerror(
            "Translation Error",
            str(e)
        )

# -----------------------------
# Copy Function
# -----------------------------
def copy_text():
    text = output_text.get("1.0", END).strip()

    if text:
        root.clipboard_clear()
        root.clipboard_append(text)

        messagebox.showinfo(
            "Copied",
            "Translated text copied successfully."
        )

# -----------------------------
# Speak Function
# -----------------------------
def speak_text():
    text = output_text.get("1.0", END).strip()

    if not text:
        messagebox.showwarning(
            "Warning",
            "No translated text available."
        )
        return

    try:
        engine = pyttsx3.init()

        voices = engine.getProperty('voices')

        if voices:
            engine.setProperty('voice', voices[0].id)

        engine.setProperty('rate', 150)
        engine.setProperty('volume', 1.0)

        print("Speaking:", text)

        engine.say(text)
        engine.runAndWait()

        print("Speech completed")

    except Exception as e:
        print("Speech Error:", e)
        messagebox.showerror(
            "Speech Error",
            str(e)
        )

# -----------------------------
# Clear Function
# -----------------------------
def clear_text():
    input_text.delete("1.0", END)
    output_text.delete("1.0", END)

# -----------------------------
# Main Window
# -----------------------------
root = Tk()

root.title("Language Translation Tool")

root.geometry("850x550")

root.configure(bg="#E8E8E8")

# -----------------------------
# Heading
# -----------------------------
Label(
    root,
    text="Language Translation Tool",
    font=("Arial", 16, "bold"),
    bg="#E8E8E8"
).pack(pady=10)

# -----------------------------
# Input Section
# -----------------------------
Label(
    root,
    text="Enter text to translate:",
    bg="#E8E8E8",
    font=("Arial", 10)
).pack()

input_text = Text(
    root,
    width=60,
    height=5,
    font=("Arial", 11)
)
input_text.pack(pady=5)

# -----------------------------
# Source Language
# -----------------------------
Label(
    root,
    text="Choose source language:",
    bg="#E8E8E8"
).pack(pady=(10, 2))

source_lang = StringVar()
source_lang.set("English")

source_menu = ttk.Combobox(
    root,
    textvariable=source_lang,
    values=list(languages.keys()),
    state="readonly",
    width=20
)
source_menu.pack()

# -----------------------------
# Target Language
# -----------------------------
Label(
    root,
    text="Choose destination language:",
    bg="#E8E8E8"
).pack(pady=(10, 2))

target_lang = StringVar()
target_lang.set("French")

target_menu = ttk.Combobox(
    root,
    textvariable=target_lang,
    values=list(languages.keys()),
    state="readonly",
    width=20
)
target_menu.pack()

# -----------------------------
# Buttons
# -----------------------------
button_frame = Frame(root, bg="#E8E8E8")
button_frame.pack(pady=15)

Button(
    button_frame,
    text="Translate",
    command=translate_text,
    width=12
).grid(row=0, column=0, padx=5)

Button(
    button_frame,
    text="Copy",
    command=copy_text,
    width=12
).grid(row=0, column=1, padx=5)

Button(
    button_frame,
    text="Speak",
    command=speak_text,
    width=12
).grid(row=0, column=2, padx=5)

Button(
    button_frame,
    text="Clear",
    command=clear_text,
    width=12
).grid(row=0, column=3, padx=5)

# -----------------------------
# Output Section
# -----------------------------
Label(
    root,
    text="Translated Text:",
    bg="#E8E8E8",
    font=("Arial", 10)
).pack()

output_text = Text(
    root,
    width=60,
    height=5,
    font=("Arial", 11)
)
output_text.pack(pady=5)

# -----------------------------
# Run Application
# -----------------------------
root.mainloop()