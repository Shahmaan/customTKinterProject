import customtkinter as ctk

ctk.set_appearance_mode("System")  # Modes: system (default), light, dark
ctk.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

window = ctk.CTk()  # create CTk window
window.geometry("1200x800")
window.title("CaseSystem @Nawaz")


def button_function():
    print("button pressed")


# widgets

# label
userVGRID_label = ctk.CTkLabel(
    window, text="VGR-ID:", text_color="white", font=("", 20)
)
userVGRID_label.place(relx=0.5, rely=0.4, anchor=ctk.CENTER)

# input field
userVGRID_input = ctk.CTkEntry(
    window, placeholder_text="Enter your VGR-ID", width=(200)
)
userVGRID_input.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

# button
userVGRID_button = ctk.CTkButton(window, text="Proceed", command=button_function)
userVGRID_button.place(relx=0.5, rely=0.6, anchor=ctk.CENTER)

# run
window.mainloop()
