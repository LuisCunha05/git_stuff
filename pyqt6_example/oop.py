import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
from PyQt6.QtGui import QIcon

class Appzao(QWidget):
    def __init__(self) -> None:
        super().__init__()
    
        self.setWindowTitle('OOP Qt6')
        self.setWindowIcon(QIcon('pyqt6_example/favicon32.png'))
        self.resize(300, 200)

        # Cria um layout. QVBoxLayout empilha os itens verticalmente 
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Adiciona um input de texto
        self.input_texto = QLineEdit()
        self.botao = QPushButton('Gerar Texto', clicked=self.mostrar_mensagem)


        layout.addWidget(self.input_texto)
        layout.addWidget(self.botao)

    def mostrar_mensagem(self):
        msg_box = QMessageBox()
        texto = self.input_texto.text()
        msg_box.setText(f"Olá, PyQt6!\n{texto}")
        msg_box.exec()


if __name__ == "__main__":

    app = QApplication(sys.argv)

    # Aplica estilo no app
    app.setStyleSheet("""
                        QWidget{
                            font-size:24px;
                            background-color:#ccc;
                        }
                        QLineEdit{
                            color:#F00;
                            font-style: italic;
                        }
                    """)

    tela = Appzao()
    tela.show()

    #Finaliza e sinaliza o fechamento do app para o windows
    sys.exit(app.exec())

