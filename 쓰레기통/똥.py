# x = 7
# def abc(a, b, c, x):
#     for x_l in range(x, -1, -1):
#         print(x_l, range(x, -1, -1))
# abc(1, 2, 3, x)

# def game_visualize(board_img, ball, position):
#   ball_size = ball.shape[0]
#   step_size = 48
#   off_set = 7

#   y_step = step_size*position[0] - round(step_size/2) + off_set
#   x_step = step_size*position[0] - round(step_size/2) + off_set

#   board_img[y_step : y_step + ball_size, x_step : x_step + ball_size] - ball

#   plt.imshow(board_img)

################################################################################################

def is_black_five(size, board, x, y):
    
    num1_black = 1
    for x_l in range(x, -1, -1): # ㅡ 가로로 이어진 돌 수 
        print(x_1, range(x, -1, -1))
        if board[y, x_l] == 1:
            num1_black += 1
    for x_r in range(x, size, +1):
        if board[y, x_r] == 1:
            num1_black += 1
    if num1_black == 5:
        return True

    num2_black = 1
    for y_u in range(x, -1, -1): # ㅣ 세로로 이어진 돌 수
        if board[y_u, x] == 1:
            num2_black += 1
    for y_d in range(x, size, +1):
        if board[y_d, x] == 1:
            num2_black += 1
    if num2_black == 5:
        return True

    x_l = x
    y_u = x
    num3_black = 1
    while (x_l-1 != -1) and (y_u-1 != -1): # \ 대각선으로 이어진 돌 수 # 실수 : or -> and
        x_l -= 1
        y_u -= 1
        if board[y_u, x_l] == 1:
            num3_black += 1
    x_r = x
    y_d = x
    while (x_r+1 != size) and (y_d+1 != size):
        x_r += 1
        y_d += 1
        if board[y_d, x_r] == 1:
            num3_black += 1
    if num3_black == 5:
        return True

    x_l = x
    y_d = x
    num4_black = 1
    while (x_l-1 != -1) and (y_d+1 != size): # / 대각선으로 이어진 돌 수
        x_l -= 1
        y_d += 1
        if board[y_d, x_l] == 1:
            num4_black += 1
    x_r = x
    y_u = x
    while (x_r+1 != size) and (y_u-1 != -1):
        x_r += 1
        y_u -= 1
        if board[y_u, x_r] == 1:
            num4_black += 1
    if num4_black == 5:
        return True
    
    # print(num1_black,num2_black,num3_black,num4_black)
    if num1_black > 5 or num2_black > 5 or num3_black > 5 or num4_black > 5:
        return None
    else:
        return False

################################################################################################

# 삼삼 검사 (열린 3이 2개 이상인지)
def is_three_three_2(size, board):
    three_open = 0 # 열린 3 개수 (2개가 되면 삼삼)

    # 가로 검사
    three = 0
    brk = False
    for y in range(size):
        for x in range(size - 4):
            line = board[y, x:x+5]

            if line.sum() == 3:
                # print(line, 1)
                three += 1
    
                if three == 2: 
                    three_open += 1
                    # print("open")
                    if three_open == 2: return True
                    brk = True
                    break
        if brk == True: break

    # 세로 검사
    three = 0  
    brk = False
    for y in range(size - 4):
        for x in range(size):
            line = board[y:y+5, x]

            if line.sum() == 3:
                # print(line, 2)
                three += 1

                if three == 2: 
                    three_open += 1
                    # print("open")
                    if three_open == 2: return True
                    brk = True
                    break
        if brk == True: break

    # 대각선 \ 검사
    three = 0
    brk = False
    for y in range(size - 4):  
        for x in range(size - 4):
            line[0] = board[y, x]
            line[1] = board[y+1, x+1]
            line[2] = board[y+2, x+2]
            line[3] = board[y+3, x+3]
            line[4] = board[y+4, x+4]

            if line.sum() == 3:
                # print(line, 3)
                three += 1
                # print(pan)
                if three == 2: 
                    three_open += 1
                    # print("open")
                    if three_open == 2:
                        line[0], line[1], line[2], line[3], line[4] = 0,0,0,0,0 ###
                        return True
                    brk = True
                    break
            line[0], line[1], line[2], line[3], line[4] = 0,0,0,0,0 ###
        if brk == True: break
    
    # 대각선 / 검사
    three = 0
    brk = False
    for y in range(size - 4):  
        for x in range(size - 4):
            line[0] = board[y, x+4]
            line[1] = board[y+1, x+3]
            line[2] = board[y+2, x+2]
            line[3] = board[y+3, x+1]
            line[4] = board[y+4, x]

            if line.sum() == 3:
                # print(line, 4)
                three += 1

                if three == 2: 
                    three_open += 1
                    if three_open == 2:
                        line[0], line[1], line[2], line[3], line[4] = 0,0,0,0,0 ###
                        return True
                    brk = True
                    break
            line[0], line[1], line[2], line[3], line[4] = 0,0,0,0,0 ###
        if brk == True: break

    # 3-3 아님
    return False


