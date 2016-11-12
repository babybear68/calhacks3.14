class User:
    def __init__(self, username, year, age, gender, major=[], interest=[], personality=[], contact=None, \
        basketball, football, soccer, tennis):
        self.username = username #string
        self.year = year #string
        self.age = age #int
        self.gender = gender #string
        self.major = major #list of string
        self.interest = interest #list of string
        self.personality = personality #list of string
        self.contact = contact #string

        self.go_events = []
        self.create_events = []
        self.label_dic = {} #map the name of a label to the label instance
    """def go_to_event(self, event):
        if len(event.participants) > event.num_limit:
            #print ("Sorry you can't join; the limit is %s people" % (event.num_limit))
            raise Exception()
        event.add_participant(self)

    def create_event(self, title, num_limit, need_approval=False, necessary=None, exclude=None, extra_options=[]):
        self.create_event.append(Event(self, title, num_limit, need_approval, necessary, exclude, extra_options))"""
