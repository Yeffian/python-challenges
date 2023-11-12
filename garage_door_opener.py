from enum import Enum

class DoorState(Enum):
    CLOSED = 0
    OPENING = 1
    OPENED = 2
    CLOSING = 3
    PAUSED_WHILE_OPENING = 4
    PAUSED_WHILE_CLOSING = 5

def garage_door(input):
    paused = False
    state = DoorState.CLOSED

    for event in input.splitlines():
        print(f'Door: {state}')
        print(event)

        if event == 'button_clicked':
            if state is DoorState.CLOSED:
                state = DoorState.OPENING
            elif state is DoorState.OPENED:
                state = DoorState.CLOSING
            elif state is DoorState.CLOSING and paused is False:
                state = DoorState.PAUSED_WHILE_CLOSING
            elif state is DoorState.OPENING and paused is False:
                state = DoorState.PAUSED_WHILE_OPENING
            elif state is DoorState.CLOSING and paused is True:
                state = DoorState.PAUSED_WHILE_CLOSING
                paused = False
            elif state is DoorState.OPENING and paused is True:
                state = DoorState.PAUSED_WHILE_OPENING
                paused = False
            elif state is DoorState.PAUSED_WHILE_CLOSING:
                state = DoorState.OPENING
            elif state is DoorState.PAUSED_WHILE_OPENING:
                state = DoorState.CLOSING
        elif event == 'cycle_complete':
            if state is DoorState.OPENING:
                state = DoorState.OPENED
            elif state is DoorState.CLOSING:
                state = DoorState.CLOSED
        


    
commands = """
button_clicked
cycle_complete
button_clicked
button_clicked
button_clicked
button_clicked
button_clicked
cycle_complete
"""
garage_door(commands)
