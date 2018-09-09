# ChucK-py-generator
# Writes a series of variables onto ChucK-file templates

import csv

# Universal vars
bpm = 120 # => bps = 120 / 60 -> 2 bps
beatsPerBar = 4 # time signature in */4
stepsPerBar = 8
stepInMs = (60 * 1000)/(bpm * (stepsPerBar/beatsPerBar))# Calculates the time between a step in ms based on bpm and time signature
tonesToAllocate = 8 # Should be designatable
sustainLeft = stepsPerBar - tonesToAllocate
gridLength = stepsPerBar * 2 # should be designatable

chuckVars = str(stepInMs) + "::ms => dur timeInMs;\n"+str(gridLength)+" => int gridLength;\n" + str(tonesToAllocate) + " => int tonesToAllocate;\ngridLength - tonesToAllocate => int sustainLeft;\n"

# templateFile = open("chuckTemplate.ck","r")
# chuckFile = open("chuckFile.ck", "w")

dataArray = []

with open("chuckTemplate.ck","r") as templateFile: template = templateFile.read()
with open("dataset.csv") as dataFile: # dataset = templateFile.read()
    csvReader = csv.reader(dataFile)
    for row in csvReader:
        print(row)
        dataArray.append(row)

print("Done")
print(dataArray)

dataChannelString = bytearray("[")

for index, imgDataRow in enumerate(dataArray):
    print(index)
    dataChannelString += imgDataRow[0] + ","

dataChannelString[len(dataChannelString)-1] = "]"
dataChannelString += " @=> int dataVals[];\n"

print(dataChannelString)


with open('chuckFile.ck', 'w') as chuckFile: chuckFile.write(chuckVars + dataChannelString + template)



# file=open("beat.ck","w")
# file.write("// impulse to filter to dac\nImpulse i => BiQuad f => dac;\n// set the filter's pole radius\n.99 => f.prad;\n// set equal gain zero's\n1 => f.eqzs;\n// initialize float variable\n0.0 => float v;\n// infinite time-loop\nwhile( true )\n{\n// set the current sample/impulse\n1.0 => i.next;\n// sweep the filter resonant frequency\n Std.fabs(Math.sin(v)) * 4000.0 => f.pfreq;\n// increment v\nv + .1 => v;\n// advance time\n100::ms => now;\n}")
# file.close()





"""
// Variables
200::ms => dur timeInMs;
16 => int gridLength;
14 => int tonesToAllocate;
gridLength - tonesToAllocate => int sustainLeft;
"""