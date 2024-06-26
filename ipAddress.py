import requestResponsens
import pinger
import threading
import graphicAddAndUpdate
import time
class ipAddress:
    def __init__(self, ip, old_state=requestResponsens.res[2]):
        self.ip = ip
        self.old_state = old_state
        self.automaticPingThread = None

    def __get_ip__(self):
        return self.ip
    
    def __get_state__(self):
        return self.old_state
    
    def stopPing(self):
        #stop the thread
        self.automaticPingThread.cancel()
        return
    
    def pingMe(self,lock):
        with lock:
            response = pinger.ping_ip(self.ip)
            self.old_state = response[0]
            print(response[1])
            print("current state : ",self.old_state)
            #print the response and the state in the log.txt file
            with open("log.txt","a") as file:
                file.write(self.__get_ip__()+"\n")
                file.write("current state : "+self.__get_state__()+"\n")    
        return
    
    def automaticPing(self,manager,ip_addresses,lock):
        #create a thread for ping operation
        ping_thread = threading.Thread(target=self.pingMe, args=(lock,))
        ping_thread.start()
        #wait for 5 seconds before pinging the ip again
        print("pinging")
        self.automaticPingThread=threading.Timer(10,self.automaticPing,args=[manager,ip_addresses,lock])
        self.automaticPingThread.start()
        if self.ip == ip_addresses[len(ip_addresses)-1].__get_ip__():
            graphicAddAndUpdate.updateList(manager.getAll().ip_addresses_container,ip_addresses)