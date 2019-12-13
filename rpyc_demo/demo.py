import rpyc
import threading

from rpyc.utils.server import ThreadedServer

class MyService(rpyc.Service):
    def on_connect(self, conn):
        # code that runs when a connection is created
        # (to init the service, if needed)
        print('on_connect...')
        pass

    def on_disconnect(self, conn):
        # code that runs after the connection has already closed
        # (to finalize the service, if needed)
        print('on_disconnect...')
        # terminate threads of connection, or threads would terminate when the client stops
        pass

    def exposed_get_answer(self): # this is an exposed method
        print('Total number of threads', threading.activeCount())
        return 42

    exposed_the_real_answer_though = 43     # an exposed attribute

    def get_question(self):  # while this method is not exposed
        return "what is the airspeed velocity of an unladen swallow?"


if __name__ == "__main__":
    print('before')
    t = ThreadedServer(MyService, hostname='0.0.0.0', port=18861)
    thread = threading.Thread(target=t.start)
    thread.start()
    print('Total number of threads', threading.activeCount())
    print('server start...')