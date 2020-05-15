'''
@lanhuage: python
@Descripttion: 
@version: beta
@Author: xiaoshuyui
@Date: 2020-05-11 08:49:06
@LastEditors: xiaoshuyui
@LastEditTime: 2020-05-15 09:31:48
'''
from PyQt5.QtWidgets import QApplication,QWidget, \
    QTextEdit,QVBoxLayout,QPushButton,QMainWindow, \
    QMessageBox,QDialog,QComboBox
     

from PyQt5.QtGui import QTextCursor ,QTextDocument
from PyQt5.QtCore import Qt

import logging
from logging.handlers  import RotatingFileHandler
from concurrent_log_handler import ConcurrentRotatingFileHandler

import sys
from utils.LayerDialog import LayerDialog
from utils.OptimizerDialog import Ops
import copy
from utils.optimizerInit import ops,loss
import numpy as np

#日志
LOG_PATH = './static/logs/log_offline.txt'
# logging.basicConfig(filename=LOG_PATH,level=logging.INFO,filemode='a',format='%(asctime)s %(message)s',datefmt='%m-%d-%Y %I:%M:%S %p')
logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
rHandler = ConcurrentRotatingFileHandler(filename=LOG_PATH,maxBytes=5*1024*1024,backupCount=5)
rHandler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
rHandler.setFormatter(formatter)

