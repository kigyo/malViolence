python early:


    class Achievement(NoRollback):
        def __init__(self, name='', image='', message='', **kwargs):
            self.name = name
            if image == '':
                ## If image is None, we will give a default image.
                self.image = Transform('gui/trophy_icon.png', fit='contain')
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

        def purge(self):
            """
            This will clear the achievements AND persistent list.

            As a standard python expression  ::  achievements.purge()
            As a screen action  ::  Function( achievements.purge )
            """
            achievement.clear_all()
            persistent.my_achievements.clear()


## DO NOT TOUCH/REUSE/CHANGE THIS AT ANY TIME!
## To clear this list use ::  achievements.purge()
default persistent.my_achievements = []
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
        "welcome": [_("Welcome to My Game!"), _("Start the game"), 'gui/trophy_icon.png', None],

        ## The None, means that the achievement will be displayed greyed-out before it is granted (or achieved).
        ## I use these terms to describe the type of achievement it is;
        ##            None = default (greyed out and can see the name and description of the achievement.)
        ##        'hidden' = Achievements with this label will be displayed as hidden.
        ##      'platinum' = The final achievement to be granted once all other achievements have been granted.

        "secret": [_("Shh... My little secret."), _("Discover the secret."), 'gui/trophy_icon.png', 'hidden'],
        "wow": [_("Outstanding!"), _("Get all achievements."), 'gui/trophy_icon.png', 'platinum'],

        "dead1": [_("DEAD END 01:"), _("Cheers! It's Cyanide."), 'gui/dead_icon.png', 'dead'], #tutorial
        "dead2": [_("DEAD END 02:"), _("Die another way."), 'gui/dead_icon.png', 'dead'], #room1 meta
        "dead3": [_("DEAD END 03:"), _("Cheers! It's Cyanide."), 'gui/dead_icon.png', 'dead'], #room1 1
        "dead4": [_("DEAD END 04:"), _("Cheers! It's Cyanide."), 'gui/dead_icon.png', 'dead'], #room1 2
        "dead5": [_("DEAD END 05:"), _("Cheers! It's Cyanide."), 'gui/dead_icon.png', 'dead'], #room1 3
        "dead6": [_("DEAD END 06:"), _("Cheers! It's Cyanide."), 'gui/dead_icon.png', 'dead'], #room2 meta
        "dead7": [_("DEAD END 07:"), _("Cheers! It's Cyanide."), 'gui/dead_icon.png', 'dead'], #room2 1
        "dead8": [_("DEAD END 08:"), _("Cheers! It's Cyanide."), 'gui/dead_icon.png', 'dead'], #room2 2
        "dead9": [_("DEAD END 09:"), _("Cheers! It's Cyanide."), 'gui/dead_icon.png', 'dead'], #room2 3
        "dead10": [_("DEAD END 10:"), _("Cheers! It's Cyanide."), 'gui/dead_icon.png', 'dead'], #room3 meta
        "dead11": [_("DEAD END 11:"), _("Cheers! It's Cyanide."), 'gui/dead_icon.png', 'dead'], #room3 1
        "dead12": [_("DEAD END 12:"), _("Cheers! It's Cyanide."), 'gui/dead_icon.png', 'dead'], #room3 2
        "dead13": [_("DEAD END 13:"), _("Cheers! It's Cyanide."), 'gui/dead_icon.png', 'dead'], #room3 3
    }

    ## Here we are simply registering the achievements.
    ## This is solely for backend use.
    for k, v in achievement_name.items():
        achievement.register(v[0])


## Here are the instances of the achievements.
## These will be added to the persistent
## list we made earlier.
default achievement_welcome = Achievement(name=achievement_name['welcome'][0], message=achievement_name['welcome'][1], image=achievement_name['welcome'][2])
default achievement_secret = Achievement(name=achievement_name['secret'][0], message=achievement_name['secret'][1], image=achievement_name['secret'][2])
default achievement_platinum = Achievement(name=achievement_name['wow'][0], message=achievement_name['wow'][1], image=achievement_name['wow'][2])

default achievement_dead1 = Achievement(name=achievement_name['dead1'][0], message=achievement_name['dead1'][1], image=achievement_name['dead1'][2])
default achievement_dead2 = Achievement(name=achievement_name['dead2'][0], message=achievement_name['dead2'][1], image=achievement_name['dead2'][2])
default achievement_dead3 = Achievement(name=achievement_name['dead3'][0], message=achievement_name['dead3'][1], image=achievement_name['dead3'][2])
default achievement_dead4 = Achievement(name=achievement_name['dead4'][0], message=achievement_name['dead4'][1], image=achievement_name['dead4'][2])
default achievement_dead5 = Achievement(name=achievement_name['dead5'][0], message=achievement_name['dead5'][1], image=achievement_name['dead5'][2])
default achievement_dead6 = Achievement(name=achievement_name['dead6'][0], message=achievement_name['dead6'][1], image=achievement_name['dead6'][2])
default achievement_dead7 = Achievement(name=achievement_name['dead7'][0], message=achievement_name['dead7'][1], image=achievement_name['dead7'][2])
default achievement_dead8 = Achievement(name=achievement_name['dead8'][0], message=achievement_name['dead8'][1], image=achievement_name['dead8'][2])
default achievement_dead9 = Achievement(name=achievement_name['dead9'][0], message=achievement_name['dead9'][1], image=achievement_name['dead9'][2])
default achievement_dead10 = Achievement(name=achievement_name['dead10'][0], message=achievement_name['dead10'][1], image=achievement_name['dead10'][2])
default achievement_dead11 = Achievement(name=achievement_name['dead11'][0], message=achievement_name['dead11'][1], image=achievement_name['dead11'][2])
default achievement_dead12 = Achievement(name=achievement_name['dead12'][0], message=achievement_name['dead12'][1], image=achievement_name['dead12'][2])
default achievement_dead13 = Achievement(name=achievement_name['dead13'][0], message=achievement_name['dead13'][1], image=achievement_name['dead13'][2])

