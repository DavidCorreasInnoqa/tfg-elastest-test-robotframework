# ------------------------------- Libraries ------------------------------- #
import json
import os

from robot.api.deco import keyword
from robotframework.po.common.PageObject import PageObject

ROBOT_LIBRARY_DOC_FORMAT = 'HTML'

# Login
btn_top_login = "//a[@routerlink='/auth/login']"
cmp_email = "//input[@name='email']"
cpm_password = "//input[@name='password']"
btn_submit_login = "//button[@type='submit']"

# SingUp
btn_top_singup = "//a[@routerlink='/auth/singup']"
btn_submit_singup = "//button[@type='submit']"

# Pagina posts
list_posts = "//app-post-list"

class MobLogin(PageObject):

    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'
    __version__ = '1.0'

    # ------------------------------- Locators ------------------------------- #
    def __init__(self):
        super().__init__('AppiumLibrary')

        current_path = os.path.dirname(os.path.abspath(__file__))
        file_name = current_path + "/../data/" + self._get_cod_pais() + '/Users.json'
        with open(file_name) as user_file:
            self.user_data = json.load(user_file)

    # ------------------------------- Keywords ------------------------------- #
    @keyword(name='Registrarse como ${rol}')
    def sing_up(self, rol):
        # Accedemos a la pagina para registrarnos
        self.osl.wait_until_element_is_visible(btn_top_singup)
        self.osl.click_element(btn_top_singup)
        self.osl.wait_until_element_is_visible(cmp_email)
        
        # Introducimos credenciales
        self.osl.input_text(cmp_email, self.user_data["Credenciales"][rol]["Email"])
        self.osl.input_text(cpm_password, self.user_data["Credenciales"][rol]["Password"])

        # Clickamos para registrarnos
        self.osl.click_element(btn_submit_singup)
        self.osl.wait_until_element_is_visible(list_posts)
    
    @keyword(name='Logarse como ${rol}')
    def login_as(self, rol):
        # Accedemos al login.
        self.osl.wait_until_element_is_visible(btn_top_login)
        self.osl.click_element(btn_top_login)
        self.osl.wait_until_element_is_visible(cmp_email)
        
        # Introducimos credenciales
        self.osl.input_text(cmp_email, self.user_data["Credenciales"][rol]["Email"])
        self.osl.input_text(cpm_password, self.user_data["Credenciales"][rol]["Password"])

        # Clickamos logearnos
        self.osl.click_element(btn_submit_login)
        self.osl.wait_until_element_is_visible(list_posts)

        
