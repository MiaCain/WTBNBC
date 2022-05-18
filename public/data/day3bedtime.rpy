day3bedtime:
    clear_dialog
    set_screen river4
    #MISSING
    "Emily and Hornet reach an old industrial ruin. They agree it'll make a good place to sleep."
    set_screen river5
    #MISSING
    "Inside it is old graffiti that says:"
    "'AL L THIS LOVE/"
    "ON ASH CHOKED'"
    $if this.data.score > 2:
        set_screen river6a
        "Hornet and Emily fall asleep next to each other."
        jump opener3
    else:
        $if this.data.tensionPoints > 5:
            set_screen river6c
            "Hornet doesn't even speak before she goes to bed across the room. Emily lies awake for a long time."
            jump opener3
        else:
            set_screen river6b
            "Hornet and Emily get to bed on the floor. Emily lies awake for a while."
            jump opener3