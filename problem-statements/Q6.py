conversions = {
    'C': lambda x: round((x * 9/5) + 32, 1),
    'F': lambda x: round((x - 32) * 5/9, 1)
}

return conversions[unit](value) if unit in conversions else "Invalid Unit"
