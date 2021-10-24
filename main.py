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
import dbConnect as db
import shutil
import random

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
        screens[4].build('TEste')
        
        

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
        original = self.ids.fingerprint.text
        fileType = original.split('\\')[-1].split('.')[-1]
        fileName = self.ids.email.text + str(random.randint(1,9999)) + '.' + fileType
        target = str(pathlib.Path(__file__).parent.resolve()) + '\\OpenCV\\database\\' + fileName
        shutil.copyfile(original, target)
        db.dbConnect().connect().registerUser('4', full_name, email, confirm_password, fileName)
        toast('Registrado com Sucesso!')

    
    def back(self):
        TelaPrincipal.switch_to(screens[0])
    
    def select_path(self, path):
        self.file.exit_manager(self.file)
        self.ids.fingerprint.text = path

    def import_digital(self):
        self.file = fileChoose
        self.file.escolherArquivo(fileChoose,self.select_path)

class TelaDeLogin(Screen):      #Tela de login       - Logar no sistema
    def build(self):
        pass

    def select_path(self, path):
        global User
        self.file.exit_manager(self.file)
        digitais = OpenCV.APIDigital().ProcurarDigital(path)
        login = self.ids.login.text
        password = self.ids.password.text
        if (len(digitais) > 0):
            for digital in digitais:
                #print(digital)
                User = db.dbConnect().connect().getUser(login,password, digital)
                if (User != None):
                    TelaPrincipal.switch_to(screens[4])
                    toast('Bem Vindo!')
                    screens[4].build(User.getNome())
        self.ids.msgError.text = "Login invalid!"

    def login(self):
        login = self.ids.login.text
        if utils.validarEmail(login):
            password = self.ids.password.text
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

class TelaDePerfil(Screen):     #Tela de perfil     - Gerenciar as digitais
    def build(self, username):
        self.ids.fullName.text = username
        i = db.dbConnect().connect().getFocoQueimadas()
        self.ids.datahora.text = i[0]
        self.ids.satelite.text = i[1]
        self.ids.municipio.text = i[2]
        self.ids.risco_fogo.text = i[3]


    def regfinger(self):
        TelaPrincipal.switch_to(screens[2])
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