'''
@lanhuage: python
@Descripttion: 
@version: beta
@Author: xiaoshuyui
@Date: 2020-05-13 16:45:13
@LastEditors: xiaoshuyui
@LastEditTime: 2020-05-14 09:52:20
'''

from PyQt5.QtWidgets import QApplication,QDialog,QComboBox,QLineEdit, \
    QPushButton
# from optimizerInit import ops,loss
from .optimizerInit import ops,loss
import sys

def getlrAndDk(lr,dk):
    if len(lr) == 0:
        lr = 0.001
    else:
        try:
            tmp = float(lr)
            lr = tmp
        except ValueError:
            lr = 0.001
    if len(dk) == 0:
        dk = 1e-6
    else:
        try:
            tmp = float(dk)
            dk = tmp
        except ValueError:
            dk = 1e-6
    
    return lr,dk

class Ops(QDialog):
    def __init__(self, parent=None, flags=None):
        super(Ops,self).__init__()
        self.setWindowTitle("Optimizers")

        self.setFixedSize(400,250)

        self.op = QComboBox(self)
        self.op.move(200,20)
        self.op.addItems(ops)
        self.op.currentIndexChanged.connect(self._changeEdit)

        self.opText = QLineEdit(self)
        self.opText.move(20,20)
        self.opText.setEnabled(False)
        self.opText.setText(self.op.currentText())


        self.loss = QComboBox(self)
        self.loss.move(200,180)
        self.loss.addItems(loss)
        self.loss.currentIndexChanged.connect(self._changeEdit)

        self.lossText = QLineEdit(self)
        self.lossText.move(20,180)
        self.lossText.setEnabled(False)
        self.lossText.setText(self.loss.currentText())

        self.submit = QPushButton(self)
        self.submit.setText("Submit")
        self.submit.move(150,220)
        self.submit.clicked.connect(self._submit)


        self.lr = QLineEdit(self)
        self.lr.move(20,60)
        self.lr.setPlaceholderText("Learning Rate")

        self.dk = QLineEdit(self)
        self.dk.move(20,100)
        self.dk.setPlaceholderText("Decay")

        self.learningRate = 0.0
        self.decayRate = 0.0


    

    def _submit(self):
        self.learningRate,self.decayRate = getlrAndDk(self.lr.text(),self.dk.text())
        self.close()

        


    def _changeEdit(self):
        self.opText.setText(self.op.currentText())
        self.lossText.setText(self.loss.currentText())
        
        


if __name__ == '__main__':
	app = QApplication(sys.argv)
	comboxDemo = Ops()
	comboxDemo.show()
	sys.exit(app.exec_())