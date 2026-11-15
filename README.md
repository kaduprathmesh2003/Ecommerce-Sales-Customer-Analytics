# E-commerce Sales & Customer Analytics

An intermediate portfolio project using **Python, SQL, Power BI and Streamlit** to explore e-commerce sales trends, customer value, product/category performance and order outcomes.

> **Dataset notice:** This project uses synthetic sample data created for portfolio demonstration. It is not real company or customer data; do not present the results as real business outcomes.

## Business questions
- What are delivered revenue, delivered orders and average order value?
- Which categories and products contribute the most delivered revenue?
- How do monthly sales and city performance change?
- What share of orders are delivered, cancelled or returned?
- Which customers have the highest delivered spend?

## Repository structure
- `data/ecommerce_orders.csv` — sample order-level dataset
- `analysis.py` — Python cleaning and KPI analysis
- `sql/schema.sql`, `sql/analysis_queries.sql` — MySQL schema and queries
- `streamlit_app.py` — interactive Streamlit dashboard
- `powerbi/Measures.dax` — Power BI KPI measures
- `powerbi/CalendarTable.dax` — date dimension expression
- `powerbi/ecommerce_theme.json` — report theme
- `powerbi/BUILD_DASHBOARD.md` — step-by-step dashboard build guide
- `POWER_BI_GUIDE.md` — overview of Power BI measures and report design
- `PROJECT_PRESENTATION.md` — interview talking points
- `reports/` — generated analysis outputs (created when Python analysis runs)

## Run locally
```bash
pip install -r requirements.txt
python analysis.py
streamlit run streamlit_app.py
```

## MySQL
Create the database/table using `sql/schema.sql`, import the CSV into `orders`, then run `sql/analysis_queries.sql`.

## Power BI dashboard
Open Power BI Desktop and follow [powerbi/BUILD_DASHBOARD.md](powerbi/BUILD_DASHBOARD.md). The guide includes data preparation, model relationships, DAX measures, a report theme and four suggested report pages.

**Important:** The repository contains the Power BI build assets and instructions, but does not yet contain a finished `.pbix` report. Build and save `Ecommerce_Sales_Customer_Analytics.pbix` in Power BI Desktop, then upload it to the `powerbi/` folder. Add dashboard screenshots to `powerbi/screenshots/`.

## Deploy Streamlit
1. Sign in to Streamlit Community Cloud with GitHub.
2. Create a new app and select this repository and branch `main`.
3. Set the main file path to `streamlit_app.py`.
4. Deploy, test the app, and add the actual public app URL here.

## Resume bullet
Built an end-to-end e-commerce analytics project using Python, SQL and Power BI to analyze order trends, customer value, category performance and fulfilment outcomes; developed an interactive Streamlit dashboard and documented business KPIs.

## Limitations
The dataset is synthetic and does not include costs, profit, marketing spend, acquisition channel, web traffic or inventory. Therefore this project does not calculate profit margin, CAC, ROAS or inventory optimization.
