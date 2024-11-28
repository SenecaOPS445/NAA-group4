#!/usr/bin/env python3
# Student ID: rlamoste
class Time:
    """Simple object type for time of the day.
       data attributes: hour, minute, second
       function attributes: __init__, __str__, __repr__
                            time_to_sec, format_time,
                            change_time, sum_time
    """
    def __init__(self,hour=12,minute=0,second=0):
        """constructor for time object""" 
        self.hour = hour
        self.minute = minute
        self.second = second
    
    def format_time(self):
        """Return time object (t) as a formatted string"""
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'
 
    def sum_times(self, t2):
        """Add two time objests and return the sum."""
        """Change this to become object method for our Time object (refer to lab7c.py and change_time() method below)"""
        self_seconds = self.time_to_sec()
        new_seconds = t2.time_to_sec()
        sum = self_seconds + new_seconds
        
        return sec_to_time(sum)

    def change_time(self, seconds):
        time_seconds = self.time_to_sec()
        nt = sec_to_time(time_seconds + seconds)
        self.hour, self.minute, self.second = nt.hour, nt.minute, nt.second 
        return None

    def time_to_sec(self):
        '''convert a time object to a single integer representing the 
        number of seconds from mid-night'''
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    def valid_time(self):
        """check for the validity of the time object attributes:
        24 > hour > 0, 60 > minute > 0, 60 > second > 0 """
        if self.hour < 0 or self.minute < 0 or self.second < 0:
           return False
        if self.minute >= 60 or self.second >= 60 or self.hour >= 24:
           return False
        return True
    
    def __str__(self):
        """return a string representation for the object self"""
        return  f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'
    
    def __repr__(self):
        '''return a string representation for the object self'''
        '''just instead of ':', you are required use the '.'  in the formatting string.'''
        return  f'{self.hour:02d}.{self.minute:02d}.{self.second:02d}'
    
    def __add__(self, t2):
        """return the result by using sum_times() method"""
        return self.sum_times(t2)


def sec_to_time(seconds):
    '''convert a given number of seconds to a time object in 
       hour, minute, second format'''
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time
