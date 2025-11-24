def discount(price, category):
    def student_discount(price):
        return price * 0.9 if price > 1000 else price * 0.95

    def regular_discount(price):
        return price * 0.85 if price > 2000 else price

    handler = {
        "student": student_discount
    }
    return handler.get(category, regular_discount)(price)
print("1200 student:", discount(1200, "student"))
print("500 student:", discount(500, "student"))
print("3000 other:", discount(3000, "other"))

