from PyQt5.QtWidgets import QApplication
from random import choice, shuffle
from time import sleep
app = QApplication([])

from m2 import *
from m3 import *
class Question:
    def __init__(self, question, answer, wrong_answer1, wrong_answer2, wrong_answer3):
        self.question = question
        self.answer = answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3
q1 = Question('У якому році Аскольд став правителем?', '860', '858', '861', '859')
q2 = Question('У якому році плутон перестав бути планетою?', '2006', '2005', '2007', '2004')
q3 = Question('У якому році пала західна римська імперія?', '476', '474', '475', '473')
q4 = Question('У якому році Україна стала незалежною?', '1991', '1989', '1990', '1988')
q5 = Question('Скільки років сьогодні було б Тарасу Шевченку?', '209', '207', '210', '206')
q6 = Question('Коли відбувалось велике переселення народів?', '4-7ст', '4-6ст', '5-7ст','3-6ст')
q7 = Question('Коли хрестили київську Русь?', '988', '989', '987', '990')
q8 = Question('Коли помер Володимер Великий?', '1015', '1013', '1014', '1012')
q9 = Question('Коли  князь Святослав став правителем?', '945', '943', '944', '942')
q10 = Question('Коли князь Ігор став правителем?', '912', '910', '911','909')

radio_buttons = [rb_ans1, rb_ans2, rb_ans3, rb_ans4]
questions = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]
def new_question():
    global cur_q
    cur_q = choice(questions)
    lb_question.setText(cur_q.question)
    lb_right_answer.setText(cur_q.answer)
    shuffle(radio_buttons)
    radio_buttons[0].setText(cur_q.wrong_answer1)
    radio_buttons[1].setText(cur_q.wrong_answer2)
    radio_buttons[2].setText(cur_q.wrong_answer3)
    radio_buttons[3].setText(cur_q.answer)
new_question()
def check():
    RadioGroup.setExclusive(False)
    for answer in radio_buttons:
        if answer.isChecked():
            if answer.text() == lb_right_answer.text():
                lb_result.setText('Правильно!')
                answer.setChecked(False)
                break
        else:
            lb_result.setText('Неправильно!')
    RadioGroup.setExclusive(True)
def click_ok():
    if btn_next.text() == "Відповісти":
        check()
        gb_question.hide()
        gb_answer.show()
        btn_next.setText('Наступне запитання')
    else:
        new_question()
        gb_question.show()
        gb_answer.hide()
        btn_next.setText('Відповісти')
btn_next.clicked.connect(click_ok)
def rest():
    window.hide()
    n = sp_rest.value() * 60
    sleep(n)
    window.show()
btn_rest.clicked.connect(rest)
def clear():
    le_question.clear()
    le_right_ans.clear()
    le_wrong_ans1.clear()
    le_wrong_ans2.clear()
    le_wrong_ans3.clear()
btn_clear.clicked.connect(clear)
def add_question():
    new_q = Question(le_question.text(), le_right_ans.text(), le_wrong_ans1.text(), le_wrong_ans2.text(), le_wrong_ans3.text())
    questions.append(new_q)
    clear()
btn_add_question.clicked.connect(add_question)

def menu_generation():
    menu_win.show()
    window.hide()
btn_menu.clicked.connect(menu_generation)
def back_menu():
    menu_win.hide()
    window.show()
btn_back.clicked.connect(back_menu)

window.show()
app.exec_()
