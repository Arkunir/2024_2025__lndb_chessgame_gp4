import pygame
import chess
import random
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import chess
import time  # Importer time pour gérer le minuteur

# Initialisation de pygame
pygame.init()

# Initialisation pour le plein écran
screen_info = pygame.display.Info()  # Obtenez les informations sur la taille de l'écran
WIDTH, HEIGHT = screen_info.current_w, screen_info.current_h  # Utilisez la résolution de l'écran
ROWS, COLS = 8, 8

# Calcul dynamique de la taille des cases en fonction de la plus petite dimension de l'écran
SQUARE_SIZE = min(WIDTH, HEIGHT) // 8  # La taille de chaque case est la plus petite dimension de la fenêtre divisée par 8

LIGHT_BROWN = (240, 217, 181)
DARK_BROWN = (181, 136, 99)

ASSETS_PATH = "testing/jeu_correct/assets/Type_2/"
PIECE_FILES = {
    'P': "wP.png", 'N': "wN.png", 'B': "wB.png", 'R': "wR.png", 'Q': "wQ.png", 'K': "wK.png",
    'p': "P.png", 'n': "N.png", 'b': "B.png", 'r': "R.png", 'q': "Q.png", 'k': "K.png"
}

PROMOTION_OPTIONS = ['q', 'r', 'n', 'b']

# Créer la fenêtre Pygame en mode maximisé
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE | pygame.NOFRAME)
pygame.display.set_caption("Jeu d'échecs")


def load_pieces():
    pieces = {}
    for piece, filename in PIECE_FILES.items():
        image = pygame.image.load(ASSETS_PATH + filename)
        # Redimensionner les pièces pour correspondre à la taille des cases
        image = pygame.transform.scale(image, (SQUARE_SIZE, SQUARE_SIZE))
        pieces[piece] = image
    return pieces

PIECES = load_pieces()
board = chess.Board()

# Variables du minuteur
time_white = 300  # Temps en secondes pour les Blancs (5 minutes)
time_black = 300  # Temps en secondes pour les Noirs (5 minutes)
start_time = time.time()  # Temps de départ du chronomètre
turn = True  # True = Blanc, False = Noir

# Définition des fonctions de dessin du jeu
def draw_board():
    for row in range(ROWS):
        for col in range(COLS):
            color = LIGHT_BROWN if (row + col) % 2 == 0 else DARK_BROWN
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

def draw_pieces():
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece:
            col = chess.square_file(square)
            row = chess.square_rank(square)
            image = PIECES[piece.symbol()]
            # Dessiner la pièce à la position appropriée sur le plateau
            screen.blit(image, (col * SQUARE_SIZE, (7 - row) * SQUARE_SIZE))

# Fonction de dessin du minuteur
def draw_timer():
    global time_white, time_black, start_time, turn
    if turn:  # Si c'est le tour des Blancs
        time_white -= (time.time() - start_time)
    else:  # Si c'est le tour des Noirs
        time_black -= (time.time() - start_time)

    start_time = time.time()  # Réinitialiser le temps de départ pour le prochain tour

    font = pygame.font.Font(None, 36)
    white_time_text = font.render(f"Blanc: {int(time_white // 60):02d}:{int(time_white % 60):02d}", True, (255, 255, 255))
    black_time_text = font.render(f"Noir: {int(time_black // 60):02d}:{int(time_black % 60):02d}", True, (255, 255, 255))

    screen.blit(white_time_text, (10, 10))  # Affichage du temps des Blancs
    screen.blit(black_time_text, (WIDTH - black_time_text.get_width() - 10, 10))  # Affichage du temps des Noirs

