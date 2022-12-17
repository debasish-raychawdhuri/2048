from enum import Enum
import random
import math


class Move(Enum):
    LEFT = 0
    RIGHT = 1
    UP = 2
    DOWN = 3


class GameState:
    def __init__(self):
        self.values = list(list(0 for j in range(0, 4)) for i in range(0, 4))
        i = int(random.random()*4)
        j = int(random.random()*4)
        self.values[i][j] = 2

    def print_state(self):
        for i in range(0, 4):
            for j in range(0, 4):
                print("{:-6}".format(self.values[i][j]), end=" ")
            print("\n")
        print("=================================")

    def get_value(self, indexes):
        (i, j) = indexes
        return self.values[i][j]

    def set_value(self, index, value):
        (i, j) = index
        self.values[i][j] = value

    def __to_true_index(i, j, move: Move):
        match move:
            case Move.LEFT:
                return (i, j)
            case Move.RIGHT:
                return (i, 3-j)
            case Move.UP:
                return (j, i)
            case Move.DOWN:
                return (3-j, i)

    def check_failed(self):
        for i in range(0, 4):
            for j in range(0, 4):
                if self.values[i][j] == 0:
                    return False
                else:
                    if i < 3 and self.values[i][j] == self.values[i+1][j]:
                        return False
                    elif j < 3 and self.values[i][j] == self.values[i][j+1]:
                        return False

        return True

    def check_won(self):
        for i in range(0, 4):
            for j in range(0, 4):
                if self.values[i][j] == 2048:
                    return True
        return False

    def move(self, move: Move):
        shifted = False
        for i in range(0, 4):
            j = 0
            while j < 4:
                current_index = GameState.__to_true_index(i, j, move)
                current_value = self.get_value(current_index)
                j += 1
                if j >= 4:
                    break
                if current_value == 0:
                    for k in range(j, 4):
                        advanced_index = GameState.__to_true_index(i, k, move)
                        advanced_value = self.get_value(advanced_index)
                        if advanced_value != 0:
                            self.set_value(current_index, advanced_value)
                            self.set_value(advanced_index, 0)
                            shifted = True
                            j -= 1
                            break
                else:
                    for k in range(j, 4):
                        advanced_index = GameState.__to_true_index(i, k, move)
                        advanced_value = self.get_value(advanced_index)
                        if advanced_value == current_value:
                            self.set_value(
                                current_index, current_value+advanced_value)
                            self.set_value(advanced_index, 0)
                            shifted = True
                            break
                        elif advanced_value != 0:
                            break

        if shifted:
            possible_indexes = []
            for i in range(0, 4):
                current_index = GameState.__to_true_index(i, 3, move)
                current_value = self.get_value(current_index)
                if current_value == 0:
                    possible_indexes.append(current_index)
            pos = int(math.floor(random.random()*len(possible_indexes)))
            index = possible_indexes[pos]
            v = int(math.ceil(random.random()*2))*2
            self.set_value(index, v)
