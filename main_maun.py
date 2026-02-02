from operators_func import add, sub, multi, divide, power, root
from user_input import user_input


def main():
    print(f'Welcome to the calculator!!🙋‍♂️\n'
          '----------------------------\n'
          'Developers: AviGross, YehudaDarmon.')
    print(f'Please choose your operator\n'
          '----------------------------\n'
          '1) ADD \n2) SUB \n3) MULTIPLY \n4) DIVIDE \n5) POWER \n6) ROOT \n7) ABSOLUTE VALUE')
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
        print('Enter the first number')
        user_numA = user_input()
        print('Enter the second number')
        user_numB = user_input()
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
    
print(main())