# Fonction pour gérer les déplacements des pièces
def get_square_under_mouse(pos):
    x, y = pos
    col = x // SQUARE_SIZE
    row = 7 - (y // SQUARE_SIZE)
    return chess.square(col, row)

# Boucle principale
running = True
selected_square = -1
while running:
    screen.fill((0, 0, 0))  # Remplir l'écran en noir avant de dessiner
    draw_board()
    draw_pieces()

    draw_timer()  # Afficher les chronomètres

    # Gestion des événements (fermer la fenêtre, sélection des pièces, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            square = get_square_under_mouse(event.pos)
            if square != -1:
                piece = board.piece_at(square)

                if selected_square == -1:  # Sélectionner une pièce
                    if piece is not None and piece.color == (chess.WHITE if turn else chess.BLACK):
                        selected_square = square
                else:  # Déplacer la pièce sélectionnée
                    move = chess.Move(selected_square, square)
                    if move in board.legal_moves:
                        board.push(move)
                        turn = not turn  # Changer de tour
                        selected_square = -1
                        start_time = time.time()  # Redémarrer le temps pour le joueur suivant

    pygame.display.update()

    # Vérifier si le temps d'un joueur est écoulé
    if time_white <= 0 or time_black <= 0:  
        winner = "Noir" if time_white <= 0 else "Blanc"
        # Afficher un message de fin de partie
        font = pygame.font.Font(None, 72)
        text = font.render(f"{winner} a gagné !", True, (255, 255, 255))
        screen.blit(text, ((WIDTH - text.get_width()) // 2, (HEIGHT - text.get_height()) // 2))
        pygame.display.update()
        pygame.time.wait(3000)  # Attendre 3 secondes avant de fermer
        running = False



def display_winner(winner):
    font = pygame.font.Font(None, 72)
    text = font.render(f"Victoire! {winner} ont gagné!", True, (255, 255, 255))
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 3))
    
    # Create "Quitter" button
    button_width, button_height = 200, 60
    button_x = WIDTH // 2 - button_width // 2
    quit_button_y = HEIGHT // 2 + 100
    quit_button_rect = pygame.Rect(button_x, quit_button_y, button_width, button_height)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if quit_button_rect.collidepoint(event.pos):
                    pygame.quit()
                    exit()

        screen.fill((0, 0, 0))  # Background black
        screen.blit(text, text_rect)

        # Draw the "Quitter" button (red with white text)
        pygame.draw.rect(screen, (255, 0, 0), quit_button_rect)  # Red button
        quit_button_text = pygame.font.Font(None, 36).render("Quitter", True, (255, 255, 255))  # White text
        screen.blit(quit_button_text, (button_x + (button_width - quit_button_text.get_width()) // 2, quit_button_y + (button_height - quit_button_text.get_height()) // 2))

        pygame.display.flip()

def display_draw(message):
    font = pygame.font.Font(None, 72)
    text = font.render(message, True, (255, 255, 255))
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))

    # Create "Quitter" button
    button_width, button_height = 200, 60
    button_x = WIDTH // 2 - button_width // 2
    quit_button_y = HEIGHT // 2 + 100
    quit_button_rect = pygame.Rect(button_x, quit_button_y, button_width, button_height)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if quit_button_rect.collidepoint(event.pos):
                    pygame.quit()
                    exit()

        screen.fill((0, 0, 0))  # Background black
        screen.blit(text, text_rect)

        # Draw the "Quitter" button (red with white text)
        pygame.draw.rect(screen, (255, 0, 0), quit_button_rect)  # Red button
        quit_button_text = pygame.font.Font(None, 36).render("Quitter", True, (255, 255, 255))  # White text
        screen.blit(quit_button_text, (button_x + (button_width - quit_button_text.get_width()) // 2, quit_button_y + (button_height - quit_button_text.get_height()) // 2))

        pygame.display.flip()

def reset_game():
    global board, game_over
    board = chess.Board()  # Réinitialiser l'échiquier à l'état initial
    game_over = False  # Remettre le flag de fin de jeu à False

def random_move():
    legal_moves = list(board.legal_moves)
    if not legal_moves:
        return None  # Aucun coup légal n'est possible
    return random.choice(legal_moves)

def check_pawn_promotion():
    global board, turn  # Assurez-vous que 'turn' est également global.
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece and piece.piece_type == chess.PAWN:
            rank = chess.square_rank(square)
            if (piece.color == chess.WHITE and rank == 7) or (piece.color == chess.BLACK and rank == 0):
                # Ouvrir une fenêtre Tkinter pour demander la promotion
                window = tk.Tk()
                window.withdraw()  # Cacher la fenêtre principale

                promote = messagebox.askyesno("Promotion", "Voulez-vous promouvoir ce pion?")
                if promote:
                    piece_choice = simpledialog.askstring("Choix de promotion", 
                                                          "Choisissez une pièce (q, r, n, b) :", 
                                                          parent=window)
                    if piece_choice in PROMOTION_OPTIONS:
                        # Déterminer la rangée de promotion
                        promotion_rank = 7 if piece.color == chess.WHITE else 0
                        promotion_square = chess.square(chess.square_file(square), promotion_rank)

                        # Effectuer la promotion avec le bon indice
                        promotion_piece = {'q': chess.QUEEN, 'r': chess.ROOK, 
                                           'n': chess.KNIGHT, 'b': chess.BISHOP}[piece_choice]
                        move = chess.Move(square, promotion_square, promotion=promotion_piece)

                        if move in board.legal_moves:
                            board.push(move)  # Appliquer la promotion correctement
                            turn = not turn  # Changer le tour après une promotion

                window.destroy()  # Fermer la fenêtre Tkinter




def check_pawn_promotion_on_click(square):
    global board, turn  # Assurez-vous que 'turn' est global.
    piece = board.piece_at(square)
    
    if piece and piece.piece_type == chess.PAWN:
        rank = chess.square_rank(square)
        
        # Vérifier si le pion est sur la 6e ligne pour les blancs ou la 1ère ligne pour les noirs
        if (piece.color == chess.WHITE and rank == 6) or (piece.color == chess.BLACK and rank == 1):
            # Ouvrir une fenêtre Tkinter pour demander la promotion
            window = tk.Tk()
            window.withdraw()  # Cacher la fenêtre principale

            promote = messagebox.askyesno("Promotion", "Voulez-vous promouvoir ce pion?")
            if promote:
                piece_choice = simpledialog.askstring("Choix de promotion", 
                                                      "Choisissez une pièce (q, r, n, b) :", 
                                                      parent=window)
                if piece_choice in PROMOTION_OPTIONS:
                    # Déterminer la rangée de promotion
                    promotion_rank = 7 if piece.color == chess.WHITE else 0
                    promotion_square = chess.square(chess.square_file(square), promotion_rank)

                    # Effectuer la promotion avec le bon indice
                    promotion_piece = {'q': chess.QUEEN, 'r': chess.ROOK, 
                                       'n': chess.KNIGHT, 'b': chess.BISHOP}[piece_choice]
                    move = chess.Move(square, promotion_square, promotion=promotion_piece)

                    if move in board.legal_moves:
                        board.push(move)  # Appliquer la promotion correctement
                        turn = not turn  # Changer le tour après une promotion

            window.destroy()  # Fermer la fenêtre Tkinter

# Fonction IA
def play_with_ai():
    global board, game_over, turn
    game_over = False
    turn = True  # True: White's turn (Player), False: Black's turn (AI)
    selected_square = -1  # Initialement aucune case sélectionnée

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            elif event.type == pygame.MOUSEBUTTONDOWN and turn and not game_over:
                square = get_square_under_mouse(event.pos)
                if square != -1:
                    piece = board.piece_at(square)

                    # Vérifier si le pion sur lequel on clique est sur la ligne avant-dernière
                    if piece and piece.piece_type == chess.PAWN:
                        check_pawn_promotion_on_click(square)  # Vérifier la promotion lors du clic

                    if selected_square == -1:  # Sélectionner une pièce
                        if piece is not None and piece.color == chess.WHITE:
                            selected_square = square
                    else:  # Déplacer la pièce sélectionnée
                        move = chess.Move(selected_square, square)

                        # Vérifier si le mouvement est légal
                        if move in board.legal_moves:
                            board.push(move)
                            check_pawn_promotion()  # Vérifier la promotion après le mouvement
                            turn = not turn
                        selected_square = -1

        draw_board()  # Dessiner le plateau
        draw_pieces()  # Dessiner les pièces
        pygame.display.flip()  # Mettre à jour l'affichage

        # Vérifier les conditions de fin de partie
        if board.is_checkmate():
            winner = "Blanc" if turn else "Noir"
            display_winner(winner)
            game_over = True
        elif board.is_stalemate() or board.is_insufficient_material() or board.is_seventyfive_moves():
            display_draw("Match nul!")
            game_over = True

        if not turn and not game_over:  # Si c'est le tour de l'IA
            pygame.time.delay(200)  # Délai de 0,2 seconde pour l'IA
            move = random_move()
            if move is not None:
                board.push(move)
                check_pawn_promotion()  # Vérifier la promotion après le mouvement
                turn = not turn
            else:
                game_over = True

        draw_board()  # Dessiner le plateau
        draw_pieces()  # Dessiner les pièces
        pygame.display.flip()  # Mettre à jour l'affichage

        # Vérifier les conditions de fin de partie
        if board.is_checkmate():
            winner = "Blanc" if turn else "Noir"
            display_winner(winner)
            game_over = True
        elif board.is_stalemate() or board.is_insufficient_material() or board.is_seventyfive_moves():
            display_draw("Match nul!")
            game_over = True

def play_with_two_players():
    global board, game_over, turn
    game_over = False
    turn = True  # True: White's turn, False: Black's turn
    selected_square = -1  # Initialement aucune case sélectionnée

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                square = get_square_under_mouse(event.pos)
                if square != -1:
                    piece = board.piece_at(square)

                    # Vérifier si le pion sur lequel on clique est sur la ligne avant-dernière
                    if piece and piece.piece_type == chess.PAWN:
                        check_pawn_promotion_on_click(square)  # Vérifier la promotion lors du clic

                    if selected_square == -1:  # Sélectionner une pièce
                        if piece is not None and piece.color == (chess.WHITE if turn else chess.BLACK):
                            selected_square = square
                    else:  # Déplacer la pièce sélectionnée
                        move = chess.Move(selected_square, square)

                        # Vérifier si le mouvement est légal
                        if move in board.legal_moves:
                            board.push(move)
                            turn = not turn
                        selected_square = -1

        draw_board()  # Dessiner le plateau
        draw_pieces()  # Dessiner les pièces
        pygame.display.flip()  # Mettre à jour l'affichage

        # Vérifier les conditions de fin de partie
        if board.is_checkmate():
            winner = "Noir" if turn else "Blanc"
            display_winner(winner)
            game_over = True
        elif board.is_stalemate() or board.is_insufficient_material() or board.is_seventyfive_moves():
            display_draw("Match nul!")
            game_over = True



        draw_board()  # Dessiner le plateau
        draw_pieces()  # Dessiner les pièces
        pygame.display.flip()  # Mettre à jour l'affichage

        # Vérifier les conditions de fin de partie
        if board.is_checkmate():
            winner = "Noir" if turn else "Blanc"
            display_winner(winner)
            game_over = True
        elif board.is_stalemate() or board.is_insufficient_material() or board.is_seventyfive_moves():
            display_draw("Match nul!")
            game_over = True



def play_ia_vs_ia():
    global board, game_over
    game_over = False
    turn = True  # True: White's turn, False: Black's turn

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        # Si c'est le tour de l'IA, effectuer un mouvement après un délai de 0,2 sec
        pygame.time.delay(200)  # Délai de 0,2 seconde pour l'IA

        move = random_move()
        board.push(move)
        turn = not turn

        draw_board()
        draw_pieces()
        pygame.display.flip()

        # Vérifier la victoire ou match nul
        if board.is_checkmate():
            display_winner("Blanc" if turn else "Noir")
            game_over = True
        elif board.is_stalemate() or board.is_insufficient_material() or board.is_seventyfive_moves():
            display_draw("Match nul!")
            game_over = True

def start_game(mode):
    global game_over
    if mode == "AI":
        play_with_ai()
    elif mode == "2 Players":
        play_with_two_players()  # Utiliser la fonction mode 2 joueurs
    elif mode == "IA vs IA":
        play_ia_vs_ia()  # Ajouter ce mode IA contre IA

# Création de la fenêtre Tkinter pour le menu
def menu_window():
    window = tk.Tk()
    window.title("Menu de sélection")

    # Définir une taille minimale pour la fenêtre
    window.geometry("300x200")  # Fixer la taille de la fenêtre à 300x200 pixels
    
    def start_ai_game():
        window.destroy()
        start_game("AI")
        
    def start_two_player_game():
        window.destroy()
        start_game("2 Players")
        
    def start_ia_vs_ia_game():
        window.destroy()
        start_game("IA vs IA")
    
    tk.Button(window, text="Jouer contre l'IA", command=start_ai_game).pack(pady=10)
    tk.Button(window, text="Jouer à 2 joueurs", command=start_two_player_game).pack(pady=10)
    tk.Button(window, text="IA vs IA", command=start_ia_vs_ia_game).pack(pady=10)
    window.mainloop()

# Démarrer le menu
menu_window()
