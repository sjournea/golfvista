import unittest

from golf_db.course import GolfCourse, GolfHole, GolfPlayer, GolfScore
from golf_db.test_data import GolfCourses, GolfPlayers, CanyonLake_Players
from util.tl_logger import TLLog
log = TLLog.getLogger('mongo')

class GolfCourseInitCase(unittest.TestCase):
  lstDicts = [
    {'name': 'Canyon Lakes', 'holes':[], 'tees':[]},
    {'name': 'Santa Clara', 'holes':[], 'tees':[]},
    {'name': 'Diablo Grande', 'holes':[], 'tees':[]},
  ]

  def test_init_empty(self):
    # check default parameters
    course = GolfCourse()
    self.assertIsNone(course.name)
    self.assertEqual(course.holes, [])
    self.assertEqual(course.tees, [])

  def test_init_from_dict(self):
    for dct in self.lstDicts:
      course = GolfCourse(dct=dct)
      self.assertEqual(dct['name'], course.name)
      self.assertEqual(dct['holes'], course.holes)
      self.assertEqual(dct['tees'], course.tees)
      
class GolfCourseDictCase(unittest.TestCase):
  def test_toDict(self):
    self.maxDiff = None
    # check course name
    for dct in GolfCourses:
      course = GolfCourse(dct=dct) 
      self.assertEqual(course.toDict(), dct)
    
  def test_fromDict(self):
    for dct in GolfCourses:
      course = GolfCourse()
      course.fromDict(dct)
      self.assertEqual(course.toDict(), dct)

  def test_equalOperator(self):
    for dct in GolfCourses:
      course = GolfCourse(dct=dct)
      course2 = GolfCourse(dct=course.toDict())
      self.assertEqual(course, course2)
      course2.holes[0].par += 1
      self.assertNotEqual(course, course2)

class GolfHoleInitCase(unittest.TestCase):
  lstDicts = [
    {'par': 5, 'handicap': 1},
    {'par': 4, 'handicap': 10},
    {'par': 3, 'handicap': 18},
  ]

  def test_init_empty(self):
    # check default parameters
    hole = GolfHole()
    self.assertIsNone(hole.par)
    self.assertIsNone(hole.handicap)

  def test_init_from_dict(self):
    for dct in self.lstDicts:
      hole = GolfHole(dct=dct)
      self.assertEqual(dct['par'], hole.par)
      self.assertEqual(dct['handicap'], hole.handicap)
      

class GolfHoleDictCase(unittest.TestCase):
  lstDicts = [
    {'par': 5, 'handicap': 1},
    {'par': 4, 'handicap': 10},
    {'par': 3, 'handicap': 18},
  ]
  def test_toDict(self):
    # check course name
    for dct in self.lstDicts:
      hole = GolfHole(dct=dct) 
      self.assertEqual(hole.toDict(), dct)
    
  def test_fromDict(self):
    # check course name
    for dct in self.lstDicts:
      hole = GolfHole() 
      hole.fromDict(dct)
      self.assertEqual(hole.toDict(), dct)

  def test_equalOperator(self):
    for dct in self.lstDicts:
      hole1 = GolfHole(dct=dct) 
      hole2 = GolfHole(dct=hole1.toDict()) 
      self.assertEqual(hole1, hole2)
      hole2.par += 1 
      self.assertNotEqual(hole1, hole2)


class GolfPlayerInitCase(unittest.TestCase):

  def test_init_empty(self):
    # check default parameters
    player = GolfPlayer()
    self.assertIsNone(player.last_name)
    self.assertIsNone(player.first_name)
    self.assertIsNone(player.nick_name)
    self.assertIsNone(player.handicap)

  def test_init_from_dict(self):
    for dct in GolfPlayers:
      player = GolfPlayer(dct=dct)
      self.assertEqual(dct['last_name'], player.last_name)
      self.assertEqual(dct['first_name'], player.first_name)
      self.assertEqual(dct['nick_name'], player.nick_name)
      self.assertEqual(dct['handicap'], player.handicap)
      

class GolfPlayerDictCase(unittest.TestCase):
  def test_toDict(self):
    for dct in GolfPlayers:
      player = GolfPlayer(dct=dct) 
      self.assertEqual(player.toDict(), dct)
    
  def test_fromDict(self):
    for dct in GolfPlayers:
      player = GolfPlayer()
      player.fromDict(dct)
      self.assertEqual(player.toDict(), dct)

  def test_equalOperator(self):
    for dct in GolfPlayers:
      player1 = GolfPlayer(dct=dct)
      player2 = GolfPlayer(dct=player1.toDict())
      self.assertEqual(player1, player2)
      player1.handicap += 1 
      self.assertNotEqual(player1, player2)


class GolfScoreInitCase(unittest.TestCase):

  def test_init_empty(self):
    # check default parameters
    player = GolfScore()
    self.assertIsNone(player.player.nick_name)
    self.assertEqual(player.gross, [])

  def test_init_from_dict(self):
    for dct in CanyonLake_Players:
      score = GolfScore(dct=dct)
      self.assertEqual(dct['player'], score.player.toDict())
      self.assertEqual(dct['gross'], score.gross)
      
