print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python lol")

"""def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
#Add code here to calculate BMI
    bmi = weight/(height * height)
#Add code here to display calculate BMI
    print("Bmi = " + str(bmi))
    if bmi < 18.5:
        print("UnderWeight")
    elif bmi >= 18.5 and bmi <= 25.0 :
        print("NormalWeight")
    else :
        print("OverWeight")

calculate_bmi(weight=70, height=1.73)"""
def main():
    display_main_menu()
    get_user_input()

def display_main_menu():
    print("Enter some numbers seperated by commas (e.g. 5,67,32):")

def get_user_input():
    x = input()
    print("Hello," + x)
    y = x.split()

    z = [float(a) for a in y ]

    print(z)

main()

