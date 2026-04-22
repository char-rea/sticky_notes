#program generates a random joke from a list of jokes.

import random

jokes = [
    "What do you call a pony with a cough?A little horse!",
    "What did one hat say to the other? You wait here. Ill go on a head.",
    "What did the shark say when he ate the clownfish? This tastes a little funny.",
    "Whats orange and sounds like a carrot? A parrot.",
    "What did the pirate say when he turned 80?Aye matey."
]
random_joke = random.choice(jokes)
print(random_joke)