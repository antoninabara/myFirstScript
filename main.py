# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# from datetime import datetime

# print(datetime.today().weekday())


def enter_name():
    return input('Hi, please enter your name: ')


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def enter_age():
    return input('Hi, please enter your age: ')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    my_name = enter_name()
    age_string = enter_age()
    age = int(age_string)
    if age >= 18:
        print_hi(my_name)
    else:
        print('Sorry, bye')




# See PyCharm help at https://www.jetbrains.com/help/pycharm/


