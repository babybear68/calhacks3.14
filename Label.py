class Label:
    pass

class Sport(Label):
    levels = {'low':1/3, 'medium':2/3, 'high':1}
    name = 'sport'


class Basketball(Sport):
    name = 'basketball'
    weights = {'basketball':0.7, 'football':0.1, 'Soccer':0.1, 'Tennis':0.1}
    def __init__(self, level = 'low'):
        self.value = self.levels[level]

class Football(Sport):
    name = 'football'
    weights = {'football':0.7, 'basketball':0.1, 'Soccer':0.1, 'Tennis':0.1}
    def __init__(self, level = 'low'):
        self.value = self.levels[level]

class Soccer(Sport):
    name = 'soccer'
    weights = {'soccer':0.7, 'football':0.1, 'basketball':0.1, 'Tennis':0.1}
    def __init__(self, level = 'low'):
        self.value = self.levels[level]

class Tennis(Sport):
    name = 'tennis'
    weights = {'tennis':0.7, 'football':0.1, 'Soccer':0.1, 'basketball':0.1}
    def __init__(self, level = 'low'):
        self.value = self.levels[level]