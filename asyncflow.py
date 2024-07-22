import threading, uuid, os

storage = {}
func_state = {}
func_result = {}

def asynchronous(func):
    func_id = str(uuid.uuid4())

    def wrapper(*args, **kwargs):
        func_result[func_id] = func(*args, **kwargs)
        func_state[func_id] = True

    def caller(*args, **kwargs):
        thread = threading.Thread(target=storage[func_id], args=args, kwargs=kwargs, daemon=False)
        thread.start()
        return func_id

    storage[func_id] = wrapper
    func_state[func_id] = False
    return caller


def wait(func_id):
    try:
        while not func_state[func_id]: pass
        return func_result[func_id]
    except (KeyboardInterrupt, SystemError, SystemExit) as e:
        raise e


def exit():
    os.kill(os.getpid(), 9)
