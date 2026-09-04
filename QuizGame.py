import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# Load quiz questions
questions = pd.read_csv("questions.csv")


# Function to start the quiz
def start_quiz():

    score = 0
    correct_answers = 0
    wrong_answers = 0

    # Get available topics
    topics = questions["Topic"].unique()

    print("\nAvailable Topics:")

    for i, topic in enumerate(topics, start=1):
        print(f"{i}. {topic}")

    # Topic selection
    while True:
        try:
            topic_choice = int(input("\nSelect a topic: "))

            if 1 <= topic_choice <= len(topics):
                selected_topic = topics[topic_choice - 1]
                break

            print("Invalid choice! Please select a valid topic.")

        except ValueError:
            print("Please enter a number.")

    # Filter questions according to selected topic
    selected_questions = questions[
        questions["Topic"] == selected_topic
    ].reset_index(drop=True)

    print("\n========================================")
    print("          PYTHON QUIZ GAME")
    print("========================================")

    name = input("Enter your name: ")

    print("\nWelcome,", name)
    print("Topic:", selected_topic)
    print("Let's start the quiz!\n")

    # Ask questions
    for index, row in selected_questions.iterrows():

        print("Question", index + 1)
        print(row["Question"])

        print("A.", row["Option A"])
        print("B.", row["Option B"])
        print("C.", row["Option C"])
        print("D.", row["Option D"])

        # Validate answer
        while True:
            answer = input("Your answer: ").upper()

            if answer in ["A", "B", "C", "D"]:
                break

            print("Invalid answer! Please enter A, B, C, or D.")

        # Check answer
        if answer == row["Answer"]:
            print("Correct!\n")
            score += 1
            correct_answers += 1

        else:
            print("Wrong!")
            print("Correct answer:", row["Answer"])
            print()
            wrong_answers += 1

    # Calculate results
    total_questions = len(selected_questions)

    percentage = (correct_answers / total_questions) * 100

    # NumPy analysis
    answer_data = np.array([correct_answers, wrong_answers])

    average_answers = np.mean(answer_data)
    maximum_answers = np.max(answer_data)
    minimum_answers = np.min(answer_data)

    # Performance classification
    if percentage >= 80:
        performance = "Excellent"
    elif percentage >= 60:
        performance = "Good"
    elif percentage >= 40:
        performance = "Average"
    else:
        performance = "Needs Improvement"

    # Display result
    print("========================================")
    print("             QUIZ RESULT")
    print("========================================")

    print("Student Name :", name)
    print("Topic :", selected_topic)
    print("Total Questions :", total_questions)
    print("Correct Answers :", correct_answers)
    print("Wrong Answers :", wrong_answers)
    print("Score :", score, "/", total_questions)
    print("Percentage :", round(percentage, 2), "%")
    print("Average Answers :", round(average_answers, 2))
    print("Maximum Answers :", maximum_answers)
    print("Minimum Answers :", minimum_answers)
    print("Performance :", performance)

    print("========================================")

    # Create performance graph
    categories = ["Correct", "Wrong"]
    values = [correct_answers, wrong_answers]

    plt.bar(categories, values)

    plt.title("Quiz Performance")
    plt.xlabel("Answer Type")
    plt.ylabel("Number of Answers")

    plt.show()

    # Save result using Pandas
    result = pd.DataFrame({
        "Student Name": [name],
        "Topic": [selected_topic],
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


# Main menu
while True:

    print("\n========================================")
    print("       QUIZ GAME & ANALYZER")
    print("========================================")
    print("1. Start Quiz")
    print("2. Exit")
    print("========================================")

    choice = input("Enter your choice: ")

    if choice == "1":
        start_quiz()

    elif choice == "2":
        print("\nThank you for using the Quiz Game!")
        break

    else:
        print("\nInvalid choice! Please enter 1 or 2.")