class RubicksCube_3x3():
    #system functions
    """
    coding:
    white = 0
    red = 1
    orange = 2
    blue = 3
    green = 4
    yellow = 5
    """

    def _transform_array(self, array : list, inversely=False) -> list:
        if not inversely:
            self.transposed_array = list(zip(*array))
            return [list(row[::-1]) for row in self.transposed_array]
        else:
            self.transposed_array = list(zip(*array))
            return [list(row) for row in self.transposed_array[::-1]]

    def _print_for_printing_massive(self, args : list) -> None:
        for self.elem in range(len(args)):
                for self.i in range(len(args[self.elem])):
                    print(args[self.elem][self.i], end=' ')
                print(end='\n')
        print('\n')

    def _checking_side(self, side : list) -> bool:
        self.first_element = side[0][0]
        for self.row in side:
            for self.element in self.row:
                if self.element != self.first_element:
                    return False
        return True


    #user functions

    def __init__(self) -> None:
        #init rubickscube with default settings and colors
        self.down = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        self.front = [
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1],
        ]
        self.back = [
            [2, 2, 2],
            [2, 2, 2],
            [2, 2, 2],
        ]
        self.left = [
            [3, 3, 3],
            [3, 3, 3],
            [3, 3, 3]
        ]
        self.right = [
            [4, 4, 4],
            [4, 4, 4],
            [4, 4, 4],
        ]
        self.top = [
            [5, 5, 5],
            [5, 5, 5],
            [5, 5, 5],
        ]

    def is_solved(self) -> bool:
        return self._checking_side(self.down) and self._checking_side(self.front) \
            and self._checking_side(self.top) and self._checking_side(self.back) and \
            self._checking_side(self.left) and self._checking_side(self.right)


    def move_right(self, backward=False) -> None:
        self.temporary = [self.down[0][2], self.down[1][2], self.down[2][2]]

        if not backward:
            self.down[0][2], self.down[1][2], self.down[2][2] = self.back[2][0], self.back[1][0], self.back[0][0] 
            self.back[2][0], self.back[1][0], self.back[0][0]  = self.top[0][2], self.top[1][2], self.top[2][2]
            self.top[0][2], self.top[1][2], self.top[2][2] = self.front[0][2], self.front[1][2], self.front[2][2]
            self.front[0][2], self.front[1][2], self.front[2][2] = self.temporary
            self.right = self._transform_array(self.right)

        else:
            self.down[0][2], self.down[1][2], self.down[2][2] = self.front[0][2], self.front[1][2], self.front[2][2]
            self.front[0][2], self.front[1][2], self.front[2][2] = self.top[0][2], self.top[1][2], self.top[2][2]
            self.top[0][2], self.top[1][2], self.top[2][2] = self.back[2][0], self.back[1][0], self.back[0][0]
            self.back[2][0], self.back[1][0], self.back[0][0] = self.temporary
            self.right = self._transform_array(self.right, inversely=True)


    def move_top(self, backward=False) -> None:
        self.temporary = [self.front[0][0], self.front[0][1], self.front[0][2]]
        
        if not backward:
            self.front[0][0], self.front[0][1], self.front[0][2] = self.right[0][0], self.right[0][1], self.right[0][2]
            self.right[0][0], self.right[0][1], self.right[0][2] = self.back[0][0], self.back[0][1], self.back[0][2]
            self.back[0][0], self.back[0][1], self.back[0][2] = self.left[0][0], self.left[0][1], self.left[0][2]
            self.left[0][0], self.left[0][1], self.left[0][2] = self.temporary
            self.top = self._transform_array(self.top)
        
        else:
            self.front[0][0], self.front[0][1], self.front[0][2] = self.left[0][0], self.left[0][1], self.left[0][2]
            self.left[0][0], self.left[0][1], self.left[0][2] = self.back[0][0], self.back[0][1], self.back[0][2]
            self.back[0][0], self.back[0][1], self.back[0][2] = self.right[0][0], self.right[0][1], self.right[0][2]
            self.right[0][0], self.right[0][1], self.right[0][2] = self.temporary
            self.top = self._transform_array(self.top, inversely=True)


    def move_front(self, backward=False) -> None:
        self.temporary = [self.down[0][0], self.down[0][1], self.down[0][2]]
        if not backward:
            self.down[0][0], self.down[0][1], self.down[0][2] = self.right[2][0], self.right[1][0], self.right[0][0]
            self.right[2][0], self.right[1][0], self.right[0][0] = self.top[2][2], self.top[2][1], self.top[2][0]
            self.top[2][0], self.top[2][1], self.top[2][2] = self.left[2][2], self.left[1][2], self.left[0][2]
            self.left[0][2], self.left[1][2], self.left[2][2] = self.temporary
            self.front = self._transform_array(self.front)

        else:
            self.down[0][0], self.down[0][1], self.down[0][2] = self.left[0][2], self.left[1][2], self.left[2][2]
            self.left[0][2], self.left[1][2], self.left[2][2] = self.top[2][2], self.top[2][1], self.top[2][0]
            self.top[2][0], self.top[2][1], self.top[2][2] = self.right[0][0], self.right[1][0], self.right[2][0]
            self.right[2][0], self.right[1][0], self.right[0][0] = self.temporary
            self.front = self._transform_array(self.front, inversely=True)


    def move_left(self, backward=False) -> None:
        self.temporary = [self.down[0][0], self.down[1][0], self.down[2][0]]

        if not backward:
                self.down[0][0], self.down[1][0], self.down[2][0] = self.front[0][0], self.front[1][0], self.front[2][0]
                self.front[0][0], self.front[1][0], self.front[2][0] = self.top[0][0], self.top[1][0], self.top[2][0]
                self.top[0][0], self.top[1][0], self.top[2][0] = self.back[2][2], self.back[1][2], self.back[0][2]
                self.back[2][2], self.back[1][2], self.back[0][2] = self.temporary
                self.left = self._transform_array(self.left)


        else:
                self.down[0][0], self.down[1][0], self.down[2][0] = self.back[2][2], self.back[1][2], self.back[0][2]
                self.back[2][2], self.back[1][2], self.back[0][2] = self.top[0][0], self.top[1][0], self.top[2][0]
                self.top[0][0], self.top[1][0], self.top[2][0] = self.front[0][0], self.front[1][0], self.front[2][0]
                self.front[0][0], self.front[1][0], self.front[2][0] = self.temporary
                self.left = self._transform_array(self.left, inversely=True)

        
    def move_back(self, backward=False) -> None:
        self.temporary = [self.top[0][0], self.top[0][1], self.top[0][2]]

        if not backward:
                self.top[0][0], self.top[0][1], self.top[0][2] = self.right[0][2], self.right[1][2], self.right[2][2]
                self.right[0][2], self.right[1][2], self.right[2][2] = self.down[2][2], self.down[2][1], self.down[2][0]
                self.down[2][2], self.down[2][1], self.down[2][0] = self.left[2][0], self.left[1][0], self.left[0][0]
                self.left[2][0], self.left[1][0], self.left[0][0] = self.temporary
                self.back = self._transform_array(self.back)

        else:
                self.top[0][0], self.top[0][1], self.top[0][2] = self.left[2][0], self.left[1][0], self.left[0][0]
                self.left[0][0], self.left[1][0], self.left[2][0] = self.down[2][0], self.down[2][1], self.down[2][2]
                self.down[2][0], self.down[2][1], self.down[2][2] = self.right[2][2], self.right[1][2], self.right[0][2]
                self.right[0][2], self.right[1][2], self.right[2][2] = self.temporary
                self.back = self._transform_array(self.back, inversely=True) 
    
    def move_down(self, backward=False) -> None:
        self.temporary = [self.front[2][0], self.front[2][1], self.front[2][2]]
        if not backward:
            self.front[2][0], self.front[2][1], self.front[2][2] = self.left[2][0], self.left[2][1], self.left[2][2]
            self.left[2][0], self.left[2][1], self.left[2][2] = self.back[2][0], self.back[2][1], self.back[2][2]
            self.back[2][0], self.back[2][1], self.back[2][2] = self.right[2][0], self.right[2][1], self.right[2][2]
            self.right[2][0], self.right[2][1], self.right[2][2] = self.temporary
            self.down = self._transform_array(self.down)

        else:
            self.front[2][0], self.front[2][1], self.front[2][2] = self.right[2][0], self.right[2][1], self.right[2][2]
            self.right[2][0], self.right[2][1], self.right[2][2] = self.back[2][0], self.back[2][1], self.back[2][2]
            self.back[2][0], self.back[2][1], self.back[2][2] = self.left[2][0], self.left[2][1], self.left[2][2]
            self.left[2][0], self.left[2][1], self.left[2][2] = self.temporary

            self.down = self._transform_array(self.down, inversely=True)

    def print_cube(self) -> None:
        print('top'); self._print_for_printing_massive(self.top)
        print('front'); self._print_for_printing_massive(self.front)
        print('down'); self._print_for_printing_massive(self.down)
        print('left'); self._print_for_printing_massive(self.left)
        print('right'); self._print_for_printing_massive(self.right)
        print('back'); self._print_for_printing_massive(self.back)
        
    def reset(self) -> None:
        self.__init__()