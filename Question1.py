1) def checkinput(n):
    try:
        int(n)
        return True
    except ValueError:
        return False
        
def dayoff(numberofday):
    if checkinput(numberofday)==True and 0<int(numberofday)<8:
        if int(numberofday)>5:
            print("выходной день")
        else:
            print("будний день")
    else:
        numberofday = input("некорректный ввод! введите цифру от 1 до 7: ")
        return dayoff(numberofday)
user_input = input("введите цифру от 1 до 7: ")
dayoff(user_input)
