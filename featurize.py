import os
import sys
import argparse
from prosody import Voice_Prosody
import pandas as pd
from datetime import datetime
'''
Featurize Wrapper for grabbing prosody features for audio stored in a folder
'''


def main(audio,fsize):
    output_path = 'Output_Folder'
    if output_path not in os.listdir():
        os.mkdir(output_path)
    df = pd.DataFrame()
    vp = Voice_Prosody()
    if os.path.isdir(audio) == False:
        print("Provided path is not a directory. Please pass a directory")
        sys.exit(1)
    for fi in os.listdir(audio):
        if '.wav' in fi:
            print('Featurizing:',fi)
            feat_dict = vp.featurize_audio(os.path.join(audio,fi),int(fsize))
            df = df.append(feat_dict,ignore_index=True)
    date = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    df.to_csv(os.path.join(output_path,'prosody_features_' + date + '.csv'))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-a','--audio_path',help='Audio Path',required=True)
    parser.add_argument('-f','--frame_size',help='Frame Size',required=True)
    args = parser.parse_args()
    main(args.audio_path,args.frame_size)
