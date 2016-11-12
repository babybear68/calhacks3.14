from user import *
from Label import *
from calculator import *
from Event import *

user1 = User('u1','Freshman', 18, 'male', )
basketball_low = Basketball('low')
user1.labels[basketball_low.name] = basketball_low
basketball_event = Event(user1,'lol', basketball_low, None, None, '', (1,3))

print(Calculator.calculate(basketball_event,user1))