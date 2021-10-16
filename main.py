from kivymd.app import MDApp
from kivy.uix.screenmanager import NoTransition, ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.label import Label
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.filemanager import MDFileManager
from kivy.utils import get_color_from_hex as C
from kivy.lang import Builder
from kivymd.toast import toast
import pathlib
import utils
import OpenCV.read as OpenCV

Window.size = (800, 600)

class ScreenManagement(ScreenManager):
    pass

class TelaDeInicio(Screen):     #Tela principal     - Possui os principais botões
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

class TelaDeRegistro(Screen):   #Tela de registro - Cadastrar usuários
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

class TelaDeLogin(Screen):      #Tela de login       - Logar no sistema
    def build(self):
        pass

    def select_path(self, path):
        self.file.exit_manager(self.file)
        if OpenCV.APIDigital().ProcurarDigital(path):
            TelaPrincipal.switch_to(screens[4])
            toast('Bem Vindo!')

    def login(self):
        global cliente, User
        login = self.ids.login.text
        if utils.validarEmail(login):
            #password = self.ids.password.text
            self.file = fileChoose
            self.file.escolherArquivo(fileChoose,self.select_path)
        else:
            self.ids.msgError.text = "Login invalid!"

    def register(self):
        TelaPrincipal.switch_to(screens[2])

    def back(self):
        TelaPrincipal.switch_to(screens[0])
        

class TelaDeRegDigital(Screen): #Tela de importação das digitais - Importar as digitais
    def build(self):
        pass

    def register_digital(self):
        ()
        
    def back(self):
        TelaPrincipal.switch_to(screens[2])

    def select_path(self, path):
        self.file.exit_manager(self.file)
        self.ids.fingerprint.text = path

    def import_digital(self):
        self.file = fileChoose
        self.file.escolherArquivo(fileChoose,self.select_path)

class TelaDePerfil(Screen):     #Tela de perfil     - Gerenciar as digitais
    
    def regfinger(self):
        TelaPrincipal.switch_to(screens[3])
    ()

class MainApp(MDApp):
    def build(self):
        global screens, TelaPrincipal
        TelaPrincipal = ScreenManagement()
        screens = [TelaDeInicio(name = 'TelaDeInicio'), TelaDeLogin(name='TelaDeLogin'),TelaDeRegistro(name='TelaDeRegistro'), TelaDeRegDigital(name='TelaDeRegDigital'), TelaDePerfil(name='TelaDePerfil')]
        TelaPrincipal.switch_to(screens[0])
        return TelaPrincipal

class fileChoose():
    def escolherArquivo(self, selectpath):

        path = str(pathlib.Path(__file__).parent.resolve())  # path to the directory that will be opened in the file manager
        self.file_manager = MDFileManager(
            exit_manager = self.exit_manager,  # function called when the user reaches directory tree root
            select_path = selectpath,  # function called when selecting a file/directory
        )
        self.file_manager.show(path)

    def exit_manager(self, *args):
        self.manager_open = False
        self.file_manager.close()
MainApp().run()