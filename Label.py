class Label:
    pass

class Sport(Label):
    levels = {'low':1/3, 'medium':2/3, 'high':1}
    name = 'sport'

class Basketball(Sport):
    name = 'basketball'
    def __init__(self, level = 'low'):
        self.value = self.levels[level]
