# Build the Power BI dashboard

This folder contains the DAX measures, date table expression and report theme for the project. The source dataset is `../data/ecommerce_orders.csv`.

## 1. Import and prepare the data

1. Open **Power BI Desktop**.
2. Select **Home → Get data → Text/CSV** and choose `data/ecommerce_orders.csv` from the repository folder.
3. Select **Transform Data**.
4. Rename the query/table to **Orders**.
5. Set data types:
   - `order_id`, `customer_id`, `product`, `category`, `payment_method`, `city`, `order_status`: Text
   - `order_date`: Date
   - `quantity`: Whole number
   - `unit_price`, `discount`, `revenue`: Decimal number
6. Check for errors and blank order IDs, then select **Close & Apply**.

The CSV's `revenue` field is already calculated as quantity × unit price × (1 − discount). Use it rather than multiplying again.

## 2. Create the model

1. In **Modeling → New table**, paste the expression in [CalendarTable.dax](CalendarTable.dax).
2. Mark `Calendar[Date]` as the date table.
3. Create a one-to-many relationship from `Calendar[Date]` to `Orders[order_date]`.
4. Sort `Calendar[Month]` by `Calendar[Month Number]`.
5. Create each measure in [Measures.dax](Measures.dax) using **Modeling → New measure**. Create them one at a time.

## 3. Import the report theme

Select **View → Themes → Browse for themes**, then choose `ecommerce_theme.json`.

## 4. Build report pages

### Page 1 — Executive Overview
- KPI cards: Delivered Revenue, Delivered Orders, Average Order Value, Unique Customers.
- Line chart: Calendar[Year Month] on X-axis; Delivered Revenue on Y-axis.
- Clustered bar chart: Orders[category] by Delivered Revenue.
- Donut chart: Orders[order_status] by Total Orders.
- Slicers: Calendar[Year], Orders[city], Orders[payment_method].

### Page 2 — Customer Insights
- Bar chart: Orders[customer_id] by Delivered Revenue; apply Top N = 10.
- Bar chart: Orders[customer_id] by Delivered Orders; apply Top N = 10.
- Cards: Unique Customers and Average Order Value.
- Slicers: Calendar[Year], Orders[city].

### Page 3 — Product & Geography
- Bar chart: Orders[product] by Delivered Revenue.
- Bar chart: Orders[city] by Delivered Revenue.
- Matrix: Orders[category] and Orders[product], with Delivered Revenue, Delivered Orders and Units Sold.
- Slicers: Calendar[Year], Orders[category].

### Page 4 — Order Quality
- Donut chart: Orders[order_status] by Total Orders.
- Cards: Delivered Order Rate, Cancellation Rate, Return Rate.
- Bar chart: Orders[payment_method] by Total Orders.
- Slicers: Calendar[Year], Orders[city].

## 5. Formatting recommendations

- Set report page size to 16:9.
- Use INR currency formatting for Delivered Revenue and Average Order Value.
- Format Delivered Order Rate, Cancellation Rate, Return Rate and Revenue MoM Change % as percentages.
- Use consistent titles, align visuals, and avoid overcrowding.
- Add a footer: "Portfolio demonstration using synthetic sample data".

## 6. Validate before publishing

- Confirm totals against the CSV and the Python analysis output.
- Check that slicers filter all relevant visuals.
- Confirm the Calendar relationship is active.
- Save the report as `Ecommerce_Sales_Customer_Analytics.pbix` in this folder.
- Add the saved PBIX and screenshots to GitHub. The PBIX is a binary Power BI Desktop file and must be saved from Power BI Desktop; this repository currently provides the complete build assets, not a finished PBIX.

## Data limitations

The dataset is synthetic. It has no cost, profit, marketing spend, traffic, acquisition channel or inventory columns. Do not report profit, margin, ROAS, CAC or inventory metrics.
