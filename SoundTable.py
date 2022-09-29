# Strings in standard guitar tuning eBGDAE

class GuitarStrings:
    
    def __init__(self):
        self.guitarStringsList = [dict() for i in range(6)] # Each cell will contain dictionares of 13 (<0,12> halfsteps) sounds on each string.
                                                            # Each halfstep on guitar has its frequency which coressponds to a set note.
                                                            # Frequencies for each halfstep are unique on a given string, hence they are the keys of the dictionary.

        a = 2**(1/12)   # Multiplying note frequency by this factor results in halfstep up of that sound 
                        # -> no need to hardcode every string halfstep frequency (only open string frequency); 
                        # multiplying starting frequency by a^12 equals 2 which is a next octave for that sound.

        # All frequencies in Hz, casted to int as better precision is not necessary

        numberOfHalftones = 13 # limiting range to <0,12> 
        
        # The hardcoded open string frequencies actually are an octave lower, meaning they true frequency is half of what is given,
        # but because it is some sort of convention to write guitar sounds one octave higher, frequencies are multiplied by two.

        # e String (thinnest/1st)
        orderOfSoundsE = ["E","F","F#","G","G#","A","A#","B","C","C#","D","D#","E"]
        for i  in range(numberOfHalftones):
            self.guitarStringsList[0][int(330*a**i)] = orderOfSoundsE[i]

        # B String (2nd)
        orderOfSoundsB = ["B","C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]
        for i  in range(numberOfHalftones):
            self.guitarStringsList[1][int(247*a**i)] = orderOfSoundsB[i]

        # G String (3rd)
        orderOfSoundsG = ["G","G#","A","A#","B","C","C#","D","D#","E","F","F#","G"]
        for i  in range(numberOfHalftones):
            self.guitarStringsList[2][int(196*a**i)] = orderOfSoundsG[i]

        # D String (4th)
        orderOfSoundsD = ["D","D#","E","F","F#","G","G#","A","A#","B","C","C#","D"]
        for i  in range(numberOfHalftones):
            self.guitarStringsList[3][int(147*a**i)] = orderOfSoundsD[i]

        # A String (5th)
        orderOfSoundsA = ["A","A#","B","C","C#","D","D#","E","F","F#","G","G#","A"]
        for i  in range(numberOfHalftones):
            self.guitarStringsList[4][int(110*a**i)] = orderOfSoundsA[i]

        # E string (thickest/6th)
        for i  in range(numberOfHalftones):
            self.guitarStringsList[5][int(82*a**i)] = orderOfSoundsE[i]

    def get_sounds(self):
        return self.guitarStringsList

    def print_table(self, mode=0):

        stringsName = "eBGDAE"

        for i in range(13):
            print("    {i}".format(i=i),sep="",end="")
        print("")
        if mode == 0: # Frequency table
            for index, strName in enumerate(stringsName):
                print("{strName}:  ".format(strName=strName),sep="",end="")
                for key in self.guitarStringsList[index].keys():
                    print("{key}  ".format(key=key),sep="",end="")
                print("")
        
        else: # Sound Table
            for index, strName in enumerate(stringsName):
                print("{strName}:  ".format(strName=strName),sep="",end="")
                for key in self.guitarStringsList[index].keys():
                    print("{key}    ".format(key=self.guitarStringsList[index][key]),sep="",end="")
                print("")
