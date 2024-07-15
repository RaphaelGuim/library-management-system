# src/main.py

import sys

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
    QApplication,
    QFrame,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QSplitter,
    QStackedWidget,
    QVBoxLayout,
    QWidget,
)

from views.manage_books_widget import BooksWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Library Management System")
        self.showMaximized()

        # Create the stacked widget
        self.stacked_widget = QStackedWidget()

        # Create the main menu widget
        self.main_menu_widget = QWidget()
        main_layout = QVBoxLayout()

        # Create the splitter
        splitter = QSplitter(Qt.Vertical)

        # Create the top section with buttons
        top_widget = QWidget()
        top_layout = QHBoxLayout()

        # Create buttons with icons
        self.book_button = QPushButton("Manage Books")
        self.book_button.setIcon(QIcon("icons/books.png"))
        self.book_button.setIconSize(QSize(64, 64))
        self.book_button.clicked.connect(self.show_books_window)

        self.user_button = QPushButton("Manage Users")
        self.user_button.setIcon(QIcon("icons/users.png"))
        self.user_button.setIconSize(QSize(64, 64))

        self.loan_button = QPushButton("Manage Loans")
        self.loan_button.setIcon(QIcon("icons/loans.png"))
        self.loan_button.setIconSize(QSize(64, 64))

        top_layout.addWidget(self.book_button)
        top_layout.addWidget(self.user_button)
        top_layout.addWidget(self.loan_button)
        top_widget.setLayout(top_layout)

        # Add the top widget to the splitter
        splitter.addWidget(top_widget)

        # Create a bottom section for additional information
        bottom_widget = QWidget()
        bottom_layout = QVBoxLayout()

        bottom_label = QLabel("Library Management System")
        bottom_label.setAlignment(Qt.AlignCenter)
        bottom_frame = QFrame()
        bottom_frame.setFrameShape(QFrame.HLine)
        bottom_frame.setFrameShadow(QFrame.Sunken)

        bottom_layout.addWidget(bottom_frame)
        bottom_layout.addWidget(bottom_label)
        bottom_widget.setLayout(bottom_layout)

        # Add the bottom widget to the splitter
        splitter.addWidget(bottom_widget)

        # Add the splitter to the main layout
        main_layout.addWidget(splitter)
        self.main_menu_widget.setLayout(main_layout)

        # Add the main menu widget to the stacked widget
        self.stacked_widget.addWidget(self.main_menu_widget)

        # Create the books management window and add it to the stacked widget
        self.books_window = BooksWindow(parent=self.stacked_widget)
        self.stacked_widget.addWidget(self.books_window)

        # Set the stacked widget as the central widget
        self.setCentralWidget(self.stacked_widget)

    def show_books_window(self):
        self.stacked_widget.setCurrentIndex(1)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
