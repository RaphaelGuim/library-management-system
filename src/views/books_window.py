# src/views/books_window.py

from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QPushButton,
    QStackedWidget,
    QVBoxLayout,
    QWidget,
)

from .manage_books_widget import ManageBooksWidget


class BooksWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Books Management")

        # Main layout
        main_layout = QVBoxLayout()

        # Back button
        self.back_button = QPushButton("Back")
        self.back_button.clicked.connect(self.back_to_main)
        main_layout.addWidget(self.back_button)

        # Horizontal layout for menu and content
        horizontal_layout = QHBoxLayout()

        # Left menu with buttons
        menu_layout = QVBoxLayout()

        self.manage_books_button = QPushButton("Manage Books")
        self.manage_books_button.setIcon(QIcon("icons/manage_books.png"))
        self.manage_books_button.setIconSize(QSize(32, 32))
        self.manage_books_button.clicked.connect(lambda: self.change_content(0))

        self.category_button = QPushButton("Category")
        self.category_button.setIcon(QIcon("icons/category.png"))
        self.category_button.setIconSize(QSize(32, 32))
        self.category_button.clicked.connect(lambda: self.change_content(1))

        self.author_button = QPushButton("Author")
        self.author_button.setIcon(QIcon("icons/author.png"))
        self.author_button.setIconSize(QSize(32, 32))
        self.author_button.clicked.connect(lambda: self.change_content(2))

        self.publisher_button = QPushButton("Publisher")
        self.publisher_button.setIcon(QIcon("icons/publisher.png"))
        self.publisher_button.setIconSize(QSize(32, 32))
        self.publisher_button.clicked.connect(lambda: self.change_content(3))

        menu_layout.addWidget(self.manage_books_button)
        menu_layout.addWidget(self.category_button)
        menu_layout.addWidget(self.author_button)
        menu_layout.addWidget(self.publisher_button)

        menu_widget = QWidget()
        menu_widget.setLayout(menu_layout)

        # Central content area
        self.content_area = QStackedWidget()

        # Create manage books widget
        self.manage_books_widget = ManageBooksWidget()

        # Add different content widgets
        self.category_widget = QLabel("Category Content")
        self.author_widget = QLabel("Author Content")
        self.publisher_widget = QLabel("Publisher Content")

        self.content_area.addWidget(self.manage_books_widget)
        self.content_area.addWidget(self.category_widget)
        self.content_area.addWidget(self.author_widget)
        self.content_area.addWidget(self.publisher_widget)

        # Add widgets to the horizontal layout
        horizontal_layout.addWidget(menu_widget)
        horizontal_layout.addWidget(self.content_area)

        main_layout.addLayout(horizontal_layout)

        self.setLayout(main_layout)

    def change_content(self, index):
        self.content_area.setCurrentIndex(index)

    def back_to_main(self):
        self.parent().setCurrentIndex(0)
