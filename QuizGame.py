import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

questions = pd.read_csv("questions.csv")

print("========================================")
print("          PYTHON QUIZ GAME")
print("========================================")

name = input("Enter your name: ")

print("\nWelcome,", name)
print("Let's start the quiz!\n")