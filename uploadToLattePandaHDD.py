# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 15:23:37 2023

@author: Derek Marsch
"""

import subprocess
import shutil


USER = 'dmarsch'
MOUNT_POINT = f'/media/{USER}/avolusion'
STATIC_IP_ADDY = '192.168.86.30'
TARGET = f'{USER}@{STATIC_IP_ADDY}:{MOUNT_POINT}'
USER_PASSWORD = 'Cookie.4597'

PSCP = 'pscp.exe'
PSCP_DIR = 'C:\\Users\\Derek Marsch\\Downloads'

TV_dict = {
    "1" : "Jace Shows",
    "2" : "Little Beth Shows",
    "3" : "Shows",
    "4" : "Shows Beth and Derek Like",
    "5" : "Unwatched Shows"
}

Movies_dict = {
    "1" : "ActionWar",
    "2" : "Christmas Movies",
    "3" : "Comedy RomCom",
    "4" : "Dramas Thrillers Suspense",
    "5" : "Jace Movies",
    "6" : "Little Beth Movies",
    "7" : "SciFi Fantasy",
    "8" : "Superhero Movies"    
}

rootDir_dict = {
    "1" : "Audiobooks",
    "2" : "eBooks",
    "3" : Movies_dict,
    "4" : TV_dict,
    "5" : "Pictures"
}

ROOT_DIR_SEL_MSG = '''\t1 for Audiobooks\n
    \t2 for eBooks\n
    \t3 for Movies\n
    \t4 for TV\n
    \t5 for Pictures\n'''
MOVIE_DIR_SEL_MSG = '''\t1 for Action/War\n
    \t2 for Christmas Movies\n
    \t3 for Comedy/RomCom\n
    \t4 for Dramas/Thrillers/Suspense\n
    \t5 for Jace Movies\n
    \t6 for Little Beth Movies\n
    \t7 for SciFi/Fantasy\n
    \t8 for Superhero Movies\n'''
    
TV_DIR_SEL_MSG = '''\t1 for Jace Shows\n
    \t2 for Little Beth Shows\n
    \t3 for Derek Shows\n
    \t4 for Shows Beth and Derek Like\n
    \t5 for Unwatched Shows\n'''

if __name__ == "__main__":
    dirSelValid = False
    while(True):
        pathToSourceDir = input('Please enter the path to the directory to be recursively copied: ').strip('"') #remove " from dragging & dropping

        while(dirSelValid == False):
            targetRootDirSel = input(f'Please enter target root directory type:\n{ROOT_DIR_SEL_MSG}')
            if(targetRootDirSel not in rootDir_dict):
                print('Selection invalid. Please try again.')
            else:
                dirSelValid = True
                                  
        if(type(rootDir_dict[targetRootDirSel]) is dict): #Movies or TV selected
            if(rootDir_dict[targetRootDirSel] == Movies_dict):
                movieDirSelValid = False
                while(movieDirSelValid == False):
                    targetDirSel = input(f'Please enter the movie category:\n{MOVIE_DIR_SEL_MSG}')
                    if(targetDirSel in Movies_dict):
                        movieDirSelValid = True
                    else:
                        print('Selection invalid. Please try again.')
                        
                pathToTargetDir = 'Movies/' + Movies_dict[targetDirSel]
            elif(rootDir_dict[targetRootDirSel] == TV_dict):
                tvDirSelValid = False
                while(tvDirSelValid == False):
                    targetDirSel = input(f'Please enter the desired directory:\n{TV_DIR_SEL_MSG}')
                    if(targetDirSel in TV_dict):
                        tvDirSelValid = True
                    else:
                        print('Selection invalid. Please try again.')
                pathToTargetDir = 'TV/' + TV_dict[targetDirSel]
        else:
            pathToTargetDir = rootDir_dict[targetRootDirSel]
        
        targetDir = input('Please enter the path to the target directory (Ex: Survivor, Survivor/Season 45, etc.): ')
        pathToTargetDir = pathToTargetDir + '/' + targetDir
        
        # print(f'TARGET: {TARGET}')
        # print(f'pscp dir: {PSCP_DIR}')
        # print(f'source dir: {pathToSourceDir}')
        # print(f'target dir: {pathToTargetDir}')
        # print(f'path to target: {TARGET}/{pathToTargetDir}')
        
        try:
            # print([PSCP, "-v", "-pw", USER_PASSWORD, "-r", pathToSourceDir, f'{TARGET}/{pathToTargetDir}'])
            result = subprocess.run([PSCP, "-v", "-pw", USER_PASSWORD, "-r", pathToSourceDir, f'{TARGET}/{pathToTargetDir}'], cwd = PSCP_DIR, capture_output = True) #broken

            # print(f'args: {result.args}')
            result.check_returncode() #raise error if return code not 0
            print('Upload successful')
            shutil.rmtree(pathToSourceDir, ignore_errors=True) # Use shutil.rmtree for cross-platform directory removal (ignore FileNotFoundError)
        except subprocess.CalledProcessError as e:
            print ( "Error:\nreturn code: ", e.returncode, "\nOutput: ", e.stderr.decode("utf-8") )
            raise
            