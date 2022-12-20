from fsm import TocMachine

def create_machine():
    machine = machine = TocMachine(
    states=["user", "lobby", "state1", "state2"],
    transitions=[
        {
            "trigger": "advance",
            "source": "user",
            "dest": "lobby",
            "conditions": "is_going_to_lobby",
        },
        {
            "trigger": "advance",
            "source": "lobby",
            "dest": "state1",
            "conditions": "is_going_to_state1",
        },
        {
            "trigger": "advance",
            "source": "lobby",
            "dest": "state2",
            "conditions": "is_going_to_state2",
        },
        {"trigger": "go_back", "source": ["state1", "state2"], "dest": "lobby"},
    ],
    initial="user",
    auto_transitions=False,
    show_conditions=True,
)

    return machine;