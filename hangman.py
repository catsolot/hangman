import random
from typing import TextIO, List
def main():
    word = pick_word()
    board = gen_board(word) 
    #print(word)
    print(list_to_string(board))
    while(check(word, board) == False):
        board = guess(word, board)
        print(list_to_string(board))
    print("You Win")

def pick_word() -> str:
    """Return a random word from the words file"""
    words = open('words.txt', 'r') 
    for i in range(1, random.randrange(1000)):
        word = words.readline()
    return word.strip()

def gen_board(word: str) -> List:
    """Creates a board list"""
    out = ""
    board: List[str] = []
    for i in range(len(word)):
        out += "_ "
    return list(out)

def list_to_string(word: List) -> str:
    """Converts a list into a string"""
    out = ""
    for i in range(len(word)):
        out += word[i]
    return out

def guess(word: str, board: str):
    new_board = list(board)
    guess = input("What is your guess: ")
    for i in range(len(word)):
        if word[i] == guess:
            new_board[2*i] = guess
    return new_board

def check(word: str, guess: List) -> bool:
    guess_word = ""
    for i in range(len(guess) // 2):
        guess_word += guess[2*i]
    if word == guess_word:
        return True
    return False

if __name__ == "__main__":
    main()
