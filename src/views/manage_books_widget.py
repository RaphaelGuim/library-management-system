# src/views/manage_books_widget.py

from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
    QHBoxLayout,
    QHeaderView,
    QLabel,
    QLineEdit,
    QPushButton,
    QTableWidget,
    QVBoxLayout,
    QWidget,
)


class ManageBooksWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Add Book button
        add_book_button = QPushButton("ADD BOOK")
        add_book_button.setIcon(QIcon("icons/add_book.png"))
        add_book_button.setIconSize(QSize(32, 32))
        layout.addWidget(add_book_button)

        # Search bar
        search_layout = QHBoxLayout()
        search_label = QLabel("Search:")
        self.search_input = QLineEdit()
        search_button = QPushButton("Search")
        search_button.clicked.connect(self.search_books)

        search_layout.addWidget(search_label)
        search_layout.addWidget(self.search_input)
        search_layout.addWidget(search_button)

        # Table
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(
            ["Title", "Author", "Category", "Publisher"]
        )
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # Pagination buttons
        pagination_layout = QHBoxLayout()
        self.prev_button = QPushButton("Previous")
        self.prev_button.clicked.connect(self.prev_page)
        self.next_button = QPushButton("Next")
        self.next_button.clicked.connect(self.next_page)

        pagination_layout.addWidget(self.prev_button)
        pagination_layout.addWidget(self.next_button)

        layout.addLayout(search_layout)
        layout.addWidget(self.table)
        layout.addLayout(pagination_layout)

        self.setLayout(layout)

    def search_books(self):
        # Placeholder function to handle search
        print(f"Searching for: {self.search_input.text()}")

    def prev_page(self):
        # Placeholder function to handle previous page
        print("Previous page")

    def next_page(self):
        # Placeholder function to handle next page
        print("Next page")
