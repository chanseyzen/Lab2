import statistics


def main():
    display_main_menu()
    INPUT = get_user_input()
    calc_average(INPUT)
    find_min_max(INPUT)
    sort_temperature(INPUT)
    calc_median_temperature(INPUT)


def display_main_menu():
    print("Welcome!")

def get_user_input():
    x = input("Enter numbers with commas")
    y = x.split(",")
    z = [float(a) for a in y]
    print(z)
    return z
def calc_average(num):
    a = sum(num)/len(num)
    print(a)
    return a
def find_min_max(num):
    MINI = min(num)
    MAXI = max(num)
    print(MINI,MAXI)
    return (MINI,MAXI)

def sort_temperature(num):
    num.sort()
    print(num)
    return num

def calc_median_temperature(num):
    MEDIAN = statistics.median(num)
    print(MEDIAN)
    return MEDIAN


main()


