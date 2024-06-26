import sys
import pyttsx3
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QSizePolicy
from PyQt5.QtCore import Qt, QThread, pyqtSignal, QObject
import pyperclip
import pyautogui
from openai import OpenAI


class Worker(QObject):
    finished = pyqtSignal(str)

    def __init__(self, text):
        super().__init__()
        self.text = text

    def run(self):
        description = fetch_description(self.text)
        self.finished.emit(description)


def fetch_description(text):
    client = OpenAI()
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": f"{text}의 뜻이 뭐야"}],
    )
    return response.choices[0].message.content


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


class TooltipWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        clip_text = pyperclip.paste()
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(10, 10, 10, 10)
        self.layout.setSpacing(10)

        self.label = QLabel("Loading description...", self)
        self.label.setWordWrap(True)
        self.label.setStyleSheet("color: black; padding: 10px; background-color: white;")
        self.label.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.closeButton = QPushButton("Close", self)
        self.closeButton.clicked.connect(self.close)

        self.speakButton = QPushButton("Speak", self)
        self.speakButton.clicked.connect(lambda: speak(self.label.text()))

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.closeButton)
        self.layout.addWidget(self.speakButton)
        self.setLayout(self.layout)

        self.adjustSize()

        mouse_x, mouse_y = pyautogui.position()
        self.setGeometry(mouse_x, mouse_y, self.width(), self.height())
        self.setWindowTitle('Text Description')
        self.setWindowFlags(Qt.Tool | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.show()

        self.start_background_task(clip_text)

    def start_background_task(self, text):
        self.thread = QThread()
        self.worker = Worker(text)
        self.worker.moveToThread(self.thread)
        self.worker.finished.connect(self.update_label)
        self.thread.started.connect(self.worker.run)
        self.thread.start()

    def update_label(self, description):
        self.label.setText(description)
        self.label.adjustSize()
        self.adjustSize()
        self.thread.quit()
        self.thread.wait()

    def closeEvent(self, event):
        app.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TooltipWindow()
    sys.exit(app.exec_())
