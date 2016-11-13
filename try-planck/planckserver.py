from datetime import datetime
from flask import Flask, abort, flash, redirect, render_template, request, url_for
import Event, User, Calculator

def filter(evs, st):
    if st == 'all':
        return evs
    result = []
    for ev in evs:
        if ev.type[0] == st:
            result.append(ev)
    return result

def sort_events(evs, usr):
    for i in range(len(evs) - 1):
        for j in range(i + 1, len(evs)):
            if Calculator.calculate(evs[i], usr) < Calculator.calculate(evs[j], usr):
                evs[i], evs[j] = evs[j], evs[i]
    return [en for en in evs if en.host is not usr]

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/goevent/<para>')
def goevent(para):
    be = sort_events(filter(events, para), user1)[0]
    return render_template('go.html', evtitle = be.title, evhost = be.host.name, evtime = be.time, evlocation = be.location, evdescription = be.description, evlowlim = be.number_limit[0], evtoplim = be.number_limit[1], evneedapp = be.need_approval)
if __name__ == '__main__':
    app.run()


event1 = Event(user1,"Maroon 5 Concert",("concert",3/5),"Oct 16 7:30 pm","Oracle Arena in Oakland","Looking for Maroon 5 fans!",(2,6),False)
event2 = Event(user2,"Berkeley Eye",("exhibit", 1/2),"Nov 6 10:30 am","Berkeley Art Museum and Pacific Film Archive","Appreciating the art collection at BAMPFA.",(2,3),True)
event3 = Event(user3,"The Big Game",("game",1/3),"Nov 19 TBD","Kabam Field at California Memorial Stadium","Come cheer for our football team Cal Bears!!",(5,15),False)
event4 = Event(user4,"Math Monday: The calculus of variations and weak KAM theory", ("talk", 4/5), "Nov 14 5:00 pm","740 Evans","Let's do math together :)",(2,5),False)
event5 = Event(user5,"Chamber music group",("music",4/5),"Dec 3 2:30 pm","Morrison Hall","Searching for two violinists and a pianist",(4,4),True)
event6 = Event(user6,"French Book Club",("reading_and_writing",3/4),"Nov 15 7:45 pm", "Free Speech Movement Cafe", "A group of French speakers discuss weekly readings.", (5,10), True)
event7 = Event(user7,"Poster Design for Dance Marathon",("painting",2/3),"Dec 2 4:00 pm", "MLK", "Design posters together for dance showcase.",(5,10),False)
event8 = Event(user8,"Poetry Slam Peer Review",("poetry",5/6),"Nov 15 1:00 pm","MLK","Read and review each other's works",(2,3),True)
event9 = Event(user9,"Go eat at Eureka",("american",1/3),"Nov 11 12:30 pm","2068 Center St","Get some good American Food",(2,4),False)
event10 = Event(user10,"Get some burrito",("mexican",1/4),"Oct 6 14:00 pm","Berkeley North Side","burrito!",(3,6),False)
event11 = Event(user11,"Thai Basil!",("asian",3/5),"Nov 18 8:00 pm", "Asian Ghetto","Can't wait for some good Thai food! Come out and join us!",(4,8),False)
event12 = Event(user12, "Mediterranean Food",("mediterranean",2/5),"Nov 25 1:00 pm", "Downtown Berkeley","Looking for a lunch date :)", (2,2),True)
event13 = Event(user13, "Thanksgiving BASKETBALL", ("basketball", 1), "Nov 26 8:00 am", "RSF", "Skilled players, come and practice with me. No gender preferences.", (3, 5), False)
event14 = Event(user14, "Intro to soccer", ("soccer", 1/3), "Nov 20 4:00 pm", "Any Lawn", "Can anybody teach me how to do basic soccer? Really interested and really need it for the week.", (2, 2), False)
event15 = Event(user15, "New to Football", ("football", 2/3), "Nov 13 3:30 pm", "Memorial Glade", "look for group football practicing", (3,9), True)
event16 = Event(user16, "Have fun and Tennis!", ("tennis", 2/3), "Nov 20 9:30 am", "Southside tennis court", "I have reserved a court for practice. Come and join me and let's split the cost.", (2, 4), False)
event17 = Event(user17, "Production by BerkeleyStage", ("concert", 2/3), "Nov 12 7:30 pm", "BerkeleyStage is the most famous theatre group at Berkeley. They have been practicing for months for this play. Come and it will be a good time. ", (2, 2), True)
event18 = Event(user18, "The Big Game",("game",1/3),"Nov 19 7:00 pm","California Memorial Stadium","Go Bears!!",(5,15),False)
event19 = Event(user19, "Google Lightning Talk", ("talk", 2/3), "Nov 14 6:00 pm", "Soda Hall", "I am a fanatic fan of tech. If you recognize my passion, let's go to the talk together and get to know each other. Dinner is provided.", (2, 2), False)
event20 = Event(user20, "Modern Art Exhibition at Berkeley Museum", ("exhibit", 1/3), "Nov 20 9:00 am", "Berkeley Museum", "Modern art is the best.", (2, 4), False)

