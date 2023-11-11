import random

class DadJoke:
    def __init__(self, prompt, answer) -> None:
        self.prompt = prompt
        self.answer = answer
    
    def __repr__(self):
        return self.prompt + " " + self.answer

with open('DadJokes.txt', 'r') as file:
    jokes = file.read().splitlines()
    jokes = list(zip(jokes[::2], jokes[1::2]))

    joke = random.choice(jokes)
    joke = DadJoke(joke[0], joke[1])

    print(joke)