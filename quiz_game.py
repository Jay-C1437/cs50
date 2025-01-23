
import tkinter as tk
from tkinter import messagebox
import random

# List of questions and answers
quiz_data = [
    {"question": "What is the capital of France?", "answers": ["Berlin", "Madrid", "Paris", "Rome"], "correct": "Paris"},
    {"question": "What is 2 + 2?", "answers": ["3", "4", "5", "6"], "correct": "4"},
    {"question": "What is the capital of Italy?", "answers": ["Venice", "Milan", "Rome", "Naples"], "correct": "Rome"},
    # Add more questions as needed
]

# Initialize score and question index
score = 0
question_index = 0

# Function to load the next question
def load_next_question():
    global question_index
    if question_index < len(quiz_data):
        question_data = quiz_data[question_index]
        question_label.config(text=question_data["question"])
        answer_var.set(None)
        for i, answer in enumerate(question_data["answers"]):
            radio_buttons[i].config(text=answer, value=answer)
    else:
        messagebox.showinfo("Quiz Completed", f"Your score is {score}/{len(quiz_data)}")
        restart_quiz()

# Function to check the answer
def check_answer():
    global score, question_index
    selected_answer = answer_var.get()
    if selected_answer == quiz_data[question_index]["correct"]:
        score += 1
    question_index += 1
    load_next_question()

# Function to restart the quiz
def restart_quiz():
    global score, question_index
    score = 0
    question_index = 0
    load_next_question()

# Create the main window
root = tk.Tk()
root.title("Quiz Game")
root.configure(bg="lightblue")

# Create a label for the question
question_label = tk.Label(root, text="", font=("Arial", 14), bg="lightblue")
question_label.pack(pady=10)

# Variable to store the selected answer
answer_var = tk.StringVar()

# Create radio buttons for each answer
radio_buttons = []
for _ in range(4):
    radio_button = tk.Radiobutton(root, text="", variable=answer_var, value="", font=("Arial", 12), bg="lightblue")
    radio_button.pack(anchor='w')
    radio_buttons.append(radio_button)

# Create a button to submit the answer
submit_button = tk.Button(root, text="Submit", command=check_answer, font=("Arial", 12), bg="green", fg="white")
submit_button.pack(pady=10)

# Load the first question
load_next_question()

# Run the main event loop
root.mainloop()
