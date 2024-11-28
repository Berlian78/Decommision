import tkinter as tk
from tkinter import messagebox, ttk

# Initialize the main window
window = tk.Tk()
window.title("Decommissioning Cost Calculator")
window.geometry("400x500")

# Constants
BIAYA_TEMPAT = 205000  # Biaya Penyimpanan Tempat per kg
BIAYA_TRANSPORT = 130000
VERY_LOW_ACTIVITY_PERSON_FACTOR = 2.5  
LOW_ACTIVITY_PERSON_FACTOR = 25  
INTERMEDIATE_ACTIVITY_PERSON_FACTOR = 50 
VERY_LOW_ACTIVITY_HOURS_FACTOR = 10
LOW_ACTIVITY_HOURS_FACTOR = 100 
INTERMEDIATE_ACTIVITY_HOURS_FACTOR = 200 
GAJI_VERY_LOW_ACTIVITY = 68000
GAJI_LOW_ACTIVITY = 88000
GAJI_INTERMEDIATE_ACTIVITY = 108000
INVESTMENT_VLLW = 681000
INVESTMENT_LLW = 6810000
INVESTMENT_ILW = 13620000
INVESTMENT_NON = 340000
LAMA_LISTRIK = 510000
LAMA_AIR = 32200
LAMA_AKOMODASI = 500000

# Function to format as Rupiah
def format_rupiah(amount):
    return f"Rp {amount:,.0f}".replace(',', '.')

# Function to calculate the decommissioning cost and required people
def calculate():
    try:
        # Get weight input
        weight_gram = float(weight_entry.get())
        if weight_gram <= 0:
            raise ValueError("Weight must be a positive number.")
        
        # Get selected activity type
        level_waste_type = activity_var.get()
        biaya_penyimpanan_transport = biaya_penyimpanan_tempat = jumlah_orang = gaji_orang = biaya_investment = 0
        biaya_lama_decom_listrik = biaya_lama_decom_air = biaya_lama_decom_akomodasi = 0

        if level_waste_type == "very low level waste":
            biaya_penyimpanan_transport = weight_gram * BIAYA_TRANSPORT
            biaya_penyimpanan_tempat = weight_gram * BIAYA_TEMPAT
            jumlah_orang = weight_gram * VERY_LOW_ACTIVITY_PERSON_FACTOR
            gaji_orang = jumlah_orang * GAJI_VERY_LOW_ACTIVITY
            biaya_investment = weight_gram * INVESTMENT_VLLW
            biaya_lama_decom_listrik = LAMA_LISTRIK * VERY_LOW_ACTIVITY_HOURS_FACTOR 
            biaya_lama_decom_air = LAMA_AIR * VERY_LOW_ACTIVITY_HOURS_FACTOR
            biaya_lama_decom_akomodasi = LAMA_AKOMODASI * VERY_LOW_ACTIVITY_HOURS_FACTOR
        elif level_waste_type == "low level waste":
            biaya_penyimpanan_transport = weight_gram * BIAYA_TRANSPORT
            biaya_penyimpanan_tempat = weight_gram * BIAYA_TEMPAT
            jumlah_orang = weight_gram * LOW_ACTIVITY_PERSON_FACTOR
            gaji_orang = jumlah_orang * GAJI_LOW_ACTIVITY
            biaya_investment = weight_gram * INVESTMENT_LLW
            biaya_lama_decom_listrik = LAMA_LISTRIK * LOW_ACTIVITY_HOURS_FACTOR 
            biaya_lama_decom_air = LAMA_AIR * LOW_ACTIVITY_HOURS_FACTOR
            biaya_lama_decom_akomodasi = LAMA_AKOMODASI * LOW_ACTIVITY_HOURS_FACTOR
        elif level_waste_type == "intermediate level waste":
            biaya_penyimpanan_transport = weight_gram * BIAYA_TRANSPORT
            biaya_penyimpanan_tempat = weight_gram * BIAYA_TEMPAT
            jumlah_orang = weight_gram * INTERMEDIATE_ACTIVITY_PERSON_FACTOR
            gaji_orang = jumlah_orang * GAJI_INTERMEDIATE_ACTIVITY
            biaya_investment = weight_gram * INVESTMENT_ILW
            biaya_lama_decom_listrik = LAMA_LISTRIK * INTERMEDIATE_ACTIVITY_HOURS_FACTOR 
            biaya_lama_decom_air = LAMA_AIR * INTERMEDIATE_ACTIVITY_HOURS_FACTOR
            biaya_lama_decom_akomodasi = LAMA_AKOMODASI * INTERMEDIATE_ACTIVITY_HOURS_FACTOR
        elif level_waste_type == "Non Radioactive":
            biaya_investment = weight_gram * INVESTMENT_NON
        else:
            raise ValueError("Please select a valid activity type.")
        
        # Calculate total cost
        Total_Biaya = (
            biaya_penyimpanan_transport +
            biaya_penyimpanan_tempat +
            gaji_orang +
            biaya_investment +
            biaya_lama_decom_listrik +
            biaya_lama_decom_air +
            biaya_lama_decom_akomodasi
        )

        # Format and display the result
        result_text.set(
            f"--- Calculation Results ---\n"
            f"Weight: {weight_gram} gram\n"
            f"Activity Type: {level_waste_type}\n"
            f"Total Cost: {format_rupiah(Total_Biaya)}"
        )

    except ValueError as e:
        messagebox.showerror("Input Error", str(e))

# Input section
tk.Label(window, text="Waste Weight (gram):").grid(row=0, column=0, padx=10, pady=10, sticky="e")
weight_entry = tk.Entry(window, font=("Arial", 12))
weight_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(window, text="Activity Type:").grid(row=1, column=0, padx=10, pady=10, sticky="e")

# Dropdown for activity type
activity_var = tk.StringVar()
activity_dropdown = ttk.Combobox(window, textvariable=activity_var, state="readonly", font=("Arial", 12))
activity_dropdown['values'] = ("Select Activity Type", "very low level waste", "low level waste", "intermediate level waste", "Non Radioactive")
activity_dropdown.current(0)
activity_dropdown.grid(row=1, column=1, padx=10, pady=10)

# Calculate button
calculate_button = tk.Button(window, text="Calculate", command=calculate, font=("Arial", 14), bg="blue", fg="white")
calculate_button.grid(row=2, column=0, columnspan=2, pady=20)

# Result display
result_text = tk.StringVar()
result_label = tk.Label(window, textvariable=result_text, font=("Arial", 12), fg="green", justify="left")
result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Run the main loop
window.mainloop()
