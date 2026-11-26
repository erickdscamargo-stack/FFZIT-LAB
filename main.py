
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse
from kivy.metrics import dp

from ffzit.arena import Arena
from ffzit.aim_trainer import AimTrainer
from ffzit.esp import ESPDemo


class ArenaView(Widget):

    def __init__(self, arena, aim, esp, **kwargs):
        super().__init__(**kwargs)
        self.arena = arena
        self.aim = aim
        self.esp = esp
        self.bind(pos=self.draw, size=self.draw)

    def draw(self, *args):
        self.canvas.clear()

        with self.canvas:
            Color(0.04, 0.04, 0.06, 1)
            from kivy.graphics import Rectangle
            Rectangle(pos=self.pos, size=self.size)

            for target in self.arena.get_targets():
                x = self.x + target["x"] / self.arena.width * self.width
                y = self.y + target["y"] / self.arena.height * self.height

                Color(1, 0.1, 0.2, 1)
                Ellipse(pos=(x-dp(12), y-dp(12)),
                        size=(dp(24), dp(24)))

            if self.esp.enabled:
                for target in self.esp.scan(
                    self.arena.width / 2,
                    self.arena.height / 2
                ):
                    x = self.x + target["x"] / self.arena.width * self.width
                    y = self.y + target["y"] / self.arena.height * self.height

                    Color(0.1, 1, 0.5, 1)
                    from kivy.graphics import Line
                    Line(rectangle=(x-dp(18), y-dp(18),
                                    dp(36), dp(36)))


class FFZITApp(App):

    def build(self):
        self.arena = Arena()
        self.aim = AimTrainer(self.arena)
        self.esp = ESPDemo(self.arena)

        root = BoxLayout(
            orientation="vertical",
            padding=dp(12),
            spacing=dp(10)
        )

        with root.canvas.before:
            Color(0.025, 0.025, 0.035, 1)
            from kivy.graphics import Rectangle
            self.bg = Rectangle(pos=root.pos, size=root.size)

        root.bind(pos=lambda o, v: setattr(self.bg, "pos", v))
        root.bind(size=lambda o, v: setattr(self.bg, "size", v))

        root.add_widget(Label(
            text="[b]FFZIT LAB[/b]",
            markup=True,
            font_size="28sp",
            size_hint_y=None,
            height=dp(55)
        ))

        self.status = Label(text="ARENA DE TREINAMENTO")
        root.add_widget(self.status)

        root.add_widget(ArenaView(
            self.arena, self.aim, self.esp
        ))

        self.score = 0
        self.score_label = Label(text="PONTOS: 0")
        root.add_widget(self.score_label)

        aim_button = Button(text="AIM DEMO ON/OFF")
        aim_button.bind(on_release=self.toggle_aim)
        root.add_widget(aim_button)

        esp_button = Button(text="ESP ON/OFF")
        esp_button.bind(on_release=self.toggle_esp)
        root.add_widget(esp_button)

        reset_button = Button(text="NOVOS ALVOS")
        reset_button.bind(on_release=self.reset)
        root.add_widget(reset_button)

        return root

    def toggle_aim(self, instance):
        self.aim.enable(not self.aim.enabled)
        self.status.text = (
            "AIM DEMO ATIVO"
            if self.aim.enabled else "AIM DEMO DESATIVADO"
        )

    def toggle_esp(self, instance):
        self.esp.enabled = not self.esp.enabled

    def reset(self, instance):
        self.arena.reset()
        self.status.text = "ARENA REINICIADA"


if __name__ == "__main__":
    FFZITApp().run()
  
