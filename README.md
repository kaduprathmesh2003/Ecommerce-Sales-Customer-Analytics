# E-commerce Sales & Customer Analytics

Intermediate portfolio project using Python, SQL, Power BI and Streamlit to explore sales trends, customer value, category performance and order outcomes.

> **Dataset:** synthetic sample data created for portfolio demonstration. It is not real company/customer data; do not present the results as real business outcomes.

## Business questions
- What are delivered sales, delivered orders and average order value?
- Which categories and products contribute most revenue?
- How do monthly sales and city performance change?
- What share of orders are delivered, cancelled or returned?
- Which customers have the highest delivered spend?

## Project files
- `data/ecommerce_orders.csv` — sample order-level dataset
- `analysis.py` — Python cleaning and KPI analysis
- `sql/schema.sql` and `sql/analysis_queries.sql` — MySQL schema and queries
- `streamlit_app.py` — interactive dashboard
- `POWER_BI_GUIDE.md` — Power BI measures and report design
- `PROJECT_PRESENTATION.md` — interview talking points
- `reports/` — generated analysis outputs

## Run locally
```bash
pip install -r requirements.txt
python analysis.py
streamlit run streamlit_app.py
```

## MySQL
Create the database/table using `sql/schema.sql`, import the CSV into `orders`, then run `sql/analysis_queries.sql`.

## Power BI
Follow `POWER_BI_GUIDE.md` to import the CSV, create DAX measures and build report pages. A `.pbix` file is not included; create it in Power BI Desktop.

## Deploy Streamlit
1. Push this repository to GitHub.
2. Sign in to Streamlit Community Cloud with GitHub.
3. Create a new app, select this repository and branch `main`, and set main file path to `streamlit_app.py`.
4. Deploy and test the public app URL.

## Resume bullet
Built an end-to-end e-commerce analytics project using Python, SQL and Power BI to analyze order trends, customer value, category performance and fulfilment outcomes; developed an interactive Streamlit dashboard and documented business KPIs.

## Limitations
The dataset is synthetic and does not include costs, profit, marketing spend, acquisition channel, web traffic or inventory. Therefore this project does not calculate profit margin, CAC, ROAS or inventory optimization.
