# Inventory Forecasting AI (GUI Version)

## Project Description
This is a beginner-friendly Python GUI project that predicts future inventory requirements using historical sales data. Users can select any CSV file at runtime and visualize forecasts and trends.  

## Features
- Select any CSV file with sales data
- Data validation and preprocessing
- Forecast inventory using Linear Regression
- Visualize actual vs predicted sales
- Forecast next 7 days inventory
- User-friendly GUI with instructions

## CSV Requirements
Your CSV must have these columns:
- `Date` (YYYY-MM-DD format)
- `Product`
- `Units_Sold`

## Technologies / Libraries
- Python 3.x
- pandas
- numpy
- matplotlib
- scikit-learn
- Tkinter (GUI)

## Installation
Clone the repository:  
```bash
git clone https://github.com/AbidulKabir-Abir/Inventory-Forecasting-AI-GUI-Version.git
cd Inventory-Forecasting-AI
pip install -r requirements.txt

Usage:

python InFoAI_GUI.py

Inventory-Forecasting-AI/
│
├── data/                  # Sample CSV files
├── InFoAI_GUI.py          # Main GUI script
├── requirements.txt       # Python dependencies
└── README.md              # Project description


