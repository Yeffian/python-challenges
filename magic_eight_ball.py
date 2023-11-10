import random

def eight_ball():
    answers = [
        "It is certain",
        "It is decidedly so",
        "Without a doubt",
        "As I see it, yes",
        "Reply hazy, try again",
        "Ask again later",
        "Cannot predict now",
        "Don’t count on it",
        "My reply is no",
        "My sources say no",
        "Outlook not so good",
        "Very doubtful"
    ]

    return random.choice(answers)