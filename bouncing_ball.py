def bouncing_ball(h: float, bounce: float, window: float) -> int:

    """
        This function solvel a taks below.

        TASK:
        A child is playing with a ball on the nth floor of a tall building. 
        The height of this floor, h, is known.

        He drops the ball out of the window. 
        The ball bounces (for example), to two-thirds of its height (a bounce of 0.66).

        His mother looks out of a window 1.5 meters from the ground.

        How many times will the mother see the ball pass in front of her window 
        (including when it's falling and bouncing?
    """

    if h > 0 and 0 < bounce < 1 and window < h:
        count = 0
        while h > window:
            h *= bounce
            count += 2
        else:
            return count-1
    else:
        return -1

print(bouncing_ball(3, 0.66, 1.5))
