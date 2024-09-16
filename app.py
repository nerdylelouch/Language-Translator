import tkinter as tk
import os
from tkinter import *
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES
import speech_recognition as sr


#font_path = os.path.join(os.getcwd(), 'DragonHunter-9Ynxj.otf')
#tk.Font(nametofont='DragonHunter').configure(fontfile=font_path)

# Initialize the translator
translator = Translator()

# Reverse lookup dictionary for language codes
lang_code_map = {v: k for k, v in LANGUAGES.items()}
text1 = ""

# Function to translate text
def translate_text():
    try:
        # Check if text_source contains text; if so, use it for translation
        if text_source.get("1.0", tk.END).strip():
            source_text = text_source.get("1.0", tk.END).strip()
            src_lang_name = combo_source_lang.get()
            dest_lang_name = combo_dest_lang.get()

            # Get the language codes from the names
            src_lang = lang_code_map.get(src_lang_name)
            dest_lang = lang_code_map.get(dest_lang_name)

            if not src_lang or not dest_lang:
                raise ValueError("Invalid source or destination language selected.")

            translation = translator.translate(source_text, src=src_lang, dest=dest_lang)
            text_result.delete("1.0", tk.END)
            text_result.insert(tk.END, translation.text)
        else:
            # If text_source is empty, attempt to recognize speech
            recognized_text = recognize_speech()
            if recognized_text:
                src_lang_name = combo_source_lang.get()
                dest_lang_name = combo_dest_lang.get()

                # Get the language codes from the names
                src_lang = lang_code_map.get(src_lang_name)
                dest_lang = lang_code_map.get(dest_lang_name)

                if not src_lang or not dest_lang:
                    raise ValueError("Invalid source or destination language selected.")

                translation = translator.translate(recognized_text, src=src_lang, dest=dest_lang)
                text_result.delete("1.0", tk.END)
                text_source.delete("1.0", tk.END)
                text_result.insert(tk.END, translation.text)
                text_source.insert(tk.END, recognized_text)
    except Exception as e:
        messagebox.showerror("Translation Error", str(e))

# Function to recognize speech
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        messagebox.showinfo("Voice Input Detected", "Please speak after clicking on 'OK'.")
        recognizer.adjust_for_ambient_noise(source)
        print("Please say something:")
        audio = recognizer.listen(source, timeout=0, phrase_time_limit=5)
        try:
            text = recognizer.recognize_google(audio)
            print(f"Recognized text: {text}")
            return text
        except sr.UnknownValueError:
            print("Could not understand audio")
            return None
        except sr.RequestError:
            print("Error with the request")
            return None

# Existing GUI setup code remains unchanged...
# Create the main window
root = tk.Tk()
root.title("Language Translator")
root.geometry("1920x1080")
root.config(background='lightblue')


#
label1 = Label(root,text= "Language Translator",font=("Castellar",35,"italic"),fg="white",bg="lightblue",padx=2,pady=5 )
label1.pack()

# Source language selection
label_source_lang = ttk.Label(root, text="Source Language",font='Castellar', background = 'lightblue')
label_source_lang.pack(pady=5)
combo_source_lang = ttk.Combobox(root, values=list(LANGUAGES.values()))
combo_source_lang.pack(pady=5)
combo_source_lang.set("english")  # Default value


# Destination language selection
label_dest_lang = ttk.Label(root, text="Destination Language",font='Castellar', background = 'lightblue')
label_dest_lang.pack(pady=5)
combo_dest_lang = ttk.Combobox(root, values=list(LANGUAGES.values()))
combo_dest_lang.pack(pady=5)
combo_dest_lang.set("spanish")  # Default value

# Text box for source text
label_source_text = ttk.Label(root, text="Source Text",font='Castellar', background = 'lightblue')
label_source_text.pack(pady=5)
text_source = tk.Text(root, height=10)
text_source.pack(pady=5)

# Translate button
button_translate = ttk.Button(root, text="Translate", command=translate_text)
button_translate.pack(pady=10)



# Text box for translation result
label_result_text = ttk.Label(root, text="Translated Text",font='Castellar', background = 'lightblue')
label_result_text.pack(pady=5)
text_result = tk.Text(root, height=10)
text_result.pack(pady=5)


# Run the application
root.mainloop()