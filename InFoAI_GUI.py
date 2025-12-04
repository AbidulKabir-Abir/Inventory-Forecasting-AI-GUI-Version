import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import tkinter as tk
from tkinter import filedialog, messagebox

def load_csv():
    file_path = filedialog.askopenfilename(
        title="Select CSV File", 
        filetypes=[("CSV Files", "*.csv")]
    )
    if not file_path:
        messagebox.showwarning("Warning", "No file selected!")
        return
    run_forecast(file_path)

def run_forecast(file_path):
    try:
        df = pd.read_csv(file_path, parse_dates=['Date'])
        df = df.sort_values('Date')
        df['Product_ID'] = df['Product'].astype('category').cat.codes
        df['Date_Ordinal'] = df['Date'].map(pd.Timestamp.toordinal)
        X = df[['Date_Ordinal', 'Product_ID']]
        y = df['Units_Sold']

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)
        model = LinearRegression()
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        mse = mean_squared_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        messagebox.showinfo("Model Results", f"MSE: {mse:.2f}\nR2 Score: {r2:.2f}")

        # Plot
        plt.figure(figsize=(10,5))
        plt.plot(df['Date'], df['Units_Sold'], label='Actual', marker='o')
        plt.plot(df['Date'].iloc[-len(y_pred):], y_pred, label='Predicted', marker='x')
        plt.xlabel('Date')
        plt.ylabel('Units Sold')
        plt.title('Inventory Forecasting')
        plt.legend()
        plt.grid(True)
        plt.show()
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI setup
root = tk.Tk()
root.title("Inventory Forecasting AI")
root.geometry("400x200")

tk.Label(root, text="Inventory Forecasting AI", font=("Arial", 16)).pack(pady=10)
tk.Button(root, text="Select CSV File and Run Forecast", command=load_csv).pack(pady=20)
tk.Label(root, text="CSV file must have: Date, Product, Units_Sold columns").pack(pady=10)

root.mainloop()
