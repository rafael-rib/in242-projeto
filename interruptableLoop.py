"""
    Use to create a permanent loop that can be stopped ...

    ... from same terminal where process was started and is running in foreground:
        CTL-C

    ... from same user account but through a different terminal
        $ kill -2 <pid>
        or $ kill -s SIGINT <pid>

"""
import signal
import time
from datetime import datetime as dtt
__all__=["InterruptableLoop",]
class InterruptableLoop:
    def __init__(self,intervalSecs=1,printStatus=True):
        self.intervalSecs=intervalSecs
        self.shouldContinue=True
        self.printStatus=printStatus
        self.interrupted=False
        if self.printStatus:
            print ("CTL-C to stop\t(or $kill -s SIGINT pid)")
        signal.signal(signal.SIGINT, self._StopRunning)
        signal.signal(signal.SIGQUIT, self._Abort)
        signal.signal(signal.SIGTERM, self._Abort)

    def _StopRunning(self, signal, frame):
        self.shouldContinue = False

    def _Abort(self, signal, frame):
        raise

    def ShouldContinue(self):
        time.sleep(self.intervalSecs)
        if self.shouldContinue and self.printStatus:
            print( ".",end="",flush=True)
        elif not self.shouldContinue and self.printStatus:
            print ("Exiting at ",dtt.now())
        return self.shouldContinue