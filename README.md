# 📊 Amazon Sales Analysis  


📊 Top Insights

💰 Total Revenue: ₹5.2M

📦 Total Orders: 8,432

🛒 Best-Selling SKU: SKU123 with ₹1.1M revenue

🏆 Top State: Maharashtra contributing 25% of sales

📈 Trend: Steady revenue growth across months## 

📌 Project Overview  
This project analyzes **Amazon Sales Data** to extract business insights.  
The workflow includes:  
- Data Cleaning & Preparation  
- Exploratory Data Analysis (EDA)  
- KPI and Summary Reports  
- Visualizations (PNG images)  
- Interactive Dashboard (Streamlit)  
- Presentation (PPT)  

---

## 📂 Repository Structure  

```
Amazon-Sales-Analysis/
│── Amazon_Sales_Analysis_Final.ipynb    # Jupyter Notebook with full analysis
│── app.py                               # Streamlit dashboard code
│── Amazon Sale Report.csv                # Raw dataset
│── outputs/                              # All generated outputs
│   ├── amazon_sales_clean.csv
│   ├── kpi_summary.csv
│   ├── monthly_sales_summary.csv
│   ├── sku_summary.csv
│   ├── state_summary.csv
│   ├── category_summary.csv
│   ├── daily_revenue.png
│   ├── monthly_revenue.png
│   ├── top_skus.png
│   ├── top_categories.png
│   ├── top_states.png
│── docs/
│   ├── Project_Report.pdf                # Final project report
│   ├── Presentation.pptx                 # PowerPoint slides
│── sql/
│   ├── amazon_sales_queries.sql          # SQL queries used for analysis
│── README.md                             # Project documentation
```

---

## 🚀 How to Run  

### 1️⃣ Run the Notebook  
```bash
jupyter notebook Amazon_Sales_Analysis_Final.ipynb
```
This will clean the dataset, generate summary CSVs, and create all images.

### 2️⃣ Run the Streamlit Dashboard  
```bash
streamlit run app.py
```

This launches the interactive dashboard for sales insights.  

---

## 📊 Key Outputs  

- **KPI Summary** → `outputs/kpi_summary.csv`  
- **Monthly Sales Summary** → `outputs/monthly_sales_summary.csv`  
- **SKU Summary** → `outputs/sku_summary.csv`  
- **State Summary** → `outputs/state_summary.csv`  
- **Category Summary** → `outputs/category_summary.csv`  
- **Visuals** → Revenue trends, Top SKUs, Categories, States  

---

## 🎯 Insights  

- Revenue trends over time (daily & monthly)  
- Best-performing SKUs & categories  
- Top contributing states  
- Overall KPIs (Total Revenue, Orders, Avg. Order Value)  

