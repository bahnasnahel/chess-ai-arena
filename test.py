import chess

plateau = chess.Board()           # un échiquier en position de départ
print(plateau)                    # l'affiche en texte
print(list(plateau.legal_moves))  # tous les coups possibles
plateau.push_san("e4")            # joue le coup e4
print(plateau)