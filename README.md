# Football Player Performance Analysis

## Overview
This project analyzes FIFA player attributes and overall ratings over time.  
It includes data loading, cleaning, merging, exploratory analysis, correlation analysis,  
and a player comparison between Lionel Messi and Cristiano Ronaldo.

## Project Structure
Sports-Performance-Analytics/
│
├── data/                         # Processed or small sample data only
│   ├── processed/                # Cleaned datasets
│   └── raw/                      # (EMPTY in GitHub — ignored via .gitignore)
│
├── notebooks/                    # Jupyter notebooks for EDA & analysis
│   ├── 01_data_cleaning.ipynb
│   ├── 02_eda.ipynb
│   └── 03_modeling.ipynb
│
├── src/                          # Python scripts (modular code)
│   ├── data_loader.py
│   ├── preprocessing.py
│   ├── visualization.py
│   └── modeling.py
│
├── reports/                      # Generated reports, images, plots
│   └── figures/
│
├── .gitignore                    # Ignore raw data, venv, large files
├── requirements.txt              # Python dependencies
├── README.md                     # Project documentation
└── venv/                         # Virtual environment (ignored)


## Features
- Load and merge FIFA player datasets  
- Clean and preprocess data  
- Analyze rating distributions  
- Explore rating trends over time  
- Compute attribute correlations  
- Compare players (Messi vs Ronaldo)

## Key Insights
- Most players have overall ratings between 60–75  
- Top correlated attributes include reactions, ball_control, and dribbling  
- Messi and Ronaldo both peak around 2015–2016  
- Messi shows a smoother upward trend, while Ronaldo has more variation

## How to Run
1. Create and activate a virtual environment  
2. Install dependencies:  
   pip install -r requirements.txt  
3. Open notebooks/01_eda.ipynb  
4. Run all cells in order

## Future Work
- Cluster players by playstyle  
- Predict player ratings using machine learning  
- Build an interactive dashboard  
- Add more players or seasons
