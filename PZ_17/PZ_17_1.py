import tkinter as tk
from tkinter import ttk, messagebox


def submit():
    if not agree_var.get():
        messagebox.showwarning("Warning", "You must agree to the Terms of Use")
        return
    data = {
        "first_name": first_name_entry.get(),
        "last_name": last_name_entry.get(),
        "screen_name": screen_name_entry.get(),
        "dob_month": dob_month_combobox.get(),
        "dob_day": dob_day_combobox.get(),
        "dob_year": dob_year_combobox.get(),
        "gender": gender_var.get(),
        "country": country_combobox.get(),
        "email": email_entry.get(),
        "phone": phone_entry.get(),
        "password": password_entry.get(),
        "confirm_password": confirm_password_entry.get()
    }
    print("Form submitted with data:", data)


def cancel():
    window.destroy()


window = tk.Tk()
window.title("Sign Up")

frame = ttk.Frame(window, padding="10 10 10 10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

gender_var = tk.StringVar(value="Male")
agree_var = tk.BooleanVar()

ttk.Label(frame, text="First Name").grid(row=1, column=0, sticky=tk.W)
first_name_entry = ttk.Entry(frame, width=30)
first_name_entry.grid(row=1, column=1, sticky=tk.W)

ttk.Label(frame, text="Last Name").grid(row=2, column=0, sticky=tk.W)
last_name_entry = ttk.Entry(frame, width=30)
last_name_entry.grid(row=2, column=1, sticky=tk.W)

ttk.Label(frame, text="Screen Name").grid(row=3, column=0, sticky=tk.W)
screen_name_entry = ttk.Entry(frame, width=30)
screen_name_entry.grid(row=3, column=1, sticky=tk.W)

ttk.Label(frame, text="Date of Birth").grid(row=4, column=0, sticky=tk.W)
dob_month_combobox = ttk.Combobox(frame,
                                  values=["January", "February", "March", "April", "May", "June", "July", "August",
                                          "September", "October", "November", "December"], width=8)
dob_month_combobox.grid(row=4, column=1, sticky=tk.W)
dob_day_combobox = ttk.Combobox(frame, values=[str(i) for i in range(1, 32)], width=5)
dob_day_combobox.grid(row=4, column=2, sticky=tk.W)
dob_year_combobox = ttk.Combobox(frame, values=[str(i) for i in range(1900, 2025)], width=7)
dob_year_combobox.grid(row=4, column=3, sticky=tk.W)

ttk.Label(frame, text="Gender").grid(row=5, column=0, sticky=tk.W)
ttk.Radiobutton(frame, text="Male", variable=gender_var, value="Male").grid(row=5, column=1, sticky=tk.W)
ttk.Radiobutton(frame, text="Female", variable=gender_var, value="Female").grid(row=5, column=2, sticky=tk.W)

ttk.Label(frame, text="Country").grid(row=6, column=0, sticky=tk.W)
country_combobox = ttk.Combobox(frame, values=["USA", "Canada", "UK", "Australia"], width=30)
country_combobox.grid(row=6, column=1, sticky=tk.W)

ttk.Label(frame, text="E-mail").grid(row=7, column=0, sticky=tk.W)
email_entry = ttk.Entry(frame, width=30)
email_entry.grid(row=7, column=1, sticky=tk.W)

ttk.Label(frame, text="Phone").grid(row=8, column=0, sticky=tk.W)
phone_entry = ttk.Entry(frame, width=30)
phone_entry.grid(row=8, column=1, sticky=tk.W)

ttk.Label(frame, text="Password").grid(row=9, column=0, sticky=tk.W)
password_entry = ttk.Entry(frame, width=30, show="*")
password_entry.grid(row=9, column=1, sticky=tk.W)

ttk.Label(frame, text="Confirm Password").grid(row=10, column=0, sticky=tk.W)
confirm_password_entry = ttk.Entry(frame, width=30, show="*")
confirm_password_entry.grid(row=10, column=1, sticky=tk.W)

agree_checkbutton = ttk.Checkbutton(frame, text="I agree to the Terms of Use", variable=agree_var)
agree_checkbutton.grid(row=11, column=1, sticky=tk.W)

button_frame = ttk.Frame(frame)
button_frame.grid(row=12, column=1, columnspan=2, pady=10, sticky=tk.E)

submit_button = ttk.Button(button_frame, text="Submit", command=submit)
submit_button.grid(row=0, column=0, padx=5)

cancel_button = ttk.Button(button_frame, text="Cancel", command=cancel)
cancel_button.grid(row=0, column=1, padx=5)

window.mainloop()
