define block_size = 80

image valid_highlight:
    Solid("#f00", xsize=block_size, ysize=block_size)
    alpha 0.5

image handle:
    Solid("#fff", xsize=block_size, ysize=block_size)
    alpha 0.25

image invalid_highlight = Solid("#0f0", width=block_size, height=block_size)

image test_part = "images/test_part.png"

# image default_part:
#     Solid("#fff")
#     alpha 0.25

define default_shape = [[1, 1],
                        [0, 1]]

# default rando_pieces = [Part(shape=[[1, 1, 0],
#                                     [0, 1, 1]],
#                              x=200, y=200),
#                         Part(x=600, y=100)]

# default p1_pieces = [Part(shape=[[1, 1]],
#                           x=6*block_size, y=1*block_size),
#                      Part(shape=[[1, 1],
#                                  [1, 1]],
#                           x=6*block_size, y=3*block_size),
#                      Part(shape=[[1, 1, 1],
#                                  [1, 0, 0]],
#                           x=6*block_size, y=6*block_size),
#                      Part(shape=[[1, 1, 1],
#                                  [1, 0, 0]],
#                           x=10*block_size, y=1*block_size),
#                      Part(shape=[[1, 1],
#                                  [1, 1]],
#                           x=10*block_size, y=4*block_size)]

# default p1_board = PartBoard(4, 4)

# default p2_pieces = [Part(shape=[[1],
#                                  [1]],
#                           x=7*block_size, y=1*block_size),
#                      Part(shape=[[1],
#                                  [1]],
#                           x=7*block_size, y=4*block_size),
#                      Part(shape=[[1, 0, 0],
#                                  [1, 1, 1]],
#                           x=1*block_size, y=7*block_size),
#                      Part(shape=[[1, 0],
#                                  [1, 1],
#                                  [0, 1]],
#                           x=9*block_size, y=1*block_size),
#                      Part(shape=[[1, 0],
#                                  [1, 1],
#                                  [0, 1]],
#                           x=12*block_size, y=1*block_size),
#                      Part(shape=[[1, 0, 1],
#                                  [1, 1, 1]],
#                           x=9*block_size, y=5*block_size),
#                      Part(shape=[[0, 1, 0],
#                                  [1, 1, 1]],
#                           x=12*block_size, y=7*block_size),

# ]

# default p2_board = PartBoard(5, 5)
