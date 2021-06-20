#Knowledge Trivia

questions = ["What is one exception?",
             "What is the second exception?"]
answers = ["Try and Except",
           "Try Except and Else"]
correct = []
wrong = []
total = 0
wrong_score = 0

for question in questions:
    print(question)

    user_answer = input("Answer: ")
    print()

    if user_answer in answers:
        correct.append(question)
        total +=1
    else:
        wrong.append(question)
        wrong_score += 1

for each in correct:
    print()
    print("You answer was correct for question: ", each)


for fail in wrong:
    print()
    print("You answer was incorrect for question: ", fail)

print()
print("Your total score is: ", total, "correct and", wrong_score, "wrong.")

input("\n\nPress enter key to exit.")    
