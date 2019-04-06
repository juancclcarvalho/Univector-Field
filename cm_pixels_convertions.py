from constants import Const

arena_w = Const.arena_w
arena_h = Const.arena_h

img_w = Const.img_w
img_h = Const.img_h

height_to_width = arena_w / arena_h
width_to_height = arena_h / arena_w

if img_w:
    convertion_factor = img_w / arena_w
elif img_h:
    convertion_factor = img_h / arena_h
else:
    convertion_factor = Const.default_convertion_factor


def setArenaSize():
    global img_w
    global img_h

    if not img_w and not img_h:
        img_w = arena_w
        img_h = arena_h

    elif not img_w:
        img_w = int(height_to_width * img_h)

    elif not img_h:
        img_h = int(width_to_height * img_w)

    elif img_w/arena_w != img_h/arena_h:
        print("The given dimensions are not proportional to the arena dimensions")
        img_w = arena_w
        img_h = arena_h

    return img_w, img_h

def convertToPixel(cm):
    return int(cm * convertion_factor)

def convertToCm(px):
    return int(px / convertion_factor)

def main():
    setArenaSize()
    print(img_w)
    print(img_h)
    print(convertToPixel(5.37))
    print(Const.de)

if __name__ == '__main__':
    main()
