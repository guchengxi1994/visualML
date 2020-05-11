'''
@lanhuage: python
@Descripttion: 
@version: beta
@Author: xiaoshuyui
@Date: 2020-05-11 16:36:29
@LastEditors: xiaoshuyui
@LastEditTime: 2020-05-11 16:36:45
'''
from PyQt5.Qt import *
class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QTextEdit_文本光标')
        self.resize(500, 500)
        self.iniUI()

    def iniUI(self):
        te = QTextEdit(self)
        self.te = te
        te.resize(self.width() * 7 / 8, self.height() * 7 / 8)
        te.move((self.width() - te.width()) / 2, 2)
        te.setStyleSheet('background-color:cyan;font-size:20px')
        te.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        btn = QPushButton(self)
        self.btn = btn
        self.btn_w = self.width() / 3
        self.btn_h = self.height() * 3 / 32
        self.btn.resize(self.btn_w, self.btn_h)
        self.btn_x = (self.width() - self.btn_w) / 2
        self.btn_y = self.height() * 7 / 8 + (self.height() / 8 - self.btn_h) / 2
        self.btn.setText('测试按钮')
        self.btn.setStyleSheet('font-size:30px')
        self.btn.move(self.btn_x, self.btn_y)



    def textChoose(self):
        tc = self.te.textCursor()
        # QTextCursor.KeepAnchor 光标把锚点扔在原处，光标跑到哪，就选中一段从锚点到光标的文本
        # QTextCursor.MoveAnchor 光标与锚点一直绑定在一起，即默认情况下的纯光标移动，不存在选中操作
        # 选中文本，范围是当前光标到 从左到右第三个位置 处
        tc.setPosition(3,QTextCursor.KeepAnchor)

        #移动光标位置，第一个参数有很多选项，可以满足不同情况下的需要
        # cursor_pos = QTextCursor.NoMove                 #光标不移动
        # cursor_pos = QTextCursor.Start                  #文档开头
        # cursor_pos = QTextCursor.End                    #文档结尾
        # cursor_pos = QTextCursor.Up                     #上一行
        # cursor_pos = QTextCursor.Down                   #下一行
        # cursor_pos = QTextCursor.Left                   #向左移动一字符
        # cursor_pos = QTextCursor.Right                  #向右移动一字符
        cursor_pos = QTextCursor.StartOfLine            #行首
        # cursor_pos = QTextCursor.StartOfBlock           #段首
        # cursor_pos = QTextCursor.StartOfWord            #单词首
        # cursor_pos = QTextCursor.EndOfLine              #行末
        # cursor_pos = QTextCursor.EndOfBlock             #段末
        # cursor_pos = QTextCursor.EndOfWord              #单词末
        # cursor_pos = QTextCursor.PreviousCharacter      #上一个字符
        # cursor_pos = QTextCursor.PreviousBlock          #上一个段落
        # cursor_pos = QTextCursor.PreviousWord           #上一个单词
        # cursor_pos = QTextCursor.NextCharacter          #下一个字符
        # cursor_pos = QTextCursor.NextBlock              #下一个段落
        # cursor_pos = QTextCursor.NextWord               #下一个单词

        tc.movePosition(cursor_pos,QTextCursor.KeepAnchor,1)
        self.te.setTextCursor(tc)  #修改完光标之后 还得反向设置回文本编辑器te


    ################################################################操作 所选择的文本
    def textGet_choosen(self):
        tc = self.te.textCursor()
        print(tc.selectedText())#打印出所选择的文本
        print(tc.selection().toPlainText()) # QDocumentFragment
        # 返回选中的表格的区域位置及大小，由四个元素组成的元组，
        # ( 左上元素行号， 选中的行数，左上元素列号，选中的列数 )
        print(tc.selectedTableCells())

        print(tc.selectionStart())#所选中内容 的位置
        print(tc.selectionEnd())

        #############################################取消选中
        # tc.clearSeletion()
        # self.te.setCursor(tc)#需要反向设置，因为光标取消了选中，所以需要重新设置光标


        ##################移除所选中的文本
        tc.removeSelectedText()
        self.te.setFocus()
    ##########################################################删除 特定文本（纯代码操作删除）
    def textDelete(self):

        tc = self.te.textCursor()
        tc.deleteChar()#删除光标右边的文本 相当于delete
        tc.deletePreviousChar()#删除光标左边的文本，相当于Backspace  
        self.te.setFocus()



if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    win = MyWindow()

    win.btn.clicked.connect(win.textGet_choosen)
    win.show()
    sys.exit(app.exec_())
