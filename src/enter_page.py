from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget

from registration import RegistrationForm
from src.sign_in import SignInForm
from ui.ui_enter_page import Ui_Form


class EnterPage(QWidget, Ui_Form):
    """Приветственное окно (войти, регистрация, выйти)"""

    # Инциализация соединения с БД
    def __init__(self, connection):
        super().__init__()
        self.connection = connection
        self.setupUi(self)
        self.initUi()

    def initUi(self):
        """Инициализация нужного интерфейса"""

        self.verticalLayout.setAlignment(Qt.AlignVCenter)

        self.btn_sign_up.clicked.connect(self.sign_up)
        self.btn_sign_in.clicked.connect(self.sign_in)
        self.btn_exit.clicked.connect(self.close)

    def sign_up(self):
        """Создание формы регистрации"""

        # В init формы регистрации передаю приветственное
        # окно (self) и соединение с БД
        self.reg_dialog = RegistrationForm(self, self.connection)
        self.reg_dialog.show()

    def sign_in(self):
        """Создание формы входа"""

        # В init формы входа передаю приветственное
        # окно (self) и соединение с БД
        self.sign_in_form = SignInForm(self, self.connection)
        self.sign_in_form.show()