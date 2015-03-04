from Dashboard.common import DashPlugin


class BaseModule(DashPlugin):
    def __init__(self):
        super(BaseModule, self).__init__()

    def _content(self):
        return {
            'ipaddcress': 'jfdfoy'
        }