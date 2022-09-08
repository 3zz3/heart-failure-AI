# Import packages
import tkinter as tk
from tkinter import *
import pandas as pd
from sklearn.tree import DecisionTreeClassifier


# Run Machine Learning algorithm
df = pd.read_csv("heart_statlog_cleveland_hungary_final - iie.org 1.csv")
global x
x = df.drop(columns=["target"])
global y
y = df['target']
model = DecisionTreeClassifier()
model.fit(x, y)

# Set up window
window = tk.Tk()
window.title("HF ML Tool")
window.configure(background="white")
  
def get_data():
    age = age_entry.get()
    # if int(age) < 0 and int(age) > 110:
    #     print("Please enter the correct age.")

    sex = sex_buttons.get()
    pain_type = pain_type_buttons.get()
    resting_bps = resting_bps_entry.get()
    cholesterol = cholesterol_entry.get()
    fstng_bld_sgr = fstng_bld_sgr_buttons.get()
    resting_ecg = resting_ecg_buttons.get()
    max_hr = hr_entry.get()
    ex_angina = ex_angina_buttons.get()
    old_peak = old_peak_entry.get()
    ST_slope = ST_slope_buttons.get()
    window.destroy()
    analysis_result = hf_prediction(age, sex, pain_type, resting_bps, cholesterol, fstng_bld_sgr, resting_ecg, max_hr, ex_angina, old_peak, ST_slope)
    results_page(analysis_result)

def hf_prediction(age, sex, pain_type, resting_bps, cholesterol, fstng_bld_sgr, resting_ecg, max_hr, ex_angina, old_peak, ST_slope):
    predictions = model.predict([[age, sex, pain_type, resting_bps, cholesterol, fstng_bld_sgr, resting_ecg, max_hr, ex_angina, old_peak, ST_slope]])
    # global score
    # score = accuracy_score(y_test, predictions) * 100
    if predictions == 1:
        return True
    else:
        return False

    

def results_page(analysis_result):
    window = tk.Tk()
    window.title("HF ML Tool")
    window.configure(background="white")

    if analysis_result is True:
        text = f"It appears that you may be suffering from a Heart Failure Disease, according to the values that you have provided. \n Please consult a professional medical body to confirm the results of our ML model."
    else:
        text = f"The results of our analysis suggest that you may not be suffering from a Heart Failure Disease. \n If you believe the results of our ML model might be wrong, please consult a professional medical body for further information."

    # Frames
    header_frame = tk.Frame()
    h2_frame = tk.Frame(master=window, relief="ridge")
    results_frame = tk.Frame()
    results_frame.configure(background="white")


    # Titles
    h1 = tk.Label(text="Heart Failure Predictor",
                        foreground="white", background="darkblue",
                        height=5, width=60, master=header_frame, relief="solid", font="Arial 18 bold")

    h2 = tk.Label(text="Results",
                        foreground="darkblue", bg="aliceblue", height=4, width=100, master=h2_frame, relief="flat", font="Calibri 14 italic")

    results_label = tk.Label(text=text,
                        foreground="darkblue", bg="white", height=10, width=100, master=results_frame, relief="sunken", font="Arial 14")

    # Pack results page
    header_frame.pack(fill=tk.BOTH, expand=False, side=tk.TOP)
    h2_frame.pack(fill=tk.BOTH, expand=False)
    results_frame.pack(fill=tk.BOTH, padx=25, pady=55)

    h1.pack(fill=tk.BOTH, side=tk.TOP)
    h2.pack(fill=tk.BOTH)
    results_label.pack()
    window.mainloop()



# Frames
header_frame = tk.Frame()
h2_frame = tk.Frame(master=window, relief="ridge")
content_frame = tk.Frame()
content_frame.configure(background="white")


# Titles
h1 = tk.Label(text="Heart Failure Predictor",
                    foreground="white", background="darkblue",
                    height=5, width=60, master=header_frame, relief="solid", font="Arial 18 bold")

h2 = tk.Label(text="Please fill your medical details below to receive a status update or prediction on current Heart Failure conditions (if any).",
                    foreground="darkblue", bg="aliceblue", height=4, width=100, master=h2_frame, relief="ridge", font="Calibri 14 italic")

# Content labels and input entries
age_label = tk.Label(text="Age:", foreground="black", bg="white", height=1, width=25,
                     master=content_frame, font="Arial 12 bold")

age_entry = tk.Entry(fg="black", bg="white", width=25, master=content_frame)

