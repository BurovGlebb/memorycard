#подключение библиотек
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication,
                            QWidget,
                            QPushButton,
                            QLabel,
                            QVBoxLayout,
                            QHBoxLayout,
                            QMessageBox,
                            QRadioButton,
                            QGroupBox,
                            QButtonGroup)
class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
question_list = []
question_list.append(Question('Государственный язык Португалии', 'Португальский', 'Английский', 'Испанский', 'Фанцузский'))
question_list.append(Question('Какого цвета нет на флаге России', 'Зелёный', 'Красный', 'Синий', 'Белый'))
question_list.append(Question('Национальная хижина якутов', 'Ураса', 'Юрта', 'Иглу', 'Хата'))
question_list.append(Question('Где находится Бразилия', 'Южная Америка', 'Северная Америка', 'Африка', 'Азия'))
question_list.append(Question('На флаге какой страны изображён кедр', 'Ливан', 'Ливия', 'Боливия', 'Болгария'))
question_list.append(Question('Какая страна самая большая в мире', 'Россия', 'США', 'Канада', 'Австралия'))
         
from random import shuffle, randint



def on_click():
    if 'Ответить' == btn_OK.text():
        check_answer()
    else:
        next_question()
        
def show_result():
    RadioGroupsBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')

def show_question():
    RadioGroupsBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    btn_answer1.setChecked(False)
    btn_answer2.setChecked(False)
    btn_answer3.setChecked(False)
    btn_answer4.setChecked(False)
    RadioGroup.setExclusive(True)
def next_question():
    main_win.total += 1
    cur_qution = randint(0, len(question_list) - 1)

    q = question_list[cur_qution]
    ask(q)
    
def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()
def show_correct(res):
    lb_Result.setText(res)
    show_result()
def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно')
        main_win.score += 1
        print('Статистика\n-Всего вопросов:', main_win.total, '\n-Правильных ответов:', main_win.score)
        print('Рейтинг:', main_win.score/main_win.total*100, '%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or  answers[3].isChecked():
            show_correct('Неправильно')
            print('Рейтинг:', main_win.score/main_win.total*100, '%')
            
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Memorycard')
main_win.cur_question = -1
main_win.resize(400, 200)

btn_OK = QPushButton('Ответить')

lb_Question = QLabel('В каком году была оснавана Моска?')
RadioGroupsBox = QGroupBox('Варианты ответов')
btn_answer1 = QRadioButton('1147')
btn_answer2 = QRadioButton('1242')
btn_answer3 = QRadioButton('1861')
btn_answer4 = QRadioButton('1943')

RadioGroup = QButtonGroup()
RadioGroup.addButton(btn_answer1)
RadioGroup.addButton(btn_answer2)
RadioGroup.addButton(btn_answer3)
RadioGroup.addButton(btn_answer4)

layoutH1 = QHBoxLayout()
layoutH2 = QVBoxLayout()
layoutH3 = QVBoxLayout()

layoutH2.addWidget(btn_answer1)
layoutH2.addWidget(btn_answer2)
layoutH3.addWidget(btn_answer3)
layoutH3.addWidget(btn_answer4)

layoutH1.addLayout(layoutH2)
layoutH1.addLayout(layoutH3)

RadioGroupsBox.setLayout(layoutH1)


AnsGroupBox = QGroupBox('Результат теста')
lb_Result = QLabel('прав ты или нет!')
lb_Correct = QLabel('ответ будет тут!')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)



layout_line1= QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupsBox)
layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide()

layout_line3 .addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2)
layout_line3.addStretch(1)

layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.addSpacing(5)

main_win.setLayout(layout_card)

main_win.total = 0
main_win.score = 0

answers = [btn_answer1,btn_answer2, btn_answer3, btn_answer4]
btn_OK.clicked.connect(on_click)

main_win.show()
app.exec_() 
