python early:


    class Achievement(NoRollback):
        def __init__(self, id='', kind="normal", **kwargs):
            self.id = id
            if kind == "normal" and id in achievement_name:
                self.name = achievement_name[id][0]
                self.message = achievement_name[id][1]
                self.image = Transform(achievement_name[id][2], fit='contain')
            elif id in death_name:
                self.name = death_name[id][0]
                self.message = death_name[id][1]
                self.image = Transform(death_name[id][2], fit='contain')


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
            if not achievement.has(trophy.id):
                achievement.grant(trophy.id)
                store.achievement_notification_list.append(trophy)

            if trophy not in persistent.my_achievements:
                ## New acheievements will appear first in the list.
                persistent.my_achievements.insert(0, trophy)

        def add_death(trophy):

            if trophy not in persistent.dead_ends:
                store.achievement_notification_list.append(trophy)
                ## New acheievements will appear first in the list.
                persistent.dead_ends.insert(0, trophy)

            if not achievement.has(trophy):
                achievement.grant(trophy)

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

    achievement.sync()
    for k, v in achievement_name.items():
        achievement.register(k)
    for k, v in death_name.items():
        achievement.register(k)

default achievement_start = Achievement('start')
default achievement_tfng = Achievement('tfng')
default achievement_room1 = Achievement('room1')
default achievement_room2 = Achievement('room2')
default achievement_room3 = Achievement('room3')
default achievement_deadfirst = Achievement('deadfirst')
default achievement_deadall = Achievement('deadall')
#default achievement_wrong = Achievement('wrong')
default achievement_end1 = Achievement('end1')
default achievement_end2 = Achievement('end2')
default achievement_end3 = Achievement('end3')
default achievement_investigate = Achievement('investigate')
default achievement_difficulty1 = Achievement('difficulty1')
default achievement_difficulty2 = Achievement('difficulty2')
default achievement_difficulty3 = Achievement('difficulty3')
default achievement_platinum = Achievement('all')

default achievement_dead1 = Achievement('dead1')
default achievement_dead2 = Achievement('dead2')
default achievement_dead3 = Achievement('dead3')
default achievement_dead4 = Achievement('dead4')
default achievement_dead5 = Achievement('dead5')
default achievement_dead6 = Achievement('dead6')
default achievement_dead7 = Achievement('dead7')
default achievement_dead8 = Achievement('dead8')
default achievement_dead9 = Achievement('dead9')
default achievement_dead10 = Achievement('dead10')
default achievement_dead11 = Achievement('dead11')
default achievement_dead12 = Achievement('dead12')
default achievement_dead13 = Achievement('dead13')