class Strategy(object):
    pass

class Journal_Strategy(Strategy):
    def should_consider(self, article, submissions):
        pass
        
    def should_accept(self, article, submissions):
        pass
    
class AuthorStrategy(Strategy):
    def should_submit(self, article, journal):
        pass
    
    def should_expedite(self, article, journal):
        pass
                
    def should_accept_offer(self, article, journal):
        pass
    
