import random
import sys

ALL_CLOSED = """
+------+  +------+  +------+
|      |  |      |  |      |
|   1  |  |   2  |  |   3  |
|      |  |      |  |      |
|      |  |      |  |      |
|      |  |      |  |      |
+------+  +------+  +------+"""

FIRST_GOAT = """
+------+  +------+  +------+
|  ((  |  |      |  |      |
|  oo  |  |   2  |  |   3  |
| /_/|_|  |      |  |      |
|    | |  |      |  |      |
|GOAT|||  |      |  |      |
+------+  +------+  +------+"""

SECOND_GOAT = """
+------+  +------+  +------+
|      |  |  ((  |  |      |
|   1  |  |  oo  |  |   3  |
|      |  | /_/|_|  |      |
|      |  |    | |  |      |
|      |  |GOAT|||  |      |
+------+  +------+  +------+"""

THIRD_GOAT = """
+------+  +------+  +------+
|      |  |      |  |  ((  |
|   1  |  |   2  |  |  oo  |
|      |  |      |  | /_/|_|
|      |  |      |  |    | |
|      |  |      |  |GOAT|||
+------+  +------+  +------+"""

FIRST_CAR_OTHERS_GOAT = """
+------+  +------+  +------+
| CAR! |  |  ((  |  |  ((  |
|    __|  |  oo  |  |  oo  |
|  _/  |  | /_/|_|  | /_/|_|
| /_ __|  |    | |  |    | |
|   O  |  |GOAT|||  |GOAT|||
+------+  +------+  +------+"""

SECOND_CAR_OTHERS_GOAT = """
+------+  +------+  +------+
|  ((  |  | CAR! |  |  ((  |
|  oo  |  |    __|  |  oo  |
| /_/|_|  |  _/  |  | /_/|_|
|    | |  | /_ __|  |    | |
|GOAT|||  |   O  |  |GOAT|||
+------+  +------+  +------+"""

THIRD_CAR_OTHERS_GOAT = """
+------+  +------+  +------+
|  ((  |  |  ((  |  | CAR! |
|  oo  |  |  oo  |  |    __|
| /_/|_|  | /_/|_|  |  _/  |
|    | |  |    | |  | /_ __|
|GOAT|||  |GOAT|||  |   O  |
+------+  +------+  +------+"""

def print_welcome_message():
    print('''The Monty Hall Problem, 
In the Monty Hall game show, you can pick one of three doors. One door
has a new car for a prize. The other two doors have worthless goats:
{}
Say you pick Door #1.
Before the door you choose is opened, another door with a goat is opened:
{}
You can choose to either open the door you originally picked or swap
to the other unopened door.

It may seem like it doesn't matter if you swap or not, but your odds
do improve if you swap doors! This program demonstrates the Monty Hall
problem by letting you do repeated experiments.

You can read an explanation of why swapping is better at
https://en.wikipedia.org/wiki/Monty_Hall_problem
'''.format(ALL_CLOSED, THIRD_GOAT))

def get_user_choice():
    while True:  
        response = input('Pick a door 1, 2, or 3 (or "quit" to stop): ').upper()
        if response == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        if response in {'1', '2', '3'}:
            return int(response)
        else:
            print('Invalid input. Please enter 1, 2, 3, or "quit".')

def display_goat_door(showGoatDoor):
    goat_doors = [FIRST_GOAT, SECOND_GOAT, THIRD_GOAT]
    print(goat_doors[showGoatDoor - 1])
    print('Door {} contains a goat!'.format(showGoatDoor))

def display_car_and_goats(doorThatHasCar):
    car_and_goats = [FIRST_CAR_OTHERS_GOAT, SECOND_CAR_OTHERS_GOAT, THIRD_CAR_OTHERS_GOAT]
    print(car_and_goats[doorThatHasCar - 1])
    print('Door {} has the car!'.format(doorThatHasCar))

def calculate_success_rate(swapWins, swapLosses, stayWins, stayLosses):
    totalSwaps = swapWins + swapLosses
    totalStays = stayWins + stayLosses
    swapSuccess = round(swapWins / totalSwaps * 100, 1) if totalSwaps != 0 else 0.0
    staySuccess = round(stayWins / totalStays * 100, 1) if totalStays != 0 else 0.0
    return swapSuccess, staySuccess

def display_results(swapWins, swapLosses, stayWins, stayLosses, swapSuccess, staySuccess):
    print()
    print('Swapping:     {} wins, {} losses, success rate {}%'.format(swapWins, swapLosses, swapSuccess))
    print('Not swapping: {} wins, {} losses, success rate {}%'.format(stayWins, stayLosses, staySuccess))
    print()

def main():
    print_welcome_message()

    swapWins, swapLosses, stayWins, stayLosses = 0, 0, 0, 0

    while True:
        doorThatHasCar = random.randint(1, 3)
        doorPick = get_user_choice()

        showGoatDoor = random.randint(1, 3)
        while showGoatDoor == doorPick or showGoatDoor == doorThatHasCar:
            showGoatDoor = random.randint(1, 3)

        display_goat_door(showGoatDoor)

        swap = input('Do you want to swap doors? Y/N: ').upper()
        if swap == 'Y':
            doorPick = [door for door in {1, 2, 3} - {doorPick, showGoatDoor}][0]

        display_car_and_goats(doorThatHasCar)

        if doorPick == doorThatHasCar:
            print('You won!')
            if swap == 'Y':
                swapWins += 1
            else:
                stayWins += 1
        else:
            print('Sorry, you lost.')
            if swap == 'Y':
                swapLosses += 1
            else:
                stayLosses += 1

        swapSuccess, staySuccess = calculate_success_rate(swapWins, swapLosses, stayWins, stayLosses)

        display_results(swapWins, swapLosses, stayWins, stayLosses, swapSuccess, staySuccess)

        input('Press Enter to repeat the experiment...')

if __name__ == "__main__":
    main()
