import random
from sympy import *


def main():
    k = 5
    box = random.choice([empty_box, bomb_box])
    elitzur_vaidman_bomb_tester(k, box)


def elitzur_vaidman_bomb_tester(k, box):
    # qubit b
    b = [1, 0]

    for i in range(k):
        # haha, let's observe this qubit without measuring it, crime is my middle name
        print("Round", i, "with qubit", b)

        # rotate by (pi/2)/k
        eps = (pi / 2) / k
        rotate(b, eps)

        # pass through black box
        box(b)

    # measure qubit clasically
    res = measure(b)
    # if res is zero, bomb has measured our qubit each iteration, so there is a bomb
    # if res is one, the box has no bomb
    print(f"guess: {'no bomb' if res == 1 else 'bomb!!!'}")
    print(f"win:   {[bomb_box, empty_box][res] == box}")


def rotate(b, eps):
    b_a, b_b = b
    b[0] = simplify(cos(eps) * b_a - sin(eps) * b_b)
    b[1] = simplify(sin(eps) * b_a + cos(eps) * b_b)


def measure(b):
    # collapse b to 0 or 1
    prob_zero = abs(b[0]) ** 2
    if random.random() < prob_zero:
        b[0] = 1
        b[1] = 0
        return 0
    else:
        b[0] = 0
        b[1] = 1
        return 1


def bomb_box(b):
    if measure(b) == 1:
        print("KABOOM")
        exit()


def empty_box(b):
    pass


if __name__ == "__main__":
    main()
