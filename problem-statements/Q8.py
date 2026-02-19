email = raw_input.strip().lower()

return email if email and email.count("@") == 1 else "Invalid Email"
