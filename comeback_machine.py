import random

funny_comebacks_with_names = [
    "If laughter is the best medicine, {name}'s face must be curing the world.",
    "I'm not saying I hate {name}, but I would unplug {name}'s life support to charge my phone.",
    "Is {name} always this stupid or is today a special occasion?",
    "{name} must have a PhD in stupidity.",
    "If I wanted to kill myself, I would climb {}'s ego and jump to {name}'s IQ.",
    "I'm not insulting {name}; I'm describing {}.",
    "I'd agree with you, {name}, but then we'd both be wrong.",
    "Mirrors can't talk, {name}. Lucky for {name}, they can't laugh either.",
    "I'd insult {name}, but the sad truth is {name} wouldn't understand it.",
    "It's impossible to underestimate {name}.",
    "Is your name Wi-fi, {name}? Because I'm feeling a connection.",
    "I'm not a photographer, {name}, but I can picture us together... just kidding!",
    "If beauty were time, {name} would be an eternity late.",
    "{name} is so ugly that when {name} popped out, the doctor said, 'Aww, what a treasure!' and {name}'s mom said, 'Yeah, let's bury it.'",
    "{name} is not stupid; {name} just has bad luck thinking.",
    "I'd agree with you, {name}, but then we'd both be wrong.",
    "I'm not lazy, {name}; I'm in energy-saving mode.",
    "Do you have a name, {name}, or can I call you mine?",
    "If {name} were any less intelligent, we'd have to water {name} twice a week.",
]

name = input('What is the name of the person who wronged you? ')
print(random.choice(funny_comebacks_with_names).format(name=name))