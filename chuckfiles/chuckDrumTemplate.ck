SndBuf buffer => dac;

4 * timeInMs => dur delayTime;
6 => int nrOfReps;
1 => float originGain;
1 => float gainOfRep;
2 => int speedOfDet;

while (true){
    originGain => gainOfRep;
    gainOfRep => buffer.gain;  
    me.dir() + "Klapp.wav" => buffer.read;
    for(0 => int i; i < nrOfReps; i++){
        delayTime/nrOfReps => now;
        gainOfRep/speedOfDet => gainOfRep;
        gainOfRep => buffer.gain;
        me.dir() + "Klapp.wav" => buffer.read;
    }
}