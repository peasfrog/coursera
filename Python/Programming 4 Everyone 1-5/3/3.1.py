h = float(raw_input("Enter Hours:"))

r = float(raw_input("Enter pay rate: "))

otMultiplier = 1.5
pay = 0

if h > 40:
    ot = h - 40
    h = 40
    pay = (h * r) + (ot * (r * otMultiplier))
else:
    pay = h * r

print pay