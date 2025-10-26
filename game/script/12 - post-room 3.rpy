default route = "neutral"
default most_explored = 1

init python:
    def inspection_sum():
        return len(room1_investigated) + len(room2_investigated) + len(room3_investigated)

    def inspector_achievement():
        if inspection_sum() >= 15:
            Achievement.add(achievement_investigate)

    def route_calculator():
        global route, most_explored
        if inspection_sum() < 6:
            route = "kill"
        elif inspection_sum() < 12 or len(room1_investigated) < 2 or len(room2_investigated) < 4 or len(room3_investigated) < 6:
            route = "neutral"
            most_explored = explored_ratio()
        else:
            route = "spare"
    
    def explored_ratio():
        rooms = [len(room1_investigated)/3, len(room2_investigated)/5, len(room3_investigated)/7]

        highest = 1
        highest_val = rooms[0]

        for i in range(len(rooms)):
            if rooms[i] > highest_val:
                highest_val = rooms[i]
                highest = i+1

        return highest


label post_room_3:
    $renpy.block_rollback()
    $ inspect = "post room"

    show screen room3_meta with None
    $ play_sound(roomsuccess)
    hide screen room3_meta with puzzle_hide

    stop music fadeout 1.0
    pause 2

    $puzzle_achievements()

    $ play_sound(doorunlock)
    pause 2

    "(Huh.{w} The screen behind you didn't turn on.)"
    "(...Guess Cautionne really was serious about the whole \"silent treatment\" thing.)"

    if len(room3_investigated) == 7:
        "(Well,{w=0.1} you did what he asked you to do,{w=0.1} right?{w} You solved his puzzles.)"
        "(You've been over the whole room with a fine comb.)"
        "(And you haven't overlooked or {i}looked away{/i} from anything.)"
        "(There's not much left you can do.{w} Time to move forward.)"
    elif len(room3_investigated) == 0:
        "(Good.{w} You must be getting close to the end.)"
        "(No time to waste,{w=0.1} then.{w} Remember your training,{w=0.1} follow protocol{w=0.1} and go finish this.)"
    else:
        "(The way should be clear now.)"
        "(You could look around a while longer...)"
        "(...But chances are high you won't like whatever else you find.)"
        "(Better keep moving.)"

    $ play_sound (footsteps3)
    $ queue_sound (footsteps3)

    scene bg room3_downstairs:
        zoom 0.335 align(0.0,0.0)
        ease 1 zoom 0.335 xalign 0.6 yalign 0.5 
        pause 1
        ease 7 xalign 0.8 yalign 0.6 zoom 1.2
    pause 9
    $ play_sound(dooropen)

    scene black with fade
    pause 2
    show bg corridor_exit with placeintro:
        zoom 0.8 xalign 0.0 yalign 0.5
        linear 20 xalign 1.0
    $ Achievement.add(achievement_room3)
    pause 3
    $ play_sound(doorclose)
    "(Looks like there are no screens in this corridor.{w} You don't think you'll see any of Dr. Danger either.)"

    show bg corridor_exit with dissolve:
        align (0.5,0.5) zoom 0.5
    pause 1
    "(...There really isn't much else to say about this hall.)"
    "(If that's the case, then...{w=0.5} this is probably close to the exit.)"

    $ route_calculator()

    if route == "spare":
        pause 1
        "(...To be honest,{w=0.1} the lack of nasally jabbering...{w=0.5} kinda puts you on edge.)"
        "(Not that you {i}like {/i}that brat who called you a lab rat and trapped you in several rooms with lethal puzzles.)"
        "(But the silence forces you to focus on something much louder and much more disturbing.{w} Thoughts that are only now coming to the forefront of your mind.)"
        "(You think about Dr. Dan —{w=0.5} no.{i} Dr. Deirdre Destrange.{/i})"
        "(You think about the results of your investigation.)"
        "(And you think about yourself:{w=0.5} a tiny cog in a massive machine.)"
        "(A sleek,{w=0.1} pristine,{w=0.1} reliable machine —{w=0.5} carefully cleansed of the blood it's spilt.)"
        "(A deep,{w=0.1} dark{w=0.1} pit hollows your stomach.)"
        $ play_sound(footsteps4)
        
        show bg corridor_exit:
            align (0.5,0.5) zoom 0.5
            ease 4 zoom 1.0 align(0.5,0.6)

        "(Slowly,{w=0.1} you make your way forward —{w=0.5} each step heavier than the last.)"

        pause 2
        jump spare_ending

    elif route == "neutral":
        "(Can't say you miss his nasally jabbering.)"
        if gui.text_size > 40:
            "(And yet...{w=0.5} you'd take it over that strange,{w=0.1} baleful{w=0.1} unease that hums at the back of your mind.)"
            "(Like the \"silent\" air conditioner in your boss's office.)"
        else:
            "(And yet...{w=0.5} you'd take it over that strange,{w=0.1} baleful{w=0.1} unease that hums at\nthe back of your mind.{w} Like the \"silent\" air conditioner in your boss's office.)"
        "(It's not about your job.{w} You did what you were supposed to.)"
        "(No,{w=0.1} rather...{w=0.5} you're bothered about the evidence itself.)"

        if most_explored == 1:
            "(But why?{w} All you remember are torture instruments and strange hobbies.{w} Nothing out of the ordinary for a villain.)"
            pause 1
            "(...Maybe you'll chew on it another day.)"
            "(For now though,{w=0.1} your priority is getting out of here.)"
            $ play_sound(footsteps4)
        elif most_explored == 2:
            "(Maybe it was those blueprints.{w} Or that corkboard.)"
            "(Yeah...{w=0.5} they were pretty scary,{w=0.1} weren't they?)"
            "(No wonder you've got goosebumps.{w} Even if Dr. Danger's dead and gone,{w=0.1} Cautionne's more than capable of taking her place.{w} You've seen it for yourself.)"
            "(There's no time to lose.{w} Better hurry back to HQ.)"
            $ play_sound(footsteps4)
        else:
            "(You can't say you're surprised about what you've learned.)"
            "(STOP's public image always felt a bit {i}too {/i}pristine to you.{w} Nowadays,{w=0.1} shady,{w=0.1} behind-the-scenes stuff is par for the course for big security organizations.)"
            "(No.{w} What {i}bothers {/i}you is your future.)"
            "(If evidence of STOP's crimes goes public,{w=0.1} your boss'll {i}definitely{/i} fire you.)"
            "(You'll lose a decent salary.{w} Your 401k.{w} Your tiny,{w=0.1} cozy{w=0.1} studio apartment.)"
            "(And though you were never fond of your job...{w=0.5} you quite liked your stable,{w=0.1} boring{w=0.1} life as is.) "
            "(Guess that's another reason to get out of here.)"
            "(Someone else will deal with the problem.{w} You'll get a fat raise,{w=0.1} and pretend it never happened.)"
            $ play_sound(footsteps4)
        jump neutral_ending

    else:
        "({i}Finally.{/i}{w} You're tired of that brat's antics.)"
        "(Yeah,{w=0.1} you didn't do your job properly.{w} You certainly didn't take advantage of the intel opportunities you were given.)"
        "(But in your position,{w=0.1} who would?)"
        "(With a little grovelling and brown-nosing,{w=0.1} you'll be back to your usual routine:{w=0.5} handing locked suitcases to labs and giving your boss his 3 o'clock coffee.)"
        "(Besides,{w=0.1} STOP will send a better agent in your place.{w} A capable one:{w=0.5} one who'll sponge up information and collect samples like there's no tomorrow.)"
        "(But that agent isn't you.{w} It's {i}never{/i} you.{w} You just come to work for a decent salary.)"
        pause 1
        "(Alright,{w=0.1} \"agent\".{w} Get going already.)"
        "(You've got a lair to break out of.)"
        $ play_sound(footsteps4)
        jump kill_ending