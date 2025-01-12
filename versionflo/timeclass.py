# class timeclass.py

#===============
# CLASS: Time
#===============

class Time:
    main_hour = 0
    max_hour = 23
    max_second_minute = 59
    '''
    Represents a clock with hours, minutes, and seconds.
    Provides functionality to increment time and convert it to seconds.
    '''
    
    def __init__(self, hour, minute, second, format="24h"):
        '''Initializes the time with hour, minute, second, and format.'''
        self.hour = hour
        self.minute = minute
        self.second = second
        self.format = format

    def in_seconds(self):
        '''Converts the time into total seconds.'''
        return self.hour * 3600 + self.minute * 60 + self.second

    def increment_time(self):
        '''Increments the time by one second.'''
        total_seconds = self.in_seconds() + 1  # Add one second
        total_seconds %= 86400  # Modulo to keep it within a 24-hour day
        self.hour, rem = divmod(total_seconds, 3600)  # Recalculate hour
        self.minute, self.second = divmod(rem, 60)  # Recalculate minute and second

    def __str__(self):
        '''Returns a string representation of the time in the selected format.'''
        if self.format == "24h":
            return f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}"
        else:
            period = "AM" if self.hour < 12 else "PM"
            hour = self.hour % 12 or 12  # Convert to 12-hour format
            return f"{hour:02d}:{self.minute:02d}:{self.second:02d} {period}"  # 12-hour format with AM/PM


#=============== 
# CLASS: Alarm 
#===============

class Alarm(Time):
    """
    Represents an alarm clock that extends the functionality of Time.
    Includes an enabled flag and a maximum display duration for the alarm sound.
    """

    max_display = 10  # Max display time for alarm in seconds
    
    def __init__(self, hour, minute, second, format, enabled=False):
        """
        Initialize an Alarm object.
        :param hour: Hour the alarm is set to.
        :param minute: Minute the alarm is set to.
        :param second: Second the alarm is set to.
        :param format: Time format ('12h' or '24h').
        :param enabled: Boolean indicating whether the alarm is active.
        """
        super().__init__(hour, minute, second, format)  # Inherit attributes from Time class
        self.enabled = enabled  # Indicates if the alarm is enabled

    def __str__(self):
        '''Returns a string representation of the alarm.'''
        if self.enabled:
            return f"Alarm: {super().__str__()}"
        else:
            return ""
        

