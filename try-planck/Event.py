class Event:
    def __init__(self, host, title, type, time, location, description, num_limit, need_approval = False, necessary = {}, exclude = {}, extra_options = {} ,participants = []):
        self.host = host # User
        self.title = title #String
        self.type = type #Tuple(String, float)
        self.time = time #??
        self.location = location #String
        self.description = description #String
        self.number_limit = num_limit # Tuple
        self.need_approval = need_approval #Bool
        self.necessary = necessary #{Label}
        self.exclude = exclude #{Label}
        self.extra_options = extra_options #{Label}
        self.participants = participants  # [User]


'''
    def count_member(self):
        return len(self.participants) + 1

    def add_participant(self,participant):
        assert self.count_member() < self.number_limit[1]:
        self.participants.append(participant)
'''
