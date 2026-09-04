import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

questions = pd.read_csv("questions.csv")

print("========================================")
print("          PYTHON QUIZ GAME")
print("========================================")

name = input("Enter your name: ")

print("\nWelcome,", name)
print("Let's start the quiz!\n")

score = 0
correct_answers = 0
wrong_answers = 0

for index, row in questions.iterrows():

    print("Question", index + 1)
    print(row["Question"])

    print("A.", row["Option A"])
    print("B.", row["Option B"])
    print("C.", row["Option C"])
    print("D.", row["Option D"])

    while True:
        answer = input("Your answer: ").upper()

        if answer in ["A", "B", "C", "D"]:
            break

        print("Invalid answer! Please enter A, B, C, or D.")

    if answer == row["Answer"]:
        print("Correct!\n")
        score += 1
        correct_answers += 1

    else:
        print("Wrong!")
        print("Correct answer:", row["Answer"])
        print()
        wrong_answers += 1

total_questions = len(questions)

percentage = (correct_answers / total_questions) * 100

answer_data = np.array([correct_answers, wrong_answers])

average_answers = np.mean(answer_data)
maximum_answers = np.max(answer_data)
minimum_answers = np.min(answer_data)

print("========================================")
print("             QUIZ RESULT")
print("========================================")

print("Student Name :", name)
print("Total Questions :", total_questions)
print("Correct Answers :", correct_answers)
print("Wrong Answers :", wrong_answers)
print("Score :", score, "/", total_questions)
print("Percentage :", round(percentage, 2), "%")

print("Average Answers :", round(average_answers, 2))
print("Maximum Answers :", maximum_answers)
print("Minimum Answers :", minimum_answers)

if percentage >= 80:
    performance = "Excellent"
elif percentage >= 60:
    performance = "Good"
elif percentage >= 40:
    performance = "Average"
else:
    performance = "Needs Improvement"

print("Performance :", performance)

print("========================================")

categories = ["Correct", "Wrong"]
values = [correct_answers, wrong_answers]

plt.bar(categories, values)

plt.title("Quiz Performance")
plt.xlabel("Answer Type")
plt.ylabel("Number of Answers")

plt.show()

result = pd.DataFrame({
    "Student Name": [name],
    "Total Questions": [total_questions],
    "Correct Answers": [correct_answers],
    "Wrong Answers": [wrong_answers],
    "Score": [score],
    "Percentage": [round(percentage, 2)],
    "Performance": [performance]
})

result.to_csv(
    "results.csv",
    mode="a",
    index=False,
    header=not os.path.exists("results.csv")
)

print("\nResult saved successfully to results.csv")