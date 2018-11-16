from pico2d import*
import random
import time
from monster import Spirit , Spirit2 , Triangle
from monster import QKrzbals
from monster import Dust


run_time = 0.0
jump = 0.0
jump_real = False
start_menu = True
jump_up=False
jump_down=False

def handle_event():
    global running, start_menu, jump, jump_real, run_time, jump_up
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            start_menu = False
            if jump_real == False:
                if event.key == SDLK_SPACE:
                   jump = time.time()*300
                   jump_up = True
        elif event.type == SDL_KEYUP:
                if event.key == SDLK_SPACE:
                    run_time = time.time()*300 - jump
                    if run_time < 10:
                        run_time = 50
                    if run_time > 400:
                        run_time = 400
                    jump_real = True


pinkbean = None
pinkbeanX, pinkbeanY = 100, 77

open_canvas(760, 570)

monsters = Spirit()
mon = QKrzbals()
dust = Dust()
spirit=Spirit2()
triangle=Triangle()

background_1= load_image('배경/back1.png')
background_2 = load_image('배경/back1.png')

pinkbean = load_image('움직이는 핑크빈/pinkbean.png')
pinkbean_jump = load_image('움직이는 핑크빈/shet.png')
pinkbean_start = load_image('배경빈/start.jpg')
pinkbean_start1 = load_image('배경빈/startt.jpg')
bar = load_image('배경/bar.png')
minibean=load_image('배경빈/bean.png')
end_file=load_image('배경/end.png')

tile1 = load_image('타일/lt1.png')
tile2 = load_image('타일/lt2.png')
tile3 = load_image('타일/lt3.png')
# spirit1=load_image('정령/1.png')
# spirit2=load_image('정령/2.png')
# spirit3=load_image('정령/3.png')
# spirit4=load_image('정령/4.png')
# spirit_white = load_image('정령/조그만 2.png')

start = load_image('배경빈/startpink.png')


# x=0
# y=1
push_tile = 0
x = 0
run_tile=0
tiles = [tile1, tile2, tile3]

background_x = 760//2
background_x_2 = 1109 + 760/2
bean = 40
image_x = 0
y = 79
running = True
tile_ID = random.randint(0, 2)
up = 0
while running:
    clear_canvas()
    if start_menu:
        delay(0.05)
        handle_event()
        timercook = int(time.time())%2
        if(timercook == 1):
            pinkbean_start.clip_draw(0,0,480,360,760/2,570/2, 760, 570)
        if(timercook == 0):
            pinkbean_start1.clip_draw(0,0,480,360,760/2,570/2, 760, 570)
        update_canvas()
        continue
    background_1.clip_draw(0, 0, 1109, 570, background_x, 570/2)
    background_2.clip_draw(0, 0, 1109, 570, background_x_2, 570 / 2)
    minibean.clip_draw(0, 0, 25, 25, bean, 530)
    x += 10
    bar.clip_draw(0,0,400,365,200,400)
    #minibean.clip_draw(0,0,25,25,40,530)
    monsters.draw()
    monsters.update()
    mon.draw()
    mon.update()
    dust.draw()
    dust.update()
    spirit.draw()
    spirit.update()
    triangle.draw()
    triangle.update()
    if x == 90:
        x = 0
    for push_tile in range(10):
        tiles[tile_ID].clip_draw(0, 0, 90, 40, push_tile * 90 - x, 21)


    if jump_real:
        if jump_up:
            up += 25
        else:
            up -= 25
        if up >= run_time:
            jump_up = False
            jump_down = True

        if not jump_up and up <= 0:
            jump = 0
            up = 0
            jump_real = False
            jump_up = False
            jump_down = False

        pinkbean_jump.clip_draw(153 * image_x, 0, 153, 141, 130, y+up ,153,130)
    else:
        pinkbean.clip_draw(102 * image_x, 0, 100, 141, 100, y)
    update_canvas()

    if bean == 5:
        clear_canvas()
        end_file.clip_draw(0, 0, 740, 380, 760, 570)
    delay(0.05)
    handle_event()
    image_x = (image_x + 1) % 8
    background_x -= 0.8
    background_x_2 -= 0.8
    bean += 0.1
    if background_x < -1109/2:
        background_x = 1109 + 760/2
    if background_x_2 < -1109 / 2:
        background_x_2 = 1109 + 760 / 2


