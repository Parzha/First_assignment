def BMI_calculator(W,H):
    H=H/100
    return(W/pow(H,2))



def BMI_calculator_american(W,H):
    return((W/pow(H,2))*703)



flag=1
while(flag==1):
    print("What measurment do you prefer => for kg/cm type 1 or for pounds/inches type 2 ")
    user_perference=int(input())

    if user_perference==1:
        flag=0
        user_weight=int(input("please enter your weight in kg"))
        user_height=int(input("please enter your height in cm"))
        BMI = BMI_calculator(user_weight, user_height)
        if 18.5<BMI<24.9:
            print("with this",BMI,"you are Normal")
        elif BMI<18.5:
            print(("with this",BMI,"you are Underweight eat something for god sake"))
        elif 25<BMI<29.9:
            print("with this", BMI, "you are Overweight bro it's time to go to gym")
        elif 30<BMI<34.9:
            print("with this", BMI, "you are Obese STOP EATING YOU NEED TO VISIT A DOCTOR")
        else:
            print("with this", BMI, "you are  Extremely Obese YOU NEED SOME SERIOUS TREATMENT MY FRIEND")



    elif user_perference ==2:
        flag = 0
        user_weight = int(input("please enter your weight in pounds"))
        user_height = int(input("please enter your height in inches"))
        BMI = BMI_calculator(user_weight, user_height)
        if 18.5 < BMI < 24.9:
            print("with this", BMI, "you are Normal")
        elif BMI < 18.5:
            print(("with this", BMI, "you are Underweight eat something for god sake"))
        elif 25 < BMI < 29.9:
            print("with this", BMI, "you are Overweight bro it's time to go to gym")
        elif 30 < BMI < 34.9:
            print("with this", BMI, "you are Obese STOP EATING YOU NEED TO VISIT A DOCTOR")
        else:
            print("with this", BMI, "you are  Extremely Obese YOU NEED SOME SERIOUS TREATMENT MY FRIEND")


    else:
         print("invalid input try again")


