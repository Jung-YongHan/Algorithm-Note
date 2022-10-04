# 리스트 변수를 인자로 받고 행과 열을 회전한 새로운 리스트를 반환하는 함수
def rotate(sticker)->list:
    row, col = len(sticker), len(sticker[0])
    rotate_sticker = [[] for _ in range(col)]
    for j in range(col):
        for i in range(row-1, -1, -1):
            rotate_sticker[j].append(sticker[i][j])
    return rotate_sticker