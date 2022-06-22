from time import *
import random

# Count Error
def mistake(string, userinput):
    error = 0
    for i in range(len(string)):
        try:
            if string[i] != userinput[i]:
                error += 1
        except:
            error += 1

    return error

# Speed Check
def speed(time_start, time_end, userinput):
    delay = time_end - time_start
    time_round = round(delay, 2)
    speed = len(userinput)/time_round

    return round(speed)


string = ['My name is A.', 'I live in Dhaka.',
          'I am professional.', 'My life it too boring.']
test_string = random.choice(string)

print('*****Typing Test*****')
print(test_string)
print()
time_start = time()
user_input = input("Please type this text:")
time_end = time()
print('Speed: ', speed(time_start, time_end, user_input),' word/sec')
print('Error: ', mistake(test_string, user_input))




    
