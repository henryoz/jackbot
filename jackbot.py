# Commented out parts work but break Python Fiddle :P

# How to run in Raspberry Pi
# 1) SSH into Raspberry Pi
# 2) Type "screen" in terminal
# 3) Run script (make sure it works!)
# 4) ctrl-a
# 5) d


import tweepy
import random
import time

consumer_key = ''
consumer_secret = ''
access_token_key = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)

api = tweepy.API(auth)


TRIGGER_TIMES = [10*60*60+30*60, 16*60*60]

def nextwakeuptime(currenttime):
	for trigger in TRIGGER_TIMES:
		if currenttime < trigger:
			return trigger
			
	return TRIGGER_TIMES[0]
	

def gettimetosleep(currenttime):
	wakeuptime = nextwakeuptime(currenttime)
	if currenttime < wakeuptime:
		return wakeuptime - currenttime
	daylength = (24*60*60)
	return daylength - currenttime + wakeuptime

pl_nouns = ["horses", "snowboards", "skinny jeans", "Dogecoins", "football boots that are a size too small", "pictures of mountains", "infographics", "fonts", "meetings", "CSS", "HTML", "penguins", "emails", "puns", "pancetta", "Codepens", "feet", "hipsters", "bronies", "T-shirts with armpit holes", "porridge", "wanky beers", "cider", "footballers", "testes", "scrums"]
verbs = ["tricked", "popped", "themed", "sobbed over", "front ended", "lunged at", "spaffed", "empowered", "puked all over", "punched", "dumped", "licked", "kicked", "obliterated", "cried at the feet of", "belittled", "jeered at", "tickled", "romped over", "crawled all over", "coded up", "trimmed", "shaved", "baked a tasty", "buried", "whipped"]
adjectives = ["hot", "trendy", "wanky", "indie", "beautiful", "pop-up", "deeply empowering", "lanky", "brave", "angry", "unapproachable", "pungent", "jazzy", "clammy", "frozen", "rancid", "tepid", "scrummy", "racy", "fetch", "responsive", "moist", "voluptuous", "depressing", "turgid", "ridiculous", "intimidating", "dazzling", "fabulous", "scabby", "scrappy"]
people = ["@hen_dubz", "@lilovescake", "Mummy", "Nathan Barley", "Roger Federer", "Drupal", "Webdesigner Depot", "Smashing Magazine", "@jackfilose", "James Blake", "Kwabs", "@katephelon", "@_emmacox", "@vmdowdeswell", "Ballbag", "@shoegazey_pie", "@simplelampoon", "@andykisaragi", "@sirjamesob", "@meg_pope", "@andyy_p", "@thirtytwo_d", "Prince", "Abs from 5ive", "Macaulay Culkin", "Benji", "Vladimir Putin", "Pervy Howard", "Arsenal", "Podolski", "Ramsey"]


def maketweet():
	sen_1 = "Just " + random.choice(verbs) + " " + random.choice(people) + "."
	sen_2 = "Thinking about how " + random.choice(adjectives) + " " + random.choice(people) + " is."
	sen_3 = "Check out my new article about " + random.choice(adjectives) + " " + random.choice(pl_nouns) + "."
	sen_4 = "Dip me in " + random.choice(pl_nouns) + " and throw me to " + random.choice(people) + "."
	sen_5 = "Spent all day looking at gifs of " + random.choice(adjectives) + " " + random.choice (pl_nouns) + "."
	sen_6 = "Goodnight, sweet " + random.choice(pl_nouns) + "."
	sen_7 = random.choice(adjectives) + " " + random.choice(pl_nouns) + " are My New Jam."
	sen_8 = "Like any self respecting soul, I admire anyone who has " + random.choice(verbs) + " " + random.choice(people) + "."
	sen_9 = "Stuck in a " + random.choice(adjectives) + " scrum about " + random.choice(pl_nouns) + "."
	sen_10 = "RT if you've ever " + random.choice(verbs) + " " + random.choice(people) + "."
	sen_11 = "When I am king, " + random.choice(people) + " will be first against the wall, for crimes against " + random.choice(pl_nouns) + "."
	sentences = [sen_1, sen_2, sen_3, sen_4, sen_5, sen_6, sen_7, sen_8, sen_9, sen_10, sen_11]
	print random.choice(sentences)
	api.update_status(random.choice(sentences))




while True:
	ltime = time.localtime()
	sid = ltime.tm_hour*60*60+ltime.tm_min*60+ltime.tm_sec	
	delay = gettimetosleep(sid)
	print "Sleeping for %d seconds" % delay
	time.sleep(delay)
	maketweet()