def is_three_three(size, board):
    three = 0

    brk = False
    for y in range(size):
        for x in range(size - 4):
            line = board[y, x:x+5]
            if line.sum() == 3:
                three += 1
                if three == 2: return True
                brk = True
                break
        if brk == True: break

    brk = False
    for y in range(size - 4):
        for x in range(size):
            line = board[y:y+5, x]
            if line.sum() == 3:
                three += 1;
                if three == 2: return True
                brk = True
                break
        if brk == True: break

    brk = False
    for y in range(size - 4):  # 열린 대각선 \ 3줄
        for x in range(size - 4):
            line[0] = board[y, x]
            line[1] = board[y+1, x+1]
            line[2] = board[y+2, x+2]
            line[3] = board[y+3, x+3]
            line[4] = board[y+4, x+4]
            if line.sum() == 3:
                three += 1
                if three == 2: 
                    line[0], line[1], line[2], line[3], line[4] = 0,0,0,0,0 ###
                    return True
                brk = True
                break
            line[0], line[1], line[2], line[3], line[4] = 0,0,0,0,0 ###
        if brk == True: break

    brk = False
    for y in range(size - 4):  # 열린 대각선 / 3줄
        for x in range(size - 4):
            line[0] = board[y, x+4]
            line[1] = board[y+1, x+3]
            line[2] = board[y+2, x+2]
            line[3] = board[y+3, x+1]
            line[4] = board[y+4, x]
            if line.sum() == 3:
                three += 1
                if three == 2:
                    line[0], line[1], line[2], line[3], line[4] = 0,0,0,0,0 ###
                    return True
                brk = True
                break
            line[0], line[1], line[2], line[3], line[4] = 0,0,0,0,0 ###
        if brk == True: break
    return False

################################################################################################

# 사사 검사
def is_four_four(size, board):
    four = 0 # 4개 줄 개수

    brk = False
    for y in range(size):  # 가로 4줄
        for x in range(size - 4):
            line = board[y, x:x+5]

            if line.sum() == 4:
                # print(line)
                four += 1
                brk = True
                break
        if brk == True: break
  
    brk = False
    for y in range(size - 4):  # 세로 4줄
        for x in range(size):
            line = board[y:y+5, x]

            if line.sum() == 4:
                # print(line)
                four += 1
                if four == 2: return True
                brk = True
                break
        if brk == True: break

    brk = False
    for y in range(size - 4):  # 대각선 \ 4줄
        for x in range(size - 4):
            line[0] = board[y, x]
            line[1] = board[y+1, x+1]
            line[2] = board[y+2, x+2]
            line[3] = board[y+3, x+3]
            line[4] = board[y+4, x+4]

            if line.sum() == 4:
                # print(line)
                four += 1
                if four == 2:
                    line[0], line[1], line[2], line[3], line[4] = 0,0,0,0,0 ###
                    return True
                brk = True
                break
            line[0], line[1], line[2], line[3], line[4] = 0,0,0,0,0 ###
        if brk == True: break

    brk = False
    for y in range(size - 4):  # 대각선 / 4줄
        for x in range(size - 4):
            line[0] = board[y, x+4]
            line[1] = board[y+1, x+3]
            line[2] = board[y+2, x+2]
            line[3] = board[y+3, x+1]
            line[4] = board[y+4, x]

            if line.sum() == 4:
                # print(line)
                four += 1
                if four == 2:
                    line[0], line[1], line[2], line[3], line[4] = 0,0,0,0,0 ###
                    return True
                brk = True
                break
            line[0], line[1], line[2], line[3], line[4] = 0,0,0,0,0 ###
        if brk == True: break

    # 4-4 아님
    return False

