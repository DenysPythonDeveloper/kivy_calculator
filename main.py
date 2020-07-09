from kivy.app import App
from kivy.config import Config
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '350')
Config.set('graphics', 'height', '400')


class MyApp(App):
    def __init__(self, **kwargs):
        super(MyApp, self).__init__(**kwargs)
        self.display = Label(
            text='0',
            font_size=50
        )

        self.button_1 = Button(
            text='1',
            font_size=24,
            on_press=self.add_number,
            background_color=[.90, .18, .18, 1]
        )

        self.button_2 = Button(
            text='2',
            font_size=24,
            on_press=self.add_number,
            background_color=[.90, .18, .18, 1]
        )

        self.button_3 = Button(
            text='3',
            font_size=24,
            on_press=self.add_number,
            background_color=[.90, .18, .18, 1]
        )

        self.button_4 = Button(
            text='4',
            font_size=24,
            on_press=self.add_number,
            background_color=[.90, .18, .18, 1]
        )

        self.button_5 = Button(
            text='5',
            font_size=24,
            on_press=self.add_number,
            background_color=[.90, .18, .18, 1]
        )

        self.button_6 = Button(
            text='6',
            font_size=24,
            on_press=self.add_number,
            background_color=[.90, .18, .18, 1]
        )

        self.button_7 = Button(
            text='7',
            font_size=24,
            on_press=self.add_number,
            background_color=[.90, .18, .18, 1]
        )

        self.button_8 = Button(
            text='8',
            font_size=24,
            on_press=self.add_number,
            background_color=[.90, .18, .18, 1]
        )

        self.button_9 = Button(
            text='9',
            font_size=24,
            on_press=self.add_number,
            background_color=[.90, .18, .18, 1]
        )

        self.button_0 = Button(
            text='0',
            font_size=24,
            on_press=self.add_number,
            background_color=[.90, .18, .18, 1]
        )

        self.button_multiply = Button(
            text='*',
            font_size=30,
            on_press=self.add_operation,
            background_color=[.29, .19, .34, 1]
        )

        self.button_minus = Button(
            text='-',
            font_size=30,
            on_press=self.add_operation,
            background_color=[.29, .19, .34, 1]
        )

        self.button_divided = Button(
            text='/',
            font_size=30,
            on_press=self.add_operation,
            background_color=[.29, .19, .34, 1]
        )

        self.button_plus = Button(
            text='+',
            font_size=30,
            on_press=self.add_operation,
            background_color=[.29, .19, .34, 1]
        )

        self.button_clear = Button(
            text='AC',
            font_size=30,
            on_press=self.clear,
            background_color=[.29, .19, .34, 1]
        )

        self.button_early = Button(
            text='=',
            font_size=30,
            on_press=self.output_on_display,
            background_color=[.29, .19, .34, 1]
        )

        self.formula = '0'


    def output_on_display(self, instance):
        self.formula = str(eval(self.formula))
        self.update_display()

    def clear(self, instance):
        self.formula = '0'
        self.update_display()


    def add_operation(self, instance):
        self.formula += str(instance.text)
        self.update_display()


    def update_display(self):
        self.display.text = self.formula


    def add_number(self, instance):
        if self.formula == '0':
            self.formula = ''
        self.formula += str(instance.text)
        self.update_display()


    def build(self):
        gl = GridLayout(cols=4, spacing=3)
        bl = BoxLayout(orientation='vertical', padding=10)
        bl.add_widget(self.display)

        gl.add_widget(self.button_7)
        gl.add_widget(self.button_8)
        gl.add_widget(self.button_9)
        gl.add_widget(self.button_divided)

        gl.add_widget(self.button_4)
        gl.add_widget(self.button_5)
        gl.add_widget(self.button_6)
        gl.add_widget(self.button_multiply)

        gl.add_widget(self.button_1)
        gl.add_widget(self.button_2)
        gl.add_widget(self.button_3)
        gl.add_widget(self.button_minus)

        gl.add_widget(self.button_clear)
        gl.add_widget(self.button_0)
        gl.add_widget(self.button_early)
        gl.add_widget(self.button_plus)

        bl.add_widget(gl)
        return bl


if __name__ == '__main__':
    MyApp().run()
