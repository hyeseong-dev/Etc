import sys
from PyQt5.QtWidgets import QApplication, QWidget # 각각의 클래스의 용도는? 
from PyQt5 import uic

class Exam(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.show()

app = QApplication(sys.argv) # ? 어떤 기능인가?
w = Exam()                  # Exam이라는 클래스를 호출해서 내가 설정한 
sys.exit(app.exec_())
