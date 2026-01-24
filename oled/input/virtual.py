import time
import queue

HOLD_TIME = 0.7
REPEAT_TIME = None

class ButtonEvent:
    def __init__(self, name, type_):
        self.name = name
        self.type = type_
        self.timestamp = time.time()

class ButtonState:
    def __init__(self):
        self.pressed = False
        self.press_time = None
        self.hold_fired = False
        self.last_repeat = None

class ButtonManager:
    def __init__(self):
        self._queue = queue.Queue()
        self._states = {}

    def press(self, name):
        state = self._states.setdefault(name, ButtonState())
        if not state.pressed:
            state.pressed = True
            state.press_time = time.time()
            state.hold_fired = False
            state.last_repeat = None
            self._queue.put(ButtonEvent(name, "PRESS"))

    def release(self, name):
        state = self._states.setdefault(name, ButtonState())
        if state.pressed:
            state.pressed = False
            state.press_time = None
            state.hold_fired = False
            state.last_repeat = None
            self._queue.put(ButtonEvent(name, "RELEASE"))

    def poll(self):
        now = time.time()
        events = []

        for name, state in self._states.items():
            if not state.pressed:
                continue

            held_time = now - state.press_time

            if held_time >= HOLD_TIME and not state.hold_fired:
                state.hold_fired = True
                state.last_repeat = now
                events.append(ButtonEvent(name, "HOLD"))

            if (
                    REPEAT_TIME is not None
                    and state.hold_fired
                    and now - state.last_repeat >= REPEAT_TIME
            ):
                state.last_repeat = now
                events.append(ButtonEvent(name, "REPEAT"))

        while not self._queue.empty():
            events.append(self._queue.get())

        return events
