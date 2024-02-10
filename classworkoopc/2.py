class Menu:
    def __init__(self, items):
        self.items = items
        self.cursor = 0 
    def to_the_right(self):
        if self.cursor < len(self.items) - 1:
            self.cursor += 1

    def display(self):
        displayed_items = [str(self.items[idx]) if idx != self.cursor else f"[{self.items[idx]}]" for idx in range(len(self.items))]
        return f"[{(', '.join(displayed_items))}]"

menu = Menu([1, 2, 3])

initial_display = menu.display()

menu.to_the_right()
display_after_first_move = menu.display()

menu.to_the_right()
display_after_second_move = menu.display()

print(initial_display, display_after_first_move, display_after_second_move,)