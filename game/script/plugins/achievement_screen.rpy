## Here we have the menu screen to display all the locked
## and unlocked achievements.

## This configuration here allows the grid to be displayed even if
## not all elements are visible. You won't get an error for grids
## that are not filled to the max.
define config.allow_underfull_grids = True

## The achievements screen.
screen achievement_menu():

    tag menu

    # variant "small"

    ## If you'd like to display a number and total of achievements you can use this...
    # use extras_menu(_("Achievements | {:01d}/{}".format(len(persistent.my_achievements), len(achievement_name) if len(persistent.my_achievements) == len(achievement_name) else len(achievement_name) - 1)), scroll="viewport"):
    ## Else, use this.
    use extras_menu(_("Achievements"), scroll="viewport"):

        style_prefix "achievements"

        frame:
            
            background None
            padding (20, 20, 20, 20)
            align (0.0, 0.0)

            vpgrid:
                
                cols 2 ## You can change this number depending on the width of your achievements.
                spacing 10

                ## Granted achievements
                for t in persistent.my_achievements:
                    
                    if achievement.has(t.id) and "DEAD" not in t.name:
                        
                        frame:
                            
                            background Solid('#0088AA') ## Nice bright blue/turquoise.

                            hbox:
                                yalign 0.5
                                xysize (100, 100)
                                
                                add achievement_name[t.id][2] size (100, 100) yalign 0.5

                                null width 20

                                vbox:
                                    spacing 0
                                    yfill False
                                    
                                    text achievement_name[t.id][0] style 'achievements_label' color '#000000'
                                    text achievement_name[t.id][1] color '#000000'

                ## Locked achievements
                for k,v in achievement_name.items():
                    ## Index '0' is the name of the achievement.
                    if not achievement.has(k) and v[3] != 'dead':

                        ## We're doing a check for all achievements
                        ## that is not a 'platinum'.
                        ## The platinum achievement will not appear
                        ## in the list.
                        ## Index '3' is the type of achievement.
                        frame:
                            
                            hbox:
                                
                                yalign 0.5
                                xysize (100, 100)
                                
                                ## This will display a locked icon.
                                add 'gui/locked_achievement.png' size (100, 100) yalign 0.5

                                null width 20

                                vbox:
                                    
                                    spacing 0
                                    yfill False

                                    ## We're setting the data feedback to represent
                                    ## the None and 'hidden' achievements.
                                    if v[3] is None:
                                        ## Index '1' is the description of the achievemnt.
                                    
                                        text str(v[0]) style 'achievements_label' color '#FFFFFF33'
                                        text str(v[1]) color '#FFFFFF33'
                                    
                                    else:
                                    
                                        text _('Hidden Achievement') style 'achievements_label' color '#FFFFFF33'

screen failchievement_menu():

    tag menu

    # variant "small"

    ## If you'd like to display a number and total of achievements you can use this...
    # use extras_menu(_("Achievements | {:01d}/{}".format(len(persistent.my_achievements), len(achievement_name) if len(persistent.my_achievements) == len(achievement_name) else len(achievement_name) - 1)), scroll="viewport"):
    ## Else, use this.
    use extras_menu(_("Failures"), scroll="viewport"):

        style_prefix "achievements"

        frame:
            
            background None
            padding (20, 20, 20, 20)
            align (0.0, 0.0)

            vpgrid:
                
                cols 2 ## You can change this number depending on the width of your achievements.
                spacing 10
                for v in death_name:
                    if v in persistent.dead_ends:
                    
                        frame:
                            
                            background Solid('#0088AA') ## Nice bright blue/turquoise.

                            hbox:
                                yalign 0.5
                                xysize (100, 100)
                                
                                add death_name[v][2] size (100, 100) yalign 0.5

                                null width 20

                                vbox:
                                    spacing 0
                                    yfill False
                                    
                                    text death_name[v][0] style 'achievements_label' color '#000000'
                                    text death_name[v][1] color '#000000'
                    else:
                        frame:
                            
                            hbox:
                                
                                yalign 0.5
                                xysize (100, 100)
                                
                                ## This will display a locked icon.
                                add 'gui/locked_achievement.png' size (100, 100) yalign 0.5

                                null width 20

                                vbox:
                                    
                                    spacing 0
                                    yfill False

                                    ## We're setting the data feedback to represent
                                    ## the None and 'hidden' achievements.
                                    if death_name[v][3] == "dead":
                                        ## Index '1' is the description of the achievemnt.
                                    
                                        text str(death_name[v][0]) style 'achievements_label' color '#FFFFFF33'
                                        #text str(v[1]) color '#FFFFFF33'
                                        text "???" color '#FFFFFF33'
                                    
                                    else:
                                    
                                        text _('Hidden Avoidable Death') style 'achievements_label' color '#FFFFFF33'


