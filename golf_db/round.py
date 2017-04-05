from .course import GolfCourse
from .score import GolfScore
from .exceptions import GolfException
from .game_factory import GolfGameFactory
from util.tl_logger import TLLog

log = TLLog.getLogger('round')

class GolfRound(object):
  """A round of golf."""
  def __init__(self, dct=None):
    super(GolfRound, self).__init__()
    self.course = None
    self.date = None
    self.scores = []
    self.games = {}
    if dct:
      self.fromDict(dct)

  def fromDict(self, dct):
    self.course = GolfCourse(dct['course'])
    self.date = dct.get('date')
    self.scores = [GolfScore(player_dct) for player_dct in dct['players']]
    self.games = dct.get('games', {})

  def toDict(self):
    return { 'course': self.course.toDict(),
             'date': self.date,
             'players': [player.toDict() for player in self.scores],
             'games': self.games,
           }

  def __eq__(self, other):
    return (self.course == other.course and
            self.date == other.date and
            self.scores == other.scores and
            self.games == other.games)

  def __ne__(self, other):
    return not self == other

  def addPlayer(self, player, tee_name):
    """Add a player to this round."""
    gs = GolfScore()
    gs.player = player
    gender = 'mens' if gs.player.gender == 'man' else 'womens'
    gs.tee = self.course.getTee(tee_name, gender=gender)
    gs.calcCourseHandicap()
    self.scores.append(gs)

  def addGame(self, game, options=None):
    """Add a game to this round.
    
    Args:
      game: Game to add.
      options: dictionary of game options.
    Returns:
      game created.
    """
    game_class = GolfGameFactory(game)
    self.games[game] = game_class(self, self.scores, options)
    return self.games[game]
  
  def start(self):
    """Start round. Start all games."""
    for game in self.games.itervalues():
      game.start()

  def addScores(self, hole, lstGross):
    """Add some scores for this round.

    Args:
      hole : hole number, 1-18.
      lstGross : gross score for each player.
    """
    if hole < 1 or hole > len(self.course.holes):
      raise GolfException('hole number must be in 1-{}'.format(len(self.course.holes)))
    if len(lstGross) != len(self.scores):
      raise GolfException('gross scores do not match number of players')
    for game in self.games.itervalues():
      game.addScore(hole-1, lstGross)

  def getGame(self, game):
    if game not in self.games:
      raise GolfException('game "{}" not found'.format(game))
    return self.games[game]
  
  def getScorecard(self, game, **kwargs):
    """Scorecard for game."""
    return self.getGame(game).getScorecard(**kwargs)
  
  def getLeaderboard(self, game, **kwargs):
    """Leaderboard for game."""
    return self.getGame(game).getLeaderboard(**kwargs)
  
  def getStatus(self, game, **kwargs):
    """Staus for game."""
    return self.getGame(game).getStatus(**kwargs)
  
  def __str__(self):
    return '{} - {:<25} - {:<25} - {}'.format(
      self.date.date(), self.course.name,
      ','.join([score.player.nick_name for score in self.scores]),
      ','.join(self.games.keys()))
