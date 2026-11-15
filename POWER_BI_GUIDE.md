# Power BI dashboard guide

1. Open Power BI Desktop and import `data/ecommerce_orders.csv` using Get Data → Text/CSV.
2. Rename the table to `Orders`. Set `order_date` to Date, `quantity` to Whole Number, and prices to Decimal Number.
3. Create these measures:

```DAX
Delivered Revenue =
CALCULATE(
    SUMX(Orders, Orders[quantity] * Orders[unit_price] * (1 - Orders[discount])),
    Orders[order_status] = "Delivered"
)

Delivered Orders =
CALCULATE(DISTINCTCOUNT(Orders[order_id]), Orders[order_status] = "Delivered")

Unique Customers =
CALCULATE(DISTINCTCOUNT(Orders[customer_id]), Orders[order_status] = "Delivered")

Average Order Value = DIVIDE([Delivered Revenue], [Delivered Orders])
```

## Suggested report pages
- Executive Overview: KPI cards, monthly revenue line chart, category revenue bar chart.
- Customer Insights: top customers by spend and order frequency.
- Product & Geography: category/product and city revenue.
- Order Quality: delivered, cancelled and returned order mix.

Add slicers for date, category, city and payment method. Format revenue as INR. A Power BI `.pbix` file is not included; build and save it in Power BI Desktop.

**Caution:** The sample data is synthetic and has no cost, profit, marketing, traffic or inventory fields. Do not claim profit margin, ROAS, CAC or inventory optimization.
