from basic import *
from numpy import rnorm
import random



class Journal(Player):
    def __init__(self, discernment=None, prestige=None, strategy=None, available_strategies=None, higher_is_smarter=False, adjustment_factor=2, max_articles = 10):
        if discernment:
            self.discernment = discernment
        else:
            self.discernment = random.randint(1, 10)
        super.__init__(self, prestige, strategy, available_strategies, higher_is_smarter, adjustment_factor)
        if self.higher_is_smarter:
            self.track_discernment_to_prestige()
        self.submissions = []
        self.signed_contracts = []
        self.max_articles = max_articles
    
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
            
    def consider(self, article, perceived_quality, expedited = False):  
        "consult strategy and decide whether to accept article."
        if self.strategy.should_accept(article, perceived_quality, self.submissions):  # passing all submissions in just in case there's a ranking strategy'
            self.update_status(article, True)
            article.author.receive_response(self, True)
            return True
        self.update_status(article, False)
        article.author.receive_response(self, False)
        return False
        
    def evaluate_article_quality(self, article):
        evaluation_error = 10 / self.discernment
        return rnorm(article.quality, evaluation_error)
    
    def receive_article(self, article, expedited = False):
        "receive an article and add it into consideration queue.  possibly consider immediately, possibly batch-consider, depending on strategy"
        if expedited: # this assumes there are no expedites w/o a prior submission.
            for submission in self.submissions:
                if submission["article"] == article:
                    submission.expedited = True
        else:
            perceived_quality = self.evaluate_article_quality(article)
            self.submissions.append({"article": article, "accepted": None, "expedited": False, "perceived_quality" = perceived_quality})  # accepted = None signifies not considered yet
        if self.strategy.should_consider(article, self.submissions):
            self.consider(article, perceived_quality, expedited)
            
    def receive_author_decision(self, article, decision):
        if decision:
            self.signed_contracts.append(article)
        else:
            for submission in self.submissions:
                if submission["article"] == article:
                    submission['accepted'] == False
