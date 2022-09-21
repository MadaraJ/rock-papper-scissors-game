human_turn = 'paper'
computer_turn = 'scissors'

if human_turn == computer_turn:
    print('Human wins!')
elif human_turn == 'paper' and computer_turn == 'rock' :
    print('Human wins!')
elif human_turn == 'scissors' and computer_turn == 'paper' :   
    print('Human wins!')
elif human_turn == 'rock' and computer_turn == 'paper' :   
    print('Human wins!')
if human_turn == 'scissors' and computer_turn == 'scissors' :
    print('Computer wins!')
if human_turn == 'scissors' and computer_turn == 'rock' :   
    print('Computer wins!') 
if human_turn == 'rock' and computer_turn == 'scissors':
    print('draw!')
