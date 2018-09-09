// Variables
200::ms => dur timeInMs;
32 => int gridLength;
16 => int tonesToAllocate;
gridLength - tonesToAllocate => int sustainLeft;

int beatGrid[gridLength];
for(0 => int i; i<gridLength; i++){
   0 => beatGrid[i];
}
for(0=> int j; j<tonesToAllocate; j++){
   Std.rand2(0, beatGrid.cap() - 1) => int pos;
   if(beatGrid[pos]==0){
       1 => beatGrid[pos];
       1 => int q;
       if(pos+q >= gridLength-1){
           0 => pos;
           0 => int q;
       }
       while (Std.rand2(0,1) != 0  && beatGrid[pos+q] == 0 && sustainLeft > 0) { // TODO -> Error handling for array out of bounds
           2 => beatGrid[pos+q];
           sustainLeft--;
           q++;
       }
   }
   else {
       while(beatGrid[pos]!=0){
           Std.rand2(0, beatGrid.cap() -1) => pos;
       }
       1 => beatGrid[pos];
   }
}
for(0 => int x;x<gridLength;x++){
   <<<beatGrid[x]>>>;
}
// ------------------------------
//Frequency constants
130.81 => float C3;
146.86 => float D3;
164.81 => float E3;
174.61 => float F3;
196.00 => float G3;
220.00 => float A3;
246.94 => float B3;
261.63 => float C4;
293.66 => float D4;
329.63 => float E4;
349.23 => float F4;
392.00 => float G4;
440.00 => float A4;
493.88 => float B4;
523.25 => float C5;
587.33 => float D5;
659.25 => float E5;
698.46 => float F5;
783.99 => float G5;
880.00 => float A5;
987.77 => float B5;
1046.50 => float C6;
1174.66 => float D6;
1318.51 => float E6;
1396.91 => float F6;
1567.98 => float G6;
1760.00 => float A6;
1975.53 => float B6;
2093.00 => float C7;
2349.32 => float D7;
2637.02 => float E7;
2793.83 => float F7;
3135.96 => float G7;
3520.00 => float A7;
3951.07 => float B7;
4186.01 => float C8;
4698.63 => float D8;
5274.04 => float E8;
5587.65 => float F8;
6271.93 => float G8;
7040.00 => float A8;
7902.13 => float B8;
[C5,D5,E5,F5,G5,A5,B5,C6,D6,E6,F6,G6,A6,B6,C7,D7,E7,F7,G7,A7,B7] @=> float LEADCSale[];
SinOsc drive => Gen17 g17 => BiQuad f => dac;
// set the filter's pole radius
.99 => f.prad;
// set equal gain zero's
1 => f.eqzs;
// initialize float variable
0.0 => float v;
float coeffArray[dataVals.cap()]; //Allocate mem
for(0 => int i; i < dataVals.cap(); i++) {
    dataVals[i] => float val;
    dataVals[i] / 256 => float coeff;
    coeff => coeffArray[i];
}
coeffArray => g17.coefs;
0.02 => g17.gain;
while (true) {
    // Loop for entire song
    //500::ms => now; // Move forward 500ms
    /* Quantify vals to tones 
    
        Vals: 0-255
        Fq range: 220hz-10000hz (Laptophögtalare)
        7 toner i en skala -> 63 över hörbart spektra
        6*7 = 42 toner
        130 -> 7902
    
    */
    for (0 => int j; j < beatGrid.cap(); j++) {
        1 => drive.gain;
        if (beatGrid[j] == 1) {
            dataVals[(j*dataVals.cap())/gridLength] => float val;
            Math.round(val/42) $ int => int noteIndex; // Calculate a note index from array
            LEADCSale[noteIndex] => drive.freq;
            Std.fabs(Math.sin(v)) * 10.00 => f.pfreq;
            v + .8 => v;
            timeInMs => now;
        }
        else {
            if (beatGrid[j] == 2) {
                timeInMs => now;
            } else {
                0 => drive.gain;
                timeInMs => now;
            }
        }
    }
}