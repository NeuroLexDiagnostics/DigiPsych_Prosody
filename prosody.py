import webrtcvad
from vad_helper import read_wave, frame_generator,vad_collector
import os
import sys 


class Voice_Prosody:
    def __init__(self):
        '''
        Class embeds methods of voice activity detection
        to generate prosodic features of voice
        '''
        
    def featurize_audio(self,audioFile):
        '''
        Central API method to call to perform audio featurization.
        '''
        if os.path.exists(audioFile) == False or '.wav' not in audioFile:
            sys.stderr.write("Path does not exist or is not a .wav file\n")
            sys.exit(1)
        preproc_audio(audioFile)

    def preproc_audio(self,audioFile):
        '''
        Preprocessing Audio File into pcm data and gain segments of data
        '''
        levels = [1,2,3] #Intensity levels
        audio, sample_rate = read_wave(audioFile)
        
        for lv in levels:
            vad = webrtcvad.Vad(lv)
            frames = list(frame_generator(30,audio,sample_rate))
            segments = vad_collector(sample_rate,30,300,vad,frames)
            print(segments)
            
            
            
    
    def getSpeechTime(self,):
        '''
        Returns Total Speech Time
        '''
    
    def getPauseTime(self,):
        '''
        Returns total Pause Time
        '''


def main():
    pros = Voice_Prosody()
    pros.featurize_audio('C:/Users/lazhang/Desktop/CombinedAudio/289107.wav')
if __name__ == '__main__':
    main()