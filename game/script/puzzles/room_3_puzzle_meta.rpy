screen room3_meta:
    sensitive not inspect
    modal True
    layer "master"
    frame padding 50,40 xfill True yfill True:
        default scrapbook_page = 1

        if scrapbook_page == 1:
            add "puzzles/room_3_meta/scrapbook2.png" xalign 0.5
            imagebutton idle Null(175,140) action SetScreenVariable("scrapbook_page",2) xpos 1402 mouse "inspect"

        else:
            add "puzzles/room_3_meta/scrapbook1.png" xalign 0.5
            imagebutton idle Null(145,135) action SetScreenVariable("scrapbook_page",1) xpos 203 ypos 75 mouse "inspect"

        hbox yalign 1.0 xalign 0.5 spacing 100:
            #memories are unlocked as the puzzles are solved
            if "quilt" in room3["solved"]:
                add "room3_meta1" xalign 1.0 at rotated(30)
            if "cooking" in room3["solved"]:
                add "room3_meta2" xalign 0.0 yalign 0.1 at rotated(-30)
            if "toys" in room3["solved"]:
                add "room3_meta3" xalign 0.4 yalign 1.0 at rotated(-5)
        
        #if len(room3["solved"]) >= 3 and room3["scrapbook_new"] < 2:
        #    timer 0.1 action Jump("room3_meta_cutscene") 
        #if room3["scrapbook_new"] == 2:
        #    use jigsaw 


        textbutton "RETURN" style "confirm_button" action Return() xalign 1.0 yalign 1.0

init python:
    
    def piece_dragged(drags, drop):
        
        if not drop:
            return
        
        p_x = drags[0].drag_name.split("-")[0]
        p_y = drags[0].drag_name.split("-")[1]
        t_x = drop.drag_name.split("-")[0]
        t_y = drop.drag_name.split("-")[1]
        
        a = []
        a.append(drop.drag_joined)
        a.append((drags[0], 3, 3))
        drop.drag_joined(a)
        
        if p_x == t_x and p_y == t_y:
            # comment next line if you don't need sound
            #renpy.music.play("Pickup_Coin.ogg", channel="sound")
            
            my_x = int(int(p_x)*active_area_size*x_scale_index)-int(grip_size*x_scale_index)+puzzle_field_xoffset
            my_y = int(int(p_y)*active_area_size*y_scale_index)-int(grip_size*y_scale_index)+puzzle_field_yoffset
            drags[0].snap(my_x,my_y, delay=0.1)
            drags[0].draggable = False
            placedlist[int(p_x),int(p_y)] = True

            for i in range(0, grid_width):
                for j in range(0, grid_height):
                    if placedlist[i,j] == False:
                        return
            store.room3["scrapbook_new"] = "solved"
            return True
        return

        
screen jigsaw:
    
    key "rollback" action [[]]
    key "rollforward" action [[]]
    
    add im.Scale("puzzles/room_3_meta/_puzzle_field.png", img_width, img_height) pos(puzzle_field_xoffset, puzzle_field_yoffset)
    
    draggroup:

        for i in range(0, grid_width):
            for j in range(0, grid_height):
                $ name = "%s-%s"%(i,j)
                $ my_x = i*int(active_area_size*x_scale_index)+puzzle_field_xoffset
                $ my_y = j*int(active_area_size*y_scale_index)+puzzle_field_yoffset
                drag:
                    drag_name name
                    child im.Scale("puzzles/room_3_meta/_blank_space.png", int(active_area_size*x_scale_index), int(active_area_size*y_scale_index) )
                    draggable False
                    xpos my_x ypos my_y
            
            
        for i in range(0, grid_width):
            for j in range(0, grid_height):
                $ name = "%s-%s-piece"%(i,j)
                drag:
                    drag_name name
                    child imagelist[i,j]
                    #droppable False
                    dragged piece_dragged
                    xpos piecelist[i,j][0] ypos piecelist[i,j][1]



default chosen_img = "images/room_3_meta.png"

default grid_width = 7
default grid_height = 5

