
# Start
def menu():
    print("")
    print(" Enter Option to Convert")
    print("")
    print("[C] Convert from Celsius")
    print("[F]Convert from fahrenheit")
    print("[M] Convert from Miles")
    print("[K] Convert from Kilometers")
    print("[In] Convert from Inches")
    print("[CM] Convert  from  Centimeters")
    print("[Q] Quit")
    op = str(input("Enter option you  would  like  to process as  shown  Above : "))
    return op

option = menu()

while option == "C" or "F":
    if option == "C":
        celsius = int(input("Enter Temp  To Convert Fahrenhite : "))
        fahren = (celsius * 9 / 5) + 32
        print(str(fahren) +"fahrenheit")
        option = menu()
    elif option == "F":
        fahren = int(input("Enter Temp To Convert to celsius : "))
        celsius = 5 / 9 * (fahren - 32)
        print(str(celsius)+"celsius")
        option = menu()
    elif option == "M":
        miles = int(input("Enter no To Convert  from Miles: "))
        kilom = miles * 0.62
        print(str(kilom) + "Miles")
        option = menu()
    elif option == "K":
        kilom = int(input("Enter no to convert from  kilometer: "))
        miles = kilom / 1.609344
        print(str(miles) + "Kilometers")
        option = menu()
    elif option == "In":
        inch = int(input("Enter no to convert from  Inches: "))
        centimeter = inch * 2.54
        print(str(centimeter) + "Centimeters")
        option = menu()

    elif option == "CM":
        centm = int(input("Enter no to convert from Centimeters : "))
        inch = centm * 0.393701
        print(str(inch) + "Inches")
        option = menu()

    elif option == "Q":
         print ("You have just quit the program")
         print(" Thank you ")


         break
    else:
         print("error  kindly  re-enter ")
         option = menu()
         break


