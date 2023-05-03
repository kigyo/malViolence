python early:


    class Achievement(NoRollback):
        def __init__(self, name='', image='', message='', **kwargs):
            self.name = name
            if image == '':
                ## If image is None, we will give a default image.
                self.image = Transform('gui/gui/trophy_icon.png.png', fit='contain')
            else:
                self.image = Transform(image, fit='contain')
            self.message = message


        def __eq__(self, value):
            """
            Since we are using a persistent list we need to do an equality
            check.

            Below we are simply checking 'self.name == value.name, self.message == value.message'
            """
            return all((self.name == value.name, self.message == value.message))

        def add(trophy):
            """
            Add/Grant Trophies/Achievements to the list.

            As a standard python expression  ::  Achievement.add( <trophy> )
            As a screen action  ::  Function( Achievement.add, <trophy> )
            """
            if not achievement.has(trophy.name):
                achievement.grant(trophy.name)
                store.achievement_notification_list.append(trophy)

            if trophy not in persistent.my_achievements:
                ## New acheievements will appear first in the list.
                persistent.my_achievements.insert(0, trophy)

        def add_death(trophy):

            if trophy not in persistent.dead_ends:
                store.achievement_notification_list.append(trophy)
                ## New acheievements will appear first in the list.
                persistent.dead_ends.insert(0, trophy)

        def purge(self):
            """
            This will clear the achievements AND persistent list.

            As a standard python expression  ::  achievements.purge()
            As a screen action  ::  Function( achievements.purge )
            """
            achievement.clear_all()
            persistent.my_achievements.clear()
            persistent.dead_ends.clear()


## DO NOT TOUCH/REUSE/CHANGE THIS AT ANY TIME!
## To clear this list use ::  achievements.purge()
default persistent.my_achievements = []
default persistent.dead_ends = []
default achievements = Achievement()

