import random


questions = {1:"TELL ME ABOUT YOURSELF.", 2:"WHAT IS/ARE YOUR STRENGTH(S)?", 3:"WHAT ARE YOUR WEAKNESSES?", 4:"TELL ME ABOUT A TIME WHEN YOU WORKED WITH A COLLEAGUE WHO IS NOT DOING THEIR SHARE OF WORK. HOW DID YOU HANDLE IT?", 5:"TELL ME ABOUT A TIME YOU WORKED IN A TEAM.", 6:"TELL ME ABOUT A TIME YOU BUILT POSITIVE RELATIONSHIPS WITH PEOPLE", 7:"TELL ME ABOUT A TIME YOU LEARNT SOMETHING NEW", 8:"TELL ME ABOUT A TIME YOU MADE AN IMPORTANT/QUICK DECISION", 9:"TELL ME ABOUT A TIME YOU WISH YOU’D HANDLED A SITUATION DIFFERENTLY WITH A COLLEAGUE", 10:"TELL ME ABOUT YOUR PROUDEST ACHIEVEMENT", 11:"TELL ME ABOUT A TIME YOU NEEDED TO GET INFORMATION FROM SOMEONE WHO WASN’T RESPONSIVE", 12:"TELL ME ABOUT A TIME WHEN YOUR TEAM ENCOUNTERED A CHANGE OF DIRECTION IN THE PROJECT", 13:"TELL ME ABOUT A TIME YOU FAILED – HOW DID YOU DEAL WITH THE SITUATION?", 14:"TALK ABOUT A TIME WHEN YOU HAD TO WORK CLOSELY WITH SOMEONE WHOSE PERSONALITY IS VERY DIFFERENT FROM YOURS?", 15:"TELL ME ABOUT A TIME YOU WERE DISSATISFIED IN YOUR WORK? WHAT COULD’VE BEEN DONE TO MAKE IT BETTER?", 16:"DESCRIBE THE PROJECT/SITUATION THAT BEST DEMONSTRATES YOUR ANALYTICAL ABILITIES -- WHAT WAS YOUR ROLE?"}

condition = 1 #to run the loop
while condition != 0:
    # press 0 to stop the looping of the questions
    question_no = list(questions.keys())
    rand_num = random.randrange(1, question_no[-1])
    print("QUESTION: {}\n".format(questions[rand_num]))
    choice = int(input("Generate another question? Press 1 for 'Yes', Press 0 for 'No' (quit) \n"))

    if choice == 0:
        break



#print(list(questions.keys()))
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

