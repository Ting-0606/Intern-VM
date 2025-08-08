import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout,QLabel, QLineEdit, QPushButton, QMessageBox

from PyQt6.QtCore import Qt


class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Window setup
        self.setWindowTitle("Login")
        self.setFixedSize(300, 200)
        
        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Layout
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        
        # Username field
        self.username_label = QLabel("Username:")
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Enter your username") # add gray word in input box
        
        # Password field
        self.password_label = QLabel("Password:")
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Enter your password")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        '''QLine....Password make type thing in box become dots'''
        
        # Login button
        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.attempt_login)
        
        # Add widgets to layout
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)
        
        # Add some spacing
        layout.setSpacing(10)#set vertical spacing between widgets in the layout
        layout.setContentsMargins(20, 20, 20, 20)#set margins around the edges of the layout
    
    def attempt_login(self):
        username = self.username_input.text()
        password = self.password_input.text()
        
        
        if username == "admin" and password == "password":
            QMessageBox.information(self, "Success", "Login successful!")
           #here can add sth to open other window
        else:
            QMessageBox.warning(self, "Error", "Invalid username or password")
            self.password_input.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    window = LoginWindow()
    window.show()
    
    sys.exit(app.exec())