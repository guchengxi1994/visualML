'''
@lanhuage: python
@Descripttion: 
@version: beta
@Author: xiaoshuyui
@Date: 2020-05-11 16:20:32
@LastEditors: xiaoshuyui
@LastEditTime: 2020-05-15 10:14:28
'''

from PyQt5.QtWidgets import QApplication,QWidget, \
    QPushButton,QTextEdit,QLabel,QDialog,QComboBox ,\
    QLineEdit,QMessageBox,QInputDialog
import sys
from . import layerInit as li
# import layerInit as li



class ALLLayer(QDialog):
    def __init__(self, parent=None, flags=None):
        super(ALLLayer,self).__init__()
        # self.setWindowTitle(self,"All layers")
        self.core = QComboBox(self)
        self.conv = QComboBox(self)
        self.pool = QComboBox(self)
        self.activation = QComboBox(self)
        self.others = QComboBox(self)

        self.submitButton = QPushButton(self)
        self.submitButton.setText("Submit")
        self.setFixedSize(300,600)

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

        self.Lothers = QLabel(self)
        self.Lothers.setText("Others")
        self.Lothers.move(50,450)


        self.core.move(100,50)
        self.core.addItems(li.all_layers_core)
        self.conv.move(100,150)
        self.conv.addItems(li.all_layers_conv)
        self.pool.move(100,250)
        self.pool.addItems(li.all_layers_pool)
        self.activation.move(130,350)
        self.activation.addItems(li.all_activations)
        self.others.addItems(li.others)
        self.others.move(100,450)
        self.submitButton.move(110,550)


        self.core.setCurrentIndex(-1)
        self.conv.setCurrentIndex(-1)
        self.pool.setCurrentIndex(-1)
        self.activation.setCurrentIndex(-1)
        self.others.setCurrentIndex(-1)

        self.core.currentIndexChanged.connect(self._changeLayer_core)
        self.conv.currentIndexChanged.connect(self._changeLayer_conv)
        self.pool.currentIndexChanged.connect(self._changeLayer_pool)
        self.activation.currentIndexChanged.connect(self._changeLayer_activation)
        self.others.currentIndexChanged.connect(self._changeLayer_others)

        
        self.layer = QLineEdit(self)
        self.layer.setEnabled(False)
        self.layer.move(80,500)
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

    def _changeLayer_others(self):
        self.layer.setText(self.others.currentText())

    def _submit(self):
        self.info = self.layer.text()
        self.close()

    # @staticmethod
    # def getData(options,parent=None):
    #     dialog = ALLLayer(parent)
    #     result = dialog.exec_()
    #     return dialog.info


def is_int(i):
    if len(i) == 0:
        return True
    else:
        try:
            num = int(i)
            return True
        except ValueError:
            return False