events = [event1,event2,event3,event4,event5,event6,event7,event8,event9,event10,event11,event12,event13,event14,event15,event16,event17,event18,event19,event20]

#create users
user3 = User("BigBear", "Senior", 22, "Male")
user3.labels = {"tennis": 1/3, "concert": 2/3, "talk": 1}

user2 = User("Elena", "Freshman", 18, "Female")
user2.labels = {"tennis": 2/3, "music": 1, "reading_and_writing": 2/3, "asian":1, "game": 1}

user1 = User("Henry", "Freshman", 18, "Male")
user1.labels = {"basketball": 1, "mexican": 1/3, "music": 2/3, "concerts": 2/3}

user4 = User("Yiming", "Freshman", 18, "Female")
user4.labels = {"concert": 2/3, "talk": 2/3, "music": 2/3, "mexican":1}

user5 = User("Parisa", "Junior", 24, "Female")
user5.labels = {"mexican":1, "asian":1, "painting": 1, "game": 2/3}

user6 = User("Mira", "Freshman", 18, "Female")
user6.labels = {"talk": 1, "music": 1, "american": 1, "1": 1, "reading_and_writing": 1}

user7 = User("Amit", "Senior", 22, "Male")
user7.labels = {"exhibit": 2/3, "asian": 1, "soccer": 2/3}

user8 = User("Sean", "Freshman", 18, "Male")
user8.labels = {"concert": 1, "music": 2/3, "soccer": 1, "asian": 1}

user9 = User("PaPaJohns", "Senior", 35, "Male")
user9.labels = {"talk": 1, "reading_and_writing": 2/3, "mediterranean": 1/3, "football": 1/3}

user10 = User("LittleBear", "Freshman", 18, "Male")
user10.labels = {"game": 2/3, "talk": 1, "tennis": 1}

user11 = User("Maureen", "Sophomore", 19, "Female")
user11.labels = {"reading_and_writing": 1, "talk": 1, "poetry": 2/3, "mediterranean": 1}

user12 = User("Janet", "Freshman", 19, "Female")
user12.labels = {"concert": 1, "music": 1, "game": 1/3, "tennis": 1, "mexican": 1}

user13 = User("Raymond", "Freshman", 19, "Male")
user13.labels = {"basketball": 2/3, "game": 2/3, "american": 1/3}

user14 = User("Jiwon", "Junior", 22, "Female")
user14.labels = {"asian": 1, "reading_and_writing": 1}

user15 = User("Micheal", "Freshman", 19, "Male")
user15.labels = {"basketball": 2/3, "american": 1/3}

user16 = User("Helen", "Sophomore", 20, "Female")
user16.labels = {"american": 1, "tennis": 2/3, "exhibit": 2/3}

user17 = User("Stephanie", "Senior", 22, "Female")
user17.labels = {"concert": 2/3}

user18 = User("Heny", "Freshman", 18, "Male")
user18.labels = {"tennis": 1, "concert": 1, "asian": 1/3, "reading_and_writing": 1/3}

user19 = User("Tiger", "Freshman", 18, "Male")
user19.labels = {"basketball": 1/3, "asian": 1, "poetry": 1, "music": 1, "talk": 1, "exhibit": 2/3}

user20 = User("Sangyeon", "Freshman", 18, "Female")
user20.labels = {"painting": 1, "asian": 1, "music": 2/3, "exhibit": 2/3, "tennis": 2/3}


users = [user1,user2,user3,user4,user5,user6,user7,user8,user9,user10,user11,user12,user13,user14,user15,user16,user17,user18,user19,user20]