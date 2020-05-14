'''
@lanhuage: python
@Descripttion: 
@version: beta
@Author: xiaoshuyui
@Date: 2020-05-11 08:49:06
@LastEditors: xiaoshuyui
@LastEditTime: 2020-05-14 10:03:13
'''
from PyQt5.QtWidgets import QApplication,QWidget, \
    QTextEdit,QVBoxLayout,QPushButton,QMainWindow, \
    QMessageBox
     

from PyQt5.QtGui import QTextCursor ,QTextDocument


import sys
from utils.LayerDialog import LayerDialog
from utils.OptimizerDialog import Ops
import copy

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
        self.addLayer.clicked.connect(self._addLayer)


        self.addOps = QPushButton(self)
        self.addOps.setText("Optimizers")
        self.addOps.move(100,150)
        self.addOps.clicked.connect(self._ops)
        

        

        self.reverse = QPushButton(self)
        self.reverse.setText("Undo")
        self.reverse.move(100,415)
        self.reverse.setToolTip("Delete Last Row")
        self.reverse.clicked.connect(self._undo)

        self.lastCodes = []
        
        self.isFirstLayer = True

        self.inputDim = ...

        self.lossCal = ""

        # self.test = QPushButton(self)
        # self.test.setText("test")
        # self.test.clicked.connect(self._insertDoc)


    def _undo(self):
        cursor = self.codeReview.textCursor()
        cursor.movePosition(QTextCursor.PreviousRow)
        cursor.select(QTextCursor.LineUnderCursor)
        cursor.deleteChar()#删除光标右边的文本 相当于delete
        cursor.deletePreviousChar()#删除光标左边的文本，相当于Backspace  
        self.codeReview.setFocus()

        # s = self.codeReview.toPlainText().split("\n")
        # print(self.lastCodes)

        # codes = list(set(s).difference(set(self.lastCodes)))

        # for i in codes:
        #     self.codeReview.insertPlainText(i)

    def _insertDoc(self,code:str):
    # def _insertDoc(self):
        # self.codeReview.insertPlainText("model = Sequential()"+'\n')
        # code = "test"
        doc = self.codeReview.document()
        curosr = QTextCursor(doc)
        searchText = "model = Sequential()"
        tmp = doc.find(searchText,curosr)

        if tmp is not None:
            curosr.movePosition(QTextCursor.StartOfLine,QTextCursor.KeepAnchor,0)
            curosr.insertText(code + '\n\n')
        
    
    def _ops(self):
        op = Ops()
        op.setWindowTitle("Optimizer")
        result = op.exec_()
        opti = op.opText.text()
        lr = op.learningRate
        decay = op.decayRate
        importCode = "from keras.optimizers import {}".format(opti)

        thisLine = "{} = {}(lr={},decay={}, momentum=0.9, nesterov=True)".format(
            opti.lower(),opti,str(lr),str(decay)
        )
        self.lossCal = op.lossText.text()
        s = self.codeReview.toPlainText().split("\n")

        if len(s) == 0 or  s==['']:
            self.codeReview.insertPlainText("from keras.models import Sequential" +"\n")
            self.codeReview.insertPlainText("\n\n")
            self.codeReview.insertPlainText("model = Sequential()"+"\n")

        if importCode not in s:
            # self.codeReview.insertPlainText()
            self._insertDoc(importCode)
            # s.insert(0,importCode+"\n")
        
        self.codeReview.insertPlainText(thisLine + '\n')

        
        # s.append(thisLine+"\n")

        




    
    def _testCode(self):
        if len(self.codeReview.toPlainText()) == 0:
            self.codeReview.insertPlainText("from keras.models import Sequential" +"\n")
        
        # s = self.codeReview.toPlainText()
        # print(s.split("\n"))

    
    def _addLayer(self):
        s = self.codeReview.toPlainText().split("\n")
        dia = LayerDialog()
        dia.setWindowTitle("Layers")
        result = dia.exec_()
        print(dia.layer.text())
        codes = []
        if len(s)>0 and s!=['']:
            pass
        else:
            codes.append("from keras.models import Sequential" +"\n")
            codes.append("\n\n")
            codes.append("model = Sequential()"+"\n")
        thisLayer = "from keras.layers import "+dia.layer.text() +"\n"
        if thisLayer in s:
            pass
        else:
            # codes.append(thisLayer)
            # codes.insert(0,thisLayer)
            self._insertDoc(thisLayer)
            
            if dia.layer.text() == "Dropout" :
                if not  self.isFirstLayer:
                    thisLine = "model.add(Dropout({}))".format(dia.dropOutRate)
                    codes.append(thisLine+"\n")
                else:
                    QMessageBox.information(self,"Error!","First Layer Must Have Input "+'\n'+" (size or dim),not Dropout!")

            if dia.layer.text() == "Input":
                pass

            if dia.layer.text() == "Dense" and self.isFirstLayer:
                # if self.isFirstLayer:
                self.isFirstLayer = False
                kernels = dia.kernel_numbers.text()
                input_dim = dia.numbers.text()
                act = dia.layer_acti.text()
                thisLine = "model.add(Dense({},activation={},input_dim={}))".format(kernels,act.lower(),input_dim)
                self.inputDim = input_dim
                codes.append(thisLine + "\n")

            elif dia.layer.text() == "Dense" and not self.isFirstLayer:
                # if self.isFirstLayer:
                # self.isFirstLayer = False
                kernels = dia.kernel_numbers.text()
                # input_dim = dia.numbers.text()
                act = dia.layer_acti.text()
                thisLine = "model.add(Dense({},activation={}))".format(kernels,act.lower())
                codes.append(thisLine + "\n")

        self.lastCodes = copy.deepcopy(codes)
        for i in codes:
            self.codeReview.insertPlainText(i)
        
        # for i in self.lastCodes:
        #     i.replace("\n","")






        
        
        

        





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
