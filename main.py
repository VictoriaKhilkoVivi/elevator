from PIL import Image, ImageDraw


WIDTH = 1200
HEIGHT = 1200
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
DOWN_POSITION = 1200
LENGTH = 100
LENGTH_FLOOR = 1200 // 6
DOWN_POSITION_HIGH_BUTTON = DOWN_POSITION - LENGTH_FLOOR*3//4
STEP = -10
FLOORS = [1, 2, 3, 4, 5, 6]


def draw_img(position_down_of_elevator, floor=None, fall=None):
    if not fall:
        phone = BLACK
    else:
        phone = RED

    image = Image.new('RGB', (WIDTH, HEIGHT), phone)
    draw = ImageDraw.Draw(image)

    #линии этажей
    for y_floor in range(DOWN_POSITION-LENGTH_FLOOR, 0, -LENGTH_FLOOR):
        draw.rectangle(((0, y_floor-15), (WIDTH, y_floor+15)), fill=BLUE)

    #кнопки на этаже
    for y_button in range(DOWN_POSITION_HIGH_BUTTON, 0, -LENGTH_FLOOR):
        draw.rectangle(((750, y_button), (850, y_button+LENGTH_FLOOR//2)), fill=WHITE)
        draw.ellipse(((785, y_button+35), (815, y_button+LENGTH_FLOOR//2-35)), fill=BLACK)

    if floor in FLOORS:
        center = 100 + (6-floor)*LENGTH_FLOOR
        draw.ellipse(((795, center-10), (805, center+10)), fill=GREEN)

    #трос лифта
    if not fall:
        draw.rectangle(((595, 0),
                        (605, position_down_of_elevator - LENGTH)), fill=WHITE)
    else:
        draw.rectangle(((595, 0),
                        (605, fall-LENGTH)), fill=WHITE)

    #лифт
    draw.rectangle(((575, position_down_of_elevator - LENGTH),
                    (625, position_down_of_elevator)), fill=WHITE)
    images.append(image)


if __name__ == '__main__':
    images = []
    floor = int(input())
    if floor == 1:
        position_up_of_elevator = 1191
    else:
        position_up_of_elevator = DOWN_POSITION - 50 - (floor-1)*LENGTH_FLOOR

    for position_down_of_elevator in range(DOWN_POSITION, position_up_of_elevator, STEP):
        if position_down_of_elevator == DOWN_POSITION:
            for j in range(DOWN_POSITION, LENGTH, STEP):
                if j == 600//2:
                    for h in range(10):
                        draw_img(position_down_of_elevator, floor)

                draw_img(position_down_of_elevator)

        draw_img(position_down_of_elevator)

        if position_down_of_elevator + STEP == position_up_of_elevator and floor != 1:
            for falling in range(position_down_of_elevator,
                                 position_down_of_elevator+LENGTH_FLOOR//8,
                                 10):
                draw_img(falling, fall=position_down_of_elevator)

            for falling in range(position_down_of_elevator+LENGTH_FLOOR//8,
                                 position_down_of_elevator+LENGTH_FLOOR//4,
                                 1):
                draw_img(falling, fall=position_down_of_elevator)

    images[0].save(
        'test.gif',
        save_all=True,
        append_images=images[1:],
        optimize=False,
        duration=40,
        loop=0
    )
