# https://cdn-learn.adafruit.com/downloads/pdf/adafruit-max98357-i2s-class-d-mono-amp.pdf


from pygame import mixer

#freq = 44100 # audio CD quality
#bitsize = -16 # unsigned 16 bit
channels = 1 # 1 is mono, 2 is stereo
#buffer = 2048 # number of samples (experiment to get right sound)
mixer.init(channels)
mixer.music.load('systemBoot.mp3')
mixer.music.set_volume(0.7)
mixer.music.play()