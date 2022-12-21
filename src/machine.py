from fsm import TocMachine

def create_machine():
    machine = machine = TocMachine(
    states=["user", "lobby", "show_current", "show_old"],
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
            "dest": "show_current",
            "conditions": "is_going_to_show_current",
        },
        {
            "trigger": "advance",
            "source": "lobby",
            "dest": "show_old",
            "conditions": "is_going_to_show_old",
        },
        {"trigger": "go_back", "source": ["show_current", "show_old"], "dest": "lobby"},
    ],
    initial="user",
    auto_transitions=False,
    show_conditions=True,
)

    return machine