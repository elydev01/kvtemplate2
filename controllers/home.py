from kivy.lang import Builder
from kivy.metrics import dp
from kivy import properties as p
from kivy.animation import Animation

from kivymd.app import MDApp as App
from kivymd.uix.screen import MDScreen


class HomeMainScreen(MDScreen):
    bg_pos = p.NumericProperty(0)
    
    def toggle_bg_pos(self):
        bg_pos = 0 if self.bg_pos > 0 else dp(self.height/2)
        Animation(bg_pos=bg_pos).start(self)


with open('views/home.kv', encoding='utf-8') as f:
    Builder.load_string(f.read())


class HomeScreenApp(App):
    def build(self):
        return HomeMainScreen()


def main():
    HomeScreenApp().run()


if __name__ == '__main__':
    main()
