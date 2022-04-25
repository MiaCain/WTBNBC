day1forest_offramp:
    set_screen blank
    "The night feels especially cold now that you're off the pathway."
    choice:
        "The rattling of Emily's trunk has been replaced by a dull thumping as it bounces over dusty ground and uneven wild grasses."
        "('I still can't believe you didn't just bring a backpack.')":
            #MISSING
            set DATA.OR.bagmention true
            add DATA.tensionPoints 1
            jump day1forest_cityview
        "(Ignore it)":
            set DATA.OR.bagmention false
            "You decide to let her be, and keep walking for a little while longer."
            jump day1forest_cityview


day1forest_cityview:
    "You approach a rise, and then, cresting it, are greeted with..."
    set_screen offramp3
    talk hrn talk "The City."
    talk em talk "It looks so tiny from here..."
    "You couldn't disagree more. It fills the entire horizon. It's dead night, but the City still glows in angry neon, screeching at the sky. You can hear the traffic from here."
    "The tracks of the railway head towards where you departed. Along it, the inner city fades into crowded suburbs, which eventually dissolve altogether."
    "Not so in the other directions; hills upon hills reach out into the darkness, grids of electric light imposed upon them by the metropole."
    "It seems so vast. Will you ever leave it?"
    talk hrn talk "Do you know how big it is?"
    "She shrugs."
    talk em talk "On paper. Did you not learn in school?"
    talk hrn talk "..."
    "You watch the city for a minute."
    choice:
        talk em talk "What does it make you feel?"
        "('Nothing')":
            set DATA.OR.cityfeeling 0
            talk hrn talk "Nothing. We're getting out, that's what matters. It's just buildings and neon now."
            talk em talk "What about the people?"
            choice:
                "She seems put off."
                "(Shrug and move on)":
                    jump day1forest_trees
        "('Sadness')":
            set DATA.OR.cityfeeling 1
            talk hrn talk "Sad, I suppose. Lots of... bad stuff in there."
            talk hrn talk "All those empty buildings, all that bad air..."
            "Emily frowns a little at your answer."
            talk em talk "Ah, I see."
            "You decide to move on."
            jump day1forest_trees
        "('Nostalgia')":
            set DATA.OR.cityfeeling 2
            add DATA.tensionPoints -1
            talk hrn talk "I don't know. Despite all of it, we..."
            talk hrn talk "We had some nice times here, you know?"
            talk hrn talk "Even though I'm glad we're getting out."
            "She smiles warmly."
            talk em talk "I think so too. It'll always be our City."
            "The thought isn't that appealing to you, but you decide to move on."
            jump day1forest_trees
        "('Hate')":
            set DATA.OR.cityfeeling 3
            add DATA.tensionPoints 1
            talk hrn talk "Bad. Fuck this place. Fuck everything it's done to us."
            "She looks shocked."
            talk em talk "I-"
            talk hrn talk "Fuck everthing it's done to ME, at least. I hope I never see it again."
            "Emily can't think of anything to say, it seems. Her eyes shine with the sky's orange tint."
            talk hrn talk "Let's go."
            jump day1forest_trees

day1forest_trees:
    set_screen blank
    "The city is still reeling through your head. Thinking about it, you remember a slogan sprayed on a concrete wall by the canal off of Metternich Square. It said..."
    "'IT'S KILLED AL L OF IT/"
    "EVEN THE STARS'"
    "Whoever wrote it wasn't wrong. There isn't a single star visible tonight. Even the moon, which you've seen on a good night now and then when getting streetfood with coworkers after a late shift, is nowhere at all. It feels dreadful."
    "You suppose the City was never as bad for Emily as it was for you, in her family's polyceramic high-rise. If it wasn't for the Section getting passed, she might never have-"
    set_screen forest1
    "You're startled to find yourself amidst the trees already. It's gotten darker, but the wind is almost gone now, beyond the quiet rustling of the pines far above."
    "The ground is littered with needles, most of them grey and brown. No grass or underbrush grows here."
    choice:
        "Emily shivers."
        "(Offer her your coat, quietly)":
            $if this.DATA.OR.bagmention:
                
        "(Ask if she wants to borrow your coat)":
        "(Ignore her)":

