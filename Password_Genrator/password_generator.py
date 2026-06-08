import customtkinter as ctk
import random
import string

ctk.set_appearance_mode("dark")
def generate_password():
    try:
        length = int(length_entry.get())

        characters = ""

        if uppercase_var.get() == "on":
            characters += string.ascii_uppercase

        if lowercase_var.get() == "on":
            characters += string.ascii_lowercase

        if numbers_var.get() == "on":
            characters += string.digits

        if symbols_var.get() == "on":
            characters += "!@#$%^&*"

        if not characters:
            password_label.configure(
                text="Select at least one option!"
            )
            return

        password = "".join(
            random.choice(characters)
            for _ in range(length)
        )

        password_label.configure(
            text=password
        )
        
        if length < 8:
            strength = "Weak"
            strength_color = "red"
        elif length < 12:
            strength = "Medium"
            strength_color = "orange"
        else:
            strength = "Strong"
            strength_color = "green"
            
        print("Strength:", strength)
        
        strength_label.configure(
            text=f"Strength: {strength}",
            text_color=strength_color
        )             

    except ValueError:
        password_label.configure(
            text="Enter valid length!"
        )
def copy_password():
    app.clipboard_clear()
    app.clipboard_append(password_label.cget("text")
)     
    
def reset_fields():
    length_entry.delete(0, "end")

    uppercase_var.set("on")
    lowercase_var.set("on")
    numbers_var.set("on")
    symbols_var.set("on")

    password_label.configure(text="----------------")
    strength_label.configure(
        text="Strength: --",
        text_color="white"
)
              
app = ctk.CTk()
app.geometry("600x650")
app.title("Smart Password Generator")

title = ctk.CTkLabel(
    app,
    text="SMART PASSWORD GENERATOR",
    font=("Arial", 24, "bold")
)
title.pack(pady=20)
subtitle = ctk.CTkLabel(
    app,
    text="Generate secure random passwords",
    text_color="gray"
)
subtitle.pack(pady=5)

length_frame = ctk.CTkFrame(app, fg_color="transparent")
length_frame.pack(pady=20)

ctk.CTkLabel(
    length_frame,
    text="Password Length",
    width=150
).pack(side="left")

length_entry = ctk.CTkEntry(
    length_frame,
    width=150
)
length_entry.pack(side="left")

uppercase_var = ctk.StringVar(value="on")
lowercase_var = ctk.StringVar(value="on")
numbers_var = ctk.StringVar(value="on")
symbols_var = ctk.StringVar(value="on")

options_label = ctk.CTkLabel(
    app,
    text="What would you like to include in your password?\n(Check or uncheck the options below)",
    font=("Arial", 14)
)
options_label.pack(pady=10)

checkbox_frame = ctk.CTkFrame(app, fg_color="transparent")
checkbox_frame.pack(pady=10)

uppercase_check = ctk.CTkCheckBox(
    checkbox_frame,
    text="Uppercase Letters",
    width=180,
    variable=uppercase_var,
    onvalue="on",
    offvalue="off"
)
uppercase_check.pack(anchor="w", pady=4)

lowercase_check = ctk.CTkCheckBox(
    checkbox_frame,
    text="Lowercase Letters",
    width=180,
    variable=lowercase_var,
    onvalue="on",
    offvalue="off"
)
lowercase_check.pack(anchor="w", pady=4)

numbers_check = ctk.CTkCheckBox(
    checkbox_frame,
    text="Numbers",
    width=180,
    variable=numbers_var,
    onvalue="on",
    offvalue="off"
)
numbers_check.pack(anchor="w", pady=4)

symbols_check = ctk.CTkCheckBox(
    checkbox_frame,
    text="Symbols",
    width=180,
    variable=symbols_var,
    onvalue="on",
    offvalue="off"
)
symbols_check.pack(anchor="w", pady=4)

button = ctk.CTkButton(
    checkbox_frame,
    text="Generate Password",
    command=generate_password
)
button.pack(pady=20)

password_title = ctk.CTkLabel(
    app,
    text="Generated Password",
    font=("Arial", 18, "bold")
)
password_title.pack(pady=(25,5))

password_label = ctk.CTkLabel(
    app,
    text="----------------",
    font=("Consolas", 16)
)
password_label.pack(pady=5)

strength_label = ctk.CTkLabel(
    app,
    text="Strength: --",
    font=("Arial", 16)
)
strength_label.pack(pady=10)

button_frame = ctk.CTkFrame(
    app,
    fg_color="transparent"
)
button_frame.pack(pady=10)

copy_button = ctk.CTkButton(
    button_frame,
    text="Copy Password",
    command=copy_password
)
copy_button.pack(side="left", padx=5)

reset_button = ctk.CTkButton(
    button_frame,
    text="Reset",
    command=reset_fields
)
reset_button.pack(side="left", padx=5)

app.mainloop()
