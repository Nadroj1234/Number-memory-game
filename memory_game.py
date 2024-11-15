# Jordan Klemm

import json
import os
import time
import random


def load_high_scores():
    with open('high_scores.json', 'r') as file:
        high_scores = json.load(file)
        return high_scores


def display_high_scores(high_scores):
    num = 0
    for name in high_scores:
        num += 1
        print(f'{num}. {name['name']} - {name['score']}')


def game(high_scores, score, round_num, name):
    high_scores = load_high_scores()
    while True:
        print(f'Round: {round_num+1}')
        rand_num = "".join([str(random.randint(0, 9))
                           for _ in range(round_num + 3)])
        break
    print(f'Remember these numbers: {rand_num}')
    start_time = time.time()
    time.sleep(3)
    end_time = time.time()
    os.system('cls' if os.name == 'nt' else 'clear')
    resp_to_rand_num = input('Enter the number you just saw: ')
    print('')
    response_time = time.time() - start_time
    if resp_to_rand_num == rand_num:
        if response_time <= 4:
            score += 100
        elif response_time <= 6:
            score += 90
        elif response_time <= 8:
            score += 70
        elif response_time > 8:
            score += 40
        round_num += 1
        print(f'Good Job! - Current score: {score}')
        game(high_scores, score, round_num, name)
    else:
        print(f'Too bad!')
        print(f'You completed {
              round_num} rounds and a final score of {score}')
        updated_high_scores(high_scores, name, score)
        save_high_score(high_scores)
        play_again = input(
            'Do you want to play again? (y/n): ').lower().strip()
        if play_again == 'y':
            main()
        else:
            quit()
    return high_scores, score


def updated_high_scores(high_scores, name, score):
    high_scores.append({"name": name, "score": score})
    high_scores.sort(key=lambda x: x["score"], reverse=True)
    if len(high_scores) >= 5:
        high_scores.pop()
    return high_scores


def save_high_score(high_scores):
    with open("high_scores.json", "w") as file:
        json.dump(high_scores, file, indent=4)


def welcome_screen():
    print('Welcome to the Number Memory Game!')


def main():
    score = 0
    resp = input('Press enter to start or q to quit: ').lower()
    name = input('Enter your name: ')
    high_scores = load_high_scores()
    high_scores = updated_high_scores(high_scores, score, name)
    welcome_screen()
    display_high_scores(high_scores)
    print('')

    round_num = 0
    while True:
        if resp == '':
            game(high_scores, score, round_num, name)
        else:
            quit()


if __name__ == '__main__':
    main()
