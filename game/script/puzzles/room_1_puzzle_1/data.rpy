define block_size = 80

image valid_highlight:
    Solid("#f00", xsize=block_size, ysize=block_size)
    alpha 0.5

image handle:
    Solid("#fff", xsize=block_size, ysize=block_size)
    alpha 0.0

image invalid_highlight = Solid("#0f0", width=block_size, height=block_size)

image test_part = "images/test_part.png"

# image default_part:
#     Solid("#fff")
#     alpha 0.25

define default_shape = [[1, 1],
                        [0, 1]]

define shape_1 = [[1, 0],
                 [1, 1],
                 [0, 1],
                 [0, 1],
                 [0, 1]]

define shape_2 = [[1, 0, 0, 0, 0],
                 [1, 1, 1, 1, 1],
                 [0, 1, 0, 0, 0]]

define shape_3 = [[1, 0, 0],
                 [1, 1, 0],
                 [1, 1, 1],
                 [1, 1, 1]]

define shape_4 = [[0, 1],
                 [0, 1],
                 [1, 1],
                 [1, 0]]

define shape_5 = [[1, 1, 1],
                 [0, 0, 1]]

define shape_6 = [[1, 1, 1],
                 [0, 0, 1]]

define shape_7 = [[1, 1],
                 [1, 1],
                 [1, 1]]

define shape_8 = [[1, 1, 1],
                  [0, 1, 0]]

define shape_9 = [[0, 1, 1, 1],
                  [1, 1, 1, 0]]

define shape_10 = [[1, 1],
                  [1, 1]]

define shape_11 = [[1],
                  [1]]

define shape_12 = [[1],
                  [1],
                  [1]]

define shape_13 = [[0, 1],
                  [1, 1]]

define shape_14 = [[1, 0],
                  [1, 1]]
