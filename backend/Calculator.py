from Label import *
class Calculator:
    weights_of_label_tpypes = \
        {Basketball.name:Basketball.weights, Football.name:Football.weights, Soccer.name: Soccer.weights, Tennis.name:Tennis.weights,\
         Music.name: Music.weights, ReadingAndWriting.name: ReadingAndWriting.weights, Painting.name: Painting.weights, Poetry.name: Poetry.weights,\
         Concert.name: Concert.weights, Exhibition.name: Exhibition.weights, Game.name: Game.weights, Talk.name: Talk.weights,\
         American.name: American.weights, Mexican.name: Mexican.weights, Asian.name: Asian.weights, Mediterranean.name: Mediterranean.weights
         }

    def get_value(user, key):
        if key in user.labels:
            return user.labels[key]
        else:
            return 0

    def calculate(event, participant):
        score = 1
        for key in Calculator.weights_of_label_tpypes[event.type[0]]:
            if key == event.type[0]:
                score -= Calculator.weights_of_label_tpypes[event.type[0]][key] * abs(event.type[1] - Calculator.get_value(participant,key))
                #print (event.type[1], Calculator.get_value(participant,key))
            else:
                score -= Calculator.weights_of_label_tpypes[event.type[0]][key] * abs(Calculator.get_value(event.host, key) - Calculator.get_value(participant,key))
                #print (Calculator.get_value(event.host, key), Calculator.get_value(participant,key))
        return score