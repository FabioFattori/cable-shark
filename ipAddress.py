import requestError
import pinger
class ipAddress:
    def __init__(self, ip, old_state=requestError.res[2]):
        self.ip = ip
        self.old_state = old_state

    def __get_ip__(self):
        return self.ip
    
    def __get_state__(self):
        return self.old_state
    
    def pingMe(self):
        response = pinger.ping_ip(self.ip)
        self.old_state = response[0]
        print(response[1])
        return response[1]