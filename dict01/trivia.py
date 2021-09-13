#! /usr/bin/env python3

import json
import random

def main():
    with open('trivia.json', 'r') as file:
        trivia_dict = json.load(file)
        answer_options = []
        if len(trivia_dict) != 0:
              print(trivia_dict[0]['question'])
              answer_options.append(trivia_dict[0]['correct_answer'])
              for y in trivia_dict[0]['incorrect_answers']:
               answer_options.append(y)
              random.shuffle(answer_options)
              print('Here are your options: ')
              for z in answer_options:
                print(z)
              users_answer = input('What is your answer? ')
              print(f'You said {users_answer.capitalize()}')
              #print(f"the correct answer is {trivia_dict[0]['correct_answer']}")
              if users_answer.capitalize() == trivia_dict[0]['correct_answer']:
                  print(f"You are correct: {trivia_dict[0]['correct_answer']}") 
              else:
                  print(f"That is incorrect, the answer is: {trivia_dict[0]['correct_answer']}")
              #    print('These answers are also incorrect:')
              #    for x in trivia_dict[0]['incorrect_answers']:
              #        print(x)



main()
