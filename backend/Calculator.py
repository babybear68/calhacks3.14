class Calculator:
    def get_value(user, key):
        if key in user.labels:
            return user.labels[key].value
        else:
            return 0

    def calculate(event, user):
        score = 1
        for key in event.type.weights:
            if key == event.type.name:
                score -= event.type.weights[key] * abs(event.type.value - Calculator.get_value(user,key))
            else:
                score -= event.type.weights[key] * abs(Calculator.get_value(event.host, key) - Calculator.get_value(user,key))
        return score
