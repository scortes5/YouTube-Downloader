import sys
from PyQt5.QtWidgets import QApplication
from view import DownloadView

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DownloadView()
    window.run()
    sys.exit(app.exec_())