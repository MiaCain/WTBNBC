day1bedtime:
    set_screen forest3
    play music empty
    "It's very hard to judge the time. You think maybe one or two in the morning, because even the roaring city seems quieter - though it could be the distance."
    "As the trees gradually grow wilder, more underbrush appears, and their neat rows become disorderly."
    "Suddenly, a huge irregular shape swims out of the darkness; the corpse of a long-dead tree, some elder of the forest, hollow and pale."
    "The bark is cracked and dry, and Pulmonaria grow by the dusty roots."
    talk em talk "That looks-"
    "She startles at a sudden yawn."
    $if this.data.score >= 1:
        "The poor darling needs her sleep..."
    talk em talk "-good. Good place to sleep. I think?"
    "You nod at her, already drawing closer."
    talk hrn talk "I don't think anyone will find us here, they don't come out here, not this deep out in the woods. We walked most of the night."
    "You take off your backpack and drop it between the roots."
    "Your shoulders ache."
    $if this.data.FORhasCoat:
        "Emily pushes her baggage next to yours, and peeks inside the hollow."
        talk em talk "It looks dry... Dirty though..."
        talk hrn talk "It's fine, you're wearing my coat anyway." 
        "She climbs inside. There's not that much room within, but you manage to sit down in the entrance anyway, leaning against her."
        jump day1bedtime_sleep
    "Emily pushes her baggage next to yours, and peeks inside the hollow."
    talk em talk "It looks dry... dirty though..."
    "You sigh, and begin taking off your coat."
    talk hrn talk "Fine, just, take it. You'll be warmer with it anyway."
    talk em talk "O-oh. That's a good idea!"
    "She slips it on, then climbs inside the hollow."
    "There's not room for both of you. You perch on the precipice, quietly annoyed. Did she never learn to say thank you?"
    $if this.data.OR.bagmention:
        add data.tensionPoints 1
        "Why didn't she bring a coat either? And that stupid trunk? There's a sour taste in your mouth. Maybe you really should have asked Cel if she wanted to..."
    jump day1bedtime_sleep


day1bedtime_sleep:
    play music sleeptime
    set_screen forest4
    "It feels good to finally rest a little. Your feet already ache a little; you can't imagine how Emily's must feel, in her stylish chitin-cyan boots."
    $if this.data.tensionPoints <= 2:
        choice:
            "Above you, the big dark coat stirs, and a pale hand slinks out, seeking your own. You reach up to grasp it lightly. You can hear Emily breathing, clearly exhausted."
            "'Good night, Emily.'":
                "You add a quiet 'Love you,' and she mumbles something in return, but you're not sure she heard you."
                jump day1dream
    "You feel yourself drifting off to sleep..."
    jump day1dream