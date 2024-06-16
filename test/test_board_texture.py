# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

import unittest
import board_texture
from board_texture import *

BOARD_23hh = [(RANK_2, SUIT_H), (RANK_3, SUIT_H)]
BOARD_234hhh = [(RANK_2, SUIT_H), (RANK_3, SUIT_H), (RANK_4, SUIT_H)]
BOARD_K95hsd = [(RANK_K, SUIT_H), (RANK_9, SUIT_S), (RANK_5, SUIT_D)]
BOARD_K957hsdc = [
    (RANK_K, SUIT_H),
    (RANK_9, SUIT_S),
    (RANK_5, SUIT_D),
    (RANK_7, SUIT_C),
]

BOARD_TTTshc = [(RANK_T, SUIT_S), (RANK_T, SUIT_H), (RANK_T, SUIT_C)]
BOARD_TTTTshcd = [
    (RANK_T, SUIT_S),
    (RANK_T, SUIT_H),
    (RANK_T, SUIT_C),
    (RANK_T, SUIT_D),
]
BOARD_TT9shc = [(RANK_T, SUIT_S), (RANK_T, SUIT_H), (RANK_9, SUIT_C)]


class TestBoardTexture(unittest.TestCase):
    def test_ranks(self):
        self.assertEqual(
            board_texture.ranks(BOARD_234hhh), set((RANK_2, RANK_3, RANK_4))
        )
        self.assertEqual(
            board_texture.ranks(BOARD_K95hsd), set((RANK_K, RANK_9, RANK_5))
        )

    def test_suits(self):
        self.assertEqual(board_texture.suits(BOARD_234hhh), set((SUIT_H,)))
        self.assertEqual(
            board_texture.suits(BOARD_K95hsd), set((SUIT_H, SUIT_S, SUIT_D))
        )

    def test_is_flop(self):
        self.assertTrue(board_texture.is_flop(BOARD_234hhh))
        self.assertTrue(board_texture.is_flop(BOARD_K95hsd))
        self.assertFalse(board_texture.is_flop(BOARD_K957hsdc))
        self.assertFalse(board_texture.is_flop(BOARD_23hh))
        self.assertFalse(board_texture.is_flop(BOARD_K957hsdc))

    def test_is_three_of_a_kind(self):
        self.assertTrue(board_texture.flop_is_three_of_a_kind(BOARD_TTTshc))
        self.assertFalse(board_texture.flop_is_three_of_a_kind(BOARD_TT9shc))
        self.assertFalse(board_texture.flop_is_three_of_a_kind(BOARD_234hhh))
        self.assertFalse(board_texture.flop_is_three_of_a_kind(BOARD_TTTTshcd))
