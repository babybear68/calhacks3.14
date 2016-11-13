from User import *
from Label import *
from Calculator import *
from Event import *

user1 = User('u1','Freshman', 18, 'male' )
user2 = User('u1','Freshman', 18, 'male' )


basketball_low = 1/3
basketball_med = 2/3

soccer_low = 1/3

user1.labels['basketball'] = Basketball.get_value('low')
user2.labels['basketball'] = basketball_med
user2.labels['baseball'] = soccer_low
user2.labels['music'] = Music.levels['little']

basketball_event = Event(user1,'lol', ('basketball',basketball_low), None, None, '', (1,3))
music_event = Event(user1,'lol', ('music', 2/3), None, None, '', (1,3))


print(user1.labels)
print(user2.labels)
print(user1 is user2)

print(Calculator.calculate(music_event,user2))