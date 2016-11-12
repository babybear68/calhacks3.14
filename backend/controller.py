class Controller:
    events = []
    users = []
    def add_label(user, Labelclass, level="low"):
        label = Labelclass()
        user.labels[label.name] = label
    def go_to_event(user, event):
        if len(event.participants) > event.num_limit[1]:
            raise Exception()
        event.participants.append(user)
    def create_event(user, title, num_limit, need_approval=False, necessary=None, exclude=None, extra_options=[]):
        Controller.events.append(Event(self, title, num_limit, need_approval, necessary, exclude, extra_options))#to data base
    def create_user(name, year, age, gender, major=[], interest=[], personality=[], contact=None):
        Controller.users.append(User(na,e, year, age, gender, major=[], interest=[], personality=[], contact=None))
    def sortevents(user):
        scores = []
        for event in events:
            scores.append([event, Calculator.calculate(event, user)])
        scores.sort(key=lambdax: x[1])
        scores.reverse()
        #display in order!
    def sort_certain_type(user, Type):
        scores = []
        for event in events:
            if isinstance(events.type, Type):
                scores.append([event, Calculator.calculate(event, user)])
        scores.sort(key=lambdax: x[1])
        scores.reverse()
        #display in order!
