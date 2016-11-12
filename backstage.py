def User:
    def __init__(self, username, password, year, age, gender, major=None, interest=None, personality=None, contact=None, \
        basketball, football, ):
        self.username = username #string
        self.password = password #string
        self.year = year #string
        self.age = age #int
        self.gender = gender #string
        self.major = major #string
        self.interest = interest #string
        self.personality = personality #string
        self.contact = contact #string

        self.go_events = []
        self.create_events = []
    """def go_to_event(self, event):
        if len(event.participants) > event.num_limit:
            #print ("Sorry you can't join; the limit is %s people" % (event.num_limit))
            raise Exception()
        event.add_participant(self)

    def create_event(self, title, num_limit, need_approval=False, necessary=None, exclude=None, extra_options=[]):
        self.create_event.append(Event(self, title, num_limit, need_approval, necessary, exclude, extra_options))"""
