'''
@lanhuage: python
@Descripttion: 
@version: beta
@Author: xiaoshuyui
@Date: 2020-05-11 08:49:06
@LastEditors: xiaoshuyui
@LastEditTime: 2020-05-11 17:15:27
'''
from PyQt5.QtWidgets import QApplication,QWidget, \
    QTextEdit,QVBoxLayout,QPushButton,QMainWindow

from PyQt5.QtGui import QTextCursor

import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setWindowTitle('Visual Machine Learning')
        self.resize(640,480)
        self.codeReview = QTextEdit(self)
        self.codeReview.setPlaceholderText("# this shows the code")

        self.codeReview.move(400,100)
        self.codeReview.setFixedWidth(200)
        self.codeReview.setFixedHeight(300)
        self.codeReview.setLineWrapMode(QTextEdit.NoWrap)

        self.testCode = QPushButton(self)
        self.testCode.setText("GO !")
        self.testCode.move(450,415)
        self.testCode.setToolTip("Test Code")
        self.testCode.clicked.connect(self._testCode)

        self.addLayer = QPushButton(self)
        self.addLayer.setText("Layer")
        self.addLayer.move(100,100)

        

        self.reverse = QPushButton(self)
        self.reverse.setText("Undo")
        self.reverse.move(100,415)
        self.reverse.setToolTip("Delete Last Row")
        self.reverse.clicked.connect(self._undo)


    def _undo(self):
        cursor = self.codeReview.textCursor()
        cursor.movePosition(QTextCursor.PreviousRow)
        cursor.select(QTextCursor.LineUnderCursor)
        cursor.deleteChar()#删除光标右边的文本 相当于delete
        cursor.deletePreviousChar()#删除光标左边的文本，相当于Backspace  
        self.codeReview.setFocus()
        # self.codeReview.setTextCurosr(cursor)

    
    def _testCode(self):
        if len(self.codeReview.toPlainText()) == 0:
            self.codeReview.insertPlainText("from keras.models import Sequential" +"\n")

        





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
