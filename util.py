from engine.color import Color
# initial_pieces = [
#             2,
#             0,
#             0,
#             0,
#             0,
#             -5,
#             0,
#             -3,
#             0,
#             0,
#             0,
#             5,
#             -5,
#             0,
#             0,
#             0,
#             3,
#             0,
#             5,
#             0,
#             0,
#             0,
#             0,
#             -2,
#         ]
# final = []
# def get_color(x):
#     color = None
#     if x > 0 :
#         color = Color.BLACK
#     if x < 0 :
#         color = Color.WHITE
#     return color
# for i , key in enumerate(initial_pieces):
#     color  = get_color(key)
#     result = (i+1,abs(key))
#     print(result)

initial_positions = [
    (1, Color.BLACK, 2),
    (2, None, 0),
    (3, None, 0),
    (4, None, 0),
    (5, None, 0),
    (6, Color.WHITE, 5),
    (7, None, 0),
    (8, Color.WHITE, 3),
    (9, None, 0),
    (10, None, 0),
    (11, None, 0),
    (12, Color.BLACK, 5),
    (13, Color.WHITE, 5),
    (14, None, 0),
    (15, None, 0),
    (16, None, 0),
    (17, Color.BLACK, 3),
    (18, None, 0),
    (19, Color.BLACK, 5),
    (20, None, 0),
    (21, None, 0),
    (22, None, 0),
    (23, None, 0),
    (24, Color.WHITE, 2),
]
print(*initial_positions[0])