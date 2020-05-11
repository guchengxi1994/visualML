'''
@lanhuage: python
@Descripttion: 
@version: beta
@Author: xiaoshuyui
@Date: 2020-05-11 16:20:32
@LastEditors: xiaoshuyui
@LastEditTime: 2020-05-11 17:26:29
'''

from PyQt5.QtWidgets import QApplication,QWidget, \
    QPushButton,QTextEdit,QLabel,QDialog,QComboBox
import sys
# from . import layerInit as li
import layerInit as li

class LayerDialog(QDialog):
    def __init__(self, parent=None, flags=None):
        super(LayerDialog,self).__init__()

        self.cb = QComboBox(self)
        self.cb.addItems(list(li.layers.keys()))

        # self.cb.currentIndexChanged



if __name__ == '__main__':
	app = QApplication(sys.argv)
	comboxDemo = LayerDialog()
	comboxDemo.show()
	sys.exit(app.exec_())