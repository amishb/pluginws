from Dashboard.common import DashPlugin
from datetime import datetime


class Time(DashPlugin):
    def __init__(self):
        super(Time, self).__init__()
        self.author = 'Amish Bhadeshia'
        self.version = '0.1'
        self.description = 'Prints current date and time'

    def _content(self):
        return {
            'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }