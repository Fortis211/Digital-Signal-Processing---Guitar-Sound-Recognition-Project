from SoundRecognition import SoundRecognition
import glob


def getFileNames(fileType="wav",dir='sounds/*.'):

	fileNameList = []

	for name in glob.glob(dir+ fileType): 
		fileNameList.append(name)

	return fileNameList

def main():

    samples = getFileNames()
    correctCounter = 0 
    len_ = len(samples)

    print ("        Sound    Note    TrueFreq   Estimated    Correct")
    for index, path in enumerate(samples):
        x = SoundRecognition(path)
        path = path[:-4]
        path = path[7:]


        correct = x.pathNameToNote()
        estimated = x.recognizeSound()[0]

       
        isEq = False
        if correct == estimated:
            isEq = True
            correctCounter += 1

        print(index, path, correct,x.extractF0(),"",estimated, isEq, sep="       " )

    print("Accuracy: ",(correctCounter/len_ )* 100, " %") 


if __name__ == '__main__':
    main()