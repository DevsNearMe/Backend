#source : appdata, beevolve, appdata, quora, statista

#The weights will be inverted for use as a multiplier when trying to estimate number of people present in a 
#particular age range. Similarly for gender so e.g foursquare has its own multiplier which would be combined
#with age and gender for this particular prediction
#foursquare
fs_weights_byage = { '18-29' : 0.40, '30-43' : 0.42, '44-53' : 0.09, '54-65' : 0.05}
fs_weights_bygender = { 'm' : 0.6, 'f' : 0.4 }
#twitter
tr_weights_byage = { '15-25' : 0.74, '26-35' : 0.15, '36-45' : 0.06, '46-55' : 0.03, '55+' : 0.02  }
tr_weights_bygender = { 'm' : 0.47, 'f' : 0.53  }
#instagram
ins_weights_byage = { '18-24' : 0.35, '25-34' : 0.33, '35-45' : 0.16, '46-55' : 0.10}
ins_weights_bygender = { 'm' : 0.682, 'f' : 0.318 }
#meetup
mtp_weights_byage = { '15-25' : 0.33, '26-35' : 0.37, '36-45' : 0.20, '46-55' : 0.05, '55+' : 0.02  }
mtp_weights_bygender = { 'm' : 0.57, 'f' : 0.43 }


def getExpectedUserCount(dev_type,gender=None,age_range=None) :
	getAbsExpUserCount(dev_type,gender,age_range) + getPredictedExpUserCount(dev_type,gender,age_range,'expected')
	pass

def getAbsUserCount(dev_type,gender=None,age_range=None) :
	#foursquare, instagram photos from location, if can geolocate tweets
	pass

def getPredictedUserCount(dev_type,gender=None,age_range=None,bound_type=None) :
	getEventUserCount(dev_type,gender,age_range,bound_type) + getPersonalizedUserCount(dev_type,gender,age_range,bound_type)
	pass

# Use Decision Tree Based prediction to trim down counts
# from meetup, eventbrite, facebook events by weather, paid/non-paid event, weather
# subtract conflicting events with same interests (Differentiate between signup and turnout)
# (0.25*weighted(meetup) + 0.4*weighted(eventbrite) + 0.35*weighted(facebook))/3 - Similar events
def getEventUserCount(dev_type,gender=None,age_range=None,bound_type=None) :
    #weigh each meetup, eventbrite, facebook events in increasing order and prune by weather,paid,giveaway
	pass

# Use Bayesian filtering to predict if a person will appear at a event based
# on past event attendance, similar people attending events at a venue, 
# series of events attended in a meetup

def getPersonalizedUserCount(dev_type,gender=None,age_range=None,bound_type=None) :
	pass

def weighByAgeRange():
	pass

def weighByGender():
	pass

#Use wunderground data to prune 

def weighByWeather():
	#Weigh down factor
	#is_rainy *0.7 is_toohot *0.8 is_storm *0.5 
	pass

#Paid event signups are more likely to be turnouts , meetup, eventbrite

def weighByPaidEvent(is_paid=True,turnout):
	#weigh up *2 if paid
	pass

#Free food/t-shirt giveaways attract more people, meetup
def weighByGiveAway():
	#weigh up *1.5 if giveaway
	pass

#potentially use waze traffic realtime data to enhance prediction
def weighByWaze():
	pass

def getMinUserCount(dev_type,gender=None,age_range=None) :
	getAbsUserCount(dev_type,gender,age_range) + getPredictedUserCount(dev_type,gender,age_range,'min')
	pass

def getMaxUserCount(dev_type,gender=None,age_range=None) :
	getAbsUserCount(dev_type,gender,age_range) + getPredictedUserCount(dev_type,gender,age_range,'max')
	pass