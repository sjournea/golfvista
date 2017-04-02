""" game.py - GolfGame class."""
from abc import ABCMeta, abstractmethod
from .exceptions import GolfException

class GolfGame(object):
  """Base class for all golf games."""
  __metaclass__=ABCMeta
  def __init__(self, golf_round, scores, options=None):
    self.golf_round = golf_round
    self.scores = scores
    self.options = options if options else {}

  def validate(self):
    """Validate a game."""
    pass

  @abstractmethod
  def start(self):
    """Start the game."""
    pass

  @abstractmethod
  def addScore(self, hole_index, lstScores):
    """add scores for a hole."""
    pass

  @abstractmethod
  def getScorecard(self, **kwargs):
    """Return scorecard dictionary for this game."""
    pass
  
  @abstractmethod
  def getLeaderboard(self, **kwargs):
    """Return leaderboard dictionary for this game."""
    pass

  def complete(self):
    """Complete a game. Overload for process when a game is complete."""
    pass


