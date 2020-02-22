class Strategy(object):
    def __init__(self):
        pass

class Journal_Strategy(Strategy):
    def should_consider(self, article, submissions):
        pass
        
    def should_accept(self, article, submissions):
        pass
    
class AuthorStrategy(Strategy):
    def should_submit(self, article, journal):
        pass
    
    def should_expedite(self, test_journal, article, accepted_journal):
        pass
                
    def should_accept_offer(self, article, journal):
        pass


class MachineGunSubmission(AuthorStrategy):
    "The conventional wisdom strategy: submit to every damn journal at once, expedite to everything, when every journal is resolved, accept the highest-ranking one"
    def should_submit(self, article, journal):
        return True
        
    def should_expedite(self, test_journal, article, accepted_journal):
        if test_journal.prestige > accepted_journal.prestige:
            return True
        return False
        