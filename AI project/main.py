import pygame
from pyamaze import maze
from collections import deque
from queue import PriorityQueue
import random
import time

start=[]
Buttons =[]
pygame.init()
font_path = pygame.font.match_font('arial')
font = pygame.font.Font(font_path, 18)
imgsstart = []
imgsgoal=[]
z=0
n =random.randint(5,14)
MazeWidth =n
MazeHeight = n
m = maze(MazeHeight, MazeWidth)
m.CreateMaze()
pos=(0,0)
black =(0,0,0)
red =(128,0,0)
green =(0,128,0)
blue = (0,0,128)
white=(255,255,255)
yellow = (255,255,51)
darkRed = (139,0,0)
rectangles= []
lines = []
rec =50
reci = 0
image_path = "C:\AI project\AI project\mouse-21693.png"
mouse= pygame.image.load(image_path)
scaled_image = pygame.Surface((rec, rec))
pygame.transform.scale(mouse, (rec, rec), scaled_image)

image_pathft="C:\AI project\AI project\dog-pawprints.png"
ftimage= pygame.image.load(image_pathft)
scaled_imageft = pygame.Surface((rec//2, rec//2))
pygame.transform.scale(ftimage, (rec//2, rec//2), scaled_imageft)

image_pathch ="C:\AI project\AI project\cheese (2).png"
cheese= pygame.image.load(image_pathch)
scaled_imagech = pygame.Surface((rec, rec))
pygame.transform.scale(cheese, (rec, rec), scaled_imagech)

 # Draw the scaled image onto the screen


Width, Height = 1000,800



win = pygame.display.set_mode((Width, Height))


pygame.display.set_caption("My Game!")
FPS = 60


def genrate_maze():
    n = random.randint(5,14)
    MazeWidth = n
    print("mazewidth afterge")
    print(MazeWidth)
    MazeHeight = n
    m = maze(MazeHeight, MazeWidth)
    m.CreateMaze()
    draw(MazeWidth,MazeHeight)
    MazeWidth

def draw_window():
    win.fill((255, 255, 255))

def draw(MazeWidth,MazeHeight):
    x = 50
    y = 50


    for i in range (1,MazeHeight+1):
        for j in range(1, MazeWidth+1):
            pygame.draw.rect(win,red, pygame.Rect(x ,  y, rec, rec))
            rectangles.append({"x":x,"y":y,"currCell":(j,i),"color":red})
            y+=rec
        y=50
        x+=rec

    x = 50
    y = 50


    for i in range (1,MazeHeight+1):
        for j in range(1, MazeWidth+1):
            currCell = (j,i)
            for d in 'ESNW':
                print(MazeWidth)
                if m.maze_map[currCell][d] == False:
                    if d == 'E':
                        pygame.draw.line(win, white, (x+rec ,y), (x+rec,y+rec) , width=3)
                        lines.append({"xs":x+rec,"ys": y, "xe":x+rec,"ye":y+rec,"ccell":currCell})
                    if d == 'W':
                        pygame.draw.line(win, white, (x ,y), (x,y+rec) , width=3)
                        lines.append({"xs":x,"ys": y, "xe":x,"ye":y+rec,"ccell":currCell})

                    if d == 'N':
                        pygame.draw.line(win, white, (x,y), (x+rec,y) , width=3)
                        lines.append({"xs":x,"ys": y, "xe":x+rec,"ye":y,"ccell":currCell})

                    if d == 'S':
                        pygame.draw.line(win, white, (x, y+rec), (x + rec, y+rec), width=3)
                        lines.append({"xs":x,"ys": y+rec, "xe":x+rec,"ye":y+rec,"ccell":currCell})

            y += rec
        x += rec
        y=50

    x =0
    y=0

    for i in range (len(rectangles)):
        print(rectangles[i]["currCell"])
    print("------------------------")
    for i in range (len(lines)):
        print(lines[i]["ccell"])
    for i in range (0,len(start)):
        pygame.draw.rect(win,red, pygame.Rect(start[i]["x"], start[i]["y"], rec, rec))
    return rectangles,rec,lines




    for img in imgsgoal:
        win.blit(scaled_image, (img["x"], img["y"]))

    for img in imgsstart:
        win.blit(scaled_image, (img["x"], img["y"]))

    print(m.maze_map)


def DFS(flag,pressct):

    rectangles, rec, lines = draw(MazeWidth,MazeHeight)
    pos = pygame.mouse.get_pos()
    fpress=0
    pressrect = {}

    win.blit(scaled_image, (imgsstart[0]["x"], imgsstart[0]["y"]))
    win.blit(scaled_imagech, (imgsgoal[0]["x"], imgsgoal[0]["y"]))

    if (len(start) > 0):

        explored = [start[0]["cell"]] #visited
        frontier = [start[0]["cell"]] #fringe
        dfsPath = {}
        dSearch = []
        while len(frontier) > 0:
            currCell = frontier.pop()
            dSearch.append(currCell)
            if currCell == start[-1]["cell"]:  #check goal
                break
            poss = 0
            for d in 'ESNW':
                if m.maze_map[currCell][d] == True:
                    if d == 'E':
                        child = (currCell[0], currCell[1] + 1)

                    if d == 'W':
                        child = (currCell[0], currCell[1] - 1)
                    if d == 'N':
                        child = (currCell[0] - 1, currCell[1])
                    if d == 'S':
                        child = (currCell[0] + 1, currCell[1])
                    if child in explored:
                        continue
                    poss += 1
                    explored.append(child)
                    frontier.append(child)
                    dfsPath[child] = currCell

            destination = start[-1]["cell"]
            path = [destination]

            while path[-1] != start[0]["cell"]:
                current_cell = path[-1]
                if current_cell in dfsPath:
                    parent_cell = dfsPath[current_cell]
                    path.append(parent_cell)
                else:
                    break




            path.reverse()
            print("pathhhhhhhhhhhhhh")
            print(path)
            print("searchhhhhh")

            print(dSearch)
        for i in range(1,len(dSearch)-1):
            for x in range(len(rectangles)):
                if dSearch[i] == rectangles[x]["currCell"]:
                    #pygame.draw.rect(win, green,
                                  #   pygame.Rect(rectangles[x]["x"], rectangles[x]["y"], rec - 6, rec - 6))

                    win.blit(scaled_imageft, (rectangles[x]["x"]+(rec//4), rectangles[x]["y"]+(rec//4)))
                    pygame.display.update()
                    time.sleep(0.05)  # Adjust the delay time as needed
              # Update the display after drawing all rectangles for each cell

        for i in range(1, len(path)-1):
            for x in range(len(rectangles)):
                if path[i] == rectangles[x]["currCell"]:
                    pygame.draw.rect(win, black,
                                     pygame.Rect(rectangles[x]["x"]+(rec//4), rectangles[x]["y"]+(rec//4), rec//2 , rec//2 ))
                    pygame.display.update()
                      # Adjust the delay time as needed

        pygame.display.update()

def BFS(flag,pressct):
    rectangles, rec, lines = (draw(MazeWidth,MazeHeight))
    pos = pygame.mouse.get_pos()
    pressrec ={}
    flagpress=0


    win.blit(scaled_image, (imgsstart[0]["x"], imgsstart[0]["y"]))
    win.blit(scaled_imagech, (imgsgoal[0]["x"], imgsgoal[0]["y"]))


    if (len(start) > 0):
        explored = [start[0]["cell"]]
        frontier = deque([start[0]["cell"]])
        bfsPath = {}
        dSearch = []

        while len(frontier) > 0:
            currCell = frontier.popleft()
            dSearch.append(currCell)

            if currCell == start[-1]["cell"]:
                break

            for d in 'ESNW':
                if m.maze_map[currCell][d]:
                    if d == 'E':
                        child = (currCell[0], currCell[1] + 1)
                    elif d == 'W':
                        child = (currCell[0], currCell[1] - 1)
                    elif d == 'N':
                        child = (currCell[0] - 1, currCell[1])
                    elif d == 'S':
                        child = (currCell[0] + 1, currCell[1])

                    if child in explored:
                        continue

                    explored.append(child)
                    frontier.append(child)
                    bfsPath[child] = currCell

        destination = start[-1]["cell"]
        path = [destination]

        while path[-1] != start[0]["cell"]:
            current_cell = path[-1]

            if current_cell in bfsPath:
                parent_cell = bfsPath[current_cell]
                path.append(parent_cell)
            else:
                break


        path.reverse()
        print("pathhhhhhhhhhhhhh")
        print(path)
        print("searchhhhhh")

        print(dSearch)
        for i in range(1, len(dSearch)-1):
            for x in range(len(rectangles)):
                if dSearch[i] == rectangles[x]["currCell"]:
                    win.blit(scaled_imageft, (rectangles[x]["x"] + (rec // 4), rectangles[x]["y"] + (rec // 4)))
                    pygame.display.update()
                    time.sleep(0.05)

        for i in range(1, len(path)-1):
            for x in range(len(rectangles)):
                if path[i] == rectangles[x]["currCell"]:
                    pygame.draw.rect(win, black,
                                     pygame.Rect(rectangles[x]["x"]+(rec//4), rectangles[x]["y"]+(rec//4), rec//2 , rec//2 ))
                    pygame.display.update()


        pygame.display.update()


def h(cell1, cell2):
    x1, y1 = cell1
    x2, y2 = cell2
    return (abs(x1 - x2) + abs(y1 - y2))

def aStar(flag,pressct):
    rectangles, rec, lines =draw(MazeWidth,MazeHeight)
    pos = pygame.mouse.get_pos()
    flagpress = 0
    g_score= {}
    f_score ={}

    win.blit(scaled_image, (imgsstart[0]["x"], imgsstart[0]["y"]))
    win.blit(scaled_imagech, (imgsgoal[0]["x"], imgsgoal[0]["y"]))



    if(len(start))>0:
        open = PriorityQueue()
        open.put((h(start[0]["cell"],start[-1]["cell"]), h(start[0]["cell"],start[-1]["cell"]), start[0]["cell"]))
        aPath = {}

        for i in range(len(rectangles)):
            g_score[rectangles[i]["currCell"]] = 999999999999

        for i in range(len(rectangles)):
            f_score[rectangles[i]["currCell"]] = 999999999999

        g_score[start[0]["cell"]] = 0
        f_score[start[0]["cell"]] = h(start[0]["cell"], start[-1]["cell"])
        searchPath=[start[0]["cell"]]


        while not open.empty():
            currCell = open.get()[2]
            searchPath.append(currCell)
            if currCell == start[-1]["cell"]:
                break
            for d in 'ESNW':
                if m.maze_map[currCell][d]==True:
                    if d=='E':
                        childCell=(currCell[0],currCell[1]+1)
                    elif d=='W':
                        childCell=(currCell[0],currCell[1]-1)
                    elif d=='N':
                        childCell=(currCell[0]-1,currCell[1])
                    elif d=='S':
                        childCell=(currCell[0]+1,currCell[1])

                    temp_g_score = g_score[currCell] + 1
                    temp_f_score = temp_g_score + h(childCell, start[-1]["cell"])


                    if temp_f_score < f_score[childCell]:
                        aPath[childCell] = currCell
                        g_score[childCell] = temp_g_score
                        f_score[childCell] = temp_g_score + h(childCell, start[-1]["cell"])
                        open.put((f_score[childCell], h(childCell, start[-1]["cell"]), childCell))

        destination = start[-1]["cell"]
        path = [destination]

        while path[-1] != start[0]["cell"]:
            current_cell = path[-1]

            if current_cell in aPath:
                parent_cell = aPath[current_cell]
                path.append(parent_cell)
            else:
                break


        path.reverse()
        print("pathhhhhhhhhhhhhh")
        print(path)
        print("searchhhhhh")
        print(searchPath)
        print("gggggggggggggggg")

        print(g_score)
        print("fffffffffffff")
        print(f_score)

        for i in range(2, len(searchPath)-1):
            for x in range(len(rectangles)):
                if searchPath[i] == rectangles[x]["currCell"]:
                    win.blit(scaled_imageft, (rectangles[x]["x"]+(rec//4), rectangles[x]["y"]+(rec//4)))
                    pygame.display.update()
                    time.sleep(0.05)

        for i in range(1, len(path)-1):
            for x in range(len(rectangles)):
                if path[i] == rectangles[x]["currCell"]:
                    pygame.draw.rect(win, black,
                                     pygame.Rect(rectangles[x]["x"]+(rec//4), rectangles[x]["y"]+(rec//4), rec//2 , rec//2 ))
                    pygame.display.update()

        pygame.display.update()


def greedy(flag,pressct):
    rectangles, rec, lines = draw(MazeWidth, MazeHeight)
    pos = pygame.mouse.get_pos()
    flagpress = 0
    g_score = {}
    f_score = {}

    win.blit(scaled_image, (imgsstart[0]["x"], imgsstart[0]["y"]))
    win.blit(scaled_imagech, (imgsgoal[0]["x"], imgsgoal[0]["y"]))

    if (len(start)) > 0:
        open = PriorityQueue()
        open.put(( h(start[0]["cell"], start[-1]["cell"]), start[0]["cell"]))
        aPath = {}

        for i in range(len(rectangles)):
            f_score[rectangles[i]["currCell"]] = 999999999999


        f_score[start[0]["cell"]] = h(start[0]["cell"], start[-1]["cell"])
        searchPath = [start[0]["cell"]]

        while not open.empty():
            currCell = open.get()[2]
            searchPath.append(currCell)
            if currCell == start[-1]["cell"]:
                break
            for d in 'ESNW':
                if m.maze_map[currCell][d] == True:
                    if d == 'E':
                        childCell = (currCell[0], currCell[1] + 1)
                    elif d == 'W':
                        childCell = (currCell[0], currCell[1] - 1)
                    elif d == 'N':
                        childCell = (currCell[0] - 1, currCell[1])
                    elif d == 'S':
                        childCell = (currCell[0] + 1, currCell[1])


                    temp_f_score =  h(childCell, start[-1]["cell"])

                    if temp_f_score < f_score[childCell]:
                        aPath[childCell] = currCell
                        f_score[childCell] = h(childCell, start[-1]["cell"])
                        open.put(( h(childCell, start[-1]["cell"]), childCell))

        destination = start[-1]["cell"]
        path = [destination]

        while path[-1] != start[0]["cell"]:
            current_cell = path[-1]

            if current_cell in aPath:
                parent_cell = aPath[current_cell]
                path.append(parent_cell)
            else:
                break


        path.reverse()
        print("pathhhhhhhhhhhhhh")
        print(path)
        print("searchhhhhh")
        print(searchPath)
        print("gggggggggggggggg")

        print(g_score)
        print("fffffffffffff")
        print(f_score)

        for i in range(2, len(searchPath) - 1):
            for x in range(len(rectangles)):
                if searchPath[i] == rectangles[x]["currCell"]:
                    win.blit(scaled_imageft, (rectangles[x]["x"] + (rec // 4), rectangles[x]["y"] + (rec // 4)))
                    pygame.display.update()
                    time.sleep(0.05)

        for i in range(1, len(path) - 1):
            for x in range(len(rectangles)):
                if path[i] == rectangles[x]["currCell"]:
                    pygame.draw.rect(win, black,
                                     pygame.Rect(rectangles[x]["x"] + (rec // 4), rectangles[x]["y"] + (rec // 4),
                                                 rec // 2, rec // 2))
                    pygame.display.update()


        pygame.display.update()
def uniform(flag,pressct):
    rectangles, rec, lines = draw(MazeWidth, MazeHeight)
    pos = pygame.mouse.get_pos()
    flagpress = 0
    g_score = {}
    f_score = {}

    win.blit(scaled_image, (imgsstart[0]["x"], imgsstart[0]["y"]))
    win.blit(scaled_imagech, (imgsgoal[0]["x"], imgsgoal[0]["y"]))

    if len(start) > 0:
        open = PriorityQueue()
        open.put((0, start[0]["cell"]))
        aPath = {}

        g_score[start[0]["cell"]] = 0
        searchPath = [start[0]["cell"]]

        while not open.empty():
            _, currCell = open.get()
            searchPath.append(currCell)
            if currCell == start[-1]["cell"]:
                break
            for d in 'ESNW':
                if m.maze_map[currCell][d]:
                    if d == 'E':
                        childCell = (currCell[0], currCell[1] + 1)
                    elif d == 'W':
                        childCell = (currCell[0], currCell[1] - 1)
                    elif d == 'N':
                        childCell = (currCell[0] - 1, currCell[1])
                    elif d == 'S':
                        childCell = (currCell[0] + 1, currCell[1])

                    temp_g_score = g_score[currCell] + 1

                    if temp_g_score < g_score.get(childCell, float('inf')):
                        aPath[childCell] = currCell
                        g_score[childCell] = temp_g_score

                        open.put((temp_g_score, childCell))

        destination = start[-1]["cell"]
        path = [destination]

        while path[-1] != start[0]["cell"]:
            current_cell = path[-1]

            if current_cell in aPath:
                parent_cell = aPath[current_cell]
                path.append(parent_cell)
            else:
                break


        path.reverse()
        print("pathhhhhhhhhhhhhh")
        print(path)
        print("searchhhhhh")
        print(searchPath)
        print("gggggggggggggggg")

        print(g_score)

        for i in range(2, len(searchPath) - 1):
            for x in range(len(rectangles)):
                if searchPath[i] == rectangles[x]["currCell"]:
                    win.blit(scaled_imageft, (rectangles[x]["x"] + (rec // 4), rectangles[x]["y"] + (rec // 4)))
                    pygame.display.update()
                    time.sleep(0.05)

        for i in range(1, len(path) - 1):
            for x in range(len(rectangles)):
                if path[i] == rectangles[x]["currCell"]:
                    pygame.draw.rect(win, black,
                                     pygame.Rect(rectangles[x]["x"] + (rec // 4), rectangles[x]["y"] + (rec // 4),
                                                 rec // 2, rec // 2))
                    pygame.display.update()
        pygame.display.update()


def highlitblock():

    mpos= pygame.mouse.get_pos()
    x,y= mpos[0],mpos[1]
    therec = {}
    frec =0
    ctime = 0
    for item in rectangles:
        if x > item["x"] and item["x"] +rec>x and y> item["y"]and y<item["y"]+rec:
            item["color"] = blue
            therec = item
            pygame.draw.rect(win, item["color"], pygame.Rect(item["x"], item["y"], rec, rec))
            frec=1



    if frec ==1:
        therec["color"] =red
        pygame.draw.rect(win, therec["color"], pygame.Rect(therec["x"], therec["y"], rec, rec))














    print()

def buttons():


    button_x = 820
    button_y = 150
    button_width = 100
    button_height = 50

    Buttons.append({"x": button_x, "y": button_y, "w": button_width, "h": button_height})

    pygame.draw.rect(win, red, (button_x, button_y, button_width, button_height))
    text_surface = font.render('DFS', True, white)
    text_rect = text_surface.get_rect(center=(button_x + button_width // 2, button_y + button_height // 2))
    win.blit(text_surface, text_rect)

    button_x = 820
    button_y = 250
    button_width = 100
    button_height = 50

    Buttons.append({"x": button_x, "y": button_y, "w": button_width, "h": button_height})

    pygame.draw.rect(win, red, (button_x, button_y, button_width, button_height))
    text_surface = font.render('BFS', True, white)
    text_rect = text_surface.get_rect(center=(button_x + button_width // 2, button_y + button_height // 2))
    win.blit(text_surface, text_rect)

    button_x = 820
    button_y = 350
    button_width = 100
    button_height = 50

    Buttons.append({"x": button_x, "y": button_y, "w": button_width, "h": button_height})

    pygame.draw.rect(win, red, (button_x, button_y, button_width, button_height))
    text_surface = font.render('A*', True, white)
    text_rect = text_surface.get_rect(center=(button_x + button_width // 2, button_y + button_height // 2))
    win.blit(text_surface, text_rect)

    button_x = 820
    button_y = 450
    button_width = 100
    button_height = 50

    Buttons.append({"x": button_x, "y": button_y, "w": button_width, "h": button_height})

    pygame.draw.rect(win, red, (button_x, button_y, button_width, button_height))
    text_surface = font.render('Uniform', True, white)
    text_rect = text_surface.get_rect(center=(button_x + button_width // 2, button_y + button_height // 2))
    win.blit(text_surface, text_rect)

    pygame.display.update()

def check(pressct):
    fpress=0

    pos= pygame.mouse.get_pos()
    pressrect ={}
    for rect in rectangles:
        if rect["x"] <= pos[0] <= rect["x"] + rec and rect["y"] <= pos[1] <= rect["y"] + rec:
            for line in lines:
                if not (line["xs"] <= pos[0] <= line["xe"] and line["ys"] <= pos[1] <= line["ye"]):
                    pressrect = rect
                    if pressct == 1:
                        imgsstart.append({"x": pressrect["x"], "y": pressrect["y"]})
                    if pressct == 2:
                        imgsgoal.append({"x": pressrect["x"], "y": pressrect["y"]})
                    print("inside lines")

                    fpress = 1

    if pressct == 1 and fpress == 1:
        win.blit(scaled_image, (imgsstart[0]["x"], imgsstart[0]["y"]))
        start.append({"x": pressrect["x"], "y": pressrect["y"], "cell": pressrect["currCell"]})

    if pressct == 2 and fpress == 1:
        win.blit(scaled_image, (imgsstart[0]["x"], imgsstart[0]["y"]))
        print("inside line 2")

        win.blit(scaled_imagech, (imgsgoal[0]["x"], imgsgoal[0]["y"]))
        start.append({"x": pressrect["x"], "y": pressrect["y"], "cell": pressrect["currCell"]})

    pygame.display.update()

draw(MazeWidth,MazeHeight)
buttons()

def main():
    run = True
    flag=0
    clock = pygame.time.Clock()
    pressct=0
    current_time = 0

    while run:
        clock.tick(FPS)
        current_time = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type==pygame.MOUSEBUTTONDOWN:
                mouse_x = pygame.mouse.get_pos()[0]
                mouse_y = pygame.mouse.get_pos()[1]
                pressct+=1
                check(pressct)

                if pressct>=3:

                    for i in range(len(Buttons)):

                        if Buttons[i]["x"] <= mouse_x <= Buttons[i]["x"] + Buttons[i]["w"] and Buttons[i]["y"] <= mouse_y <=Buttons[i]["y"] + Buttons[i]["h"]:

                            current_time = 0
                            if i ==0:
                                DFS(flag,pressct)


                            if i==1:
                                BFS(flag,pressct)




                            if i ==2:

                                aStar(flag,pressct)

                            if i ==3:

                                uniform(flag,pressct)













        pygame.display.update()







if __name__== "__main__":
   main()
