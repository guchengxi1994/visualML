'''
@lanhuage: python
@Descripttion: 
@version: beta
@Author: xiaoshuyui
@Date: 2020-05-11 16:20:32
@LastEditors: xiaoshuyui
@LastEditTime: 2020-05-12 09:50:35
'''

from PyQt5.QtWidgets import QApplication,QWidget, \
    QPushButton,QTextEdit,QLabel,QDialog,QComboBox ,\
    QLineEdit
import sys
# from . import layerInit as li
import layerInit as li



class ALLLayer(QDialog):
    def __init__(self, parent=None, flags=None):
        super(ALLLayer,self).__init__()
        self.core = QComboBox(self)
        self.conv = QComboBox(self)
        self.pool = QComboBox(self)
        self.activation = QComboBox(self)

        self.submitButton = QPushButton(self)
        self.submitButton.setText("Submit")
        self.setFixedSize(300,500)

        self.Lcore = QLabel(self)
        self.Lcore.setText("Core")
        self.Lcore.move(50,50)

        self.Lconv = QLabel(self)
        self.Lconv.setText("Conv")
        self.Lconv.move(50,150)

        self.Lpool = QLabel(self)
        self.Lpool.setText("Pooling")
        self.Lpool.move(50,250)

        self.Lactivation = QLabel(self)
        self.Lactivation.setText("Activation")
        self.Lactivation.move(50,350)

        self.core.move(100,50)
        self.core.addItems(li.all_layers_core)
        self.conv.move(100,150)
        self.conv.addItems(li.all_layers_conv)
        self.pool.move(100,250)
        self.pool.addItems(li.all_layers_pool)
        self.activation.move(130,350)
        self.activation.addItems(li.all_activations)
        self.submitButton.move(110,450)

        self.core.currentIndexChanged.connect(self._changeLayer_core)
        self.conv.currentIndexChanged.connect(self._changeLayer_conv)
        self.pool.currentIndexChanged.connect(self._changeLayer_pool)
        self.activation.currentIndexChanged.connect(self._changeLayer_activation)

        
        self.layer = QLineEdit(self)
        self.layer.setEnabled(False)
        self.layer.move(80,400)
        self.layer.setText(self.core.currentText())

        self.submitButton.clicked.connect(self._submit)

        self.info = self.layer.text()



    def _changeLayer_core(self):
        self.layer.setText(self.core.currentText())

    def _changeLayer_conv(self):
        self.layer.setText(self.conv.currentText())

    def _changeLayer_pool(self):
        self.layer.setText(self.pool.currentText())

    def _changeLayer_activation(self):
        self.layer.setText(self.activation.currentText())

    def _submit(self):
        self.info = self.layer.text()
        self.close()

    # @staticmethod
    # def getData(options,parent=None):
    #     dialog = ALLLayer(parent)
    #     result = dialog.exec_()
    #     return dialog.info



class LayerDialog(QDialog):
    def __init__(self, parent=None, flags=None):
        super(LayerDialog,self).__init__()
        self.setFixedSize(400,200)
        
        self.layer = QLineEdit(self)
        self.layer.setEnabled(False)
        self.layer.move(50,20)

        self.cb = QComboBox(self)
        self.cb.addItems(list(li.layers.keys()))
        self.cb.move(200,20)
        
        self.layer.setText(self.cb.currentText())
        self.cb.currentIndexChanged.connect(self._changeLayer)

        self.cbPlus = QPushButton(self)
        self.cbPlus.move(300,15)
        self.cbPlus.setFixedSize(31,31)
        self.cbPlus.setStyleSheet("QPushButton{border-image: url(../static/imgs/plus.png)}")
        self.cbPlus.setToolTip("Show More")
        self.cbPlus.clicked.connect(self._getMore)

        self.activation = QComboBox(self)
        self.activation.addItems(li.all_activations)

        self.numbers = QLineEdit(self)
        self.numbers.setPlaceholderText("Kernel numbers")
        self.numbers.move(50,100)

        # self.cb.currentIndexChanged

    def _changeLayer(self):
        self.layer.setText(self.cb.currentText())

    def _getMore(self):
        dia = ALLLayer()
        result = dia.exec_()
        self.layer.setText(dia.info)

    # @staticmethod
    # def getData(options,parent=None):
    #     dialog = ALLLayer(parent)
    #     result = dialog.exec_()
    #     return dialog.info
        


if __name__ == '__main__':
	app = QApplication(sys.argv)
	comboxDemo = LayerDialog()
	comboxDemo.show()
	sys.exit(app.exec_())