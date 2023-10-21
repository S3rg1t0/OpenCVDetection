from PySide2.QtWidgets import QApplication
import sys
from core.app import App


if __name__ == "__main__":
    app = QApplication()
    window = App()
    window.show()
    sys.exit(app.exec_())

