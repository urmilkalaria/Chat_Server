import OneOnOne_Server
import Mserver
import threading

thread1 = threading.Thread(target=OneOnOne_Server.run)
thread1.start()
print("one on one server started")
thread2 = threading.Thread(target=Mserver.run)
thread2.start()
print("Chat room started")
