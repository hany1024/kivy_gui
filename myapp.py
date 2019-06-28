from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import ButtonBehavior
from kivy.uix.image import Image

class HomeScreen(Screen):
    pass


class ImageButton(ButtonBehavior, Image):
    pass


class SettingsScreen(Screen):
    pass

kv = Builder.load_file("my2.kv")

class FirstApp(App):
    def build(self):
        return kv

    def change_screen(self,screen_name):
        screen_manager = self.root.ids["screen_manager"]
        screen_manager.current = screen_name



if __name__=="__main__":
    FirstApp().run()