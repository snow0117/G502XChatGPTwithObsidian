import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton
from PyQt5.QtCore import Qt
import pyperclip
import pyautogui
from openai import OpenAI


def fetch_description(text):
    client = OpenAI()
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": f"{text}의 뜻이 뭐야"}],
    )
    return response.choices[0].message.content


class TooltipWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        clip_text = pyperclip.paste()
        description = fetch_description(clip_text)
        layout = QVBoxLayout()
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(10)

        self.label = QLabel(description, self)
        self.label.setWordWrap(True)
        self.label.setStyleSheet("color: black; padding: 10px; background-color: white;")
        self.label.adjustSize()

        closeButton = QPushButton("Close", self)
        closeButton.clicked.connect(self.close)

        layout.addWidget(self.label)
        layout.addWidget(closeButton)
        self.setLayout(layout)

        self.adjustSize()

        mouse_x, mouse_y = pyautogui.position()
        self.setGeometry(mouse_x, mouse_y, self.width(), self.height())
        self.setWindowTitle('Text Description')
        self.setWindowFlags(Qt.Tool | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.show()

    def closeEvent(self, event):
        app.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TooltipWindow()
    sys.exit(app.exec_())



