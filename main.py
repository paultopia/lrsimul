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
        self.submissions = []  # list for both journals to track what they got and authors to track were they submitted.

class Author(Player):
    def add_article(self, quality=None):
        self.article = Article(quality)
        if higher_is_smarter:
            self.track_article_to_prestige()
        
    def track_article_to_prestige(self):
        "higher adjustment factor = smaller move of discernment toward prestige. (1 = discernment just becomes prestige)"
        if self.prestige > self.article.quality:
            self.article.quality = self.article.quality + ((self.prestige - self.article.quality) / self.adjustment_factor)
        if self.article.quality > self.prestige:
            self.article.quality = self.article.quality - ((self.article.quality - self.prestige) / self.adjustment_factor)
            
    def submit(journal):  # consult strategy and decide whether to submit to a journal.  probably also make a list of which journals have been sumbitted to etc.
        pass 
        # TODO

class Journal(Player):
    def __init__(self, discernment=None, prestige=None, strategy=None, available_strategies=None, higher_is_smarter=False, adjustment_factor=2):
        if discernment:
            self.discernment = discernment
        else:
            self.discernment = random.randint(1, 10)
        super.__init__(self, prestige, strategy, available_strategies, higher_is_smarter, adjustment_factor)
        if self.higher_is_smarter:
            self.track_discernment_to_prestige()
    
    def track_discernment_to_prestige(self):  
        "higher adjustment factor = smaller move of discernment toward prestige. (1 = discernment just becomes prestige)"
        if self.prestige > self.discernment:
            self.discernment = self.discernment + ((self.prestige - self.discernment) / self.adjustment_factor)
        if self.discernment > self.prestige:
            self.discernment = self.discernment - ((self.discernment - self.prestige) / self.adjustment_factor)
            
    def consider(article):  # consult strategy and decide whether to accept article.  probably also keep list of what articles have been received etc.
        pass
        # TODO

#### THIS IS THE HARD PART... DEFINING THE STRATEGY SPACE

def Strategy(object):
    pass

def Journal_Strategy(Strategy):
    pass
    
def AuthorStrategy(Strategy):
    pass
    
    
def Game(object):
    "do the setup, pick strategies, adjudgment factors, assign prestiges, create articles and assign to authors, etc. and run game"
    pass
    
if __name__ = "__main__":
    print("One day, this will be implemented and then I will run the game.")