# ChucK-py-generator
# Writes a series of variables onto ChucK-file templates

import csv
import subprocess

# Universal vars
bpm = 120 # => bps = 120 / 60 -> 2 bps
beatsPerBar = 4 # time signature in */4
stepsPerBar = 8
stepInMs = (60 * 1000)/(bpm * (stepsPerBar/beatsPerBar))# Calculates the time between a step in ms based on bpm and time signature
tonesToAllocate = 8 # Should be designatable
sustainLeft = stepsPerBar - tonesToAllocate
gridLength = stepsPerBar * 2 # should be designatable

chuckVars = str(stepInMs) + "::ms => dur timeInMs;\n"+str(gridLength)+" => int gridLength;\n" + str(tonesToAllocate) + " => int tonesToAllocate;\ngridLength - tonesToAllocate => int sustainLeft;\n"

dataArray = []


templateFileNames = [["chuckLeadTemplate.ck", "chuckLeadFile.ck"], ["chuckDrumTemplate.ck", "chuckDrumFile.ck"], ["chuckBassTemplate.ck", "chuckBassFile.ck"], ["chuckRythmTemplate.ck", "chuckRythmFile.ck"]]

with open("dataset.csv") as dataFile: # dataset = templateFile.read()
    csvReader = csv.reader(dataFile)
    for row in csvReader:
        print(row)
        dataArray.append(row)

print("Done")
print(dataArray)


for channelIndex, templateFileName in enumerate(templateFileNames):
    dataChannelString = bytearray("[")
    for idx, imgDataRow in enumerate(dataArray):
        print(imgDataRow)
        dataChannelString += imgDataRow[channelIndex] + ","

    dataChannelString[len(dataChannelString)-1] = "]"
    dataChannelString += " @=> int dataVals[];\n"

    print(dataChannelString)

    with open(templateFileName[0],"r") as templateFile: template = templateFile.read()
    with open(templateFileName[1], 'w') as chuckFile: chuckFile.write(chuckVars + dataChannelString + template)

#subprocess.call("chuck chuck*File.ck", shell=True)
