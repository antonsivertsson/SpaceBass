SndBuf buffer => dac;

800::ms => dur timeInMs;
6 => int nrOfReps;
1 => float originGain;
1 => float gainOfRep;
2 => int speedOfDet;

while (true){
    originGain => gainOfRep;
    gainOfRep => buffer.gain;  
    me.dir() + "Klapp.wav" => buffer.read;
    for(0 => int i; i < nrOfReps; i++){
        timeInMs/nrOfReps => now;
        gainOfRep/speedOfDet => gainOfRep;
        gainOfRep => buffer.gain;
        me.dir() + "Klapp.wav" => buffer.read;
    }
}