# PyQtWindowPushButton.py 

import sys 
from PyQt5.QtWidgets import * 

class PushButtonWindow(QMainWindow): # 푸쉬버튼을 만들기위한 빵틀
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setWindowTitle('PushButtonWindow')

        btn = QPushButton('Click me', self) #1st arg는 글자삽입, 두번쨰는 인스턴스 self 넣기
        btn.move(20,20) # (0,0)은 창 왼쪽 상단임. x축 20, y축 아래로 20 
        btn.clicked.connect(self.btn_clicked) 
        # 바로 위 이벤트를 활성화 시켜주는 메서드가 바로 clicked()임. 
        # 그 이벤트를 함수로 연동시켜주는 메서드는 connect()임 
        #  

    def btn_clicked(self):
        QMessageBox.about(self, '메시지','clicked') # QtWidgets에 있는 클래스중에서 QMessageBox를 불러옴

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PushButtonWindow() # 바로위의 클래스를 통해서 window라는 인스턴스 생성 
    window.show()    # 바로위 window인스턴스를 통해서 show()통해 시각적으로 보여줌.
    app.exec_()