default x_scale_index = 1
default y_scale_index = 1

define puzzle_field_size = 650
define puzzle_field_xoffset = 600
define puzzle_field_yoffset = 300
define puzzle_piece_size = 450
define grip_size = 75
define active_area_size = puzzle_piece_size - (grip_size * 2)


#turn this into a function and initialize all variables
label jigsaw_puzzle:
#####################################################################################################
    python:
        
        img_width, img_height = renpy.image_size(chosen_img)
        
        
        # scales down an image to fit the puzzle_field_size
        if img_width >= img_height and img_width > puzzle_field_size:
            img_scale_down_index = round( (1.00 * puzzle_field_size / img_width), 6)
            img_to_play = im.FactorScale(chosen_img, img_scale_down_index)
            img_width = int(img_width * img_scale_down_index)
            img_height = int(img_height * img_scale_down_index)
            
        elif img_height >= img_width and img_height > puzzle_field_size:
            img_scale_down_index = round( (1.00 * puzzle_field_size / img_height), 6)
            img_to_play = im.FactorScale(chosen_img, img_scale_down_index)
            img_width = int(img_width * img_scale_down_index)
            img_height = int(img_height * img_scale_down_index)
            
        else:
            img_to_play = chosen_img
        
        x_scale_index = round( (1.00 * (img_width/grid_width)/active_area_size), 6)
        y_scale_index = round( (1.00 * (img_height/grid_height)/active_area_size), 6)
        
        
        mainimage = im.Composite((int(img_width+(grip_size*2)*x_scale_index), int(img_height+(grip_size*2)*y_scale_index)),(int(grip_size*x_scale_index), int(grip_size*y_scale_index)), img_to_play)
        
        testvar = "this happened"
        
        # some calculations
        top_row = []
        for i in range (0, grid_width):
            top_row.append(i)
            
        bottom_row = []
        for i in range (0, grid_width):
            bottom_row.append(grid_width*(grid_height-1)+i)
            
        left_column = []
        for i in range (0, grid_height):
            left_column.append(grid_width*i)
            
        right_column = []
        for i in range (0, grid_height):
            right_column.append(grid_width*i + (grid_width-1) )
        
        
        # randomly makes the shape of each puzzle piece
        # (starts from top row, fills it in from left to right, then - next row)
        jigsaw_grid = []
        for i in range(0,grid_height):
            for j in range (0,grid_width):
                jigsaw_grid.append([9,9,9,9])   # [top, right, bottom, left]
                
        for i in range(0,grid_height):
            for j in range (0,grid_width):
                if grid_width*i+j not in top_row:
                    if jigsaw_grid[grid_width*(i-1)+j][2] == 1:
                        jigsaw_grid[grid_width*i+j][0] = 2
                    else:
                        jigsaw_grid[grid_width*i+j][0] = 1
                else:
                    jigsaw_grid[grid_width*i+j][0] = 0
                    
                if grid_width*i+j not in right_column:
                    jigsaw_grid[grid_width*i+j][1] = renpy.random.randint(1,2)
                else:
                    jigsaw_grid[grid_width*i+j][1] = 0
                    
                if grid_width*i+j not in bottom_row:
                    jigsaw_grid[grid_width*i+j][2] = renpy.random.randint(1,2)
                else:
                    jigsaw_grid[grid_width*i+j][2] = 0
                    
                if grid_width*i+j not in left_column:
                    if jigsaw_grid[grid_width*i+j-1][1] == 1:
                        jigsaw_grid[grid_width*i+j][3] = 2
                    else:
                        jigsaw_grid[grid_width*i+j][3] = 1
                else:
                    jigsaw_grid[grid_width*i+j][3] = 0
                    
        
        # makes description for each puzzle piece
        piecelist = dict()
        imagelist = dict()
        placedlist = dict()
        testlist = dict()
        
        for i in range(0,grid_width):
            for j in range (0,grid_height):
                piecelist[i,j] = [int(renpy.random.randint(0, int(config.screen_width * 0.9 - puzzle_field_size))+puzzle_field_size), int(renpy.random.randint(0, int(config.screen_height * 0.8)))]
                
                temp_img = im.Crop(mainimage, int(i*active_area_size*x_scale_index), int(j*active_area_size*y_scale_index), int(puzzle_piece_size*x_scale_index), int(puzzle_piece_size*y_scale_index))
        
        # makes puzzle piece image using its shape description and tile pieces
        # (will rotate them to form top, right, bottom and left sides of puzzle piece)
                imagelist[i,j] = im.Composite(
        (int(puzzle_piece_size*x_scale_index), int(puzzle_piece_size*y_scale_index)),
        (0,0), im.AlphaMask(temp_img, im.Scale(im.Rotozoom("puzzles/room_3_meta/_00%s.png"%(jigsaw_grid[grid_width*j+i][0]), 0, 1.0), int(puzzle_piece_size*x_scale_index), int(puzzle_piece_size*y_scale_index))),
        (0,0), im.AlphaMask(temp_img, im.Scale(im.Rotozoom("puzzles/room_3_meta/_00%s.png"%(jigsaw_grid[grid_width*j+i][1]), 270, 1.0), int(puzzle_piece_size*x_scale_index), int(puzzle_piece_size*y_scale_index))),
        (0,0), im.AlphaMask(temp_img, im.Scale(im.Rotozoom("puzzles/room_3_meta/_00%s.png"%(jigsaw_grid[grid_width*j+i][2]), 180, 1.0), int(puzzle_piece_size*x_scale_index), int(puzzle_piece_size*y_scale_index))),
        (0,0), im.AlphaMask(temp_img, im.Scale(im.Rotozoom("puzzles/room_3_meta/_00%s.png"%(jigsaw_grid[grid_width*j+i][3]), 90, 1.0), int(puzzle_piece_size*x_scale_index), int(puzzle_piece_size*y_scale_index)))
        )
                placedlist[i,j] = False

    return



