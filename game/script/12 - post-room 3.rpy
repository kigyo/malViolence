default route = "neutral"
default most_explored = 1

label post_room_3:
    $Achievement.add(achievement_room3)
    "(Huh. The screen above you didn't turn on.)"
    "(...Guess Cautionne really was serious about the whole \"silent treatment\" thing.)"

    if len(room3["investigated"]) == 10: #TODO: fix amount
        "(Well, you did what he asked you to do, right? You solved his puzzle.)"
        "(You've been over the whole room with a fine comb.)"
        "(And you haven't overlooked or {i}looked away{/i} from anything.)"
        "(There's not much left you can do. Time to move forward.)"
    elif len(room3["investigated"]) == 0:
        "(Good. You must be getting close to the end.)"
        "(No time to waste, then. Remember your training, follow protocol and go finish this.)"
    else:
        "(The way should be clear now.)
        (You could look around a while longer...)"
        "(...But chances are high you won't like whatever else you find.)"
        "(Better keep moving.)"

    scene bg corridor_exit at bg with wipeleft
    "(Looks like there're no screens in this corridor. You don't think you'll see any of Dr. Danger either.)"
    "(...There really isn't much else to say about this hall.)"
    "(If that's the case, then... this is probably close to the exit.)"

    #TODO: "Ending calculator"
    #TODO: "Most explored calculator"

    if route == "spare":
        pause
        "(...To be honest, the lack of nasally jabbering... kinda puts you on edge.)"
        "(Not that you {i}liked {/i}that brat who trapped you in a room with lethal puzzles and called you a lab rat.)"
        "(But the silence forces you to focus on something much louder and much more disturbing. Thoughts that've collapsed in your mind like juices from a rotting apple.)"
        "(You think about Dr. Dan – no.{i} Dr. Deidre Destrange.){/i}"
        "(You think about the results of your investigation.)"
        "(And you think about yourself: a tiny cog in a massive machine. A sleek, pristine, reliable machine - carefully cleansed of the blood it's spilt.)"
        "(A deep, dark pit hollows your stomach.)"
        "(Slowly, you make your way forward – each step heavier than the last.)"
        jump spare_ending

    elif route == "spare":
        "(Can't say you miss his nasally jabbering.)"
        "(And yet... you'd take it over the strange, baleful unease that hums at the back of your mind. Like the \"silent\" air conditioner in your boss's office.)"
        "(It's not about your job. You did what you were supposed to"
        "(No, rather... you're bothered about the evidence itself.)"

        if most_explored == 1:
            "(But why? All you remember are torture instruments and strange hobbies. Nothing out of the ordinary for a villain.)"
            pause 1
            "(...Maybe you'll chew on it another day.)"
            "(For now though, your priority is getting out of here.)"
        elif most_explored == 2:
            "(Maybe it was those blueprints. Or that corkboard.)"
            "(Yeah... they were pretty scary, weren't they?)"
            "(No wonder you've got goosebumps. Even if Dr. Danger's dead and gone, Cautionne's more than capable of taking her place. You've seen it for yourself.)"
            "(There's no time to lose. Better hurry back to HQ.)"
        else:
            "(You can't say you're surprised about what you've learned.)"
            "(STOP's public image always felt a bit {i}too {/i}pristine to you. Nowadays, shady, behind-the-scenes stuff is par for the course for big security organizations.)"
            "(No. What {i}bothers {/i}you is your future.)"
            "(If evidence of STOP's crimes goes public, your boss'll {i}definitely{/i} fire you.)"
            "(You'll lose a decent salary. Your 401k. Your tiny, cozy studio apartment.)"
            "(And though you were never fond of your job... you quite liked your stable, boring life.) "
            "(Guess that's another reason to get out of here.)"
            "(Someone else will deal with the problem. You'll get a fat raise, and pretend it never happened.)"
        jump neutral_ending

    else:
        "({i}Finally. {/i}You're tired of that brat's antics.)"
        "(Yeah, you didn't do your job properly. But in your position – who would?)"
        "(With a little grovelling and brown-nosing, you'll be back to your usual routine: handing locked suitcases to labs and giving your boss his 3 o'clock coffee.)"
        "(Besides, STOP'll send a better agent in your place. A capable one: one who'll slurp up information like the fruit smoothies you get for lunch.)"
        "(But not you. Never you. You just came here for the bonus pay.)"
        pause 1
        "(Alright, “agent”. Get going already.)"
        "(You've got a lair break out of.)"
        jump kill_ending