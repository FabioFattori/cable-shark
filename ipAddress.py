import requestError
import pinger
import threading
import time
class ipAddress:
    def __init__(self, ip, old_state=requestError.res[2]):
        self.ip = ip
        self.old_state = old_state
        self.timer = time.time()

    def __get_ip__(self):
        return self.ip
    
    def __get_state__(self):
        return self.old_state
    
    def pingMe(self):
        response = pinger.ping_ip(self.ip)
        self.old_state = response[0]
        print(response[1])
        return response[1]
    
    def automaticPing(self):
        #create a thread for ping operation
        ping_thread = threading.Thread(target=self.pingMe, args=())
        ping_thread.start()
        #wait for 5 seconds before pinging the ip again
        print("pinging")
        threading.Timer(5,self.automaticPing).start()