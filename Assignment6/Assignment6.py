
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print("Enter Student  Personal Detals")
print("----------------------------------------------")
first_name = input("Enter First Names : ")
last_name = input("Enter Last name")
student_id = input("Enter Students ID number :")
genders = input("Enter Gender enter M for male and F for  female : ")
city = input("Enter City : ")
country = input("Enter  Country : ")
continent = input("Enter  Continent  of  residence Enter A if form  (Africa ) and O if from Other : ")
email = input("Enter students email address : ")
phone_no = input("Enter  Phone Number : ")
print()
print(":::::::::::::::::::::::::::::::::::::::::::::")
print("Enter Marks  for the  Quiz and  Test ")
print(":::::::::::::::::::::::::::::::::::::::::::::")

Quiz1 = int(input("Enter Marks for Quiz 1 "))
while Quiz1 > 100:
    print("Error")
    print("Kindly re-Enter the Quiz marks should  not  be greater  than  100 ")
    Quiz1 = int(input("Quiz 1 "))

Quiz2 = int(input("Enter Marks for Quiz 2 : "))
while Quiz2 > 100:
    print("Error")
    print("Kindly re-Enter the Quiz 2 marks should  not  be greater  than  100 ")
    Quiz2 = int(input("Quiz 2 "))

Quiz3 = int(input("Enter Marks  for Quiz 3 : "))
while Quiz3 > 100:
    print("Error")
    print("Kindly re-Enter the Quiz 3 marks should  not  be greater  than  100 ")
    Quiz3 = int(input("Quiz 3 "))
print()
print(" Enter Marks  for  Tests taken ")

Test1 = int(input("Enter marks for test 1 : "))
while Test1 > 100:
    print("Error")
    print("Kindly re-Enter the Quiz 3 marks should  not  be greater  than  100 ")
    Test1 = int(input("Test 1 "))

Test2 = int(input("Enter marks for test 2 : "))
while Test2 > 100:
    print("error")
    print("Kindly re-Enter the Quiz 3 marks should  not  be greater  than  100 ")
    Test2 = int(input("Test 2 "))


zoomcalls = int(input("Enter Zoom  call participated  enter range no 1-3: "))

while zoomcalls > 3:
    print("error")
    print("Kindly enter range from 1-3")
    zoomcalls = int(input("Enter Zoom  call participated  : "))

homework_no = int(input("Enter  no of home programming assigment done enter no 1-10: "))

while homework_no >= 10:
    print("error")
    print("Kindly enter range from 1-9")
    homework_no = int(input("Enter  no of home programming assigment done: "))



quiz_avg = (((Quiz1 + Quiz2 + Quiz3 + Test1 + Test2) / 500) * 100)
ZoomScore = ((zoomcalls / 3) * 9)
AssignScore = ((homework_no / 10) * 10)



# Print  Report
print("")
print("-----------------------------")
print("Student  Details")
print("----------------------------")
print("Student Name :" + first_name + "" +last_name )
print("ID Number : ", student_id)
print("Mobile No : ", phone_no)
print("City of Residence : ",  city)
print("Country of Residence : ", country)
print("Email : ", email)
print("Gender : ",  genders)
print("-----------------------------------------------")
print("Students Marks from Quiz, Test and Assignments")
print("------------------------------------------------")
print("Quiz 1 Marks : " + str(Quiz1) + " Quiz 2 Marks :" + str(Quiz2) + " Quiz 3 Marks : " + str(Quiz3) + " Average Marks  for Quiz: "+ str(quiz_avg) )
print("Test 1  Marks : " + str(Test1) + " Test 2 marks :" + str(Test2))
print("Zoom Classes attended : " + str(zoomcalls) + " so you have recived " + str(ZoomScore) + " Points for attending zoom classes ")
print("Assignments Done: " + str(homework_no) + " points recived for  assignment done: " + str(AssignScore))

if genders =="F" and quiz_avg>= 76:
        if continent =="A":
            awardStatus = "To get Scholarship"
        else:
            awardStatus = "To get Partial Scholarship"
elif genders=="M" and quiz_avg>= 80:
        if continent == "A":
            awardStatus = "Full Scholarship Awarded"
        else:
            awardStatus = "To get Partial Scholarship"
else:
            awardStatus = "Sorry  you dont qualify"
print("-----------------------------------")
print(awardStatus)
print("-----------------------------------")
