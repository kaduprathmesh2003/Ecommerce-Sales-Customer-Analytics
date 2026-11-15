from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "ecommerce_orders.csv"

def load_orders():
    return pd.read_csv(DATA, parse_dates=["order_date"])

def test_required_columns_exist():
    df = load_orders()
    expected = {
        "order_id", "order_date", "customer_id", "product", "category",
        "quantity", "unit_price", "discount", "payment_method", "city",
        "order_status", "revenue"
    }
    assert expected.issubset(df.columns)

def test_order_ids_are_unique():
    df = load_orders()
    assert df["order_id"].is_unique

def test_revenue_matches_quantity_price_discount():
    df = load_orders()
    expected = (df["quantity"] * df["unit_price"] * (1 - df["discount"])).round(2)
    actual = df["revenue"].round(2)
    assert (expected - actual).abs().max() < 0.02

def test_status_values_are_expected():
    df = load_orders()
    assert set(df["order_status"].dropna().unique()).issubset(
        {"Delivered", "Cancelled", "Returned"}
    )

def test_dataset_has_valid_numeric_values():
    df = load_orders()
    assert (df["quantity"] > 0).all()
    assert (df["unit_price"] >= 0).all()
    assert df["discount"].between(0, 1).all()
