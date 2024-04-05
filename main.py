from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import operator
from os import path
class MeuApp(QMainWindow):

    def localPath(self, relativo):
        return f'{path.dirname(path.realpath(__file__))}\\{relativo}'
    
    def __init__(self):
        super().__init__()
        loadUi(self.localPath('calculadoraiphone.ui'), self)
    
        
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
        
        
        self.btn0.clicked.connect(lambda:self.pegarNum(self.btn0))
        self.btn1.clicked.connect(lambda:self.pegarNum(self.btn1))
        self.btn2.clicked.connect(lambda:self.pegarNum(self.btn2))
        self.btn3.clicked.connect(lambda:self.pegarNum(self.btn3))
        self.btn4.clicked.connect(lambda:self.pegarNum(self.btn4))
        self.btn5.clicked.connect(lambda:self.pegarNum(self.btn5))
        self.btn6.clicked.connect(lambda:self.pegarNum(self.btn6))
        self.btn7.clicked.connect(lambda:self.pegarNum(self.btn7))
        self.btn8.clicked.connect(lambda:self.pegarNum(self.btn8))
        self.btn9.clicked.connect(lambda:self.pegarNum(self.btn9))
        self.btnIgual.clicked.connect(self.mostrarResposta)
        self.btnAC.clicked.connect(self.limpar)
        self.btnDivisao.clicked.connect(lambda:self.definirOperacao(self.div))
        self.btnMais.clicked.connect(lambda:self.definirOperacao(self.soma))
        self.btnMenos.clicked.connect(lambda:self.definirOperacao(self.sub))
        self.btnMult.clicked.connect(lambda:self.definirOperacao(self.mult))
        self.btnPorcentagem.clicked.connect(self.porcentagem)
        self.btnMaisMenos.clicked.connect(self.numeroNegativo)
        self.btnVirgula.clicked.connect(lambda:self.pegarNum(self.btnVirgula))
    num1 = 0
    num2 = 0
    op = None
    numresultado = 0


    def numeroNegativo(self):
        numeroAtual = self.pegarDisplay()
        numeroAtual *= -1
        self.mostrarDisplay(numeroAtual)
    
        
        

    def resultado(self):
        if self.op:
            self.num2 = self.pegarDisplay()
            return self.op(self.num1, self.num2)
        else:
            print('nao tem operacao feita')

    def mostrarResposta(self): 
        if self.op:
            if self.num2:
                self.num1 = self.pegarDisplay()
            else:
                self.num2 = self.pegarDisplay()
 
            self.numResult = self.op()
            self.mostrarDisplay(self.numResult)


    def mostrarDisplay(self, value):
        value = str(value).replace('.',',')
        self.resultado.setText(value)



    
    def pegarDisplay(self):
        value = self.resultado.text()
        value = value.replace(',','.')
        try: value = int(value)
        except: value = float(value)
        return value
        
    
    
    #limpar
    def limpar(self):
            self.resultado.clear()
            self.resultado.setNum(0)
 

    def pegarNum(self, btn):
        ultimoValor = str( self.pegarDisplay() )
        #Digitando virgula
        if btn.text() == ',':
            if isinstance(self.pegarDisplay(), float):
                return
        #Digitando numeros
        else:
            # Se for numero inteiros
            if isinstance(self.pegarDisplay(), int):
                if self.pegarDisplay() == 0:
                    ultimoValor = ''
            # Se for numero float
            else:
                if self.resultado.text()[-1] == ",":
                    ultimoValor = self.resultado.text()
        self.mostrarDisplay(ultimoValor + btn.text())



    def definirOperacao(self, operacao):
        self.op = operacao
        self.num1 = int(self.pegarDisplay())
        self.num2 = 0
        self.mostrarDisplay(0)

    #operações
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

