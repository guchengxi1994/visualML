'''
@lanhuage: python
@Descripttion: 
@version: beta
@Author: xiaoshuyui
@Date: 2020-05-13 16:45:13
@LastEditors: xiaoshuyui
@LastEditTime: 2020-05-13 17:33:20
'''

from PyQt5.QtWidgets import QApplication,QDialog,QComboBox,QLineEdit
from optimizerInit import ops
# from .optimizerInit import ops
import sys

class Ops(QDialog):
    def __init__(self, parent=None, flags=None):
        super(Ops,self).__init__()
        self.setWindowTitle("Optimizers")

        self.setFixedSize(300,200)

        self.op = QComboBox(self)
        self.op.move(200,20)
        self.op.addItems(ops)
        self.op.currentIndexChanged.connect(self._changeEdit)

        self.opText = QLineEdit(self)
        self.opText.move(20,20)
        self.opText.setEnabled(False)
        self.opText.setText(self.op.currentText())

    def _changeEdit(self):
        self.opText.setText(self.op.currentText())
        


if __name__ == '__main__':
	app = QApplication(sys.argv)
	comboxDemo = Ops()
	comboxDemo.show()
	sys.exit(app.exec_())