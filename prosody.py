import py-webrtcvad

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
        preproc_audio(audioFile)
    def preproc_audio(self,audioFile):
        '''
        Performs preprocessing of audio
        - Create Temp Folder for Extracted Sub-Audio. 
        - Perform the multi-intensity segmentation of audio data.
        - Question: Do we even need to write out audio? What if we just
        get the segmented length parameters, would that be more computationally efficient?
        '''
    
    def getSpeechTime(self,):
        '''
        Returns Total Speech Time
        '''
    
    def getPauseTime(self,):
        '''
        Returns total Pause Time
        '''