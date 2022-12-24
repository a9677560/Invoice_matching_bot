from fsm import TocMachine

def create_machine():
    machine = machine = TocMachine(
    states=["lobby", "show_use", "show_current", "show_old", "match", "match1", "match2", "match3", "match0", "end_match", "second_match", "prize_match"],
    transitions=[
        {
            "trigger": "advance",
            "source": "lobby",
            "dest": "show_current",
            "conditions": "is_going_to_show_current",
        },
        {
            "trigger": "advance",
            "source": "lobby",
            "dest": "show_use",
            "conditions": "is_going_to_show_use",
        }, 
        {
            "trigger": "advance",
            "source": "lobby",
            "dest": "show_old",
            "conditions": "is_going_to_show_old",
        },
        {
            "trigger": "advance",
            "source": "lobby",
            "dest": "match",
            "conditions": "is_going_to_match",
        },
        {
            "trigger": "advance",
            "source": "match",
            "dest": "match1",
            "conditions": "is_going_to_match1",
        },
        {
            "trigger": "advance",
            "source": "match",
            "dest": "match2",
            "conditions": "is_going_to_match2",
        },
        {
            "trigger": "advance",
            "source": "match",
            "dest": "match3",
            "conditions": "is_going_to_match3",
        },
        {
            "trigger": "advance",
            "source": "match",
            "dest": "match0",
            "conditions": "is_going_to_match0",
        },
        {
            "trigger": "advance",
            "source": "match",
            "dest": "end_match",
            "conditions": "is_going_to_end_match",
        },
        {
            "trigger": "advance",
            "source": "second_match",
            "dest": "prize_match",
            "conditions": "is_going_to_prize_match",
        },
        {
            "trigger": "advance",
            "source": "prize_match",
            "dest": "match",
            "conditions": "is_going_to_back_match",
        },
        {
            "trigger": "advance",
            "source": "prize_match",
            "dest": "lobby",
            "conditions": "is_going_to_back_lobby",
        },                                                                              
        {"trigger": "go_back", "source": ["show_current", "show_old", "match0", "show_use", "second_match", "end_match"], "dest": "lobby"},
        {"trigger": "go_back_match", "source": ["match3"], "dest": "match"},
        {"trigger": "go_second_match", "source": ["match1", "match2"], "dest": "second_match"},
    ],
    initial="lobby",
    auto_transitions=False,
    show_conditions=True,
)

    return machine