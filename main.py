from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.slider import Slider
from kivy.core.window import Window

Window.clearcolor = (0.02, 0.02, 0.05, 1)

class BrazilSensiPro(App):
    def build(self):
        self.correct_key = "MD RAYHAN" 
        self.is_active = False
        self.main_layout = BoxLayout(orientation='vertical', padding=30, spacing=15)
        self.show_login_screen()
        return self.main_layout

    def show_login_screen(self):
        self.main_layout.clear_widgets()
        self.main_layout.add_widget(Label(text="COMMANDO TEAM\nACTIVATION REQUIRED", font_size='22sp', bold=True, color=(1, 0, 0, 1), halign="center"))
        self.key_input = TextInput(hint_text="Enter Your Name Key...", password=True, multiline=False, size_hint=(1, 0.2), halign="center")
        self.main_layout.add_widget(self.key_input)
        login_btn = Button(text="UNLOCK APP", size_hint=(1, 0.3), background_color=(0, 1, 0.5, 1), bold=True)
        login_btn.bind(on_press=self.check_key)
        self.main_layout.add_widget(login_btn)

    def check_key(self, instance):
        if self.key_input.text.upper() == self.correct_key:
            self.show_main_interface()
        else:
            self.key_input.text = ""
            self.key_input.hint_text = "WRONG NAME! ACCESS DENIED"

    def show_main_interface(self):
        self.main_layout.clear_widgets()
        self.main_layout.add_widget(Label(text="BRAZIL SENSI V2.3", font_size='30sp', bold=True, color=(0, 1, 1, 1)))
        self.main_layout.add_widget(Label(text="Smart Drag Power", color=(1, 1, 0, 1)))
        self.main_layout.add_widget(Slider(min=0, max=100, value=98))
        self.btn = Button(text="START OPTIMIZATION", size_hint=(1, 0.4), background_color=(0, 0.4, 1, 1), bold=True)
        self.main_layout.add_widget(self.btn)
        self.main_layout.add_widget(Label(text="Developed by: MD RAYHAN", font_size='14sp', color=(0.5, 0.5, 0.5, 1)))

if __name__ == "__main__":
    BrazilSensiPro().run()
      
