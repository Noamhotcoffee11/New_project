# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import shutil
from gc import collect
import os
from glob import glob

def create_directory(dataset_path: str) -> str:
    '''
    

    Returns
    -------
    string.
        Reset the content in the folders for a clean restart

    '''
    collect()
    dataset_path=os.path.expanduser(dataset_path)
    
    if os.path.exists(f'{dataset_path}/classes'):
        shutil.rmtree(f'{dataset_path}/classes')

    os.mkdir(f'{dataset_path}/classes')
    os.mkdir(f'{dataset_path}/classes/ai')
    os.mkdir(f'{dataset_path}/classes/real')

    return dataset_path