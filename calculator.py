class Calculator:
    def calculate(event, user):
        score = 0
        for key in event.weights:
            if type(user.label_dic[key]) is type(event.label):
                score += event.weights[key] * abs(event.label.value - user.label.value)
            else:
                score += event.weights[key] * abs(event.host.label.value - user.label.value)
        return score
            
