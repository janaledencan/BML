
try:
    grade=input("Enter number whick represents grade (0.0 - 1.0): ")

    if (grade >= '0.9') and (grade <= '1.0'):
        print('A')
    elif grade >= '0.8' and (grade <= '1.0'):
        print('B')
    elif grade >= '0.7' and (grade <= '1.0'):
        print('C')
    elif grade >= '0.6' and (grade <= '1.0'):
        print('D')
    elif grade < '0.6' and (grade <= '1.0'):
        print('F')
    elif (grade < '0.0') or (grade > '1.0'):
        print("Number is not valid.")

except:
    print("You have not entered any number")