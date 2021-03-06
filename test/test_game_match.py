import unittest
import datetime

from golf_db.round import GolfRound
from golf_db.player import GolfPlayer
from golf_db.course import GolfCourse
#from golf_db.test_data import GolfRounds,GolfCourses, GolfPlayers
from golf_db.db import GolfDBAdmin
#from golf_db.game import GolfGame, SkinsGame, NetGame
from golf_db.game_match import MatchGame
#from golf_db.game_factory import GolfGameFactory
#from golf_db.exceptions import GolfException


class GolfMatchGameTest(unittest.TestCase):
  @classmethod
  def setUpClass(cls):
    cls.db = GolfDBAdmin(database='golf_game_test')
    cls.db.create()
    
  def setUp(self):
    course_name = 'Canyon Lakes'
    tee_name = 'Blue'
    date_of_round = datetime.datetime(2017, 3, 23)
    lstPlayers = ['sjournea', 'snake']
    
    self.gr = GolfRound()
    self.gr.course = self.db.courseFind(course_name, dbclass=GolfCourse)[0]
    self.gr.date = date_of_round
    for email in lstPlayers:
      pl = self.db.playerFind(email, dbclass=GolfPlayer)[0]
      self.gr.addPlayer(pl, tee_name)

  def test_game_init(self):
    g = MatchGame(self.gr, self.gr.scores)
    
  def test_game_start(self):
    g = MatchGame(self.gr, self.gr.scores)
    g.start()
    for pl in g.scores:
      self.assertEquals(pl._score, 18*[None])
      self.assertEqual(len(pl._bumps), 18)
      self.assertEquals(pl._hole, 18*[None])
      self.assertEquals(pl._score, 18*[None])
      self.assertEquals(pl._in, 0)
      self.assertEquals(pl._out, 0)
      self.assertEquals(pl._total, 0)
      
  def test_game_add_score(self):
    g = MatchGame(self.gr, self.gr.scores)
    g.start()
    g.addScore(1, [4,4])
    
  def test_game_scorecard(self):
    g = MatchGame(self.gr, self.gr.scores)
    g.start()
    g.addScore(1, [4,4])
    dct = g.getScorecard()
    self.assertIn('header', dct)
    self.assertIn('players', dct)

  def test_game_leaderboard(self):
    g = MatchGame(self.gr, self.gr.scores)
    g.start()
    g.addScore(1, [4,4])
    dct = g.getLeaderboard()
    self.assertIn('hdr', dct)
    self.assertIn('leaderboard', dct)

  def test_game_status(self):
    g = MatchGame(self.gr, self.gr.scores)
    g.start()
    dct = g.getStatus()
    self.assertIn('line', dct)
    #self.assertIn('next_hole', dct)
    #self.assertIn('par', dct)
    #self.assertIn('handicap', dct)
    #self.assertEqual(dct['next_hole'], 1)
    #self.assertEqual(dct['par'], self.gr.course.holes[0].par)
    #self.assertEqual(dct['handicap'], self.gr.course.holes[0].handicap)
    #for index in range(18):
      #g.addScore(index, [4,4])
      #dct = g.getStatus()
      #self.assertIn('line', dct)
      #self.assertIn('next_hole', dct)
      #self.assertIn('par', dct)
      #self.assertIn('handicap', dct)
      #if index < 17:
        #self.assertEqual(dct['next_hole'], index+2)
        #self.assertEqual(dct['par'], self.gr.course.holes[index+1].par)
        #self.assertEqual(dct['handicap'], self.gr.course.holes[index+1].handicap)
      #else:
        #self.assertIsNone(dct['next_hole'])
        #self.assertIsNone(dct['handicap'])
        #self.assertEqual(dct['par'], self.gr.course.total)
