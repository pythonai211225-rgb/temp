# רשימה של ציונים חייבים להיות בין 0 ל100
# אם ציון לא בטווח התעלם
# אם המשתמש מכניס -999 לעצור את התוכנה רק אם יש 10 ציונים
# הדפס כמה ציונים, את הגבוהה בניהם, ממוצע כיתתי
if __name__ == '__main__':
    print('starting')
    grades = []
    while True:
        try:
            grade = int(input('Enter grade: '))
        except ValueError:
            print('Invalid grade, please enter again')
            continue

        if grade == -999:
            if len(grades)>=10:
                break
            else:
                print(' There are not enough grades, please continue entering more grades')
                continue

        elif grade<0 or grade>100:
            print('Invalid grade, please enter again')
            continue


        else:
            grades.append(grade)

    print(len(grades))
    print(max(grades))
    print(sum(grades)/len(grades))




