from PyQt5.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget, QLineEdit, QLabel
from PyQt5.QtCore import Qt
from download import download_video

class DownloadView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Download View")
        self.setGeometry(100, 100, 300, 200)
        
        # Create a central widget and set a layout
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
         
        # Create title label
        self.title_label = QLabel("YouTube Video Downloader", self)
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setStyleSheet("""
            QLabel {
                font-size: 18px;
                font-weight: bold;
                color: #333;
                padding: 10px;
            }
        """)
        layout.addWidget(self.title_label)

        # Create input field for URL
        self.url_input = QLineEdit(self)
        self.url_input.setPlaceholderText("Enter YouTube URL")
        layout.addWidget(self.url_input)

        # Add a button to the layout
        self.download_button = QPushButton("Download", self)
        layout.addWidget(self.download_button)
        
        # Connect the button to a method using lambda
        self.download_button.clicked.connect(lambda: download_video(self.url_input.text(), None))
        
        # Apply styles
        self.apply_styles()

    def apply_styles(self):
        # Set styles for the main window
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f0f0f0;
                min-width: 500px;
                min-height: 400px;
            }
            QLineEdit {
                border: 1px solid #ccc;
                border-radius: 4px;
                padding: 5px;
                font-size: 14px;
            }
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                border-radius: 4px;
                padding: 10px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)

    def download_action(self):
        print("Download button clicked!")

    def run(self):
        self.show()