sex_label = tk.Label(text="Sex:", foreground="black", bg="white", height=1, width=25,
                     master=content_frame, font="Arial 12 bold")
# Gender check list
sex_buttons = tk.StringVar()
sex_buttons.set("x")
s1 = tk.Radiobutton(master=content_frame, text='Male', value='1', variable=sex_buttons, fg="black", bg="white", font="Arial 12", activebackground="aliceblue")
s2 = tk.Radiobutton(master=content_frame, text='Female', value='0', variable=sex_buttons, fg="black", bg="white", font="Arial 12", activebackground="aliceblue")


pain_type_label = tk.Label(text="Chest pain type:", foreground="black", bg="white", height=1, width=25,
                     master=content_frame, font="Arial 12 bold")
# Chest pain type check list
pain_type_buttons = tk.StringVar()
pain_type_buttons.set("x")
pt1 = tk.Radiobutton(master=content_frame, text='Typical Angina', value='1', variable=pain_type_buttons, fg="black", bg="white", font="Arial 12", activebackground="aliceblue")
pt2 = tk.Radiobutton(master=content_frame, text='Atypical Angina', value='2', variable=pain_type_buttons, fg="black", bg="white", font="Arial 12", activebackground="aliceblue")
pt3 = tk.Radiobutton(master=content_frame, text='Non-Anginal Pain', value='3', variable=pain_type_buttons, fg="black", bg="white", font="Arial 12", activebackground="aliceblue")
pt4 = tk.Radiobutton(master=content_frame, text='Asymptomatic', value='4', variable=pain_type_buttons, fg="black", bg="white", font="Arial 12", activebackground="aliceblue")


# Resting BPS
resting_bps_label = tk.Label(text="Resting BP/S (mmHg):", foreground="black", bg="white", height=1, width=25,
                     master=content_frame, font="Arial 12 bold")
resting_bps_entry = tk.Entry(fg="black", bg="white", width=25, master=content_frame)

# Cholesterol 
cholesterol_label = tk.Label(text="Cholesterol (mg/dl):", foreground="black", bg="white", height=1, width=25,
                     master=content_frame, font="Arial 12 bold")
cholesterol_entry = tk.Entry(fg="black", bg="white", width=25, master=content_frame)

# Fasting blood sugar check list
fstng_bld_sgr_buttons = tk.StringVar()
fstng_bld_sgr_buttons.set("x")
fstng_bld_sgr_label = tk.Label(text="Fasting Blood Sugar:", foreground="black", bg="white", height=1, width=25,
                     master=content_frame, font="Arial 12 bold")
fstng_bld_sgr_1 = tk.Radiobutton(master=content_frame, text='> 120 mg/dl', value='1', variable=fstng_bld_sgr_buttons, fg="black", bg="white", font="Arial 12", activebackground="aliceblue")
fstng_bld_sgr_2 = tk.Radiobutton(master=content_frame, text='< 120 mg/dl', value='0', variable=fstng_bld_sgr_buttons, fg="black", bg="white", font="Arial 12", activebackground="aliceblue")

# Resting ECG check list
resting_ecg_buttons = tk.StringVar()
resting_ecg_buttons.set("x")
resting_ecg_label = tk.Label(text="Resting ECG:", foreground="black", bg="white", height=1, width=25,
                     master=content_frame, font="Arial 12 bold")
resting_ecg_1 = tk.Radiobutton(master=content_frame, text='Normal', value='0', variable=resting_ecg_buttons, fg="black", bg="white", font="Arial 12", activebackground="aliceblue")
resting_ecg_2 = tk.Radiobutton(master=content_frame, text='ST-T wave abnormality (T wave inversions\nand/or ST elevation or depression of > 0.05 mV)', value='1', variable=resting_ecg_buttons, fg="black", bg="white", font="Arial 12", activebackground="aliceblue")
resting_ecg_3 = tk.Radiobutton(master=content_frame, text="Left Ventricular Hypertrophy (showing probable\nor definite LVH by Estes' criteria)", value='2', variable=resting_ecg_buttons, fg="black", bg="white", font="Arial 12", activebackground="aliceblue") 

# Heart Rate
hr_label = tk.Label(text="MAX Heart Rate (60-202):", foreground="black", bg="white", height=1, width=25,
                     master=content_frame, font="Arial 12 bold")
hr_entry = tk.Entry(fg="black", bg="white", width=25, master=content_frame)

