import random
while True:
    user_action=input('enter a choice(rock,paper,scissors):')
    possible_action=['rock','paper','scissors']
    computer_action=random.choice(possible_action)
    print('you chose {user_action},computer chose{computer_action}')
    if user_action==computer_action:
        print('both player selected{user_action}.its a tie!')
    elif user_action=='rock':
        if computer_action=='scissors':
            print('rock smashes scissor!you win')
        else:
            print('paper cover rock!you lose')
    elif user_action=='paper':
        if computer_action=='rock':
            print('paper cover rock!you win')
        else:
            print('scissor cuts paper!you lose')
    elif user_action=='scissor':
        if computer_action=='paper':
            print('scissor cuts paper!you win')
        else:
            print('rock smashes scissor!you lose')