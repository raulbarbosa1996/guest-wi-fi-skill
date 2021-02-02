from mycroft import MycroftSkill, intent_file_handler


class GuestWiFi(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('fi.wi.guest.intent')
    def handle_fi_wi_guest(self, message):
        self.speak_dialog('fi.wi.guest')


def create_skill():
    return GuestWiFi()

