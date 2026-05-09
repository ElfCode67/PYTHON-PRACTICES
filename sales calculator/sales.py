# SAMPLE SALES DATA (product, price, quantity)
sales = [
    ("Laptop", 1200, 3),
    ("Mouse", 25, 15),
    ("Keyboard", 45, 8),
    ("Monitor", 300, 5),
    ("USB Cable", 10, 30),
    ("Headphones", 80, 12)
]

# ----- LIST COMPREHENSIONS -----

# 1. Calculate total revenue for each product
revenues = [price * quantity for _, price, quantity in sales]
print("💰 Individual revenues:", revenues)

# 2. Get products over $50
expensive_products = [name for name, price, _ in sales if price > 50]
print("💎 Expensive products (>$50):", expensive_products)

# 3. Apply 10% discount to all prices
discounted_prices = [price * 0.9 for _, price, _ in sales]
print("🏷️ Discounted prices (10% off):", [round(p, 2) for p in discounted_prices])

# 4. Filter high quantity items (over 10 units)
bulk_items = [(name, qty) for name, _, qty in sales if qty > 10]
print("📦 Bulk items (>10 units):", bulk_items)

# 5. Create formatted strings
descriptions = [f"{name}: ${price} × {qty} = ${price*qty}" for name, price, qty in sales]
print("\n📋 FULL INVOICE:")
for desc in descriptions:
    print(f"   {desc}")

# ----- LAMBDA FUNCTIONS -----

print("\n" + "="*50)
print("📊 USING LAMBDA FUNCTIONS")

# 6. Sort products by price (lowest to highest)
sorted_by_price = sorted(sales, key=lambda x: x[1])
print("\n📈 Sorted by price (cheapest first):")
for product in sorted_by_price[:3]:
    print(f"   {product[0]}: ${product[1]}")

# 7. Sort by revenue (highest first)
sorted_by_revenue = sorted(sales, key=lambda x: x[1] * x[2], reverse=True)
print("\n💰 Top 3 revenue generators:")
for product in sorted_by_revenue[:3]:
    revenue = product[1] * product[2]
    print(f"   {product[0]}: ${revenue}")

# 8. Apply tax using lambda with map()
tax_rate = 0.08  # 8% tax
with_tax = list(map(lambda x: (x[0], x[1] * x[2] * (1 + tax_rate)), sales))
print(f"\n🧾 Total including {tax_rate*100}% tax:")
for name, total in with_tax:
    print(f"   {name}: ${total:.2f}")

# 9. Filter using lambda with filter()
high_value = list(filter(lambda x: x[1] * x[2] > 500, sales))
print("\n⭐ High value products (revenue > $500):")
for product in high_value:
    revenue = product[1] * product[2]
    print(f"   {product[0]}: ${revenue}")

# ----- COMBINING BOTH -----

print("\n" + "="*50)
print("🎯 FINAL SUMMARY")

# One-liner: Get names of products with revenue over $400 after discount
premium_after_discount = [
    name for name, price, qty in sales 
    if (price * 0.9) * qty > 400
]
print(f"Premium products (after 10% discount, revenue > $400): {premium_after_discount}")

# Total revenue using lambda + sum
total_revenue = sum(map(lambda x: x[1] * x[2], sales))
print(f"💰 Total store revenue: ${total_revenue}")

# Average price using lambda + statistics
avg_price = sum(map(lambda x: x[1], sales)) / len(sales)
print(f"📊 Average product price: ${avg_price:.2f}")