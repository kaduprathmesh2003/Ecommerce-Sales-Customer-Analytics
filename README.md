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
- `streamlit_app.py` — interactive dashboard with five tabs
- `.streamlit/config.toml` — dashboard theme
- `tests/test_dataset.py` — data-quality tests
- `.github/workflows/validate.yml` — automated checks on pushes and pull requests
- `powerbi/Measures.dax` — Power BI KPI measures
- `powerbi/CalendarTable.dax` — date dimension expression
- `powerbi/ecommerce_theme.json` — Power BI report theme
- `powerbi/BUILD_DASHBOARD.md` — step-by-step Power BI build guide
- `DEPLOYMENT_CHECKLIST.md` — deployment and final publishing steps

## Run locally
```bash
pip install -r requirements.txt
python analysis.py
streamlit run streamlit_app.py
```

## Dashboard features
The Streamlit dashboard includes:
1. **Executive overview** — delivered revenue, orders, customers, average order value, monthly revenue and category performance.
2. **Customer insights** — top customers by delivered spend and order count.
3. **Product & geography** — product, category and city performance.
4. **Order quality** — delivery, cancellation and return rates plus payment-method mix.
5. **Data explorer** — filtered order records and CSV export.

Use the sidebar to filter by date, category, city and payment method.

## MySQL
Create the database/table using `sql/schema.sql`, import the CSV into `orders`, then run `sql/analysis_queries.sql`.

## Power BI dashboard
Open Power BI Desktop and follow [powerbi/BUILD_DASHBOARD.md](powerbi/BUILD_DASHBOARD.md). The folder contains DAX measures, a date-table expression, a theme and a four-page report plan.

**Important:** A finished Power BI Desktop `.pbix` report has not yet been created or uploaded. Build and save `Ecommerce_Sales_Customer_Analytics.pbix` in Power BI Desktop, then add it to `powerbi/` along with dashboard screenshots.

## Deploy Streamlit
1. Sign in to Streamlit Community Cloud using GitHub.
2. Create a new app and select this repository and branch `main`.
3. Set the main file path to `streamlit_app.py`.
4. Deploy, test all tabs and filters, and record the actual public app URL.
5. Add the verified app URL here; no live URL is claimed until deployment is completed.

## Automated validation
GitHub Actions runs dataset tests, the Python analysis pipeline and a Python syntax check when changes are pushed to `main` or a pull request targets `main`.

To run the tests locally:
```bash
pip install -r requirements.txt pytest
pytest -q
```

## Resume bullet
Built an end-to-end e-commerce analytics portfolio project using Python, SQL, Power BI and Streamlit to analyze order trends, customer value, product/category performance and fulfilment outcomes; developed interactive dashboards and automated dataset validation.

## Limitations
The dataset is synthetic and does not include costs, profit, marketing spend, acquisition channel, web traffic or inventory. Therefore this project does not calculate profit margin, CAC, ROAS or inventory optimization.
