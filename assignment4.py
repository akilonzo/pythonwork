print ("Enter First and Last Name:")
fname = input('First name :')
lname = input('Last name :')
fullnames = fname + " " + lname
phone = input('Phone No : ')
email = input("Enter Customers Email : ")
country =input("Enter Country : ")
city = input("Enter City :")
credit_score = int(input("Enter Credit score : "))
price = int(input("Enter  Price of  House You Wish to buy : "))
print("")

if  credit_score >= 780 and 850 :
    credit_status = "Excellent "
    down_payment = 0.0 * price
elif credit_score >= 740 and 779:
     credit_status = "Very  Good"
     down_payment = 0.2 * price
elif credit_score >= 720 and 739:
     credit_status = "Above  Average"
     down_payment= 0.3 * price
elif credit_score >= 680 and 719:
     credit_status = "Average"
     down_payment= 0.6 * price
elif credit_score >= 620 and 679:
     credit_status = "Average"
     down_payment= 0.18 * price
elif credit_score >= 580 and 619:
     credit_status = "Poor Credit "
     down_payment= 0.20 * price
elif credit_score > 520:
     credit_status = "Very Poor Credit"
     down_payment= 0.25 * price
else :
    print("error")
    down_payment = 0
    credit_status ="Credit is  too low "



print("Customers name: " + fullnames)
print("Mobile no:" + phone)
print("Email No: " + email)
print("Country : " + country)
print("City : " + city)
print("")
print("Price of New House : " + str(price))
print("credit Score : " + str(credit_score))
print("Loan Down payment : " + str(down_payment))
print("Your  Credit status is : " + credit_status)