logger.addHandler(rHandler)

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


        self.addCompile = QPushButton(self)
        self.addCompile.setText("Compile")
        self.addCompile.move(100,200)
        self.addCompile.clicked.connect(self._compile)
        

        

        self.reverse = QPushButton(self)
        self.reverse.setText("Undo")
        self.reverse.move(100,415)
        self.reverse.setToolTip("Delete Last Row")
        self.reverse.clicked.connect(self._undo)

        # self.lastCodes = []
        
        self.isFirstLayer = True

        self.inputDim = ...

        self.lossCal = ""

        self.opzName = ""

        self.FirstLayer = ""
        self.LastLayer = ""
        self.LastLayerDense = ...


        # self.test = QPushButton(self)
        # self.test.setText("test")
        # self.test.clicked.connect(self._insertDoc)

    
    def _compile(self):
        logger.info("Trying to compile")
        if len(self.lossCal)>0:
            thisCode = "model.compile(loss='{}',optimizer='{}',metrics=['accuracy'])".format(self.lossCal,self.opzName)
            # logger.error("Trying to compile")

        else:
            
            dia = QDialog()
            btn = QPushButton('OK',dia)
            com = QComboBox(dia)
            com.addItems(ops)
            com.move(50,50)

            com2 = QComboBox(dia)
            com2.addItems(loss)
            com2.move(50,100)

            btn.move(50,150)
            btn.clicked.connect(dia.close)
            dia.setWindowTitle("Dialog")
            dia.setWindowModality(Qt.ApplicationModal)
            dia.exec_()

            thisCode = "model.compile(loss='{}',optimizer='{}',metrics=['accuracy'])"\
                .format(com2.currentText(),com.currentText())

        # print(thisCode)
        self.codeReview.insertPlainText(thisCode+"\n")
        logger.info("Compile finished")





    def _undo(self):
        cursor = self.codeReview.textCursor()
        cursor.movePosition(QTextCursor.PreviousRow)
        cursor.select(QTextCursor.LineUnderCursor)
        cursor.deleteChar()#删除光标右边的文本 相当于delete
        cursor.deletePreviousChar()#删除光标左边的文本，相当于Backspace  
        self.codeReview.setFocus()
        logger.info("Delete last line")

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
        self.opzName = opti.lower()
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
        
        if isinstance(self.inputDim,type(Ellipsis)):
            QMessageBox.information(self,"ERROR!","没有输入！")
        else:
            self._insertDoc("import numpy as np")
            codes = []
            if self.FirstLayer == self.LastLayer :
                QMessageBox.information(self,"ERROR!","仅有一个输入层是不行滴！")
            elif self.LastLayerDense == "Dropout" and self.FirstLayer != self.LastLayer:
                QMessageBox.information(self,"ERROR!","你们家神经网络最后一层能Dropout?！")
            else:
                if self.inputDim.startswith("("):
                    tmp1 = self.inputDim.replace("(","(100")
                    tmp2 = self.inputDim.replace("(","(20")
                    codes.append("x_train = np.random.random(({}))".format(tmp1))
                    codes.append("x_test = np.random.random(({}))".format(tmp2))
                    codes.append("y_train = keras.utils.to_categorical(np.random.randint({}, size=(100, 1)), num_classes={})".format(self.LastLayerDense))
                    codes.append("y_test = keras.utils.to_categorical(np.random.randint({}, size=(20, 1)), num_classes={})".format(self.LastLayerDense))

                else:
                    codes.append("x_train = np.random.random((1000,{}))".format(self.inputDim))
                    codes.append("x_test = np.random.random((100,{}))".format(self.inputDim))
                    codes.append("y_train = keras.utils.to_categorical(np.random.randint({}, size=(100, 1)), num_classes={})".format(self.LastLayerDense))
                    codes.append("y_test = keras.utils.to_categorical(np.random.randint({}, size=(20, 1)), num_classes={})".format(self.LastLayerDense))

                codes.append("model.fit(x_train, y_train, batch_size=32, epochs=10)")
                codes.append("score = model.evaluate(x_test, y_test, batch_size=64)")

                for i in codes:
                    self.codeReview.insertPlainText(i+'\n')
            

        
        # s = self.codeReview.toPlainText()
        # print(s.split("\n"))

    
    def _addLayer(self):
        logger.info("Trying to add layer")
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
                    self.LastLayer = thisLine
                    self.LastLayerDense = "Dropout"
                    logger.info("Adding Dropout succeeded")
                else:
                    logger.warning("Adding Failed ===> First Layer Must Have Input (size or dim),not Dropout!")
                    QMessageBox.information(self,"Error!","First Layer Must Have Input "+'\n'+" (size or dim),not Dropout!")

            if dia.layer.text() == "Input":
                pass

            if dia.layer.text().startswith("Conv"):
                if dia.layer.text() == "Conv2D" and self.isFirstLayer:
                    kernels = dia.kernel_numbers.text()
                    input_dim = dia.numbers.text()
                    act = dia.layer_acti.text()
                    kernel_size = dia.kernel_size.text()
                    strides = dia.strides.text()
                    thisLine = "model.add(Conv2D({}, {}, activation='{}', input_shape={},strides={})".format(kernels,kernel_size,act,input_dim,strides)

            if dia.layer.text() == "Dense" and self.isFirstLayer:
                # if self.isFirstLayer:
                self.isFirstLayer = False
                kernels = dia.kernel_numbers.text()
                input_dim = dia.numbers.text()
                act = dia.layer_acti.text()
                thisLine = "model.add(Dense({},activation='{}',input_dim={}))".format(kernels,act.lower(),input_dim)
                self.FirstLayer = thisLine
                self.LastLayer = thisLine
                self.LastLayerDense = kernels
                self.inputDim = input_dim
                codes.append(thisLine + "\n")
                logger.info("Adding Dense succeeded")

            elif dia.layer.text() == "Dense" and not self.isFirstLayer:
                # if self.isFirstLayer:
                # self.isFirstLayer = False
                kernels = dia.kernel_numbers.text()
                # input_dim = dia.numbers.text()
                act = dia.layer_acti.text()
                thisLine = "model.add(Dense({},activation='{}'))".format(kernels,act.lower())
                codes.append(thisLine + "\n")
                self.LastLayer = thisLine
                self.LastLayerDense = kernels
                logger.info("Adding Dense succeeded")

        # self.lastCodes = copy.deepcopy(codes)
        for i in codes:
            self.codeReview.insertPlainText(i)
        
        # for i in self.lastCodes:
        #     i.replace("\n","")






if __name__ == "__main__":
    logger.info("Program Starting ...")
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
