if age < 12:
    price = 8
elif age >= 65:
    price = 10
else:
    price = 12 if is_student else 15

return price
