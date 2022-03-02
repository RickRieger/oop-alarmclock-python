from alarm_clock import AlarmClock

my_clock = AlarmClock()

print(f'Hello, this is clock. ========> WE LOVE CLOCK!')
def run_application():
    print('====================CLOCK=====================')
    show_time_and_alarm()
    choice = input('What would you like to do?  a. Set time. b. Set alarm. c. Toggle alarm on or off. (a,b or c)    ')
    if choice == 'a':
        time = input('What time would you like to set the clock to? (enter a time followed by am or pm)     ')
        my_clock.set_time(time)
        run_application()
    elif choice == 'b':
        time = input('What time would you like to set the alarm to? (enter a time followed by am or pm)     ')
        my_clock.set_alarm(time)
        run_application()
    elif choice == 'c':
        my_clock.toggle_alarm()
        run_application()
    else:print('Please check your input!')    
    
def show_time_and_alarm():
    print(f'The current time is: {my_clock.current_time}')
    if my_clock.alarm_is_on == True:
        print(f'The alarm is on and set to go off at: {my_clock.time_alarm_is_set_to}')
    else: print('The alarm is not on!')



run_application()    