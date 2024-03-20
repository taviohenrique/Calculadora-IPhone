from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import operator

class MeuApp(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('calculadoraiphone.ui', self)
        
        self.btn0: QPushButton
        self.btn1: QPushButton
        self.btn2: QPushButton
        self.btn3: QPushButton
        self.btn4: QPushButton
        self.btn5: QPushButton
        self.btn6: QPushButton
        self.btn7: QPushButton
        self.btn8: QPushButton
        self.btn9: QPushButton
        self.btnAC: QPushButton
        self.btnDivisao: QPushButton
        self.btnIgual: QPushButton
        self.btnMais: QPushButton
        self.btnMenos: QPushButton
        self.btnMaisMenos: QPushButton
        self.btnMult: QPushButton
        self.btnPorcentagem: QPushButton
        self.btnVirgula: QPushButton
        self.resultado: QLabel
        
        
        self.btn0.clicked.connect(lambda:self.pegarNum('0'))
        self.btn1.clicked.connect(lambda:self.pegarNum('1'))
        self.btn2.clicked.connect(lambda:self.pegarNum('2'))
        self.btn3.clicked.connect(lambda:self.pegarNum('3'))
        self.btn4.clicked.connect(lambda:self.pegarNum('4'))
        self.btn5.clicked.connect(lambda:self.pegarNum('5'))
        self.btn6.clicked.connect(lambda:self.pegarNum('6'))
        self.btn7.clicked.connect(lambda:self.pegarNum('7'))
        self.btn8.clicked.connect(lambda:self.pegarNum('8'))
        self.btn9.clicked.connect(lambda:self.pegarNum('9'))
        self.btnAC.clicked.connect(self.limpar)
        self.btnDivisao.clicked.connect(lambda:self.definirOperacao((lambda:self.div)))
        self.btnIgual.clicked.connect(self.mostrarResposta)
        self.btnMais.clicked.connect(lambda:self.definirOperacao(self.soma))
        self.btnMenos.clicked.connect(lambda:self.definirOperacao(self.sub))
        # self.btnMaisMenos.clicked.connect(self.numeroNegativo)
        self.btnMult.clicked.connect(lambda:self.definirOperacao(self.mult))
        self.btnPorcentagem.clicked.connect(self.porcentagem)
        # self.btnVirgula.clicked.connect(self.colocarVirgula)
    num1 = 0
    num2 = 0
    op = None
    numresultado = 0


    def limpar(self):
        self.resultado.clear()
        self.resultado.setNum(0)
    

    def pegarNum(self, numero):
        if self.pegarDisplay() != '0':
            self.numeroatual = int(self.pegarDisplay())
            self.resultado.setNum(self.numeroatual + numero)
        else:self.resultado.setNum(numero)
            
        
    def definirOperacao(self, operacao):
        self.op = operacao
        self.num1 = (self.resultado.text())
        self.num2 = 0
        self.resultado.setNum(0)


    def resposta(self):
        if self.op:
            self.num2 = self.pegarDisplay()
            return self.op()

    def mostrarResposta(self):
        if self.op:
            if self.num2:
                self.num1 = self.pegarDisplay()
            else:self.num2 = self.pegarDisplay()
            self.numresultado = self.op()
            self.resultado.setNum(self.numresultado())


    # def numeroNegativo(self):
    #     if self.resultado.text() != '0':
    #         inverter = self.resultado.text() * -1
    #         self.resultado.setText(inverter)
        
        

    # def colocarVirgula(self):
    #     if not '.' in self.resultado.text():
    #         # virgula = str(virgula).replace('.',',')
    #         self.resultado.setText(self.resultado.text() + '.')
    #         # print(virgula)

    
    def mostrarDisplay(self, value):
        value = str(value).replace('.',',')
        self.resultado.setText(value)



    
    def pegarDisplay(self):
        value = self.resultado.text()
        value = value.replace(',','.')
        try: value = int(value)
        except: value = float(value)
        return value
            


    def soma(self):
        return self.num1 + self.num2

    def sub(self):
        return self.num1 - self.num2

    def mult(self):
        return self.num1 * self.num2
    
    def div(self):
        return self.num1 / self.num2

    
    def porcentagem(self):
        porcento = self.pegarDisplay()/100
        if self.op == self.soma or self.op == self.sub:
            porcento = self.num1 * porcento
        self.mostrarDisplay(porcento)

            


            
    


if __name__ == '__main__':
    app = QApplication([])
    janela = MeuApp()
    janela.show()
    app.exec_()


