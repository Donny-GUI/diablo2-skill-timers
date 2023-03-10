import threading
import time

class Timer:
    """ 
    Threaded Timer. Used by the skill slot class
    to keep track of the time that has passed 
    since this skill has been reset 
    """
    def __init__(self, duration_seconds: int):
        self.started = False
        self.ended = True
        self.duration = duration_seconds
        self.fps = 91/self.duration
        self.spf = self.duration/91
        self.thread_timer = threading.Thread(target=self.__start__)
        self.frame_index = -1
        self.running = False
    
    def start(self):
        """ starts the timer  """
        
        self.started = True
        self.ended = False
        self.thread_timer.start()
    
    def __start__(self):
        """ thread that is tied to the start method """
        
        duration = self.duration
        time_started = time.time()
        self.running = True
        while self.running:
            delta_time = time.time() - time_started
            
            self.frame_index = 91  - round(91/round(delta_time))
            if delta_time > duration:
                break
            
        self.started = False
        self.ended = True