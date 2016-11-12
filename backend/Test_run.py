from User import *
from Label import *
from Calculator import *
from Event import *

user1 = User('u1','Freshman', 18, 'male' )
user2 = User('u1','Freshman', 18, 'male' )


basketball_low = Basketball('low')
basketball_med = Basketball('medium')

soccer_low = Soccer('low')

user1.labels[basketball_low.name] = basketball_low
user2.labels[basketball_med.name] = basketball_med
user2.labels[soccer_low.name] = soccer_low

basketball_event = Event(user1,'lol', basketball_low, None, None, '', (1,3))

print(user1.labels)
print(user2.labels)
print(user1 is user2)

print(Calculator.calculate(basketball_event,user2))