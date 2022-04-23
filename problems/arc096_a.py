# C - Half and Half
# 可能性があるのは以下のパターン
# A                    , B                    , C
# -----------------------------------------------------------
# X                    , Y                    , 0             # Cが割高
# X - min(X, Y)        , Y - min(X, Y)        , min(X, Y) * 2 # Cが割安
# max(0, X - max(X, Y)), max(0, Y - max(X, Y)), max(X, Y) * 2 # 余計に買っても安いくらいCが激安

A, B, C, X, Y = map(int, input().split())

price = min(
    A * X + B * Y + C * 0,
    A * (X - min(X, Y)) + B * (Y - min(X, Y)) + C * (min(X, Y) * 2),
    A * (max(0, X - max(X, Y))) + B * (max(0, Y - max(X, Y))) + C * (max(X, Y) * 2),
)
print(price)