init python:

    achievement.steam_position = "top right"

    achievement_name = {

        ## How to set up achievements
        # "achievement_key": [_("Name of Achievement"), _("Description"), '<image_path_here>', '<type>'],

        ## Note: If you decide to add/amend any achievement's data long after the game has started or
        ##       an achievement has been granted you will have to do a full reset of the game for those
        ##       changes to be reflected. I.e. Delete persistent data.

        ## Example
        #"welcome": [_("Welcome to My Game!"), _("Start the game"), "gui/trophy_icon.png", None],

        ## The None, means that the achievement will be displayed greyed-out before it is granted (or achieved).
        ## I use these terms to describe the type of achievement it is;
        ##            None = default (greyed out and can see the name and description of the achievement.)
        ##        'hidden' = Achievements with this label will be displayed as hidden.
        ##      'platinum' = The final achievement to be granted once all other achievements have been granted.

        "start": [_("Rude Awakening"), _("Find yourself trapped under Cautionne's thumb."), "gui/trophy_icon.png", None],
        "tfng": [_("TFNG"), _("Get past the first of Cautionne's traps."), "gui/trophy_icon.png", None],
        "room1": [_("Lab Partner"), _("Escape from Cautionne's evil lab."), "gui/trophy_icon.png", None],
        "room2": [_("Private Study"), _("Get past the villains' workshop."), "gui/trophy_icon.png", None],
        "room3": [_("Housewarming"), _("Proceed past the villains' living quarters."), "gui/trophy_icon.png", None],
        "deadfirst": [_("Trial and Error"), _("Find out what happens when you make a mistake."), "gui/trophy_icon.png", None],
        "deadall": [_("A for Effort"), _("Make {i}all{/i} the mistakes. For science."), "gui/trophy_icon.png", None],
        "end1": [_("Breakout Role"), _("Escape."), "gui/trophy_icon.png", None],
        "end2": [_("Mission Accomplished"), _("Finish the job."), "gui/trophy_icon.png", None],
        "end3": [_("Communication Error"), _("Meet an ending."), "gui/trophy_icon.png", None],
        "investigate": [_("Busybody"), _("Leave no stone unturned."), "gui/trophy_icon.png", None],
        "difficulty1": [_("Diligent Puzzler"), _("Clear all puzzles without skipping them."), "gui/trophy_icon.png", "hidden"],
        "difficulty2": [_("Skilled Puzzler"), _("Clear all puzzles on normal difficulty or harder."), "gui/trophy_icon.png", "hidden"],
        "difficulty3": [_("Hardcore Puzzler"), _("Clear every puzzle on the hardest difficulty."), "gui/trophy_icon.png", "hidden"],
        "all": [_("Noble Laureate"), _("Earn all achievements."), "gui/trophy_icon.png", 'platinum'],
    }

    if persistent.skullicon == True:
        death_name = {
            "dead1": [_("DEAD END 01:"), _("Cheers! It's Cyanide."), "gui/dead_icon.png", 'dead'], #tutorial
            "dead2": [_("DEAD END 02:"), _("Marbleous Slapstick!"), "gui/dead_icon.png", 'dead'], #room1 meta
            "dead3": [_("DEAD END 03:"), _("A Mindblowing Conclusion!"), "gui/dead_icon.png", 'dead'], #room1 1
            "dead4": [_("DEAD END 04:"), _("Trouble-shooting?"), "gui/dead_icon.png", 'dead'], #room1 2
            "dead5": [_("DEAD END 05:"), _("A Venom-enal End!"), "gui/dead_icon.png", 'dead'], #room1 3
            "dead6": [_("DEAD END 06:"), _("Stop Me If You Think You've Word This One Before..."), "gui/dead_icon.png", 'dead'], #room2 meta
            "dead7": [_("DEAD END 07:"), _("Pinpricked."), "gui/dead_icon.png", 'dead'], #room2 1
            "dead8": [_("DEAD END 08:"), _("A Taste of Sobering Punishment."), "gui/dead_icon.png", 'dead'], #room2 2
            "dead9": [_("DEAD END 09:"), _("Didn't Make The Cut."), "gui/dead_icon.png", 'dead'], #room2 3
            "dead10": [_("DEAD END 10:"), _("Holy Scrap!"), "gui/dead_icon.png", 'dead'], #room3 meta
            "dead11": [_("DEAD END 11:"), _("Quilt In Action."), "gui/dead_icon.png", 'dead'], #room3 1
            "dead12": [_("DEAD END 12:"), _("Get Stuffed."), "gui/dead_icon.png", 'dead'], #room3 2
            "dead13": [_("DEAD END 13:"), _("Flipping Miserable!"), "gui/dead_icon.png", 'dead'], #room3 3
        }
    elif persistent.skullicon == False:
        death_name = {
            "dead1": [_("DEAD END 01:"), _("Cheers! It's Cyanide."), "gui/dead_icon_alt.png", 'dead'], #tutorial
            "dead2": [_("DEAD END 02:"), _("Marbleous Slapstick!"), "gui/dead_icon_alt.png", 'dead'], #room1 meta
            "dead3": [_("DEAD END 03:"), _("A Mindblowing Conclusion!"), "gui/dead_icon_alt.png", 'dead'], #room1 1
            "dead4": [_("DEAD END 04:"), _("Trouble-shooting?"), "gui/dead_icon_alt.png", 'dead'], #room1 2
            "dead5": [_("DEAD END 05:"), _("A Venom-enal End!"), "gui/dead_icon_alt.png", 'dead'], #room1 3
            "dead6": [_("DEAD END 06:"), _("Stop Me If You Think You've Word This One Before..."), "gui/dead_icon_alt.png", 'dead'], #room2 meta
            "dead7": [_("DEAD END 07:"), _("Pinpricked"), "gui/dead_icon_alt.png", 'dead'], #room2 1
            "dead8": [_("DEAD END 08:"), _("A Taste of Sobering Punishment."), "gui/dead_icon_alt.png", 'dead'], #room2 2
            "dead9": [_("DEAD END 09:"), _("Didn't Make The Cut."), "gui/dead_icon_alt.png", 'dead'], #room2 3
            "dead10": [_("DEAD END 10:"), _("Holy Scrap!"), "gui/dead_icon_alt.png", 'dead'], #room3 meta
            "dead11": [_("DEAD END 11:"), _("Quilt In Action."), "gui/dead_icon_alt.png", 'dead'], #room3 1
            "dead12": [_("DEAD END 12:"), _("Get Stuffed."), "gui/dead_icon_alt.png", 'dead'], #room3 2
            "dead13": [_("DEAD END 13:"), _("Flipping Miserable!"), "gui/dead_icon_alt.png", 'dead'], #room3 3
        }


    for k, v in achievement_name.items():
        achievement.register(v[0])
    for k, v in death_name.items():
        achievement.register(v[0])

