# record(order_id): adds the order_id to the log
# get_last(i): gets the ith last element from the log.

class Log_Size:
    def __init__(self,log_size):
        self.log=list()
        self.log_size=log_size

    def get_last_element(self,index):
        return self.log[-index]

    def record(self,order_id):
        self.log.append(order_id)

        if len(self.log)> self.log_size:
            self.log = self.log[1:]

l = Log_Size(5)
l.record(1)
l.record(2)
print(l.log)
l.record(3)
l.record(4)
l.record(5)
print(l.log)
print(l.get_last_element(2))
print(l.get_last_element(3))
l.record(6)
l.record(7)
l.record(8)
l.record(9)
print(l.log)
print(l.get_last_element(4))
print(l.get_last_element(1))



