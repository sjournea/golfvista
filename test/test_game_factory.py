import unittest

from golf_db.game_factory import GolfGameFactory, GolfGameList
from golf_db.exceptions import GolfException
from golf_db.game_skins import SkinsGame
from golf_db.game_net import NetGame
from golf_db.game_gross import GrossGame


class GolfGameFactoryTest(unittest.TestCase):
  def test_games_list(self):
    lstGames = GolfGameList()
    lst = sorted(lstGames)
    self.assertListEqual(lstGames, lst)
    
  def test_games(self):
    lstGames = [
      ('skins', SkinsGame),
      ('gross', GrossGame),
      ('net', NetGame),
    ]
    for game, game_class in lstGames:
      gm_cls = GolfGameFactory(game)
      self.assertEqual(gm_cls, game_class)
    
  def test_bad_game(self):
    with self.assertRaises(GolfException):
      gm_cls = GolfGameFactory('bad_golf_game_name')

