from random import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Line

class Drawing_components(Widget):

    def on_touch_down(self, touch):
        color = (random(),1 ,1)
        with self.canvas:
            Color(*color, mode="hsv")
            d = 30
            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
            touch.ud["line"] = Line(points=(touch.x, touch.y))

    def on_touch_move(self, touch):
        touch.ud["Line"].points += [touch.x, touch.y]

class Drawing_app(App):

    def build(self):
        parent = Widget()
        self.painter = Drawing_components()
        clearbtn = Button(text = "Clear")
        clearbtn.bind(on_release = self.clear_canvas)
        parent.add_widget(self.painter)
        parent.add_widget(clearbtn)
        return parent

    def clear_canvas(self, obj):
        self.painter.canvas.clear()

if __name__ == "__main__":
    Drawing_app().run()



