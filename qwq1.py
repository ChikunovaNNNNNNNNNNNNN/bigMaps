import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton
from PyQt6.QtWidgets import QLabel, QLineEdit
import os
import pygame
import requests


def run_pygame():
    """Запускает окно pygame."""
    server_address = 'https://static-maps.yandex.ru/v1?'
    api_key = 'f3a0fe3a-b07e-4840-a1da-06f18b2ddf13'
    ll_spn = f'll={q},{w}&spn={e}'
    map_request = f"{server_address}{ll_spn}&apikey={api_key}"
    response = requests.get(map_request)
    if not response:
        print("Ошибка выполнения запроса:")
        print(map_request)
        print("Http статус:", response.status_code, "(", response.reason, ")")
        sys.exit(1)
    map_file = "map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)

    pygame.init()
    screen = pygame.display.set_mode((600, 450))
    screen.blit(pygame.image.load(map_file), (0, 0))
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()
    os.remove(map_file)


q, w, e = 0, 0, 0


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.q, self.w, self.e = q, w, e

    def initUI(self):
        self.setGeometry(300, 300, 400, 400)
        self.setWindowTitle('Распили меня болгаркой')

        self.btn = QPushButton('Кнопка', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(100, 150)
        self.btn.clicked.connect(self.hello)

        self.name_label = QLabel(self)
        self.name_label.setText("масштаб")
        self.name_label.move(40, 10)

        self.name_input = QLineEdit(self)
        self.name_input.move(100, 10)

        self.name_labelq = QLabel(self)
        self.name_labelq.setText("координата1")
        self.name_labelq.move(40, 40)

        self.name_inputq = QLineEdit(self)
        self.name_inputq.move(100, 40)

        self.name_labelw = QLabel(self)
        self.name_labelw.setText("координата1")
        self.name_labelw.move(40, 90)

        self.name_inputw = QLineEdit(self)
        self.name_inputw.move(100, 90)

    def hello(self):
        global q, w, e
        self.e = self.name_input.text()
        self.q = self.name_inputq.text()
        self.w = self.name_inputw.text()
        e = self.e
        q = self.q
        w = self.w
        print(f"q = {self.name_inputw.text()}, w = {self.name_inputq.text()}, e = {self.name_input.text()}")
        print(q, w, e)
        run_pygame()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
