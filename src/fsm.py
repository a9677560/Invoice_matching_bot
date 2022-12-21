from transitions.extensions import GraphMachine

from utils import send_text_message
from invoice import sendUse, showCurrent, showOld

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_lobby(self, event):
        text = event.message.text
        return True

    def is_going_to_show_current(self, event):
        text = event.message.text
        return text == "當期號碼"

    def is_going_to_show_old(self, event):
        text = event.message.text
        return text.lower() == "前期號碼"

    def on_enter_lobby(self, event):
        print("I'm entering lobby")

        reply_token = event.reply_token
        send_text_message(reply_token, sendUse())

    def on_enter_show_current(self, event):
        print("I'm entering show current")

        showCurrent(event);
        self.go_back()

    """
    def on_exit_state1(self):
        print("Leaving state1")
    """

    def on_enter_show_old(self, event):
        print("I'm entering show old")

        showOld(event);
        self.go_back()