class LayerDialog(QDialog):
    def __init__(self, parent=None, flags=None):
        super(LayerDialog,self).__init__()
        # self.setWindowTitle(self,"Layers")
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
        self.cbPlus.setStyleSheet("QPushButton{border-image: url(./static/imgs/plus.png)}")
        self.cbPlus.setToolTip("Show More")
        self.cbPlus.clicked.connect(self._getMore)


        self.puz = QPushButton(self)
        self.puz.move(350,95)
        self.puz.setFixedSize(31,31)
        self.puz.setStyleSheet("QPushButton{border-image: url(./static/imgs/puz.png)}")
        self.puz.setToolTip("Show Hint")
        self.puz.clicked.connect(self._showHint)


        self.layer_acti = QLineEdit(self)
        self.layer_acti.setEnabled(False)
        self.layer_acti.move(50,60)


        self.activation = QComboBox(self)
        self.activation.addItems(li.all_activations)
        self.activation.move(200,60)
        self.layer_acti.setText(self.activation.currentText())
        self.activation.currentIndexChanged.connect(self._changeLayer)

        self.submit = QPushButton(self)
        self.submit.move(150,165)
        self.submit.setText("Submit")
        self.submit.clicked.connect(self._submit)

        self.numbers = QLineEdit(self)
        self.numbers.setPlaceholderText("Input Size ")
        self.numbers.move(50,100)

        self.numbers.setStyleSheet("background-color: white;")

        self.kernel_size = QLineEdit(self)
        self.kernel_size.setPlaceholderText("Kernel Size ")
        self.kernel_size.move(200,100)

        # self.numbers.setStyleSheet("background-color: white;")


        self.kernel_numbers = QLineEdit(self)
        self.kernel_numbers.setPlaceholderText("Kernel numbers")
        self.kernel_numbers.move(50,135)
        self.kernel_numbers.setStyleSheet("background-color: white;")

        self.paddingType = QComboBox(self)
        self.paddingType.move(200,135)
        self.paddingType.addItems(li.padding)

        self.strides = QLineEdit(self)
        self.strides.move(280,135)
        self.strides.setPlaceholderText('strides')
        self.strides.setFixedWidth(50)

        self.TrueFlag = False

        self.dropOutRate = 0.1

        # self.cb.currentIndexChanged

    def _changeLayer(self):
        self.layer.setText(self.cb.currentText())
        self.layer_acti.setText(self.activation.currentText())

    def _getMore(self):
        dia = ALLLayer()
        dia.setWindowTitle("All layers")
        result = dia.exec_()
        self.layer.setText(dia.info)
    
    def _submit(self):
        
        if self.layer.text() == "Input":
            self.layer_acti.setText("")
            # print(self.numbers.text())
            if self.layer_acti.text() == "LeakyReLU":
                self.layer_acti.setText("Leaky")

            if is_int(self.numbers.text()):
                self.TrueFlag = True
                self.close()
                # pass
            else:
                tmp = self.numbers.text()
                tmp = tmp.replace("（","(").replace("）",")").replace("，",',')
                if tmp.startswith("(") and tmp.endswith(")"):
                    tmp2 = tmp[1:-1]
                    tmpL = tmp2.split(",")
                    if len(tmpL)>0:
                        for i in tmpL:
                            num = 0
                            # print(i)    ## (123,123,3)
                            if not is_int(i):
                                num = 1
                            #     continue
                            # else:
                                self.numbers.setStyleSheet("background-color: green;")
                                QMessageBox.information(self,"警告","输入有问题！"+"\n"+"不是数字，也不是元组！")
                                # break
                        if num != 0:
                            pass
                        else:
                            self.TrueFlag = True
                            self.close()
                    else:
                        self.numbers.setStyleSheet("background-color: green;")
                        QMessageBox.information(self,"警告","输入有问题！"+"\n"+"不符合输入要求！")
                else:
                    self.numbers.setStyleSheet("background-color: green;")
                    QMessageBox.information(self,"警告","输入有问题！")
        elif self.layer.text() == "Dropout":
            d, okPressed = QInputDialog.getDouble(self, "Get double","Value:", 0, 0,1)
            if okPressed:
                if d == float(1):
                    d = 0.5
                self.dropOutRate = d
                self.close()
                # print(d)
        # elif self.layer.text().startswith("Conv"):
        #     # pass
        #     if is_int(self.kernel_size.text()):


        else:
            if  not self.layer.text().startswith("Conv"):

                if is_int(self.numbers.text()) and(is_int(self.kernel_numbers.text())):
                    self.TrueFlag = True
                    self.close()
                else:
                    self.numbers.setStyleSheet("background-color: green;")
                    self.kernel_numbers.setStyleSheet("background-color: green;")
                    QMessageBox.information(self,"警告","输入有问题！")
            
            else:
                if is_int(self.strides.text()):
                    pass
                else:
                    self.strides.setText("1")
                
                if is_int(self.kernel_size.text()):
                    self.kernel_size.setText("({},{})".format(self.kernel_size.text(),self.kernel_size.text()))
                elif self.kernel_size.text().startswith("(") and self.kernel_size.text().endswith(")"):
                    tmp = self.kernel_size.text().replace("(","").replace(")","")
                    tmps = tmp.split(",")
                    if len(tmps) != 2:
                        self.kernel_size.setStyleSheet("background-color: green;")
                        QMessageBox.information(self,"警告","输入有问题！")
                    else:
                        a = tmps[0]
                        b = tmps[1]
                        if is_int(a) and is_int(b) and a == b:
                            # pass
                            self.close()
                        else:
                            self.kernel_size.setStyleSheet("background-color: green;")
                            QMessageBox.information(self,"警告","输入有问题！")



        

    def _showHint(self):
        QMessageBox.information(self,"提示","数字或者元组!"+"\n"+"eg. 5(number) or (256,256,3) (tuple)")

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