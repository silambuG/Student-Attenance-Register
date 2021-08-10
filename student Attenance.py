

listStd = ["ABDUL", "ABU", "MARISHA", "NIVI", "NITHIN", "SIDHU",






           ]


def manageStudent():

    print(""" 

  ------------------------------------------------------
 |======================================================| 
 |======== Welcome To Student Management System	========|
 |======================================================|
  ------------------------------------------------------

Enter 1 : To View Student's List 
Enter 2 : To Add New Student 
Enter 3 : To Search Student 
Enter 4 : To Remove Student   """)

    try:
        userInput = int(input("Please Select An Above Option: "))
    except ValueError:
        exit("\nHey! That's Not A Number")
    else:
        print("\n")


    if (userInput == 1):
        print("List Students\n")
        for students in listStd:
            print("# {}".format(students))

    elif (userInput == 2):
        newStd = input("Enter New Student: ")
        if (newStd in listStd):
            print("\nThis Student {} Already In The Database".format(newStd))
        else:
            listStd.append(newStd)
            print("\n# New Student {} Successfully Add \n".format(newStd.upper()))
            for students in listStd:
                print("# {}".format(students))

    elif (userInput == 3):
        srcStd = input("Enter Student Name To Search: ")
        if (srcStd in listStd):
            print("\# Record Found Of Student {}".format(srcStd))
        else:
            print("\n# No Record Found Of Student {}".format(srcStd))

    elif (userInput == 4):
        rmStd = input("Enter Student Name To Remove: ")
        if (rmStd in listStd):
            listStd.remove(rmStd)
            print("\n# Student {} Successfully Deleted \n".format(rmStd))
            for students in listStd:
                print("# {}".format(students))
        else:
            print("\# No Record Found of This Student {}".format(rmStd))

    elif (userInput < 1 or userInput > 4):
        print("Please Enter Valid Option")



    runagain=str(input("I you want to run again y/n:"))
    if runagain=="y":
        manageStudent()
    else:
        print("...........YORR JOB COMPLETED.............")
manageStudent()



