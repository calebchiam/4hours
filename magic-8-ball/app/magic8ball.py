"""
Command-line interface 'Encik-style' magic 8 ball
"""
import random

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

responses = {
    "yes": ["Do one time, do swee swee",
            "Do what you want, just don't get caught.",
            "Own time own target, carry on"],
    "no": ["Gennermen, wake up your idea.",
            "Mai lai lah",
            "Fuck you understand"],
    "maybe": ["Don't make your problem my problem",
              "By right, cannot. By left, can.",
              "Wear helmet then cannot think is it?"]
}

if __name__ == "__main__":
    while True:
        print("What do you want to ask the Encik 8-ball?")
        qn = input()
        if "?" not in qn: continue
        response_type = random.choice(list(responses.keys()))
        response = random.choice(responses[response_type])
        print(bcolors.WARNING + response + bcolors.ENDC)
        print()
