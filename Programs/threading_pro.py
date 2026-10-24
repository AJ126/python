import threading

thread = threading.current_thread()

print('Thread object:', thread)
print('Thread name:', thread.name)
print('Thread ID:', thread.ident)

class mythread(threading.Thread):
    def run(self):
        for i in range(11):
            print('child thread: ', i)

t = mythread()
t.start()
