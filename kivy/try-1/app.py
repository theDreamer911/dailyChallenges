from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class SayHello(App):
    def build(self):
        self.window = GridLayout() # membuat window baru
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x":0.5, "center_y": 0.5}

        # Logo
        self.window.add_widget(Image(source="logo.png")) # menambah widget image
        
        # Sambutan
        self.greeting = Label(
            text="Sebutkan siapa kamu?",
            font_size=24,
            color='#f3d3cb') # Menambahkan widget yang meminta nama
        self.window.add_widget(self.greeting) 

        # Form
        self.user = TextInput(
                        multiline=False,
                        padding_y = (18,18),
                        size_hint = (0.6, 0.4)
                        )
        self.window.add_widget(self.user)

        # Tombol
        self.button = Button(
                        text='Sapa',
                        size_hint = (0.6, 0.4),
                        bold = True,
                        background_color="f3d3cb",
                       # background_normal = ""
                        )
        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)

        return self.window


    def callback(self, instance):
        self.greeting.text = "Hai " + self.user.text + "!"

if __name__ == '__main__':
    SayHello().run()