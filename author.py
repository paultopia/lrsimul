from basic import *
from numpy import rnorm
import random


class Author(Player):
    def add_article(self, quality=None):
        self.article = Article(quality)
        if higher_is_smarter:
            self.track_article_to_prestige()
        self.article.author = self
        self.article.author_perceived_quality = rnorm(self.article.quality, 1)  # maybe could vary this in a more complicated version of the model
        
    def track_article_to_prestige(self):
        "higher adjustment factor = smaller move of discernment toward prestige. (1 = discernment just becomes prestige)"
        if self.prestige > self.article.quality:
            self.article.quality = self.article.quality + ((self.prestige - self.article.quality) / self.adjustment_factor)
        if self.article.quality > self.prestige:
            self.article.quality = self.article.quality - ((self.article.quality - self.prestige) / self.adjustment_factor)
            
    def submit(self, journal):  
        "consult strategy and decide whether to submit to a journal."
        if self.strategy.should_submit(journal, article):
            journal.receive_article(self.article, expedited=False)
            article.submissions.append({"journal": journal, "expedited": False, "accepted": None})
            
    def receive_response(self, journal, accepted):
        "handle response from journal"
        pass
        # TODO
        
    def expedite(self, journal):
        "checks to see if should expedite at test_journal given acceptance at accepted_journal"
        if self.strategy.should_expedite(test_journal, self.article, accepted_journal):
            test_journal.receive_article(self.article, expedited=True)
            for submission in article.submissions:
                if submission["journal"] == test_journal:
                    submission["expedited"] = True
