import tkinter as tk
from tkinter import messagebox
import random


questions = [
    {'question': 'What is the engine of a M5 E60?', 'choices': ['V10', 'V8', 'i6', 'V6'], 'answer': 'V10', 'hint_50_50': ['V10', 'V8']},
    {'question': 'What is the capital of Azerbaijan?', 'choices': ['Paris', 'Baku', 'Azerbaijan City', 'Cape Town'], 'answer': 'Baku', 'hint_50_50': ['Baku', 'Cape Town']},
    {'question': 'What is the capital of Italy?', 'choices': ['Rome', 'Milan', 'San Marino', 'Zagreb'], 'answer': 'Rome', 'hint_50_50': ['Rome', 'Milan']},
    {'question': 'What is the most expensive cryptocurrency right now?', 'choices': ['Ethereum', 'Litecoin', 'Bitcoin', 'Polkadot'], 'answer': 'Bitcoin', 'hint_50_50': ['Bitcoin', 'Litecoin']},
    {'question': 'What is the definition of GPU?', 'choices': ['Grand Prix United', 'Graphical Prix Unite', 'No Answer', 'Graphics Processing Unit'], 'answer': 'Graphics Processing Unit', 'hint_50_50': ['Graphics Processing Unit', 'Grand Prix United']},
    {'question': 'What is the currency of Azerbaijan?', 'choices': ['Iranian Dollars', 'Euro', 'Manat', 'Yen'], 'answer': 'Manat', 'hint_50_50': ['Manat', 'Yen']},
    {'question': 'Who is the richest person on Earth right now?', 'choices': ['Elon Musk', 'Bill Gates', 'Mark Zuckerberg', 'Mark Cuban'], 'answer': 'Elon Musk', 'hint_50_50': ['Elon Musk', 'Bill Gates']},
    {'question': 'What is the largest desert in the world?', 'choices': ['Sahara', 'Gobi', 'Kalahari', 'Antarctic Desert'], 'answer': 'Antarctic Desert', 'hint_50_50': ['Antarcticas Desert', 'Sahara']},
    {'question': 'Which planet is known for its rings?', 'choices': ['Mars', 'Jupiter', 'Saturn', 'Uranus'], 'answer': 'Saturn', 'hint_50_50': ['Saturn', 'Uranus']},
    {'question': 'What is 10 * 10?', 'choices': ['90', '100', '110', '120'], 'answer': '100', 'hint_50_50': ['100', '110']},
    {'question': 'What is the tallest mountain in the world?', 'choices': ['Mount Kilimanjaro', 'Mount Everest', 'K2', 'Mount McKinley'], 'answer': 'Mount Everest', 'hint_50_50': ['Mount Everest', 'K2']},
    {'question': 'What does WWW stand for in web addresses?', 'choices': ['World Wide Web', 'Web World Wide', 'Wide Web World', 'Web Wide World'], 'answer': 'World Wide Web', 'hint_50_50': ['World Wide Web', 'Web World Wide']},
    {'question': 'Whats the newest Iphone model', 'choices': ['Iphone 15', 'Iphone 19', 'Z Flip', 'Iphone 8E'], 'answer': 'Iphone 15', 'hint_50_50': ['Iphone 15', 'Z Flip']}

]


prizes = [100, 200, 400, 800, 1600, 3200, 6400, 12500, 25000, 50000, 100000, 200000, 400000, 800000, 1000000]

