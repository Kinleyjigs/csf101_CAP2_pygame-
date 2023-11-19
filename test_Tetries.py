
import unittest
from pygame_Tetries import pygame_Tetries
# import pygame_Tetries.py as pygame_Tetries

class TestTetris(unittest.TestCase):
    def setUp(self):
        self.test_block_i = pygame_Tetries.BlockI(self.tetris)
        self.test_block_j = pygame_Tetries.BlockJ(self.tetris)
        self.test_block_l = pygame_Tetries.BlockL(self.tetris)
        self.test_block_o = pygame_Tetries.BlockO(self.tetris)
        self.test_block_s = pygame_Tetries.BlockS(self.tetris)
        self.test_block_t = pygame_Tetries.BlockT(self.tetris)
        self.test_block_z = pygame_Tetries.BlockZ(self.tetris)
        self._turns = (1, 2, 3, 0)

    def test_go_down(self):
        self.tetris.start(self.test_block_j)
        self.tetris.go(pygame_Tetries.Move.DOWN)
        self.assertEqual(pygame_Tetries.background_blocks[2][4].number, 2)

    def test_go_left(self):
        self.tetris.start(self.test_block_j)
        self.tetris.go(pygame_Tetries.Move.LEFT)
        self.assertEqual(pygame_Tetries.background_blocks[0][3].number, 2)

    def test_go_right(self):
        self.tetris.start(self.test_block_j)
        self.tetris.go(pygame_Tetries.Move.RIGHT)
        self.assertEqual(pygame_Tetries.background_blocks[0][5].number, 2)

    def test_turn_i(self):
        self.tetris.start(self.test_block_i)
        self.tetris.go(pygame_Tetries.Move.DOWN)
        for state in self._turns:
            self.test_block_i.turn()
            self.assertEqual(self.tetris.state, state)

    def test_turn_j(self):
        self.tetris.start(self.test_block_j)
        self.tetris.go(pygame_Tetries.Move.DOWN)
        for state in self._turns:
            self.test_block_j.turn()
            self.assertEqual(self.tetris.state, state)

    def setUp(self):
       pygame.init()
       self.screen = pygame.display.set_mode((800, 600))

    def test_display_game_over(self):
       display_game_over()
       self.assertIn("GAME OVER", pygame.display.get_surface().get_at((70, SCREEN_HEIGHT // 2 - 62)))
       self.assertIn("Press Q to quit ", pygame.display.get_surface().get_at((90, SCREEN_HEIGHT // 2 + 20)))
       self.assertIn("Press Space to play again", pygame.display.get_surface().get_at((90, SCREEN_HEIGHT // 2 + 60)))

    def tearDown(self):
       pygame.quit()

if __name__ == '__main__':
   unittest.main()

    # Add similar tests for other shapes as well

if __name__ == '__main__':
    unittest.main()
