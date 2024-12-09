# two player of chess game in python with pygame!
# set up variable, images and game loop

import pygame

pygame.init()
width = 1000
height = 900
screen = pygame.display.set_mode([width, height])
pygame.display.set_caption("Two-player pygame chess!")
font = pygame.font.Font("freesansbold.ttf", 20)
big_font = pygame.font.Font("freesansbold.ttf", 50)
timer = pygame.time.Clock()
fps = 60
# game variable and images
white_pieces = ["rook","knight","bishop","king","queen","bishop","knight","rook",
                "pawn","pawn","pawn","pawn","pawn","pawn","pawn","pawn",]
white_location = [(0, 0),(1, 0),(2, 0),(3, 0),(4, 0),(5, 0),(6, 0),(7, 0),
                  (0, 1),(1, 1),(2, 1),(3, 1),(4, 1),(5, 1),(6, 1),(7, 1),]

black_pieces = ["rook","knight","bishop","king","queen","bishop","knight","rook",
                "pawn","pawn","pawn","pawn","pawn","pawn","pawn","pawn",]
black_location = [(0, 7),(1, 7),(2, 7),(3, 7),(4, 7),(5, 7),(6, 7),(7, 7),
                  (0, 6),(1, 6),(2, 6),(3, 6),(4, 6),(5, 6),(6, 6),(7, 6),]

captured_pieces_white = []
captured_pieces_black = []
# 0 - white turn no selection: 1-white turn pieces selected: 2- black turn no selection: 3- black turn pieces selected
turn_step = 0
selection = 100
valid_move = []
# load in game piece images (king, queen, rook, bishop, knight, pawn) x 2
black_queen = pygame.transform.scale(pygame.image.load("Images/black queen.png"), (80, 80))
black_queen_small = pygame.transform.scale(
    pygame.image.load("Images/black queen.png"), (45, 45)
)
black_king = pygame.transform.scale(pygame.image.load("Images/black king.png"), (80, 80))
black_king_small = pygame.transform.scale(
    pygame.image.load("Images/black king.png"), (45, 45)
)
black_bishop = pygame.transform.scale(
    pygame.image.load("Images/black bishop.png"), (80, 80)
)
black_bishop_small = pygame.transform.scale(
    pygame.image.load("Images/black bishop.png"), (45, 45)
)
black_knight = pygame.transform.scale(
    pygame.image.load("Images/black knight.png"), (80, 80)
)
black_knight_small = pygame.transform.scale(
    pygame.image.load("Images/black knight.png"), (45, 45)
)
black_rook = pygame.transform.scale(pygame.image.load("Images/black rook.png"), (80, 80))
black_rook_small = pygame.transform.scale(
    pygame.image.load("Images/black rook.png"), (45, 45)
)
black_pawn = pygame.transform.scale(pygame.image.load("Images/black pawn.png"), (65, 65))
black_pawn_small = pygame.transform.scale(
    pygame.image.load("Images/black pawn.png"), (45, 45)
)
white_queen = pygame.transform.scale(pygame.image.load("Images/white queen.png"), (80, 80))
white_queen_small = pygame.transform.scale(
    pygame.image.load("Images/white queen.png"), (45, 45)
)
white_king = pygame.transform.scale(pygame.image.load("Images/white king.png"), (80, 80))
white_king_small = pygame.transform.scale(
    pygame.image.load("Images/white king.png"), (45, 45)
)
white_bishop = pygame.transform.scale(
    pygame.image.load("Images/white bishop.png"), (80, 80)
)
white_bishop_small = pygame.transform.scale(
    pygame.image.load("Images/white bishop.png"), (45, 45)
)
white_knight = pygame.transform.scale(
    pygame.image.load("Images/white knight.png"), (80, 80)
)
white_knight_small = pygame.transform.scale(
    pygame.image.load("Images/white knight.png"), (45, 45)
)
white_rook = pygame.transform.scale(pygame.image.load("Images/white rook.png"), (80, 80))
white_rook_small = pygame.transform.scale(
    pygame.image.load("Images/white rook.png"), (45, 45)
)
white_pawn = pygame.transform.scale(pygame.image.load("Images/white pawn.png"), (65, 65))
white_pawn_small = pygame.transform.scale(
    pygame.image.load("Images/white pawn.png"), (45, 45)
)
white_images = [
    white_pawn,
    white_bishop,
    white_rook,
    white_knight,
    white_king,
    white_queen,
]
white_images_small = [
    white_pawn_small,
    white_bishop_small,
    white_rook_small,
    white_knight_small,
    white_king_small,
    white_queen_small,
]

black_images = [
    black_pawn,
    black_bishop,
    black_rook,
    black_knight,
    black_king,
    black_queen,
]
black_images_small = [
    black_pawn_small,
    black_bishop_small,
    black_rook_small,
    black_knight_small,
    black_king_small,
    black_queen_small,
]

piece_list = ["pawn", "queen", "king", "rook", "bishop", "knight"]
# check variable/ flashing counter


# draw main game board
def draw_board(): ...


# draw peices onto board
def draw_pieces():
    for i in range(len(white_pieces)):
        index = piece_list.index(white_pieces[i])
        if white_pieces[i] == "pawn":
            screen.blit(
                white_pawn,
                (white_location[i][0] * 100 + 22, white_location[i][1] * 100 + 30))
        else:
            screen.blit(
                white_images[index],
                (white_location[i][0] * 100 + 10, white_location[i][1] * 100 + 10))
            
    for i in range(len(black_pieces)):
        index = piece_list.index(black_pieces[i])
        if black_pieces[i] == "pawn":
            screen.blit(
                white_pawn,
                (black_location[i][0] * 100 + 22, black_location[i][1] * 100 + 30))
        else:
            screen.blit(
                black_images[index],
                (black_location[i][0] * 100 + 10, black_location[i][1] * 100 + 10))

    # for i in range(32):
    #     column = i % 4
    #     row = i // 4
    #     if row % 2 == 0:
    #         pygame.draw.rect(screen, "light grey")


# game loop
run = True
while run:
    timer.tick(fps)
    screen.fill("dark grey")
    draw_board()
    draw_pieces()

    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
pygame.quit()
