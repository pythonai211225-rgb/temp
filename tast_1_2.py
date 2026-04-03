#קבל רשימה
#מיין את הרישמה
#מצא את האיבר האמצעי אם יש אם אין תן את הממוצע שלי שני באיברים האמצעים

def find_middle(lst):
    if len(lst) == 0:
        print('The list is empty, please enter another list')
        return None

    lst.sort()
    middle_index = len(lst) // 2

    if len(lst) % 2 == 1:
        return float(lst[middle_index])
    else:
        return (lst[middle_index - 1] + lst[middle_index]) / 2



if __name__ == '__main__':
    while True:
        s = input('Enter numbers separated by commas: ')
        try:
            lst = [float(x) for x in s.split(',')]
            break
        except ValueError:
            print("Invalid input! Please enter a list of numbers separated by commas.")

    print(find_middle(lst))



