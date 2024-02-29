import random
from turtle import Screen, Turtle
import time

# screen = Screen()
#
# screen.setup(width=600, height=600)
# screen.bgcolor("black")
# screen.title("My Snake Game")
# screen.tracer(0)
# starting_positions = [(0, 0), (-20, 0), (-40, 0)]
#
# segments = []
#
#
# for position in starting_positions:
#     new_segment = Turtle("square")
#     new_segment.color("white")
#     new_segment.penup()
#     new_segment.goto(position)
#     segments.append(new_segment)

# screen.update()

game_is_on = True

print('creating list of numbers')
num_list = [];
for num in range(0, 1000000):
    num_list.append(num)

print('randomizing list of numbers')
random.shuffle(num_list)


# Total numbers assigned to each position
num_12 = 242857
num_11 = 202381
num_10 = 161905
num_9 = 121429
num_8 = 80952
num_7 = 40476

# Slice the numbers out to lists for each position
numbers_for_12 = num_list[0:num_12]
numbers_for_11 = num_list[num_12:(num_12+num_11)]
numbers_for_10 = num_list[num_12+num_11:(num_12+num_11+num_10)]
numbers_for_9 = num_list[num_12+num_11+num_10:(num_12+num_11+num_10+num_9)]
numbers_for_8 = num_list[num_12+num_11+num_10+num_9:(num_12+num_11+num_10+num_9+num_8)]
numbers_for_7 = num_list[num_12+num_11+num_10+num_9+num_8:(num_12+num_11+num_10+num_9+num_8+num_7)]

# and bowl winners
bowl_winner_1 = num_list[num_12+num_11+num_10+num_9+num_8+num_7:(num_12+num_11+num_10+num_9+num_8+num_7+50000)]
bowl_winner_2 = num_list[num_12+num_11+num_10+num_9+num_8+num_7+50000:(num_12+num_11+num_10+num_9+num_8+num_7+100000)]
bowl_winner_3 = num_list[num_12+num_11+num_10+num_9+num_8+num_7+100000:(num_12+num_11+num_10+num_9+num_8+num_7+150000)]


# print(len(numbers_for_12))
# print(len(numbers_for_11))
# print(len(numbers_for_10))
# print(len(numbers_for_9))
# print(len(numbers_for_8))
# print(len(numbers_for_7))
#
#
# print(len(bowl_winner_1))
# print(len(bowl_winner_2))
# print(len(bowl_winner_3))
# print(len(numbers_for_12)+len(numbers_for_11)+len(numbers_for_10)+len(numbers_for_9)+len(numbers_for_8)+len(numbers_for_7)+len(bowl_winner_1)+len(bowl_winner_2)+len(bowl_winner_3))

# print(f"12th Place Numbers: ${numbers_for_12}")
# print(f"11th Place Numbers: ${numbers_for_11}")
# print(f"10th Place Numbers: ${numbers_for_10}")
# print(f"9th Place Numbers: ${numbers_for_9}")
# print(f"8th Place Numbers: ${numbers_for_8}")
# print(f"7th Place Numbers: {numbers_for_7}")
win12 = 0
win11 = 0
win10 = 0
win9 = 0
win8 = 0
win7 = 0
winb1 = 0
winb2 = 0
winb3 = 0

test = 1
for _ in range(0, test):
    lottery_winner = random.randint(0, 999999)
    print(_)
    # print(f"Winning lottery number: {lottery_winner}")
    if lottery_winner in numbers_for_12:
        win12 += 1
    if lottery_winner in numbers_for_11:
        win11 += 1
    if lottery_winner in numbers_for_10:
        win10 += 1

    if lottery_winner in numbers_for_9:
        win9 += 1
    if lottery_winner in numbers_for_8:
        win8 += 1
    if lottery_winner in numbers_for_7:
        win7 += 1
    if lottery_winner in bowl_winner_1:
        winb1 += 1
    if lottery_winner in bowl_winner_2:
        winb2 += 1
    if lottery_winner in bowl_winner_3:
        winb3 += 1


print(f"12 WINS { win12 / test}")
print(f"11 WINS { win11 / test}")
print(f"10 WINS  {  win10 / test}")
print(f"9 WINS  { win9 / test}")
print(f"8 WINS  { win8 / test}")
print(f"7 WINS  {  win7 / test}")
print(f"CONTENDER WINS  {  winb1 / test}")
print(f"BBQ WINS  { winb2 / test}")
print(f"TOILET WINS  { winb3 / test}")


# while game_is_on:
#     screen.update()
#     time.sleep(.1)
#     for seg in segments:
#         seg.forward(20)
#


# screen.exitonclick()