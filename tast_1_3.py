#קבל מחרוזת הכוללת קו תחתון (_)
#יצציר פונקציה שמחזירה את המחרות ללא קו תחתון
#הפוף את האות שאחרי הקו התחתון לאות גדולה

def snake_case_removal(n):
    x = list(n)
    while True:
        try:
            i = x.index('_')  # מצא את האינדקס של '_'
            x[i + 1] = x[i + 1].upper()  # המרה לאות גדולה
            x.pop(i)  # הסרת '_'
        except ValueError:
            break
    return ''.join(x)

if __name__ == '__main__':

    str = input('please enter a string with a snake case: ')
    print(snake_case_removal(str))