# Exercise Angina check list
ex_angina_buttons = tk.StringVar()
ex_angina_buttons.set("x")
ex_angina_label = tk.Label(text="Exercise-induced angina:", foreground="black", bg="white", height=1, width=25,
                     master=content_frame, font="Arial 12 bold")
ex_angina_1 = tk.Radiobutton(master=content_frame, text='Yes', value='1', variable=ex_angina_buttons, fg="black", bg="white", font="Arial 12", activebackground="aliceblue")
ex_angina_2 = tk.Radiobutton(master=content_frame, text='No', value='0', variable=ex_angina_buttons, fg="black", bg="white", font="Arial 12", activebackground="aliceblue")

# Oldpeak ST depression induced by exercise relative to rest
old_peak_label = tk.Label(text="Oldpeak ST:", foreground="black", bg="white", height=1, width=25,
                     master=content_frame, font="Arial 12 bold")
old_peak_entry = tk.Entry(fg="black", bg="white", width=25, master=content_frame)

# Slope of the peak exercise ST segment
ST_slope_label = tk.Label(text="ST slope:", foreground="black", bg="white", height=1, width=25,
                     master=content_frame, font="Arial 12 bold")
# ST slope check list
ST_slope_buttons = tk.StringVar()
ST_slope_buttons.set("x")
ST_slope_1 = tk.Radiobutton(master=content_frame, text='Upsloping', value='1', variable=ST_slope_buttons, fg="black", bg="white", font="Arial 12", activebackground="aliceblue")
ST_slope_2 = tk.Radiobutton(master=content_frame, text='Flat', value='2', variable=ST_slope_buttons, fg="black", bg="white", font="Arial 12", activebackground="aliceblue")
ST_slope_3 = tk.Radiobutton(master=content_frame, text='Downsloping', value='3', variable=ST_slope_buttons, fg="black", bg="white", font="Arial 12", activebackground="aliceblue")


# Submit button
submit_button = tk.Button(text="Submit!", fg="white",bg="darkblue", height=1, width=25, font="Calibri 12", command=get_data)


# Pack headers
header_frame.pack(fill=tk.BOTH, expand=False, side=tk.TOP)
h2_frame.pack(fill=tk.BOTH, expand=False)

h1.pack(fill=tk.BOTH, side=tk.TOP)
h2.pack(fill=tk.BOTH)


# Pack form contents
content_frame.pack(expand=True)

age_label.grid(row=0, column=0, pady=15)
age_entry.grid(row=0, column=1, padx=0, sticky="w")

sex_label.grid(row=2, column=0)
s1.grid(row=2, column=1, sticky="w")
s2.grid(row=2, column=2, sticky="w", pady=15)

pain_type_label.grid(row=4, column=0)
pt1.grid(row=4, column=1, sticky="w")
pt2.grid(row=4, column=2, sticky="w")
pt3.grid(row=5, column=1, sticky="w")
pt4.grid(row=5, column=2, sticky="w", pady=10)

resting_bps_label.grid(row=6, column=0, pady=15)
resting_bps_entry.grid(row=6, column=1, sticky="w")

cholesterol_label.grid(row=7, column=0, pady=15)
cholesterol_entry.grid(row=7, column=1, sticky="w")

fstng_bld_sgr_label.grid(row=8, column=0, pady=15)
fstng_bld_sgr_1.grid(row=8, column=1, sticky="w")
fstng_bld_sgr_2.grid(row=8, column=2, sticky="w")


resting_ecg_label.grid(row=9, column=0, pady=15)
resting_ecg_1.grid(row=9, column=1, sticky="w")
resting_ecg_2.grid(row=9, column=2, sticky="w")
resting_ecg_3.grid(row=10, column=1, sticky="w")

hr_label.grid(row=11, column=0, pady=15)
hr_entry.grid(row=11, column=1, sticky="w")

ex_angina_label.grid(row=12, column=0, pady=15)
ex_angina_1.grid(row=12, column=1, sticky="w")
ex_angina_2.grid(row=12, column=2, sticky="w")

old_peak_label.grid(row=13, column=0, pady=15)
old_peak_entry.grid(row=13, column=1, sticky="w")

ST_slope_label.grid(row=14, column=0, pady=15)
ST_slope_1.grid(row=14, column=1, sticky="w")
ST_slope_2.grid(row=14, column=2, sticky="w")
ST_slope_3.grid(row=15, column=1, sticky="w")

# Pack submit button
submit_button.pack(side=tk.BOTTOM, pady=17)

# Run the window widget
window.mainloop()






























































