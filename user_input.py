def user_input():
    while True:
        user = input()
        try:
            return int(user)
        except (ValueError, TypeError):
            pass
        try:
            return float(user)
        except (ValueError, TypeError):
            pass
        print('You can choose only number')

print(user_input())