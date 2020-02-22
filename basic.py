from numpy import rnorm
import random


class NoStrategiesAvailableError(Exception):
    "raised when author or journal attempts to select a strategy, but there aren't any"
    pass

class Article(object):
    def __init__(self, quality=None):
        if quality:
            self.quality = quality
        else:
            self.quality = random.randint(1, 10)
        self.author = None  # this sort of thing is going to grossly abuse python's reference semantics and I hope it's right
        self.submissions = []
            
class Player(object):
    def __init__(self, prestige=None, strategy=None, available_strategies=None, higher_is_smarter=False, adjustment_factor=2):
        if prestige:
            self.prestige = prestige
        else:
            self.prestige = random.randint(1, 10)
        if strategy:
            self.strategy = strategy
        else:
            try:
                self.strategy = random.choice(available_strategies)
            except:
                raise NoStrategiesAvailableError
        self.higher_is_smarter = higher_is_smarter
        self.adjustment_factor = adjustment_factor
