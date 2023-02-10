import time


def invoke_later(fn, ms):
    pass


# invoke_later_wrapper(fn, ms)

invoke_later(print("world"), 400)
invoke_later(print("world"), 400)
invoke_later(print("hjh"), 5)

function_call_queue = []


def calculate_time_to_execute(ms):
    return (round(time.time() * 1000)) + ms


def invoke_later_wrapper(fn, ms):
    function_call_queue.append((fn, calculate_time_to_execute(ms)))
    call_next()


def call_next():
    _, next_ms = function_call_queue[0]

    invoke_later(handle_current, next_ms)


def handle_current():
    fn, _ = function_call_queue.pop(0)
    call_next()
    fn()
