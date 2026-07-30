import json


def load_questions():
    with open("questions.json", "r", encoding="utf-8") as file:
        questions = json.load(file)

    return questions


def run_quiz():
    questions = load_questions()

    score = 0

    for question in questions:
        print()
        print(question["question"])

        print("A)", question["options"][0])
        print("B)", question["options"][1])
        print("C)", question["options"][2])
        print("D)", question["options"][3])

        answer = input("Your answer: ").upper()

        if answer == question["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            print("❌ Incorrect!")

    print()
    print("Quiz Finished!")
    print("Your Score:", score, "/", len(questions))

    if score >= 8:
        print("Excellent job! 🎉")
    elif score >= 5:
        print("Good effort! 👍")
    else:
        print("Keep practicing! 📚")