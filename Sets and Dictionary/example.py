users = [
    {"id": 1, "total": 100, "coupon": "P20"},
    {"id": 2, "total": 200, "coupon": "P30"},
    {"id": 3, "total": 300, "coupon": "P40"}
]

discounts = {
    "P20": (0.2, 0),
    "P30": (0.3, 0), 
    "P40": (0.4, 10)
}

for user in users:
    percent, fixed = discounts.get(user["coupon"], (0,0))
    discount = user["total"] * percent + fixed
    print(f"User {user["id"]} got this discount: {discount}")
