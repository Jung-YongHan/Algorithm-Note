# ����Ʈ ������ ���ڷ� �ް� ��� ���� ȸ���� ���ο� ����Ʈ�� ��ȯ�ϴ� �Լ�
def rotate(sticker)->list:
    row, col = len(sticker), len(sticker[0])
    rotate_sticker = [[] for _ in range(col)]
    for j in range(col):
        for i in range(row-1, -1, -1):
            rotate_sticker[j].append(sticker[i][j])
    return rotate_sticker