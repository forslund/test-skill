from mycroft import MycroftSkill, intent_file_handler


class TestMsk(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('test1.intent')
    def handle_msk_test(self, message):
        self.speak_dialog('test1')

    @intent_file_handler('test2.intent')
    def handle_msk_test2(self, message):
        self.speak_dialog('test2')

    @intent_file_handler('test3.intent')
    def handle_msk_test3(self, message):
        self.speak('test3')

    @intent_file_handler('test4.intent')
    def handle_msk_test4(self, message):
        self.speak('test4')

def create_skill():
    return TestMsk()

