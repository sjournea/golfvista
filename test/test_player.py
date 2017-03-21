import unittest

from golf_db.player import GolfPlayer
from golf_db.test_data import GolfPlayers


class GolfPlayerInitCase(unittest.TestCase):

  def test_init_empty(self):
    # check default parameters
    player = GolfPlayer(email='sjournea@gmail.com', handicap=20.0)
    player.validate()
    self.assertEqual(player.email, 'sjournea@gmail.com')
    self.assertIsNone(player.last_name)
    self.assertIsNone(player.first_name)
    self.assertIsNone(player.nick_name)
    self.assertEqual(player.handicap, 20)

  def test_init_from_dict(self):
    for dct in GolfPlayers:
      player = GolfPlayer(dct=dct)
      player.validate()
      self.assertEqual(dct['last_name'], player.last_name)
      self.assertEqual(dct['first_name'], player.first_name)
      self.assertEqual(dct['nick_name'], player.nick_name)
      self.assertEqual(dct['handicap'], player.handicap)
      

class GolfPlayerDictCase(unittest.TestCase):
  def test_toDict(self):
    for dct in GolfPlayers:
      player = GolfPlayer(dct=dct)
      player.validate()
      self.assertEqual(player.toDict(), dct)
    
  def test_fromDict(self):
    for dct in GolfPlayers:
      player = GolfPlayer()
      player.fromDict(dct)
      player.validate()
      self.assertEqual(player.toDict(), dct)

  def test_equalOperator(self):
    for dct in GolfPlayers:
      player1 = GolfPlayer(dct=dct)
      player2 = GolfPlayer(dct=player1.toDict())
      self.assertEqual(player1, player2)
      player1.handicap += 1 
      self.assertNotEqual(player1, player2)

