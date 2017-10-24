from ee import EventEmitter


ee = EventEmitter()


def add_print():
    print("aaa")


def add2_print():
    print("#"*30)


def add3_print():
    print("bbb")

ee.emit('print')

ee.on('print', add_print)
ee.on('print', add2_print)
ee.prepend_listener('print', add2_print)
ee.once('print', add3_print)


ee.emit('print')
ee.emit('print')

ee.remove_listener('print', add2_print)
ee.emit('print')

ee.on('sum', lambda x, y: print(str(x+y)))

ee.emit('sum', 5, 10)