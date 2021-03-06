# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 11:59:42 2016

@author: dreostilab (Elena Dreosti)
"""
# -----------------------------------------------------------------------------
# Set "Library Path" - Social Zebrafish Repo

# Set Library Paths
import sys
sys.path.append(r'Z:/D R E O S T I   L A B/Hande/Virtual_Assay_Files&Settings/Virtual_Behaviour_Libraries')
#sys.path.append(lib_path)

# Import useful libraries
import os
import glob
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import scipy.signal as signal
import CV_ARK
import scipy.misc as misc
from scipy import stats
import SZ_utilities as SZU
import SZ_macros as SZM
import SZ_video as SZV
import BONSAI_ARK

## Read Folder List
#folderListFile = base_path + r'\Adam_Ele\Shared Programming\Python\Social Zebrafish\Folder Lists\Dreosti_LAb\\Wt_Nacre'
#
#folderListFile = folderListFile + r'\Folder_List_Wt_Nacre.txt'

#folderListFile = (base_path + r'\Adam_Ele\Shared Programming\Python\Social Zebrafish\Folder Lists\Dreosti_LAb\Wt_Nacre')
#folderListFile = folderListFile + r'\Folder_List_Wt_Nacre_test.txt'

#folderListFile = (base_path + r'\Adam_Ele\Shared Programming\Python\Social Zebrafish\Folder Lists\Isolation_experiments')
#folderListFile = folderListFile + r'\Folder_List_Isolation_test.txt'

#folderListFile = (base_path + r'\Python_ED\Folder_List')
#folderListFile = folderListFile + r'\SocialFolderList_2017_05_25_Condition_A.txt'

#folderListFile = r'\\128.40.155.187\data\D R E O S T I   L A B\Isolation_Experiments\New_Tracking\Folder_List\Long_Isolation_All_Isolated.txt'

folderListFile = r'Z:/D R E O S T I   L A B/Hande/Virtual_Behaviour/Experiment_1/Folder_List/Virtual_Behaviour_Complete_List_EXP_1.txt'

dark = False
control = False  
multiple = False
groups, ages, folderNames, fishStatus = SZU.read_folder_list_3fish(folderListFile)

# Bulk analysis of all folders
for idx,folder in enumerate(folderNames):
    
    # Get Folder Names
    NS_folder, S_folder, C_folder = SZU.get_folder_names_3fish(folder)
    Stimulus_folder = S_folder + '/Social_Fish'

    # ---------------------
    # Process Video (NS)
    bonsaiFiles = glob.glob(NS_folder + '\*.bonsai')
    bonsaiFiles = bonsaiFiles[0]
    ROIs = BONSAI_ARK.read_bonsai_crop_rois(bonsaiFiles)
    ROIs = ROIs[:, :]
    fxS, fyS, bxS, byS, exS, eyS, areaS, ortS, motS = SZV.improved_fish_tracking_3fish(NS_folder, NS_folder, ROIs)

    # Save Tracking (NS)
    for i in range(0,3):
        # Save NS
        filename = NS_folder + r'\tracking'+ str(i+1) + '.npz'
        fish = np.vstack((fxS[:,i], fyS[:,i], bxS[:,i], byS[:,i], exS[:,i], eyS[:,i], areaS[:,i], ortS[:,i], motS[:,i]))
        np.savez(filename, tracking=fish.T)
    
    # ---------------------
    # Process Video (S)
    bonsaiFiles = glob.glob(S_folder + '\*.bonsai')
    bonsaiFiles = bonsaiFiles[0]
    ROIs = BONSAI_ARK.read_bonsai_crop_rois(bonsaiFiles)
    ROIs = ROIs[:, :]
    fxS, fyS, bxS, byS, exS, eyS, areaS, ortS, motS = SZV.improved_fish_tracking_3fish(S_folder, S_folder, ROIs)

    # Save Tracking (S)
    for i in range(0,3):
        # Save S_test
        filename = S_folder + r'\tracking'+ str(i+1) + '.npz'
        fish = np.vstack((fxS[:,i], fyS[:,i], bxS[:,i], byS[:,i], exS[:,i], eyS[:,i], areaS[:,i], ortS[:,i], motS[:,i]))
        np.savez(filename, tracking=fish.T)

    # ---------------------
    # Process Video (Stimulus)
    bonsaiFiles = glob.glob(Stimulus_folder + '\*.bonsai')
    bonsaiFiles = bonsaiFiles[0]
    ROIs = BONSAI_ARK.read_bonsai_crop_rois(bonsaiFiles)
    ROIs = ROIs[:, :]
    fxS, fyS, bxS, byS, exS, eyS, areaS, ortS, motS = SZV.improved_fish_tracking_3fish(S_folder, Stimulus_folder, ROIs)

    # Save Tracking (Stimulus)
    for i in range(0,3):
        # Save S_test
        filename = Stimulus_folder + r'\tracking'+ str(i+1) + '.npz'
        fish = np.vstack((fxS[:,i], fyS[:,i], bxS[:,i], byS[:,i], exS[:,i], eyS[:,i], areaS[:,i], ortS[:,i], motS[:,i]))
        np.savez(filename, tracking=fish.T)
    
    # Close Plots
    plt.close('all')
    
# End of Tracking    



