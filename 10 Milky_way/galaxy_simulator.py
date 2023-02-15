import tkinter as tk
from random import randint, uniform, random
import math

# MAIN ENTERING DATA ===============================================================

# radiowave bubble diameter
SCALE = 500  # enter 225 to see Earth radiowave buble diametre

# nuumber of developed civivlizations in Drake equation
NUM_CIVS = 156000

root = tk.Tk()
root.title("Milkyway galaxy")
c = tk.Canvas(root, width=1000, height=800, bg='black')
c.grid()
c.configure(scrollregion=root.bbox("all"))

# Milkyway size in light years
DISC_RADIUS = 50000
DISC_HEIGHT = 1000
DISC_VOL = math.pi * DISC_RADIUS * 2 * DISC_HEIGHT


def scale_galaxy():
    disc_radious_scaled = DISC_RADIUS / SCALE
    bubble_vol = 4 / 3 * math.pi * (SCALE / 2) ** 3
    disc_vol_scaled = DISC_VOL / bubble_vol

    return disc_radious_scaled, disc_vol_scaled


def detect_prob(disc_vol_scaled):
    ratio = NUM_CIVS / disc_vol_scaled
    if ratio < 0.002:
        detect_prob = 0
    elif ratio == 5:
        detect_prob = 1
    else:
        detect_prob = -0.004757 * ratio ** 4 + 0.06681 * ratio ** 3 - 0.3605 * \
                      ratio ** 2 + 0.9215 * ratio + 0.00826
    return round(detect_prob, 3)


def random_polar_coordinates(disc_radious_scaled):
    r = random()
    theta = uniform(0, 2 * math.pi)
    x = round(math.sqrt(r) * math.cos(theta) * disc_radious_scaled)
    y = round(math.sqrt(r) * math.sin(theta) * disc_radious_scaled)

    return x, y


def spirals(b, r, rot_fac, fuz_fac, arm):
    """
    b - constant in logatithmic spiral
    r - scaled galaxy radius
    rot_fac rotation coefficient
    fuz_fac random shift of a star in an arm
    """

    spiral_stars = []
    fuzz = int(0.030 * abs(r))
    theat_max_degree = 520
    for i in range(theat_max_degree):
        theta = math.radians(i)
        x = r * math.exp(b * theta) * math.cos(theta + math.pi) + randint(-fuzz, fuzz) + fuz_fac
        y = r * math.exp(b * theta) * math.sin(theta + math.pi) + randint(-fuzz, fuzz) + fuz_fac
        spiral_stars.append((x, y))

    for x, y in spiral_stars:
        if arm == 0 and int(x % 2) == 0:
            c.create_oval(x - 2, y - 2, x + 2, y + 2, fill='white', outline='')
        elif arm == 0 and int(x % 2) != 0:
            c.create_oval(x - 1, y - 1, x + 1, y + 1, fill='white', outline='')
        elif arm == 1:
            c.create_oval(x, y, x, y, fill='white', outline='')


def star_haze(disc_radious_scaled, density):
    x, y = random_polar_coordinates(disc_radious_scaled)
    c.create_text(x, y, fill='white', font=('Helvetica', '7'), text='.')


def main():
    """ Count probability of encounter and drow a galaxy"""

    disc_radious_scaled, disc_vol_scaled = scale_galaxy()
    detection_prob = detect_prob(disc_vol_scaled)

    spirals(b=0.3, r=disc_radious_scaled, rot_fac=2, fuz_fac=1.5, arm=0)

    spirals(b=0.3, r=disc_radious_scaled, rot_fac=1.91, fuz_fac=1.5, arm=1)
    spirals(b=0.3, r=-disc_radious_scaled, rot_fac=-2, fuz_fac=1.5, arm=0)
    spirals(b=0.3, r=-disc_radious_scaled, rot_fac=-2.09, fuz_fac=1.5, arm=1)
    spirals(b=0.3, r=-disc_radious_scaled, rot_fac=0.5, fuz_fac=1.5, arm=0)
    spirals(b=0.3, r=-disc_radious_scaled, rot_fac=0.4, fuz_fac=1.5, arm=1)
    spirals(b=0.3, r=-disc_radious_scaled, rot_fac=-0.5, fuz_fac=1.5, arm=0)
    spirals(b=0.3, r=-disc_radious_scaled, rot_fac=-0.6, fuz_fac=1.5, arm=1)
    star_haze(disc_radious_scaled, density=8)

    c.create_text(-455, -360, fill='white', anchor='w',
                  text=f'One pixel = {SCALE} light years')
    c.create_text(-455, -330, fill='white', anchor='w',
                  text=f'Probability of encounter for {NUM_CIVS} civilizations {detection_prob}')

    if SCALE == 225:
        c.create_rectangle(115, 75, 116, 76, fill='red', outline='')
        c.create_text(118, 72, fill='red', anchor='w', text='<----------- Earth radiobubble')


    root.mainloop()


if __name__ == '__main__':
    main()
