from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class VRApp(App):
    def build(self):
        # Головний контейнер на весь екран (горизонтальний поділ для лівого та правого ока)
        root = BoxLayout(orientation='horizontal')

        # Ліва частина екрана (для лівого ока)
        left_eye = BoxLayout(orientation='vertical', padding=10)
        left_eye.add_widget(Label(text='[ Ліве око ]\nVR Клієнт працює!', font_size=24, halign='center'))
        # Права частина екрана (для правого ока)
        right_eye = BoxLayout(orientation='vertical', padding=10)
        right_eye.add_widget(Label(text='[ Праве око ]\nVR Клієнт працює!', font_size=24, halign='center'))

        root.add_widget(left_eye)
        root.add_widget(right_eye)

        return root


if __name__ == '__main__':
    VRApp().run()