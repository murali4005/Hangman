# create a list of words
# randomly select a word and replace with same no of blanks
# Ask the user to guess
import random
import hangman_art as ha
import hangman_words as hw

lives = 6

chosen_word = random.choice(hw.word_list)
word_length = len(chosen_word)
display = []
for i in range(0,word_length):
  display += '_'

print('Welcome to Hangman!! \n')
print(ha.logo)
print(' ')
print(display)

end_of_game = False

while not end_of_game:
  
  guess = input('\nGuess a letter! ').lower()

  
  if guess in display:
    print(f'You are already guessed {guess}')
    
  for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
      display[position] = guess

  if guess not in chosen_word:
    lives -= 1
    print(f'You guessed {guess} which is not in the word, you lose a life')
    print(ha.stages[lives])
    if lives == 0:
      end_of_game = True
      print('You Lose! ')

  print(' ')
  print(display)

  if '_' not in display:
    end_of_game = True
    print('You win!')
  

print(chosen_word)  



      
      
    
  
  