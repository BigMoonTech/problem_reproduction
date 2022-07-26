import sys

from PySide6.QtWidgets import QMainWindow, QApplication

from MainWindow import UiMainWindow
from infrastructure.PathResolver import resolve_path


class MainWindow(QMainWindow, UiMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setup_ui(self)
        self.education_textbox.setSource(resolve_path('data/edu/FecalPositiveRoundworm.md'))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationDisplayName('VeTools')
    main_window = MainWindow()
    main_window.setWindowTitle('VeTools')
    main_window.show()
    sys.exit(app.exec())
