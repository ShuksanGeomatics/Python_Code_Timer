import time
class gTimer:
    '''A class to create different timers to track progress during script execution.'''
    def __init__(self):
        #Sets/stores the time the gTimer object is created...
        self.starttime = time.time()
        #Store the time in minutes between instantiation and the most recent elapsed() method call....
        self.elapsedtime = "not set, call elapsed() to set an interval time"
        #Store the time in minutes between instantiation and the last elapsed() method call....
        self.endtime = "not set, call elapsed to set an interval time"
        
    def print_start_time(self):
        #Converts the start time from seconds since the epoch to human time...
        print("Started on ",  time.asctime(time.localtime(self.starttime)))
        
    def elapsed(self):
        #Returns the  minutes from the gTimer object instantiation to when this method is called...
        #If the endTime method was called the timer is finished and this will return an error...
        if type(self.elapsedtime) == tuple:
            print("This timer was stopped at ", self.elapsedtime, "minutes")
        else:   
            self.elapsedtime = round((time.time() - self.starttime)/60,1)
            print(self.elapsedtime, "minutes")
            
    def print_end_time(self):
        #Converts the end time from seconds since the epoch to human time...
        #Calling this method freezed the endtime and elapsedtime
        if type(self.elapsedtime) == tuple:
            print("This timer was stopped at ", self.elapsedtime, "minutes")
        else:
            self.endtime = time.time() - self.starttime
            self.elapsedtime = round(self.endtime/60,1)
            print("Finished in ", self.elapsedtime, " minutes on ", time.asctime(time.localtime(time.time())))
            self.endtime = (self.endtime,)
            self.elapsedtime = (self.elapsedtime,)
            
            
##USE EXAMPLE            
#my_timer = gTimer()
#my_timer.print_start_time()
#my_timer.print_end_time()