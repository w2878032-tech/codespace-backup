import json
import sys
from pathlib import Path

def load_products():
    path = Path(__file__).with_name("products.json")
    return json.loads(path.read_text(encoding="utf-8"))

def low_stock(products, threshold=10):
    return [p for p in products if p["stock"] < threshold]

if __name__ == "__main__":
    products = load_products()
    for item in low_stock(products):
        print(f"{item['name']}: 庫存 {item['stock']}，需要補貨")
