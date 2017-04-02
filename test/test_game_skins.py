import unittest
import datetime

from golf_db.round import GolfRound
#from golf_db.test_data import GolfRounds,GolfCourses, GolfPlayers
from golf_db.db import GolfDB
from golf_db.game_skins import SkinsGame
from golf_db.exceptions import GolfException


class GolfSkinsGameTest(unittest.TestCase):
  @classmethod
  def setUpClass(cls):
    cls.db = GolfDB(database='golf_game_test')
    cls.db.create()
    
  def setUp(self):
    course_name = 'Canyon Lakes'
    tee_name = 'Blue'
    date_of_round = datetime.datetime(2017, 3, 23)
    lstPlayers = ['sjournea', 'snake']
    
    self.gr = GolfRound()
    self.gr.course = self.db.courseFind(course_name)
    self.gr.date = date_of_round
    for email in lstPlayers:
      pl = self.db.playerFind(email)
      self.gr.addPlayer(pl, tee_name)

  def test_game_init(self):
    g = SkinsGame(self.gr, self.gr.scores)
    
  def test_game_start(self):
    g = SkinsGame(self.gr, self.gr.scores)
    g.start()
    for pl in g.scores:
      self.assertEquals(pl.net['score'], 18*[0])
      self.assertEquals(pl.net['in'], 0)
      self.assertEquals(pl.net['out'], 0)
      self.assertEquals(pl.net['total'], 0)
      self.assertEquals(pl.skins['skin'], 18*[0])
      self.assertEquals(pl.skins['in'], 0)
      self.assertEquals(pl.skins['out'], 0)
      self.assertEquals(pl.skins['total'], 0)
    self.assertEqual(g.carryover, 1)
    
  def test_game_add_score(self):
    g = SkinsGame(self.gr, self.gr.scores)
    g.start()
    g.addScore(1, [4,4])
    
  def test_game_scorecard(self):
    g = SkinsGame(self.gr, self.gr.scores)
    g.start()
    g.addScore(1, [4,4])
    dct = g.getScorecard()
    self.assertIn('header', dct)
    self.assertIn('skins', dct)

  def test_game_leaderboard(self):
    g = SkinsGame(self.gr, self.gr.scores)
    g.start()
    g.addScore(1, [4,4])
    dct = g.getLeaderboard()
    self.assertIn('hdr', dct)
    self.assertIn('leaderboard', dct)