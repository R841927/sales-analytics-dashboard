# 📊 Sales Analytics Dashboard

An interactive sales analytics dashboard built using Python, Streamlit, Pandas, and Plotly. It helps users analyze sales performance, revenue, and profit through interactive charts and filters.

## 🚀 Features

- Upload sales data in Excel (`.xlsx`) or CSV (`.csv`) format.
- View total revenue, total profit, and total orders.
- Filter sales data by region and product.
- Visualize sales performance through interactive charts.
- Download filtered data as a CSV file.
- Explore sample sales data to understand dashboard functionality.

## 🛠️ Technologies Used

- **Python** — Core programming language
- **Streamlit** — Interactive dashboard interface
- **Pandas** — Data processing and analysis
- **Plotly Express** — Interactive data visualizations
- **OpenPyXL** — Excel file support

## 📁 Project Structure

```text
sales-analytics-dashboard/
├── app.py
├── requirements.txt
├── README.md
├── PROJECT_DOCUMENTATION.md
└── sample_sales.xlsx
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd sales-analytics-dashboard
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your actual GitHub repository URL.

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the dashboard

```bash
streamlit run app.py
```

The dashboard will open in your browser, usually at `http://localhost:8501`.

## 📈 How to Use

1. Start the application.
2. Upload a sales dataset in Excel or CSV format.
3. Ensure the dataset contains the required columns: `Product`, `Region`, `Sales`, `Profit`, and `Month`.
4. Select regions and products using the sidebar filters.
5. Review the sales metrics and charts.
6. Download the filtered dataset if required.

## 📊 Sample Data

The project includes a sample Excel dataset for testing the dashboard. The displayed results depend on the dataset uploaded.

## 🎯 Learning Objectives

This project demonstrates practical skills in data handling, data analysis, interactive visualization, and dashboard development using Python.

## 🔮 Future Improvements

- Monthly sales trend analysis
- Additional profit and product performance insights
- Improved data validation and error handling
- Deployment for public access

## 👨‍💻 Author

**Rupesh Thakur**

GitHub: Add your GitHub profile URL here.

LinkedIn: Add your LinkedIn profile URL here.

## 📄 License

This project is available for educational and portfolio purposes.

