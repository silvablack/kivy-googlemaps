from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from maps import Maps
from kivy.garden.mapview import MapView

class LoginScreen(GridLayout):

    def __init__(self,**kwargs):
        super(LoginScreen,self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='Usuário'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
        self.add_widget(Label(text='Senha'))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)

class MyApp(App):

    def build(self):
        mapview = MapView(zoom=11,lat=-2.519495,lon=-44.247695)
        return mapview
        """return LoginScreen()"""



if __name__=='__main__':
    MyApp().run()
