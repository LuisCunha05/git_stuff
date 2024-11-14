import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QLineEdit, QVBoxLayout
from PyQt6.QtGui import QIcon

def mostrar_mensagem():
    msg_box = QMessageBox()
    texto = input_texto.text()
    msg_box.setText(f"Olá, PyQt6!\n{texto}")
    msg_box.exec()

app = QApplication(sys.argv)


# Cria uma janela
tela = QWidget()
tela.setWindowTitle("Procedural Qt6")
tela.setWindowIcon(QIcon('pyqt6_example/favicon32.png'))
tela.setGeometry(200, 200, 300, 200)

# Cria um layout. QVBoxLayout empilha os itens verticalmente 
layout = QVBoxLayout()
tela.setLayout(layout)

# Adiciona um input de texto
input_texto = QLineEdit()

# Adiciona um botão a janela
botao = QPushButton("Clique aqui")
botao.clicked.connect(mostrar_mensagem)

# Adiciona os Widget no layout
layout.addWidget(input_texto)
layout.addWidget(botao)

# Exibe a janela
tela.show()

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

# App.exec executa o loop da aplicação e sys.exit finaliza aplicação
sys.exit(app.exec())
