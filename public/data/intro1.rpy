intro1:
    set_screen intro1
    clear_dialog
    "The two of you have come a long way. All the way to Peele Station, the final stop on the West Line."
    "The night is bitter, bitter cold. Emily shakes a little. You wonder again why she didn't bring a warmer coat."
    choice:
        talk em talk "Is this it?"
        "I suppose so.":
            jump test
        "It can't be!":
            "Emily thinks for a moment."
            talk em talk "Yes. We need to keep going. Let's get out of dodge."
            "She points at a videocamera. It's trained at the tracks. Her arm is pale."
test:  
    clear_dialog
    talk em talk "I don't want it to be. We have to keep going! Look!"
        "She points at a videocamera. It's trained at the tracks. Her arm is pale."
        talk em talk "They'll know we're here by the morning, Hornet!"
        choice:
            talk hrn talk "We have to keep going then."
            "Why didn't you bring a warmer jacket?":
                talk hrn talk "In fact, why didn't you bring ANY jacket?"
                "Emily scowls."
                talk em talk "You told me to dress warm. This is a warm dress."
                talk em talk "Besides, I like the colour."
            "Should we find a road?":
                "test LOL"
            