init python:

    ## These two functions are the ones that will be used
    ## to handle the list as achievements are added to it.

    def achievement_notification_show():
        ## This is to force the notification to show if
        ## the list is not empty.
        store.achievement_is_done = False
        if achievement_notification_list:
            store.achievement_notification_list.pop(0)


    def achievement_notification_done():
        ## This is to tell RenPy that the notification list
        ## is now empty and sets the variable to True.
        if not achievement_notification_list:
            store.achievement_is_done = True

    config.overlay_screens.append("achievement_notification_catcher")

    def all_endings():
        if achievement_end1 in persistent.my_achievements and achievement_end2 in persistent.my_achievements and achievement_end3 in persistent.my_achievements and persistent.game_clear == False:
            persistent.game_clear = True
            renpy.notify("You have unlocked a special extras screen in the Main Menu!")

    ## Here we have a funtion that is passive.
    def passive_function():
        ## This code here will grant the platinum achievement.
        all_endings()
        if len(persistent.my_achievements) >= (len(achievement_name) - 1):
            Achievement.add(achievement_platinum)
    
    def deadend(cheevo):
        if len(persistent.dead_ends) == 0:
            Achievement.add(achievement_deadfirst)
        Achievement.add_death(cheevo)
        if len(persistent.dead_ends) >= (len(death_name)):
            Achievement.add(achievement_deadall)

define config.periodic_callback = passive_function


## The notification screen.
## By default, the notification will appear at the top of the screen.
## If you want to change this you'll have to amend the transform 'achievement_appear'.

default achievement_notification_list = []
default achievement_is_done = False

## This screen will catch any achievement that is in the list.
screen achievement_notification_catcher():

    if len(achievement_notification_list) > 0 and not renpy.get_screen('achievement_notification'):
        timer 0.5 repeat True:
            action [SetVariable('achievement_is_done', False), Show('achievement_notification')]

    if not achievement_is_done:
        timer 2.0 repeat True:
            action If(len(achievement_notification_list) > 0,
                true=[Hide("achievement_notification"), Function(achievement_notification_show)],
                false=[Function(achievement_notification_done)])


screen achievement_notification():

    zorder 100

    if achievement_notification_list:

        frame at achievement_appear:
            align (0.5, 0.0)
            padding (20, 20, 20, 20)

            hbox:
                xysize (100, 100)
                if isinstance(achievement_notification_list[0], str):
                    add death_name[achievement_notification_list[0]][2]
                else:
                    add achievement_notification_list[0].image
                
                null width 20

                vbox:
                    yalign 0.5
                    xminimum 340
                    xmaximum 440
                    yfill False
                    xfill False

                    if isinstance(achievement_notification_list[0], str):
                        text death_name[achievement_notification_list[0]][0]:
                            color gui.accent_color size 25
                    else:
                        text str(achievement_notification_list[0].name):
                            color gui.accent_color size 25

                    if isinstance(achievement_notification_list[0], str):
                        text death_name[achievement_notification_list[0]][1]:
                            style 'victory_message_text'
                    else:
                        text str(achievement_notification_list[0].message):
                            style 'victory_message_text'

style victory_message_text:
    color "#ffffff"
    size 16

transform achievement_appear:
    subpixel True
    on show:
        yoffset -160.0 alpha 1.0
        easein 0.2 yoffset 5.0
        easeout 0.1 yoffset 0.0

    on hide:
        yoffset 0.0
        easein 0.2 yoffset 5.0
        easeout 0.1 yoffset -160.0
        alpha 0.0


style achievements_vbox is vbox
style achievements_text is text
style achievements_frame is frame

style achievements_vbox:
    minimum (330, 100)
    maximum (360, 100)
    spacing 2
    yfill False

style achievements_label:
    size 26
    outlines [(1, '#00000022', 0, 1)]
    yalign 0.5

style achievements_text:
    size 16 xoffset 2
    yalign 0.5

style achievements_locked_text:
    color "#555555"
    size 16

style achievements_frame:
    background Solid('#444444')
    minimum (500, 140)
    align (0.5, 0.5)
    padding (15, 15, 15, 15)
