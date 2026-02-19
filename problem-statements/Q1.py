
amount, tip_percent = map(float, (amount, tip_percent))

return round(amount * (1 + tip_percent / 100), 2)
