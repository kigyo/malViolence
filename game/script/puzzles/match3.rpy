default match3 = []
default match3_pos = []

define match3_rows = 6
define match3_cols = 9

default match3_selected_row = 0
default match3_selected_col = 0
default match3_selected_row_temp = 0
default match3_selected_col_temp = 0

define match3_piece_size = 100

default match3_sensitive = True

default match3_points = 0
default match3_pointloop = 0
default match3_points_temp = 0
default match3_time = 90
default match3_goal = 500

init python:
    def match3_start(timer=90, goal=500):
        global match3, match3_pos, match3_points, match3_points_temp, match3_time, match3_goal
        match3_points_temp = 0
        match3_points = 0
        match3_time = timer
        match3_goal = goal

        store.match3_sensitive = True
        
        store.match3_selected_row = -1
        store.match3_selected_col = -1
        store.match3_selected_row_temp = -1
        store.match3_selected_col_temp = -1
        for row in range(0,match3_rows):
            match3.append([])
            match3_pos.append([])
            for col in range(0,match3_cols):
                match3[row].append(renpy.random.randint(1,6))
                match3_pos[row].append(0)
        renpy.call_screen("match3")

    def match3_vertical(row, col):
        if row >= 0 and row < match3_rows-2:
            if match3[row][col]==match3[row+1][col]==match3[row+2][col]:
                return True
        return False
        
    def match3_horizontal(row, col):
        if col >= 0 and col < match3_cols-2:
            if match3[row][col]==match3[row][col+1]==match3[row][col+2]:
                return True
        return False
    
    def match3_T_or_L(row, col, kind="vertical"):
        global match3, match3_points_temp, match3_time
        found = False
        for i in range(0,-3,-1):
            for j in range(3):
                if kind == "vertical" and match3_horizontal(row+j,col+i) or kind == "horizontal" and match3_vertical(row+i,col+j):
                    found = [row+j,col+i]
                    if kind == "horizontal":
                        found = [row+i,col+j]
                    break
        if found:
            print("apply points")
            found_1,found_2 = found[0],found[1]+1
            found_3,found_4 = found[0],found[1]+2
            if kind == "horizontal":
                found_1,found_2 = found[0]+1,found[1]
                found_3,found_4 = found[0]+2,found[1]
            match3_points_temp+=(match3[found_1][found_2]+match3[found_3][found_4])*2
            match3_time+=4
            match3[found_1][found_2],match3[found_3][found_4]=0,0

    def match3_scoring():
        global match3, match3_pos, match3_points_temp, match3_time
        for row in range(0,match3_rows):
            for col in range(0,match3_cols):
                base_point = 1
                
                if match3_vertical(row, col):
                    match3_points_temp+=(match3[row][col]+match3[row+1][col]+match3[row+2][col])*2
                    if row < match3_rows-3 and match3[row][col]==match3[row+3][col]:
                        if row < match3_rows-4 and match3[row][col]==match3[row+4][col]:
                            match3_points_temp+=match3[row+4][col]*4
                            match3_time+=4
                            match3[row+4][col]=0
                        match3_points_temp+=match3[row+3][col]*3
                        match3_time+=2
                        match3[row+3][col]=0
                    else:
                        match3_T_or_L(row, col)
                    base_point,match3[row+1][col],match3[row+2][col]=0,0,0
                
                if match3_horizontal(row, col):
                    match3_points_temp+=(match3[row][col]+match3[row][col+1]+match3[row][col+2])*2
                    if col < match3_cols-3 and match3[row][col]==match3[row][col+3]:
                        if col < match3_cols-4 and match3[row][col]==match3[row][col+4]:
                            match3_points_temp+=match3[row][col+4]*4
                            match3_time+=4
                            match3[row][col+4]=0
                        match3_points_temp+=match3[row][col+3]*3
                        match3_time+=2
                        match3[row][col+3]=0
                    else:
                        match3_T_or_L(row, col, "horizontal")
                    base_point,match3[row][col+1],match3[row][col+2]=0,0,0
                if base_point == 0:
                    match3[row][col]=0
            renpy.pause(0.05)

        # generate new pieces
        for row in range(match3_rows-1,-1,-1):
            for col in range(0,match3_cols):
                if match3[row][col] == 0:
                    fall_height = 1
                    for z in range(row-1, -1, -1):
                        if match3[z][col] > 0:
                            match3[row][col]=match3[z][col]
                            match3[z][col]=0
                            fall_height = row+1-z
                            break
                    if match3[row][col] == 0:
                        fall_height = row+1
                        match3[row][col] = renpy.random.randint(1,6)
                    if row != match3_rows-1 and match3_pos[row+1][col] < 0:
                        fall_height = -(match3_pos[row+1][col]/100)
                    match3_pos[row][col]-=fall_height*100
        for q in range(4*match3_rows):
            for row in range(0,match3_rows):
                for col in range(0,match3_cols):
                    if match3_pos[row][col] < 0:
                        match3_pos[row][col]+=25
            renpy.pause(.000001)
        return
        
