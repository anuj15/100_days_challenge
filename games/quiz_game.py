from data import question_data

questions = {}
counter = 0
score = 0

for i in question_data:
    questions[i['question']] = i['correct_answer']

for i in questions.keys():
    counter += 1
    user_answer = input(f"Q.{counter} {i} ").lower()
    if user_answer == questions[i].lower():
        score += 1
        print(f"Right answer!\n")
    else:
        print(f"Wrong answer! The correct answer is '{questions[i]}'\n")

print(f"Your final score is {score}")

if __name__ == '__main__':
    print("Start")
