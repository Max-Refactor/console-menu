import msvcrt
import os


class menu:
    def __init__(self, items: list):
        self.active_item = 0
        self.items = items

        self.current_item_name = self.items[self.active_item]
    
    def clear(self):
        os.system("clear" if os.name != "nt" else "cls")
    
    def show(self, clear_screen: bool = True):
        if clear_screen: self.clear()
        for item in range(len(self.items)):
            self.current_item_name = self.items[item]
            if self.active_item == item: print(f"\033[31m> \033[47;30m{self.current_item_name}\033[m")
            else: print(f"\033[0m  {self.current_item_name}")
    
    def run(self, clear_screen: bool = True):
        while True:
            self.show(clear_screen=clear_screen)
            key = msvcrt.getch()

            if key == b'H':
                if self.active_item <=0:
                    self.active_item = len(self.items) - 1
                else:
                    self.active_item -= 1
            elif key == b'P':
                if self.active_item >= len(self.items) -1:
                    self.active_item = 0
                else:
                    self.active_item += 1
            elif key == b'\r':
                self.clear()
                self.current_item_name = self.items[self.active_item]
                return self.current_item_name
            elif key == b'\x1b':
                break


if __name__ == "__main__":
    answer = menu(["Hello!", "Goodbye!"]).run()
    if answer == "Hello!":
        print("How are you?")
        input()
        answer2 = menu(["I'm fine.", "Goodbye!"]).run()
    else:
        if answer is not None:
            print(answer)
