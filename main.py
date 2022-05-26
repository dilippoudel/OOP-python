current_score = 20
cards = [3, 6, 1, 8]
for x in range(len(cards)):
    if len(cards) > 1:
        current_card = cards[0]
        cards.remove(current_card)
        user_answer = input("Is the coming card greater than current one? ans: Yes/y or No/n: ")

        user_output = ''
        real_output = ''
        if user_answer.lower() == 'y' or 'yes':
            user_output += 'Higher'
        else:
            user_output += 'Lower'
        if current_card > cards[0]:
            real_output += 'Higher'
        else:
            real_output += 'Lower'

        if user_output == real_output:
            current_score += 20
            print('Congratulation, You won 20 points')
        else:
            current_score -= 15
            print('Sorry, You loose 15 points.')

        print(f'Your current score is {current_score}')
    else:
        print(f'Your Final score is {current_score}')

