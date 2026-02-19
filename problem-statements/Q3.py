passing = [g for g in grades if g >= 50]

return float(sum(passing) / len(passing)) if passing else 0.0
