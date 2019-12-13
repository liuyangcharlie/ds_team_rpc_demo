import rpyc

c = rpyc.connect("172.17.0.2", 18861)
c.root.get_answer()

