day4morning:
    play music rainsong
    set_screen blank
    "You wake to a gruesomely cold morning."
    "Rain is thundering down on the roof. Some drips in through cracks, though you find yourself dry; just chilly."
    "You pull on Hornet's coat."
    "It takes you a moment to spot her. She must have rolled around a bit."
    if (> $data.tensionPoints 3):
        "You wake her, perhaps more roughly than is really warranted. As she stirs, you climb to the hole, and peek outside."
    else:
        "You wake her with a gentle nudge. As she stirs, you climb to the entrance."
    set_screen end1
    "It's a torrent outside. Puddles have gathered in the great clefts that marr the path, rivulets are washing the caked dust from the trees and underbrush into the path, and into the river."
    "You pull Hornet's coat over your head and peek outside. The river is swelling, the surface a grey broiling torrent, looking more like mud than water."
    choice:
        "When you duck back in, Hornet is yawning."
        "'Good morning.":
            if (> $data.tensionPoints 3):
                talk em talk "Morning."
                talk hrn talk "Nnnrhg."
                "She clutches her head, in apparent pain."
                talk hrn talk "Bad... dreams."
                talk em talk "You'll be fine. Let's eat."
                talk hrn talk "No, I..."
                "Something is wrong. You feel annoyed."
                talk em talk "What is it?"
                talk hrn talk "I feel... sick. Give me a moment."
            else:
                talk em talk "Good morning. Are you alright?"
                talk hrn talk "Nnnnh. No... Bad dreams..."
                "She rubs her temples, frowning."
                "You think back to your own dream... What was it again..?"
                talk em talk "Do you need anything?"
                "You crouch down by her."
                talk em talk "We should get some food..."
                talk hrn talk "N-no. I feel a bit sick, no food for me..."
    "She takes her green sweater off. She has a dark shirt on underneath."
    "There's the slightest bad smell about her. Something is... off."
    talk hrn talk "I feel... warm."
    talk em talk "Is it fever?"
    talk hrn talk "Dunno... Don't think so..."
    "She groans, and gets to her feet, swaying a little."
    talk hrn talk "Just... We have to, keep moving. Do you mind eating later?"
    talk em talk "No, but..."
    talk hrn talk "Trust me, Emily, I just... need to move on. This place is..."
    "She shakes her head, and picks up her backpack."
    talk em talk "At least take your jacket back!"
    "You move to pull an arm free."
    if (> $data.tensionPoints 3):
        talk hrn talk "Keep... The jacket."
        "She hisses. She seems suddenly annoyed."
        talk hrn talk "Keep my scarf for all I care. Come on."
    else:
        talk hrn talk "Keep the jacket, Hornet."
        "She smiles, though it looks slightly pained."
        talk hrn talk "I just... Need to cool down."
    "You're not sure about this. But you follow her outside all the same, after hurriedly stuffing your pillow in your suitcase."

    "The rain is horrible. It is very cold, and passing under leaves means much of it is chalky with that dust."
    "You can't see further than a few feet, and it's certainly not weather for easy conversation."
    "You almost sink back into a stupor, plodding on, feeling the rain ruin your hair. You should have brought a raincoat. Or an umbrella..."
    if (> $data.tensionPoints 5):
        talk pa talk "You have both those in the City."
        talk pa talk "A full covered balcony terrace made from ceramic glass, even... If you want it."
    "A sudden gasp tears you from your thoughts."
    talk em talk "What is it?"
    choice:
        talk hrn talk "M-my arm..."
        "(Take a look)":
            "You trudge to her side, and lean in."
            set_screen end2
            "There's a black... mark..? Growing about her wrist. It's splotchy and indistinct."
            talk hrn talk "My... fingers are stiff..."
            "She tries to wriggle them, to demonstrate. The ring and little finger barely move at all."
            "There's an evil smell coming from this... wound. Whatever it is."
            talk em talk "Do you want to turn back..?"
            "You sound unsure, you know."
            talk hrn talk "No... It's fine, I think..."
            "She sounds half delirious. But when you push the issue, she just shakes her head."
            talk hrn talk "We need to get. Away."
            talk hrn talk "...the City."
            talk em talk "If you're sure, Hornet."
            "You stick to her side as you keep on."
        "(Ignore her)":
            "You ignore her, remembering how she reacted to your own cut."
            add data.tensionPoints 1
            add data.score -1
            "After a moment, you can hear her join you in walking again."
    set_screen end1
    "..."
    "Time stretches on. There's nothing to see but a thick wall of rain."
    "You're cold to the bone."
    "A sudden splash wakes you up. You turn to see, and-"
    set_screen end3
    play music hornet
    "Hornet is standing there, dazed. Her arm is lying in a puddle on the floor."
    "Her backpack is gone. You rush to her side."
    "Your dream... Did your dream do this...? Your belly is full of guilt all of a sudden."
    talk hrn talk "Emily. I'm... I'm feeling very, dizzy..."
    "You rush to the side. The rest is a blur."
    set_screen blank
    "You help her back to the ruin. You leave the arm in the dirt, not wanting to touch it. Her stump is dark too, and a similar discolouration creeps up her other arm."
    "Rain is running in rivulets down her body. When you come across her backpack, you swing it over your shoulders, still supporting the shorter woman."
    "Hornet's breath comes out in great clouds, her forehead and body steaming in the cold air."
    "It seems like forever until the ruin finally swims up out of the rain again. You find the hole, and bring her inside."
    jump day4noon