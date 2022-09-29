import librosa  # library for audio analysis
import matplotlib.pyplot as plt
import librosa.display
import numpy as np
from SoundTable import GuitarStrings

class SoundRecognition:

    def __init__(self,samplePath,samplingRate=44100):
        self.samplePath = samplePath
        self.soundTable = GuitarStrings().get_sounds()
        self.audioTimeSeries, self.samplingRate = librosa.load(samplePath, samplingRate, mono=True) # loading audio sample 
        
        # Getting sample note frequencies - f0 - array of fundamental frequencies in sample, needs to be refined

        self.f0, self.voiced_flag, self.voiced_probs = librosa.pyin(self.audioTimeSeries, fmin=30, fmax=335)

    def extractF0(self):
        F0 = []
        for f in self.f0:
            if np.isnan(f):
                pass
            else:
                if f>40 and f<800:
                    F0.append(f)
        if F0:   # if F0 not empty
            return int(np.average(F0))
        else: 	 # if F0 is an empty list 
            return 0 

    def recognizeSound(self):
        # Guitar sounds are written an octave higher than they actually are, hence f0 multiplied by two as
        # sounds in SoundTable follows this convention.
        f0 = 2*self.extractF0() - 1 
        if f0 == -1: # can happen when fmin is a low value
            return "error","error"
        freq = []
        for index, string in enumerate(self.soundTable):
            # freq is a list of 3-element tuples, where each tuple consists of difference between F0 and frequency on halfstep,
            # frequency on given halfstep and index which corresponds to the string number
            freq.append( min( [(abs(f0-k), k, index) for k in string.keys()] ) )
        key = min(freq)[1]
        index = min(freq)[2]
        
        return self.soundTable[index][key],key # returns pair of Note and corresponding frequency (octave higher)

    def pathNameToNote(self):

        name = self.samplePath[:-4]
        name = name[7:]

        stringsName = "eBGDAE"
        string = 0

        for index, strName in enumerate(stringsName):
            if strName == name[0]:
                string = index
                break

        halfstepNum = name[1:]
        if halfstepNum[0] == "E":
            halfstepNum = halfstepNum[1:]

        for index, key in enumerate(self.soundTable[string].keys()):
            if index == int(halfstepNum):
                return self.soundTable[string][key] 


    def makeF0Plot(self):
        # code from https://librosa.org/doc/main/generated/librosa.pyin.html
        times = librosa.times_like(self.f0)
        fig, ax = plt.subplots()
        ax.set(title='pYIN fundamental frequency estimation')
        ax.plot(times, self.f0, label='f0', color='cyan', linewidth=3)
        ax.legend(loc='upper right')
        #

    def makeWavePlot(self): # us
        plt.figure()
        librosa.display.waveplot(self.audioTimeSeries, sr=self.samplingRate)
    
    def showPlots(self):
        plt.show()
        
    
