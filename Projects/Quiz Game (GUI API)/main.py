from question_model import Question
from data import qdata
from quiz_brain import QuizBrain
from ui import UI

question_bank =[]
for _ in qdata:
    question_bank.append(Question(_['question'],_['correct_answer']))

q=QuizBrain(question_bank)

u=UI(q)

#q.next_questioner()

#int(2.59)=2 #casting

#x: int
#x=1

#def check(age: int)->bool: