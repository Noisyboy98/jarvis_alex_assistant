import utils
import config
import datetime

class Time:

    def launch(self):
        now = datetime.datetime.now()
        midday = 'Am' if now.time() < datetime.time(12) else 'Pm'
        utils.speak(self.response .format(minute = now.minute,hour = now.hour,midday=midday,day = now.day,month = now.month,dateMonthName = now.strftime("%d %B"), year= now.year))