class Label:
    pass

#### Sports ####

class Sport(Label):
    #deftness
    levels = {'low':1/3, 'medium':2/3, 'high':1}
    default_level = 0
    name = 'sport'

    def get_value(level):
        return Sport.levels[level]

class Basketball(Sport):
    name = 'basketball'
    weights = {'basketball':0.7, 'football':0.1, 'soccer':0.1, 'tennis':0.1}


class Football(Sport):
    name = 'football'
    weights = {'football':0.7, 'basketball':0.1, 'soccer':0.1, 'tennis':0.1}

class Soccer(Sport):
    name = 'soccer'
    weights = {'soccer':0.7, 'football':0.1, 'basketball':0.1, 'tennis':0.1}

class Tennis(Sport):
    name = 'tennis'
    weights = {'tennis':0.7, 'football':0.1, 'soccer':0.1, 'basketball':0.1}


#### Public_Events ####

class PublicEvents(Label):
    #frequency
    levels = {'seldom':1/3, 'sometimes':2/3, 'often':1}
    default_level = 0
    name = 'public_events'

    def get_value(level):
        return PublicEvents.levels[level]

class Concert(PublicEvents):
    name = 'concert'
    weights =  { 'concert':0.7,'exhibition':0.1,'game':0.1,'talk':0.1 }

class Exhibition(PublicEvents):
    name = 'exhibition'
    weights = {'exhibition':0.7,'game':0.1,'talk':0.1,'concert':0.1 }

class Game(PublicEvents):
    name = 'game'
    weights = {'game':0.7,'talk':0.1,'concert':0.1,'exhibition':0.1 }

class Talk(PublicEvents):
    name = 'talk'
    weights = {'talk':0.7,'concert':0.1,'exhibition':0.1,'game':0.1}

#### Arts and Creativity####
class ArtAndCreativity:
    #devotion
    levels  = {'little': 1/3,'medium':2/3,'high':1}
    name = 'art_and_creativity'
    default_level = 0

    def get_value(level):
        return ArtAndCreativity.levels[level]

class Music(ArtAndCreativity):
    name = 'music'
    weights =  {  'music':0.7,'reading_and_writing':0.1,'painting':0.1,'poetry':0.1  }

class ReadingAndWriting(ArtAndCreativity):
    name = 'reading_and_writing'
    weights = {'reading_and_writing':0.7,'painting':0.1,'poetry':0.1,'music':0.1}

class Painting(ArtAndCreativity):
    name = 'painting'
    weights = {'painting':0.7,'poetry':0.1,'music':0.1,'reading_and_writing':0.1}

class Poetry(ArtAndCreativity):
    name = 'poetry'
    weights = {'poetry':0.7,'music':0.1,'reading_and_writing':0.1,'painting':0.1}


#### Food ####
class Food:
    levels = {'so-so':1/3, 'like':2/3, 'favorite':1}
    name = 'food'
    default_level = 0

    def get_value(level):
        return Food.levels[level]

class American(Food):
    name = 'american'
    weights =  {  'american':0.7,'mexican':0.1,'asian':0.1,'mediterranean':0.1  }

class Mexican(Food):
    name = 'mexican'
    weights = {'mexican':0.7,'asian':0.1,'mediterranean':0.1,'american':0.1 }

class Asian(Food):
    name = 'asian'
    weights = {'asian':0.7,'mediterranean':0.1,'american':0.1,'mexican':0.1 }

class Mediterranean(Food):
    name = 'mediterranean'
    weights = {'mediterranean':0.7,'american':0.1,'mexican':0.1,'asian':0.1 }


def create_string(list):
    for i in range(4):
        print (" '{0}':0.7,'{1}':0.1,'{2}':0.1,'{3}':0.1 ".format(list[i%4],list[(i+1)%4],list[(i+2)%4],list[(i+3)%4]))

def create_dict(list):
    for i in range(4):
        print (" {0}.name: {0}.weights, {1}.name: {1}.weights,{2}.name: {2}.weights,{3}.name: {3}.weights".format(list[i%4],list[(i+1)%4],list[(i+2)%4],list[(i+3)%4]))




create_dict(['Concert','Exhibition','Game','Talk'])