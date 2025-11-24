def classify_age(age):
    if age < 13:
        return "Child"
    elif age < 20:
        return "Teenager"
    elif age < 60:
        return "Adult"
    else:
        return "Senior"

print(classify_age(8))
print(classify_age(17))
print(classify_age(35))
print(classify_age(72))
