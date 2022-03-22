import os
import speech_recognition as sr
import pyttsx3
import subprocess
import mafilDetectTFlite


r=sr.Recognizer()
engine=pyttsx3.init()

while (1==1):
	with sr.Microphone() as source:
		os.system('cls||clear')

		#print("Call me to login")
		#passw=r.listen(source)
		#print("Checking...")
		#ps=r.recognize_google(passw)
		#print(ps)
		#if (("login" in ps) or ("mafil" in ps) or ("marvel" in ps) or ("map of" in ps) or ("mackerel" in ps)):
		#	print("Granted")
		#else:
		#	print("Acces Denied")

	msgBoot = ("""Hello how can I assist?""")
	def speakBoot(message):
		engine=pyttsx3.init()
		engine.setProperty('rate', 140)
		engine.setProperty('volume', 1)
		voices = engine.getProperty('voices')
		engine.setProperty('voice', voices[3].id)
		engine.say('{}'.format(message))
		engine.runAndWait()

	print(msgBoot)
	speakBoot(msgBoot)

	with sr.Microphone() as source:
		print('Start speaking I am listening')
		audio=r.listen(source)
		print('Done listening')
	ch = r.recognize_google(audio, language = 'en-GB')

	# SYSTEM CHECK
	if (("system" in ch ) or ("check" in ch)) and (("run" in ch) or ("load")):
		msgSystemCheck=("""System Check""")
		msgSystemMotors=("""Checking Motors one rotation in each direction""")
		def speakSystemCheck(message):
			engine=pyttsx3.init()
			engine.setProperty('rate', 140)
			engine.setProperty('volume', 1)
			voices = engine.getProperty('voices')
			engine.setProperty('voice', voices[3].id)
			engine.say('{}'.format(message))
			engine.runAndWait()
			
		print(msgSystemCheck)
		speakSystemCheck(msgSystemCheck)
		speakSystemCheck(msgSystemMotors)

	# DRIVE MODE	
	elif (("drive" in ch)or ("mode" in ch)):
		msgDriveMode=("""Drive Mode""")
		def speakDriveMode(message):
			engine=pyttsx3.init()
			engine.setProperty('rate', 140)
			engine.setProperty('volume', 1)
			voices = engine.getProperty('voices')
			engine.setProperty('voice', voices[3].id)
			engine.say('{}'.format(message))
			engine.runAndWait()

		print(msgDriveMode)
		speakDriveMode(msgDriveMode)

	# Shutdown System	
	elif (("shut" in ch)or ("down" in ch)):
		msgshutDown=("""System Powering down in 1 minute""")
		def speakshutDown(message):
			engine=pyttsx3.init()
			engine.setProperty('rate', 140)
			engine.setProperty('volume', 1)
			voices = engine.getProperty('voices')
			engine.setProperty('voice', voices[3].id)
			engine.say('{}'.format(message))
			engine.runAndWait()

		print(msgshutDown)
		speakshutDown(msgshutDown)
		subprocess.run(["shutdown"]) # Run Shutdown with subprocess, dowsnt w

	# Who are you?
	elif (("who" in ch) and ("you" in ch)):
		msgWho1=("""My acronym is Movement Autonomos Feedback Image Learning""")
		msgWho2=("""I am a prototype Artificial Intelligence that learns and provides feedback""")	
		def speakWho(message):
			engine.setProperty('rate', 140)
			engine.setProperty('volume', 1)
			voices = engine.getProperty('voices')
			engine.setProperty('voice', voices[3].id)
			engine.say('{}'.format(message))
			engine.runAndWait()

		print(msgWho1)
		speakWho(msgWho1)
		print(msgWho2)
		speakWho(msgWho2)

	#What can you do?
	elif (("what" in ch) and ("can" in ch)):
		msgWhat1=("""I can be controlled using a keyboard""")
		msgWhat2=("""My ears are a mic that listens to things""")	
		msgWhat3=("""A speaker is used for my mouth""")
		msgWhat4=("""I have eyes for detecting objects so I know what I am looking at""")
		msgWhat5=("""My wheels encode their position which means I know where I am""")	
		msgWhat6=("""I am getting sonar for touching walls and objects""")
		msgWhat7=("""Then I will move by myself""")
		msgWhat8=("""see things""")	
		msgWhat9=("""respond""")
		msgWhat10=("""and learn""")		
		def speakWhat(message):
			engine=pyttsx3.init()
			engine.setProperty('rate', 140)
			engine.setProperty('volume', 1)
			voices = engine.getProperty('voices')
			engine.setProperty('voice', voices[3].id)
			engine.say('{}'.format(message))
			engine.runAndWait()

		print(msgWhat1)
		speakWhat(msgWhat1)
		print(msgWhat2)
		speakWhat(msgWhat2)
		print(msgWhat3)
		speakWhat(msgWhat3)
		print(msgWhat4)
		speakWhat(msgWhat4)
		print(msgWhat5)
		speakWhat(msgWhat5)
		print(msgWhat6)
		speakWhat(msgWhat6)
		print(msgWhat7)
		speakWhat(msgWhat7)
		print(msgWhat8)
		speakWhat(msgWhat8)
		print(msgWhat9)
		speakWhat(msgWhat9)
		print(msgWhat10)
		speakWhat(msgWhat10)

	# Move Forward
	elif (("move" in ch) and ("forward" in ch)):
		msgBest1=("""Moving forward one meter""")	
		def speakBest(message):
			engine.setProperty('rate', 140)
			engine.setProperty('volume', 1)
			voices = engine.getProperty('voices')
			engine.setProperty('voice', voices[3].id)
			engine.say('{}'.format(message))
			engine.runAndWait()

		print(msgBest1)
		speakBest(msgBest1)
		print(msgBest2)
		speakWho(msgBest2)
else:
	print("Unable to recognize what you said")
	print("Continuing ")