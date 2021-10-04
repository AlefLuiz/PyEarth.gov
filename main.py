from kivymd.app import MDApp
from kivy.uix.screenmanager import NoTransition, ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.label import Label
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.utils import get_color_from_hex as C
from kivy.lang import Builder
import utils

Window.size = (800, 600)

class ScreenManagement(ScreenManager):
    pass

#Tela principal - Possui os botões Login e Registrar
class TelaDeInicio(Screen):
    def build(self):
        pass

    def login(self):
        TelaPrincipal.switch_to(screens[1])

    def register(self):
        TelaPrincipal.switch_to(screens[2])

    #Botão de registro de digital, será retirado no programa final (apenas testes)
    def regfinger(self):
        TelaPrincipal.switch_to(screens[3])

    #Botão de visualização do perfil, será retirado no programa final (apenas testes)
    def profile(self):
        TelaPrincipal.switch_to(screens[4])

#Tela de registro - Cadastrar usuários
class TelaDeRegistro(Screen):
    def build(self):
        pass

    def register(self):
        
        full_name = self.ids.full_name.text

        # Campo do Email e suas verificações #
        email = self.ids.email.text
        if not utils.validarEmail(email):
            self.ids.msgError.text = "Email invalid!"
            return

        password = self.ids.password.text
        if (utils.validarSenha(password)):
            confirm_password = self.ids.confirm_password.text
            if not confirm_password == password:
                self.ids.msgError.text = "Password is NOT the same as entered"
                return

            self.back()
        else:
            self.ids.msgError.text = "The password must be between 6 and 20 characters long, with at least one number, one uppercase letter, one lowercase letter and a special symbol."
            return
    
    def back(self):
        TelaPrincipal.switch_to(screens[0])

#Tela de login - Logar no sistema
class TelaDeLogin(Screen):
    def build(self):
        pass

    def login(self):
        global cliente, User
        login = self.ids.login.text
        if utils.validarEmail(login):
            password = self.ids.password.text
        else:
            self.ids.msgError.text = "Login invalid!"

    def register(self):
        TelaPrincipal.switch_to(screens[2])

    def back(self):
        TelaPrincipal.switch_to(screens[0])

#Tela de registro de digitais - Importar as digitais
class TelaDeRegDigital(Screen):
    
    def build(self):
        pass

    def import_digital(self):
        ()

    def register_digital(self):
        ()
        
    def back(self):
        TelaPrincipal.switch_to(screens[4])

#Tela de registro de digitais - Importar as digitais
class TelaDePerfil(Screen):
    
    def regfinger(self):
        TelaPrincipal.switch_to(screens[3])
    ()

#Tela necessária para o funcionamento
class MainApp(MDApp):
    def build(self):
        global screens, TelaPrincipal
        TelaPrincipal = ScreenManagement()
        screens = [TelaDeInicio(name = 'TelaDeInicio'), TelaDeLogin(name='TelaDeLogin'),TelaDeRegistro(name='TelaDeRegistro'), TelaDeRegDigital(name='TelaDeRegDigital'), TelaDePerfil(name='TelaDePerfil')]
        TelaPrincipal.switch_to(screens[0])
        return TelaPrincipal

MainApp().run()