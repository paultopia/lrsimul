import random
from strategies import *


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

class Author(Player):
    def add_article(self, quality=None):
        self.article = Article(quality)
        if higher_is_smarter:
            self.track_article_to_prestige()
        self.article.author = self
        
    def track_article_to_prestige(self):
        "higher adjustment factor = smaller move of discernment toward prestige. (1 = discernment just becomes prestige)"
        if self.prestige > self.article.quality:
            self.article.quality = self.article.quality + ((self.prestige - self.article.quality) / self.adjustment_factor)
        if self.article.quality > self.prestige:
            self.article.quality = self.article.quality - ((self.article.quality - self.prestige) / self.adjustment_factor)
            
    def submit(self, journal, expedited = False):  # consult strategy and decide whether to submit to a journal.  probably also make a list of which journals have been sumbitted to etc.  also to be called by receipt method as an expedite
        if self.strategy.should_submit(journal, article):
            journal.receive_article(self.article, expedited)
            article.submissions.append({"journal": journal, "expedited": expedited, "accepted": None})
            
    def receive_response(self, journal, accepted):
        "handle response from journal"
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
        self.submissions = []
        self.signed_contracts = []
    
    def track_discernment_to_prestige(self):  
        "higher adjustment factor = smaller move of discernment toward prestige. (1 = discernment just becomes prestige)"
        if self.prestige > self.discernment:
            self.discernment = self.discernment + ((self.prestige - self.discernment) / self.adjustment_factor)
        if self.discernment > self.prestige:
            self.discernment = self.discernment - ((self.discernment - self.prestige) / self.adjustment_factor)
    
    def update_status(self, article, accepted):
        for submission in self.submissions:
            if submission["article"] == article:
                submission['accepted'] = accepted
            
    def consider(self, article, expedited = False):  
        "consult strategy and decide whether to accept article."
        if self.strategy.should_accept(article, self.submissions):  # passing all submissions in just in case there's a ranking strategy'
            self.update_status(article, True)
            article.author.receive_response(self, True)
            return True
        self.update_status(article, False)
        article.author.receive_response(self, False)
        return False
    
    def receive_article(self, article, expedited = False):
        "receive an article and add it into consideration queue.  possibly consider immediately, possibly batch-consider, depending on strategy"
        if expedited: # this assumes there are no expedites w/o a prior submission.
            for submission in self.submissions:
                if submission["article"] == article:
                    submission.expedited = True
        else:
            self.submissions.append({"article": article, "accepted": None, "expedited": False})  # accepted = None signifies not considered yet
        if self.strategy.should_consider(article, self.submissions):
            self.consider(article, expedited)
            
    def receive_author_decision(self, article, decision):
        if decision:
            self.signed_contracts.append(article)
        else:
            for submission in self.submissions:
                if submission["article"] == article:
                    submission['accepted'] == False


    
    
class Game(object):
    "do the setup, pick strategies, adjudgment factors, assign prestiges, create articles and assign to authors, etc. and run game"
    pass
    # TODO


        
if __name__ = "__main__":
    print("One day, this will be implemented and then I will run the game.")