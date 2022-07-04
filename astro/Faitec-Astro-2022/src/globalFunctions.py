
from operator import truediv


def click(mouse, screen_i, x_init, x_final, y_init, y_final):
    image_size_x = screen_i[0][0]
    image_size_y = screen_i[0][1]
    return (image_size_x*x_init/screen_i[1][0])<= mouse[0] <= (image_size_x*x_final/screen_i[1][0]) and (image_size_y*y_init/screen_i[1][1]) <= mouse[1] <=(image_size_y*y_final/screen_i[1][1])