from kivy.app import  App
from kivy.uix.boxlayout import BoxLayout
import subprocess
from kivy.clock import Clock


class HeadsetControlApp(BoxLayout):
    def __init__(self):
        super(HeadsetControlApp, self).__init__()
        self.disable_led()
        Clock.schedule_once(lambda dt: self.refresh_batery())
        Clock.schedule_interval(lambda dt: self.refresh_batery(), 3)

    def disable_led(self):
        try:
            subprocess.check_output("headsetcontrol -l 0", shell=True)
        except:
            self.ids.bateria.text = 'Headset desligado'.title()
        finally:
            self.ids.estado.text = 'Desligado'

    def enable_led(self):
        try:
            subprocess.check_output("headsetcontrol -l 1", shell=True)
        except:
            self.ids.bateria.text = 'Headset desligado'.title()
        finally:
            self.ids.estado.text = 'Ligado'

    def refresh_batery(self):
        try:
            output = str(subprocess.check_output("headsetcontrol -b", shell=True)).lower()
            if 'charging' in output:
                output = 'Carregando'
            else:
                pos = output.find('%')
                output = output[pos - 3:pos + 1].strip()
            self.ids.bateria.text = str(output)
        except:
            self.ids.bateria.text = 'headset desligado'.title()
            self.ids.bateria.font_size = '30sp'




class Window(App):
    def build(self):
        return HeadsetControlApp()


Window().run()
