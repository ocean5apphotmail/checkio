#  井字游戏，有时也被称为“进攻和防守”，是一个两人玩家（X和O）轮流标志着3×3的网格的空间的连珠游戏。最先在任意一条直线（水平线，垂直线或对角线）上成功连接三个标记的一方获胜。
#
# 但我们不去玩这个游戏。你将是这个游戏的裁判。你被赋予游戏的结果，以及你必须判断游戏是平局还是有人胜出，以及谁将会成为最后的赢家。如果X玩家获胜，返回“X”。如果O玩家获胜，返回“O”。如果比赛是平局，返回“D”。
#
# x-o-referee
#
# 游戏的结果是作为字符串形式的列表，其中“X”和“O”是玩家的标志，“.”是空格。
#
# 输入: 游戏结果作为字符串形式的列表(Unicode)。
#
# 输出: “X”，“O”或“D”作为字符串形式。
#
# 范例:
# checkio([
#     "X.O",
#     "XX.",
#     "XOO"]) == "X"
# checkio([
#     "OO.",
#     "XOX",
#     "XOX"]) == "O"
# checkio([
#     "OOX",
#     "XXO",
#     "OXX"]) == "D"
#  如何使用： 此任务中的概念将有助于您遍历数据类型。这还可以用在游戏的算法上，让你知道如何去检查结果。
#
# 前提:
# 要么有一个赢家，要么平局
# len(game_result) == 3
# all(len(row) == 3 for row in game_result)
from typing import List


def checkio(game_result: List[str]) -> str:
    return "D" or "X" or "O"


if __name__ == "__main__":
    print("Example:")
    print(checkio(["X.O", "XX.", "XOO"]))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(["X.O", "XX.", "XOO"]) == "X", "X wins"
    assert checkio(["OO.", "XOX", "XOX"]) == "O", "O wins"
    assert checkio(["OOX", "XXO", "OXX"]) == "D", "Draw"
    assert checkio(["O.X", "XX.", "XOO"]) == "X", "X wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