# while(x<1600):
#     if y==1:
#         a.draw_now(557-z,410)
#         while (v<800):
#             v = v + 59
#             if(vv>59):
#                 vv=0
#             t3.draw(v-vv,17)
#         p1.draw(100,77)
#         update_canvas()
#         y = 2
#         x = x + 2
#         z = z + 1
#         v=0
#         vv = vv + 6
#         delay(0.05)
#         clear_canvas()
#         get_events()
#     if (y == 2):
#         a.draw_now(557-z, 410)
#         while (v<800):
#             v = v + 59
#             if (vv>59):
#                 vv = 0
#             t3.draw(v-vv,17)
#         p2.draw(100, 77)
#         update_canvas()
#         y = 3
#         x=x+2
#         z = z + 1
#         v=0
#         vv = vv + 6
#         delay(0.05)
#         clear_canvas()
#         get_events()
#     if (y == 3):
#         a.draw_now(557-z, 410)
#         while (v<800):
#             v = v + 59
#             if (vv>59):
#                 vv = 0
#             t3.draw(v-vv,17)
#         p3.draw(100, 77)
#         update_canvas()
#         y = 4
#         x=x+2
#         z = z + 1
#         v=0
#         vv = vv + 6
#         delay(0.05)
#         clear_canvas()
#         get_events()
#     if (y == 4):
#         a.draw_now(557-z, 410)
#         while (v<800):
#             v = v + 59
#             if (vv>59):
#                 vv = 0
#             t3.draw(v-vv,17)
#         p4.draw(100, 77)
#         update_canvas()
#         y = 5
#         x=x+2
#         z = z + 1
#         v = 0
#         vv = vv + 6
#         delay(0.05)
#         clear_canvas()
#         get_events()
#     if (y == 5):
#         a.draw_now(557-z,410)
#         while (v<800):
#             v = v + 59
#             if(vv>59):
#                 vv=0
#             t3.draw(v-vv,17)
#         p5.draw(100, 77)
#         update_canvas()
#         y = 6
#         x=x+2
#         z = z + 1
#         v = 0
#         vv = vv + 6
#         delay(0.05)
#         clear_canvas()
#         get_events()
#     if (y == 6):
#         a.draw_now(557-z,410)
#         while (v<800):
#             v = v + 59
#             if (vv>59):
#                 vv = 0
#             t3.draw(v-vv,17)
#         p6.draw(100, 77)
#         update_canvas()
#         y = 7
#         x=x+2
#         z = z + 1
#         v = 0
#         vv = vv + 6
#         delay(0.05)
#         clear_canvas()
#         get_events()
#     if (y == 7):
#         a.draw_now(557-z,410)
#         while (v<800):
#             v = v + 59
#             if (vv>59):
#                 vv = 0
#             t3.draw(v-vv,17)
#         p7.draw(100, 77)
#         update_canvas()
#         y = 8
#         x=x+2
#         z = z + 1
#         v = 0
#         vv = vv + 6
#         delay(0.05)
#         clear_canvas()
#         get_events()
#     if (y == 8):
#         a.draw_now(557-z,410)
#         while (v<800):
#             v = v + 59
#             if (vv>59):
#                 vv = 0
#             t3.draw(v-vv,17)
#         p8.draw(100, 77)
#         update_canvas()
#         y = 9
#         x = x + 2
#         z = z + 1
#         v = 0
#         vv = vv + 6
#         delay(0.05)
#         clear_canvas()
#         get_events()
#     if (y == 9):
#         a.draw_now(557-z,410)
#         while (v<800):
#             v = v + 59
#             if (vv>59):
#                 vv = 0
#             t3.draw(v-vv,17)
#         p7.draw(100, 77)
#         update_canvas()
#         y = 10
#         x = x + 2
#         z = z + 1
#         v = 0
#         vv = vv + 6
#         delay(0.05)
#         clear_canvas()
#         get_events()
#     if (y == 10):
#         a.draw_now(557-z,410)
#         while (v<800):
#             v = v + 59
#             if (vv>59):
#                 vv = 0
#             t3.draw(v-vv,17)
#         p6.draw(100, 77)
#         update_canvas()
#         y = 11
#         x = x + 2
#         z = z + 1
#         v = 0
#         vv = vv + 6
#         delay(0.05)
#         clear_canvas()
#         get_events()
#     if (y == 11):
#         a.draw_now(557-z,410)
#         while (v<800):
#             v = v + 59
#             if(vv>59):
#                 vv=0
#             t3.draw(v-vv,17)
#         p5.draw(100, 77)
#         update_canvas()
#         y = 12
#         x = x + 2
#         z = z + 1
#         v = 0
#         vv = vv + 6
#         delay(0.05)
#         clear_canvas()
#         get_events()
#     if (y == 12):
#         a.draw_now(557-z,410)
#         while (v<800):
#             v = v + 59
#             if (vv>59):
#                 vv = 0
#             t3.draw(v-vv,17)
#         p4.draw(100, 77)
#         update_canvas()
#         y = 13
#         x = x + 2
#         z = z + 1
#         v = 0
#         vv = vv + 6
#         delay(0.05)
#         clear_canvas()
#         get_events()
#     if (y == 13):
#         a.draw_now(557-z,410)
#         while (v<800):
#             v = v + 59
#             if (vv> 59):
#                 vv = 0
#             t3.draw(v-vv,17)
#         p3.draw(100, 77)
#         update_canvas()
#         y = 14
#         x = x + 2
#         z = z + 1
#         v = 0
#         vv = vv + 6
#         delay(0.05)
#         clear_canvas()
#         get_events()
#     if (y == 14):
#         a.draw_now(557-z,410)
#         while (v<800):
#             v = v + 59
#             if (vv > 59):
#                 vv = 0
#             t3.draw(v-vv,17)
#         p2.draw(100, 77)
#         update_canvas()
#         y = 2
#         x = x + 2
#         z = z + 1
#         v = 0
#         vv = vv + 6
#         delay(0.05)
#         clear_canvas()
#         get_events()

close_canvas()