screen control_scr:
    
    default current_file = 0
    if current_file != 0:
        
        $ img_width, img_height = renpy.image_size(current_file)
        
        if img_width>500 or img_height>500:
            if img_width > img_height:
                $ preview_scale = 500.00 / img_width
            else:
                $ preview_scale = 500.00 / img_height
        else:
            $ preview_scale = 1
            
        $ preview = im.FactorScale(current_file, preview_scale)
        
        add preview pos (640, 100)
        
        
    
    python:

        extensions = [ ".jpg", ".jpeg", ".png", ".webp" ]

        image_files = [ ]

        for fn in renpy.list_files():
            if fn[0] == "_" or fn.startswith("gui") or fn.startswith("puzzles/room_3_meta"):
                continue

            lfn = fn.lower()

            for i in extensions:
                if lfn.endswith(i):
                    image_files.append(fn)

        image_files.sort()
    
    frame:
        background Frame("puzzles/room_3_meta/_puzzle_field.png", 0, 0)
        xpos 100 ypos 100
        
        side "c b r":
             area (0, 0, 500, 500)

             viewport id "vp":
                 draggable True
                 mousewheel True

                 vbox:
                     xminimum 500
                     for pic in image_files:
                         $ a = image_files.index(pic)+1
                         button:
                             background None
                             text "Image [a]" size 30
                             action SetScreenVariable("current_file", pic)
                             
                             size_group "pic_buttons"


             bar value XScrollValue("vp")
             vbar value YScrollValue("vp")
    
    vbox:
        xpos 40 ypos 100 spacing 20
        
        for i in range (2, 12):
            textbutton "[i]" action SetVariable("grid_height", i)
            
    hbox:
        xpos 100 ypos 50 spacing 20
        
        for i in range (2, 12):
            textbutton "[i]" action SetVariable("grid_width", i)
    
    $ number_of_pieces = (grid_width*grid_height)
    text "[number_of_pieces] pieces" size 35 xalign 0.75 ypos 50
    
    
    button:
        text "Done" size 35
        action If(current_file != 0, Return(current_file))
        align (0.75, 0.95)
    
