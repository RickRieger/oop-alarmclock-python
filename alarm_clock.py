
class AlarmClock:

    def __init__(self):
        self.current_time = '12:00pm'
        self.alarm_is_on = False
        self.time_alarm_is_set_to = '4:30am'

    def set_time(self, time):
        self.current_time = time
        print(f'The current time is now {self.current_time}')    

    def set_alarm(self, time):
        self.time_alarm_is_set_to = time
        print(f'The alarm is now set to: {self.time_alarm_is_set_to}')    

    def toggle_alarm(self):
        if self.alarm_is_on == False:
            self.alarm_is_on = True
            print(f'The alarm is on!')    
        else: self.alarm_is_on = False    
        print(f'The alarm is off!')    