default achievement_start = Achievement(name=achievement_name['start'][0], message=achievement_name['start'][1], image=achievement_name['start'][2])
default achievement_tfng = Achievement(name=achievement_name['tfng'][0], message=achievement_name['tfng'][1], image=achievement_name['tfng'][2])
default achievement_room1 = Achievement(name=achievement_name['room1'][0], message=achievement_name['room1'][1], image=achievement_name['room1'][2])
default achievement_room2 = Achievement(name=achievement_name['room2'][0], message=achievement_name['room2'][1], image=achievement_name['room2'][2])
default achievement_room3 = Achievement(name=achievement_name['room3'][0], message=achievement_name['room3'][1], image=achievement_name['room3'][2])
default achievement_deadfirst = Achievement(name=achievement_name['deadfirst'][0], message=achievement_name['deadfirst'][1], image=achievement_name['deadfirst'][2])
default achievement_deadall = Achievement(name=achievement_name['deadall'][0], message=achievement_name['deadall'][1], image=achievement_name['deadall'][2])
#default achievement_wrong = Achievement(name=achievement_name['wrong'][0], message=achievement_name['wrong'][1], image=achievement_name['wrong'][2])
default achievement_end1 = Achievement(name=achievement_name['end1'][0], message=achievement_name['end1'][1], image=achievement_name['end1'][2])
default achievement_end2 = Achievement(name=achievement_name['end2'][0], message=achievement_name['end2'][1], image=achievement_name['end2'][2])
default achievement_end3 = Achievement(name=achievement_name['end3'][0], message=achievement_name['end3'][1], image=achievement_name['end3'][2])
default achievement_investigate = Achievement(name=achievement_name['investigate'][0], message=achievement_name['investigate'][1], image=achievement_name['investigate'][2])
default achievement_difficulty1 = Achievement(name=achievement_name['difficulty1'][0], message=achievement_name['difficulty1'][1], image=achievement_name['difficulty1'][2])
default achievement_difficulty2 = Achievement(name=achievement_name['difficulty2'][0], message=achievement_name['difficulty2'][1], image=achievement_name['difficulty2'][2])
default achievement_difficulty3 = Achievement(name=achievement_name['difficulty3'][0], message=achievement_name['difficulty3'][1], image=achievement_name['difficulty3'][2])
default achievement_platinum = Achievement(name=achievement_name['all'][0], message=achievement_name['all'][1], image=achievement_name['all'][2])

default achievement_dead1 = Achievement(name=death_name['dead1'][0], message=death_name['dead1'][1], image=death_name['dead1'][2])
default achievement_dead2 = Achievement(name=death_name['dead2'][0], message=death_name['dead2'][1], image=death_name['dead2'][2])
default achievement_dead3 = Achievement(name=death_name['dead3'][0], message=death_name['dead3'][1], image=death_name['dead3'][2])
default achievement_dead4 = Achievement(name=death_name['dead4'][0], message=death_name['dead4'][1], image=death_name['dead4'][2])
default achievement_dead5 = Achievement(name=death_name['dead5'][0], message=death_name['dead5'][1], image=death_name['dead5'][2])
default achievement_dead6 = Achievement(name=death_name['dead6'][0], message=death_name['dead6'][1], image=death_name['dead6'][2])
default achievement_dead7 = Achievement(name=death_name['dead7'][0], message=death_name['dead7'][1], image=death_name['dead7'][2])
default achievement_dead8 = Achievement(name=death_name['dead8'][0], message=death_name['dead8'][1], image=death_name['dead8'][2])
default achievement_dead9 = Achievement(name=death_name['dead9'][0], message=death_name['dead9'][1], image=death_name['dead9'][2])
default achievement_dead10 = Achievement(name=death_name['dead10'][0], message=death_name['dead10'][1], image=death_name['dead10'][2])
default achievement_dead11 = Achievement(name=death_name['dead11'][0], message=death_name['dead11'][1], image=death_name['dead11'][2])
default achievement_dead12 = Achievement(name=death_name['dead12'][0], message=death_name['dead12'][1], image=death_name['dead12'][2])
default achievement_dead13 = Achievement(name=death_name['dead13'][0], message=death_name['dead13'][1], image=death_name['dead13'][2])