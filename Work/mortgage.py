# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months = 0

extra_payment  = 1000.0
extra_payment_start_month = 61
extra_payment_end_month = 108

while principal > 0:
    months += 1
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment

    # Apply extra payment if within the specified months
    if months >= extra_payment_start_month and months <= extra_payment_end_month:
        principal = principal - extra_payment
        total_paid = total_paid + extra_payment 
    
    # Ensure we don't pay more than the remaining principal
    if principal < 0:
        total_paid = total_paid + principal # Adjust final payment
        principal = 0.0  # To avoid negative principal in final month

    print(f"{months}  {total_paid:.2f}  {principal:.2f} ")


print(f"Total paid {total_paid:.2f}")
print(f"Months {months} or {months // 12} years and {months % 12} months")

