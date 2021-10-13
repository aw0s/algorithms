def draw_triangle(base: int, height: int) -> None:
    for line_length in range(1, height, 2):
        print(f"{' ' * ((height - line_length) // 2)}{'*' * line_length}")


draw_triangle(10, 20)
