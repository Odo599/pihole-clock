def check_events(buttons):
    for event in buttons.poll():
        print(event.name, event.type)