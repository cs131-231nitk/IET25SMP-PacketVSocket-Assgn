import os
import time

#Questions Data
quiz_data = {
    1 : {
        "question": "What is IP address?",
        "options": ["Internal Program", "Internet Protocol", "Interface Processor"],
        "answer" : 2,
        "correct_message": "Well done! That's the right answer.",
        "fail_message": "Oops! That’s not quite right."
    },
    2 : {
        "question": "Which device is used to connect multiple networks together?",
        "options": ["Switch", "Hub", "Router"],
        "answer": 3,
        "correct_message": " Great job — you got it right!",
        "fail_message": "Wrong answer. Better luck on the next one"
    },
    3: {
        "question" : "Which protocol is used to send E-Mail?",
        "options": ["FTP", "SMPT", "HTTP"],
        "answer": 2,
        "correct_message": "Yep, that's correct!",
        "fail_message": "That’s a miss. You’ll get the next one!"
    },
    4 : {
        "question" : "Which protocol is used to browse the web securely?",
        "options": ["HTTPS", "HTTP", "SSH"],
        "answer": 1,
        "correct_message": "Correct! You're on fire! 🔥",
        "fail_message": "That’s the wrong choice."
    },
    5 : {
        "question" : "Which of the following is the private IP address?",
        "options" : ["8.8.8.8", "192.168.1.1", "172.32.0.1"],
        "answer": 2,
        "correct_message": "That’s the spirit — correct!",
        "fail_message": "That was incorrect. Don’t give up!"
    },
    6 : {
        "question" : "What is the primary function of DNS in networking?",
        "options": ["Encrypt", "Assign IP addresses", "Translate domain names to IP addresses"],
        "answer": 3,
        "correct_message": "Nailed it!",
        "fail_message": "That was wrong."
    }
}
logo = """
░█▀▀░█▀█░█▄█░█▀█░█░█░▀█▀░█▀▀░█▀▄░░░█▀█░█▀▀░▀█▀░█░█░█▀█░█▀▄░█░█░▀█▀░█▀█░█▀▀░░░▄▀▄░█░█░▀█▀░▀▀█
░█░░░█░█░█░█░█▀▀░█░█░░█░░█▀▀░█▀▄░░░█░█░█▀▀░░█░░█▄█░█░█░█▀▄░█▀▄░░█░░█░█░█░█░░░█\█░█░█░░█░░▄▀░
░▀▀▀░▀▀▀░▀░▀░▀░░░▀▀▀░░▀░░▀▀▀░▀░▀░░░▀░▀░▀▀▀░░▀░░▀░▀░▀▀▀░▀░▀░▀░▀░▀▀▀░▀░▀░▀▀▀░░░░▀\░▀▀▀░▀▀▀░▀▀▀                                                                                                                                                           
"""


no_of_questions = len(quiz_data)
score = 0
for i in range(1, no_of_questions + 1):
    print(logo)
    print()
    print(quiz_data[i]["question"])
    print("Options: ")
    print("1.", quiz_data[i]["options"][0])
    print("2.", quiz_data[i]["options"][1])
    print("3.", quiz_data[i]["options"][2])
    print()
    guessed = int(input("Enter your choice (1/2/3): "))
    if guessed not in [1, 2, 3]:
        raise ValueError("Invalid answer!")
    if type(guessed) != int:
        raise ValueError("That's an invalid input!")
    if guessed == quiz_data[i]["answer"]:
        score += 1
        print(quiz_data[i]["correct_message"])
    else:
        print(quiz_data[i]["fail_message"])
    
    if(i == no_of_questions):
        print("Your total score is ", score)
    else:
        print("Your current score is ", score)
        time.sleep(2)
        os.system("cls")
print()
print("Thank you for attempting the quiz. Hope you enjoyed.")
    
        
