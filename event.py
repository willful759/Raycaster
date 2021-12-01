subscribers = {}

def subscribe(event, callback):
    if event not in subscribers:
        subscribers[event] = [callback]
    else:
        subscribers[event].append(callback)

def broadcast(event, *data):
    if not event in subscribers:
        return
    for callback in subscribers[event]:
        callback(*data)
