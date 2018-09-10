from mycroft import MycroftSkill, intent_file_handler


class TestMsk(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('msk.test.intent')
    def handle_msk_test(self, message):
        self.speak_dialog('msk.test')


def create_skill():
    return TestMsk()