class MillionaireGame:
    def __init__(self, window):
        self.window = window
        self.window.title("Who Wants to Be a Millionaire? - Made by Ziya Mehtiyev")
        self.window.geometry("1200x600")
        self.window.configure(bg="#1e1e1e")
        
        self.current_money = 0
        self.current_question_index = 0
        self.hints_used = {'50/50': False, 'Call a Friend': False}
        self.time_left = 90
        
        self.setup_ui()
        self.load_new_question()


    def setup_ui(self):
        self.main_frame = tk.Frame(self.window, bg="#1e1e1e")
        self.main_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.prize_frame = tk.Frame(self.window, bg="#1e1e1e", width=200)
        self.prize_frame.pack(side=tk.RIGHT, fill=tk.Y)

        self.title_label = tk.Label(self.main_frame, text="Who Wants to Be a Millionaire?", bg="#1e1e1e", fg="#ffffff", font=("Arial", 24, "bold"))
        self.title_label.pack(pady=20)

        self.question_label = tk.Label(self.main_frame, text="", wraplength=600, bg="#2c2c2c", fg="#ffffff", font=("Arial", 18, "bold"))
        self.question_label.pack(pady=20, padx=20)
        
        self.choices_frame = tk.Frame(self.main_frame, bg="#1e1e1e")
        self.choices_frame.pack(pady=10, padx=20)
        
        self.choice_buttons = []
        for i in range(4):
            btn = tk.Button(self.choices_frame, text="", width=70, height=2, command=lambda i=i: self.check_answer(i), bg="#3c3c3c", fg="#ffffff", font=("Arial", 14), relief=tk.RAISED, bd=2)
            btn.pack(pady=5, padx=10, fill=tk.X)
            self.choice_buttons.append(btn)
        
        self.hint_frame = tk.Frame(self.main_frame, bg="#1e1e1e")
        self.hint_frame.pack(pady=10, padx=20)

        self.hint_50_50_button = tk.Button(self.hint_frame, text="Use 50/50 Hint", command=self.use_hint_50_50, bg="#4caf50", fg="white", font=("Arial", 12), relief=tk.RAISED, bd=2)
        self.hint_50_50_button.grid(row=0, column=0, padx=10)
        
        self.call_friend_button = tk.Button(self.hint_frame, text="Call a Friend", command=self.call_a_friend, bg="#f44336", fg="white", font=("Arial", 12), relief=tk.RAISED, bd=2)
        self.call_friend_button.grid(row=0, column=1, padx=10)
        
        
        self.money_label = tk.Label(self.main_frame, text="Current Prize: $100", bg="#1e1e1e", fg="#ffffff", font=("Arial", 16, "bold"))
        self.money_label.pack(pady=20)
        
        self.timer_label = tk.Label(self.main_frame, text="Time Left: 01:30", bg="#1e1e1e", fg="#ffffff", font=("Arial", 16, "bold"))
        self.timer_label.pack(pady=10)
        
        self.questions_remaining_label = tk.Label(self.main_frame, text="", bg="#1e1e1e", fg="#ffffff", font=("Arial", 16, "bold"))
        self.questions_remaining_label.pack(pady=10)
        
        self.prize_labels = []
        for i in range(len(prizes)):
            label = tk.Label(self.prize_frame, text=f"{i + 1}. ${prizes[i]}", bg="#2c2c2c", fg="#ffffff", font=("Arial", 14))
            label.pack(pady=2, padx=10, anchor=tk.W)
            self.prize_labels.append(label)
        
        self.cash_out_button = tk.Button(
        self.main_frame, 
        text="Cash Out", 
        command=self.cash_out, 
        bg="#ff9800", 
        fg="white", 
        font=("Arial", 12, "bold")
)
        self.cash_out_button.pack(pady=20, padx=20, side=tk.TOP)  

    def load_new_question(self):
        if self.current_question_index >= len(questions):
            messagebox.showinfo("Congratulations!", "You have completed all the questions and won 1MIL! Nice one :)!")
            self.window.quit()
            return
        
        current_question = questions[self.current_question_index]
        self.current_choices = current_question['choices']
        random.shuffle(self.current_choices)
        
        self.question_label.config(text=current_question['question'])
        
        for i in range(4):
            self.choice_buttons[i].config(text=self.current_choices[i], state=tk.NORMAL, bg="#3c3c3c", fg="#ffffff")
        
        questions_remaining = len(questions) - self.current_question_index
        self.questions_remaining_label.config(text=f"Questions Remaining: {questions_remaining}")
        
        for i in range(len(self.prize_labels)):
            if i == self.current_question_index:
                self.prize_labels[i].config(bg="#4caf50")
            else:
                self.prize_labels[i].config(bg="#2c2c2c")
        
        self.time_left = 90  
        self.update_timer()  
    
    def update_timer(self):
        minutes = self.time_left // 60  
        seconds = self.time_left % 60   
        self.timer_label.config(text=f"Time Left: {minutes:02}:{seconds:02}")  
        
        if self.time_left <= 0:
            self.end_game()  
        else:
            self.time_left -= 1  
            self.timer_id = self.window.after(1000, self.update_timer) 

    def check_answer(self, index):
        correct_answer = questions[self.current_question_index]['answer']
        correct_index = questions[self.current_question_index]['choices'].index(correct_answer)
        
        if self.current_choices[index] == correct_answer:
            self.current_money = prizes[self.current_question_index]
            self.money_label.config(text=f"Current Prize: ${self.current_money}")
            self.current_question_index += 1
            self.window.after_cancel(self.timer_id) 
            self.load_new_question()  
        else:
            self.choice_buttons[correct_index].config(bg="#4caf50")
            self.choice_buttons[index].config(bg="#f44336") 
            self.end_game() 
    
    def use_hint_50_50(self):
        if self.hints_used['50/50']:
            messagebox.showinfo("Hint Used", "You have already used the 50/50 hint.")
            return
        
        hint_choices = questions[self.current_question_index]['hint_50_50']
        
        for i in range(4):
            if self.current_choices[i] not in hint_choices:
                self.choice_buttons[i].config(state=tk.DISABLED)
        
        self.hints_used['50/50'] = True
        self.hint_50_50_button.config(state=tk.DISABLED)
    
    def call_a_friend(self):
        if self.hints_used['Call a Friend']:
            messagebox.showinfo("Hint Used", "You have already used the 'Call a Friend' hint.")
            return
        
        correct_answer = questions[self.current_question_index]['answer']
        messagebox.showinfo("Call a Friend", f"Your friend thinks the answer might be: {correct_answer}")
        self.hints_used['Call a Friend'] = True
        self.call_friend_button.config(state=tk.DISABLED)
    
    def cash_out(self):
        messagebox.showinfo("Cash Out", f"You've cashed out with ${self.current_money}!")
        self.window.quit()
    
    def end_game(self):
        messagebox.showinfo("Game Over", f"Game over! You won ${self.current_money}. you made me go broke...")
        self.window.quit()

window = tk.Tk()
MillionaireGame(window)
window.mainloop()