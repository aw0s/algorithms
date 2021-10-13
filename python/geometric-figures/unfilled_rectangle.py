def draw_rectangle(length: int, width: int) -> None:
    horizontal_sides = (0, length - 1)  # sides indexing starts from 0
    for i in range(length):
        if i in horizontal_sides:
            print('*' * width)
        else:
            print(f"*{' ' * (width - 2)}*")


draw_rectangle(10, 20)
