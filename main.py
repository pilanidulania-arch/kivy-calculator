from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout


class CalculatorLayout(BoxLayout):

    def button_press(self, button):
        if button == "C":
            self.ids.input_box.text = ""
        else:
            self.ids.input_box.text += button

    def calculate(self):
        try:
            result = str(eval(self.ids.input_box.text))
            self.ids.input_box.text = result
        except:
            self.ids.input_box.text = "Error"


class CalculatorApp(App):
    def build(self):
        return Builder.load_file("calculator.kv")


if __name__ == "__main__":
    CalculatorApp().run()