screen match3():
    sensitive match3_sensitive
    if match3_goal:
        text str(match3_points) + "/" + str(match3_goal)
    else:
        text str(match3_points)
    if match3_time:
        text str(int(match3_time)) xalign .99
        if match3_sensitive:
            timer 1 repeat True action If(match3_time>0,true=SetVariable('match3_time',match3_time-1),false=Return())
    fixed xalign 0.5 yalign 0.5 xoffset 470 yoffset 215:
        for row in range(0,match3_rows):
            for col in range(0,match3_cols):
                showif row*110+match3_pos[row][col] > 0:
                    imagebutton idle("match3_"+str(match3[row][col])+".png"):
                        xoffset(col*110) yoffset(row*110+match3_pos[row][col]) 
                        action[SetVariable('match3_selected_col',col),SetVariable('match3_selected_row',row),ui.callsinnewcontext("match3_turn")]
                        at match3_animations

label match3_turn:
    show screen match3
    $match3_sensitive = False
    if match3_selected_row>=0:
        if match3_selected_row in(match3_selected_row_temp+1,match3_selected_row_temp-1) and match3_selected_col==match3_selected_col_temp:
            pass
        elif match3_selected_col in(match3_selected_col_temp+1,match3_selected_col_temp-1) and match3_selected_row==match3_selected_row_temp:
            pass
        else:
            jump match3_set_selected
        if match3_selected_row_temp>=0:
            $match3_temp=match3[match3_selected_row][match3_selected_col]
            $match3[match3_selected_row][match3_selected_col]=match3[match3_selected_row_temp][match3_selected_col_temp]
            $match3[match3_selected_row_temp][match3_selected_col_temp]=match3_temp
            label match3_score:
                $match3_scoring()
                if match3_points_temp>0:
                    $match3_pointloop+=1
                    $match3_points+=match3_points_temp
                    $match3_points_temp=0
                    jump match3_score
                if match3_pointloop==0:
                    $match3_temp=match3[match3_selected_row_temp][match3_selected_col_temp]
                    $match3[match3_selected_row_temp][match3_selected_col_temp]=match3[match3_selected_row][match3_selected_col]
                    $match3[match3_selected_row][match3_selected_col]=match3_temp
                $match3_pointloop=0
                $match3_selected_row=-1
                $match3_selected_row_temp=-1
        else:
            label match3_set_selected:
                $match3_selected_row_temp=match3_selected_row
                $match3_selected_col_temp=match3_selected_col
    $match3_sensitive = True
    return

transform match3_animations:
    on show:
        alpha 0
        ease 0.3 alpha 1
    on hover:
        ease 0.15 matrixcolor BrightnessMatrix(0.2)
    on idle:
        ease 0.15 matrixcolor BrightnessMatrix(0)

#TODO: replace images
#TODO: replace "blank" with small "poof"/disappear animation
#TODO: improve feedback; hover and click state for the buttons