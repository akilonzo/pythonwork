print ("Enter First and Last Name:")
fname = input('First name :')
lname = input('Last name :')
fullnames = fname + " " + lname

print("Enter Customers Phone Number: ")
phone = input('Phone No')
print("Enter Customer's email address: ")
email = input('email')

price = 10000
has_good_credit = True

if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price

print("Customers name: " + fullnames)
print("Mobile no:" + phone)
print("Email No: " + email)
print("Loan Down payment :" + str(down_payment))