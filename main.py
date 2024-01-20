from kivy.app import App
from pytube import YouTube
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
import os
from kivy.uix.scrollview import ScrollView
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.label import Label
from kivymd.toast import toast
from android.permissions import request_permissions, Permission
toast("YouTube video downloader\nBy KareKaren")

kv = '''<MainWidget>:
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: 'YT.png'
    boxl: box
    BoxLayout:
        orientation: 'vertical'
        id: box
        box: box1
        box0: box2
        BoxLayout:
            id: box1
            reci: reci
            size_hint_y: None
            height: 50
            
            TextInput:
                id: nameee
                multiline: True
                size_hint: (.9, None)
                height: 50
                font_size: 40
                pos_hint:{"center_x":0.5}
                hint_text: "                                              Ссылка "

        BoxLayout:
            orientation: 'vertical'
            id: box2
            nameee: nameee
            
            ScrollView:
                do_scroll_x: True
                do_scroll_y: True
                
                Label:
                    size_hint: (1, None)
                    height: self.texture_size[1]
                    text_size: self.width, None
                    width: self.texture_size[0] + 20  # Добавляем отступы по ширине текста
                    halign: 'center'  # Центрирование текста по горизонтали
                    #padding: 10  # Отступы по ширине текста
                    id: reci
                    markup: True
                    font_size: 50
                    text: '[b][color=F7FF01][b]'
                    #size_hint_x: None
                    #width: 200
                    #pos_hint:{"center_x": 1,"center_y":1}
                
            Button:
                markup: True
                font_size: 70
                text: '[b][color=FF0905]Скачать[b]'
                size_hint: (.9, None)
                pos_hint:{"center_x":0.5}
                on_press: root.say_reci()
                '''
class MainWidget(BoxLayout):
    data_output = ObjectProperty()
    data_input = ObjectProperty()
    boxl = ObjectProperty()
    nameee = ObjectProperty()
    def client(self, data): pass
    
    def say_reci(self):
          if self.boxl.box0.nameee.text == '':
              self.boxl.box0.nameee.text = 'Введите ссылку!'
              toast("Без ссылки нельзя!")
          try:
              toast("Загрузка данных... не закрывайте приложение!")
              video = YouTube(self.boxl.box0.nameee.text)
              self.boxl.box.reci.text = f'[b][color=F7FF01]Название[color=FFFFFF]: {video.title}\n\n[color=F7FF01]Длина[color=FFFFFF]: {video.length} сек.\n\n[color=F7FF01]Размер[color=FFFFFF]: {video.streams.get_highest_resolution().filesize / 1024 ** 2:.2f} Мегабайт[b]'
              toast("Загрузка видео... не закрывайте приложение!")
              video.streams.get_highest_resolution().download(output_path="/storage/emulated/0")
              toast("Видео сохранено в папку 0")
          except Exception as e:
              self.boxl.box.reci.text = '[b][color=FF0905]Видео не найдено![b]\n'
    	              
class MainApp(MDApp):
    def build(self):
        Builder.load_string(kv)
        return MainWidget()


if __name__ == '__main__':
    app = MainApp()
    app.run()