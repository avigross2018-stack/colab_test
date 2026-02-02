from operators_func import add, sub, multi, divide, power, root, absolute_value, triangle_area, square_area, rectangle_area, circle_area
from user_input import user_input


def main():
    print(f'Welcome to the calculator!!\n'
          '----------------------------\n'
          'Developers: AviGross, YehudaDarmon.')
    print(f'Please choose your operator\n'
        '----------------------------\n'
        '1) ADD \n2) SUB \n3) MULTIPLY \n4) DIVIDE \n5) POWER \n6) ROOT \n7) ABSOLUTE VALUE\n'
            '8) TRIANGLE AREA \n9) SQUARE AREA \n10) RECTANGLE AREA \n11) CIRCLE AREA')
    while True:
        user_operator_choice = input()
        if user_operator_choice == '1':
            print('Enter the first number')
            user_numA = user_input()
            print('Enter the second number')
            user_numB = user_input()
            return add(user_numA, user_numB)
        
        elif user_operator_choice == '2':
            print('Enter the first number')
            user_numA = user_input()
            print('Enter the second number')
            user_numB = user_input()
            return sub(user_numA, user_numB)
        
        elif user_operator_choice == '3':
            print('Enter the first number')
            user_numA = user_input()
            print('Enter the second number')
            user_numB = user_input()
            return multi(user_numA, user_numB)
        
        elif user_operator_choice == '4':
            while True:
                print('Enter the first number')
                user_numA = user_input()
                print('Enter the second number')
                user_numB = user_input()
                if user_numB == 0:                
                    print(divide(user_numA, user_numB))
                    print('Choose again')
                    continue
                else:
                    return divide(user_numA, user_numB)
        
        elif user_operator_choice == '5':
            print('Enter the first number')
            user_numA = user_input()
            print('Enter the second number')
            user_numB = user_input()
            return power(user_numA, user_numB)
        
        elif user_operator_choice == '6':
            print('Enter the number')
            user_numA = user_input()       
            return root(user_numA)
        
        elif user_operator_choice == '7':
            print('Enter the number')
            user_numA = user_input()       
            return absolute_value(user_numA)
        
        elif user_operator_choice == '8':
            print('Enter the base')
            user_numA = user_input()
            print('Enter the hight')
            user_numB = user_input()
            return triangle_area(user_numA, user_numB)
        
        elif user_operator_choice == '9':
            print('Enter the size of the side')
            user_numA = user_input()       
            return square_area(user_numA)
        
        elif user_operator_choice == '10':
            print('Enter the first side')
            user_numA = user_input()
            print('Enter the second side')
            user_numB = user_input()
            return rectangle_area(user_numA, user_numB)
        
        elif user_operator_choice == '11':
            print('Enter the radius')
            user_numA = user_input()       
            return circle_area(user_numA)
        else:
            print('Invalid!! Try again.')
            continue

print(main())