# 백이 5목이 될 수 있을 때, 같은 라인 장목검사 
                            # (sum(line) == 4 and ( 
                            # ((x-1 > -1) and (board[y, x-1] == 1)) or
                            # ((x+5 < size) and (board[y, x+5] == 1)))) or

# 각 좌표마다 주변 좌표의 점수들을 곱한 보드를 줌
def sum_adjacent_scores_board(whose_turn, size, board):
    
    score_board = whose_score_board(whose_turn, size, board)
    sum_adjacent_board = np.zeros([size, size])

    for y in range(size):
        for x in range(size):
            if board[y][x] == 0: # 돌이 이미 놓여있으면 0점

                if board[y][x] == -1: # 금수 자리 -1점
                    sum_adjacent_board[y][x] = -1
                    continue
                
                value = 1

                # ㅡ 가로쪽 주변 점수를 곱함
                for x_l in range(x-1, x-5, -1):
                    if (x_l == -1): break
                    if board[y][x_l] == 0:
                        value *= 1.001**score_board[y][x_l]#*(5-(x-x_l))
                
                for x_r in range(x+1, x+5, +1):
                    if (x_r == size): break
                    if board[y][x_r] == 0:
                        value *= 1.001**score_board[y][x_r]#*(5-(x_r-x))
                
                # ㅣ 세로쪽 주변 점수를 곱함
                for y_u in range(y-1, y-5, -1):
                    if (y_u == -1): break
                    if board[y_u][x] == 0:
                        value *= 1.001**score_board[y_u][x]#*(5-(y-y_u))
                
                for y_d in range(y+1, y+5, +1):
                    if (y_d == size): break
                    if board[y_d][x] == 0:
                        value *= 1.001**score_board[y_d][x]#*(5-(y_d-y))
                
                # \ 대각선쪽 주변 점수를 곱함
                x_l = x
                y_u = y
                for i in range(4):
                    if (x_l-1 == -1) or (y_u-1 == -1): break
                    x_l -= 1
                    y_u -= 1
                    if board[y_u][x_l] == 0:
                        value *= 1.001**score_board[y_u][x_l]#*(5-(x-x_l))
                
                x_r = x
                y_d = y
                for i in range(4):
                    if (x_r+1 == size) or (y_d+1 == size): break
                    x_r += 1
                    y_d += 1
                    if board[y_d][x_r] == 0:
                        value *= 1.001**score_board[y_d][x_r]#*(5-(x_r-x))
                
                # / 대각선쪽 주변 점수를 곱함
                x_l = x
                y_d = y
                for i in range(4):
                    if (x_l-1 == -1) or (y_d+1 == size): break
                    x_l -= 1
                    y_d += 1
                    if board[y_d][x_l] == 0:
                        value *= 1.001**score_board[y_d][x_l]#*(5-(y_d-y))
                
                x_r = x
                y_u = y
                for i in range(4):
                    if (x_r+1 == size) or (y_u-1 == -1): break
                    x_r += 1
                    y_u -= 1
                    if board[y_u][x_r] == 0:
                        value *= 1.001**score_board[y_u][x_r]#*(5-(y-y_u))
                
                sum_adjacent_board[y][x] = round(value, 2)

    return sum_adjacent_board

