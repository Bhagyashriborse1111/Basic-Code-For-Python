p=float(input("Enter principle:"))
r=float(input("Enter rate:"))
t=int(input("Enter time:"))
si = (p*r*t)/100
ci =p*((1+(r/100))**t)-p
print("simple intrest = ",si)
print("compound intrest = ",ci)