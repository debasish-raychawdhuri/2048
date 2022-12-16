from gamestate import Move, GameState

import readchar

state = GameState()

while True:
    state.print_state()
    if state.check_failed():
        print("Failed")
        break
    elif state.check_won():
        print("You Won!")
        break
    input = readchar.readchar()
    match input:
        case 'a':
            state.move(Move.LEFT)
        case 'd':
            state.move(Move.RIGHT)
        case 'w':
            state.move(Move.UP)
        case 's':
            state.move(Move.DOWN)
        case 'l':
            exit(0)
