"""
Board texture utility functions
"""

RANK_A = 14
RANK_K = 13
RANK_Q = 12
RANK_J = 11
RANK_T = 10
RANK_9 = 9
RANK_8 = 8
RANK_7 = 7
RANK_6 = 6
RANK_5 = 5
RANK_4 = 4
RANK_3 = 3
RANK_2 = 2

SUIT_S = "s"
SUIT_H = "h"
SUIT_C = "c"
SUIT_D = "d"


def ranks(cards):
    """Get set of ranks contained on board"""
    return set(r for (r, _) in cards)


def suits(cards):
    """Get set of suits contained on board"""
    return set(s for (s, _) in cards)


def is_flop(cards):
    """Check if cards form a valid flop (i.e., length 3)"""
    return len(cards) is 3


def flop_is_three_of_a_kind(cards):
    """Check if flop contains three of a kind"""
    return is_flop(cards) and len(ranks(cards)) is 1


def flop_is_paired(cards):
    """Check if flop contains three of a kind"""
    return is_flop(cards) and len(ranks(cards)) is 2


def flop_is_unpaired(cards):
    """Check if flop contains three of a kind"""
    return is_flop(cards) and len(ranks(cards)) is 3


def flop_is_monotone(cards):
    """Check if flop is a monotone board"""
    return is_flop(cards) and len(suits(cards)) is 1


def flop_is_fd(cards):
    """Check if flop is a monotone board"""
    return is_flop(cards) and len(suits(cards)) is 2


def flop_is_rainbow(cards):
    """Check if flop is a monotone board"""
    return is_flop(cards) and len(suits(cards)) is 3


def board_has_high_rank(board, high_rank):
    """Check if board has specified rank for high card"""
    return sorted(ranks(board))[-1] == high_rank


def board_is_lte_than_rank(board, max_rank):
    """Check if all boards cards have rank less than or equal to max rank"""
    return sorted(ranks(board))[-1] <= max_rank


def board_is_gte_than_rank(board, max_rank):
    """Check if all boards cards have rank greater than or equal to max rank"""
    return sorted(ranks(board))[-1] >= max_rank


def board_is_ace_high(board):
    """Check if highest rank is A"""
    return board_has_high_rank(board, RANK_A)


def board_is_k_high(board):
    """Check if highest rank is K"""
    return board_has_high_rank(board, RANK_K)


def board_is_q_high(board):
    """Check if highest rank is Q"""
    return board_has_high_rank(board, RANK_Q)


def board_is_j_high(board):
    """Check if highest rank is J"""
    return board_has_high_rank(board, RANK_J)


def board_is_t_high(board):
    """Check if highest rank is T"""
    return board_has_high_rank(board, RANK_T)


def board_is_broadway(board):
    """Check if board is all broadway"""
    return board_is_gte_than_rank(board, RANK_T)
