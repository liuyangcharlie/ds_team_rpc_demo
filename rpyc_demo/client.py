import rpyc
import threading

def connect_and_call():
    c = rpyc.connect("172.17.0.2", 18861)
    print(c.root.get_answer())

t = threading.Thread(target=connect_and_call)
t.start()
print('client start...')
input('any key')
