#קבל מחרוזות מהמשתמש
#ברגע שקיבלת QUIT עצור את התוכנה
#בדוק אם יש מחרוזת קפולה
#אם יש ציין זאת אם אין ציין זאת
def duplicates_finder(a_list):
    if len(a_list) != len(set(a_list)):
        print("There were duplicates")
    else:
        print("There were no duplicates")

if __name__ == '__main__':
    list_of_string =[]
    while True:
        v = input('Enter string: ')
        if v == "quit":
            break
        else:
            list_of_string.append(v)
    duplicates_finder(list_of_string)

    list_of_string2 = list_of_string.copy()

