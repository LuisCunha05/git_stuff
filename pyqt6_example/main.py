import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QTextEdit, QVBoxLayout
from PyQt6.QtGui import QIcon

class Appzao(QWidget):
    def __init__(self) -> None:
        super().__init__()
    
        self.setWindowTitle('Appzâo Brabo')
        self.setWindowIcon(QIcon('favicon32.png'))
        self.resize(400, 450)

        layout = QVBoxLayout()
        self.setLayout(layout)

        #Widgets
        self.input_text = QLineEdit()
        button_send = QPushButton('&Gerar Texto', clicked=self.generateText)
        self.output_text = QTextEdit()
        outro_b = QPushButton('Hehe', clicked=lambda: print('LOL'))


        layout.addWidget(self.input_text)
        layout.addWidget(button_send)
        layout.addWidget(self.output_text)

    def generateText(self):
        atual = self.input_text.text()
        self.output_text.setText(
            f"""|{'*' * 10}{'#' * 10}{'*' * 10}|\n|{' ' * 16}{atual:_^10}{' ' * 16}|\n|{'*' * 10}{'#' * 10}{'*' * 10}|""")


app = QApplication(sys.argv)
app.setStyleSheet("""
                    QWidget{
                        font-size:24px;
                        color:#ccc;
                    }
                    QLineEdit{
                        color:#00F;
                        width:200px;
                    }
""")

tela = Appzao()
tela.show()

#Finaliza e sinaliza o fechamento do app para o windows
sys.exit(app.exec())

