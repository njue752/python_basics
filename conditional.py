# if.....else...statement
votes=4000
if votes>2500:
    print("You've won the election")
    print("You are the governor")

else:
    print("You've failed the election")



marks=0
if marks>80 and marks<=100:
    print("You have an A")

elif marks>70 and marks<81:
    print("You have a B")

elif marks>60 and marks<71:
    print("You have a C")

elif marks>50 and marks<61:
    print("You have a D")

elif marks>40 and marks<51:
    print("You have a E")

elif marks>=0 and marks<41:
    print("You have failed ")

else:
    print("Please Enter a value between 0 and 100 ")



    # use if else to create an atm machine that pops up a toast when a condition is fulfilled if one withdraws above 20000
    # output should be,"you have withdrawn above the recomm" ,above 10000 ."you have withdrawn below recomm" and
    # below 10000 "you have withdrawn less"
    # use users input

amount=float(input("How much cash do you wish to withdraw? "))
if amount>20000:
    print("You have withdrawn above the recomm")
elif amount>10000 and amount<20000:
    print("You have withdrawn  recomm")
else:
    print("You have withdrawn less")




# for loop
# while loop
