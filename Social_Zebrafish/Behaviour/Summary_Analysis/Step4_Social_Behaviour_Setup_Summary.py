# -*- coding: utf-8 -*-
"""
Created on Sun May 11 14:01:46 2014

@author: kampff
"""

# -----------------------------------------------------------------------------
# Set "Library Path" - Social Zebrafish Repo
lib_path = r'C:\Repos\Dreosti-Lab\Social_Zebrafish\libs'
#-----------------------------------------------------------------------------
# Set "Base Path" for this analysis session
#base_path = r'\\128.40.155.187\data\D R E O S T I   L A B\Isolation_Experiments\Python_Analysis_Adam'
base_path = r'\\128.40.155.187\data\D R E O S T I   L A B'

# Set Library Paths
import sys
sys.path.append(lib_path)

# Import useful libraries
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import scipy.misc as misc
from scipy import stats
import seaborn as sns
import pandas as pd

# Import local modules
import SZ_utilities as SZU
import SZ_macros as SZM
import SZ_video as SZV
import SZ_analysis as SZA
import SZ_summary as SZS
import BONSAI_ARK
import glob
import pylab as pl


# -----------------------------------------------------------------------------
# Function to load all summary statistics and make a summary figure
# -----------------------------------------------------------------------------

# Analysis folder lONG isolation
#analysisFolder = base_path + r'\Isolation_Experiments\Python_Analysis_Long_Isolation_New_Script3\Analysis_Folder\Controls_new'
#analysisFolder = base_path + r'\Isolation_Experiments\Python_Analysis_Long_Isolation_New_Script3\Analysis_Folder\Isolated_New'

# Analysis folder SHORT isolation 24h or 48h
#analysisFolder = base_path + r'\Isolation_Experiments\Python_Analysis_Short_Isolation\Analysis_Folder\Control_new'
#analysisFolder = base_path + r'\Isolation_Experiments\Python_Analysis_Short_Isolation\Analysis_Folder\24h_new'
#analysisFolder = base_path + r'\Isolation_Experiments\Python_Analysis_Short_Isolation\Analysis_Folder\48h_new'

# Analysis folder EARLY isolation up to 7dpf
#analysisFolder = base_path + r'\Isolation_Experiments\Python_Analysis_7days_Isolation\Analysis_folder\Controls_new'
#analysisFolder = base_path + r'\Isolation_Experiments\Python_Analysis_7days_Isolation\Analysis_folder\Isolated_new'

#NEW
#analysisFolder = base_path + r'\Isolation_Experiments\Python_Analysis_Long_Isolation_New_Script3\Analysis_Folder\Isolated_New - Copy\SPP_Red'
#analysisFolder = base_path + r'\Isolation_Experiments\Python_Analysis_Long_Isolation_New_Script3\Analysis_Folder\Isolated_New - Copy\SP_Orange'
#analysisFolder = base_path + r'\Isolation_Experiments\Python_Analysis_Long_Isolation_New_Script3\Analysis_Folder\Isolated_New - Copy\NP_Gray'
#analysisFolder = base_path + r'\Isolation_Experiments\Python_Analysis_Long_Isolation_New_Script3\Analysis_Folder\Isolated_New - Copy\MP_Cyan'
#analysisFolder = base_path + r'\Isolation_Experiments\Python_Analysis_Long_Isolation_New_Script3\Analysis_Folder\Isolated_New - Copy\MPP_Blue'

#analysisFolder = base_path + r'\Isolation_Experiments\Python_Analysis_Long_Isolation_New_Script3\Analysis_Folder\Controls_new - Copy\SPP_Red'
#analysisFolder = base_path + r'\Isolation_Experiments\Python_Analysis_Long_Isolation_New_Script3\Analysis_Folder\Controls_new - Copy\SP_Orange'
#analysisFolder = base_path + r'\Isolation_Experiments\Python_Analysis_Long_Isolation_New_Script3\Analysis_Folder\Controls_new - Copy\NP_Gray'
#analysisFolder = base_path + r'\Isolation_Experiments\Python_Analysis_Long_Isolation_New_Script3\Analysis_Folder\Controls_new - Copy\MP_Cyan'
#analysisFolder = base_path + r'\Isolation_Experiments\Python_Analysis_Long_Isolation_New_Script3\Analysis_Folder\Controls_new - Copy\MPP_Blue'



#analysisFolder = base_path + r'\Isolation_Experiments\Python_Analysis_Short_Isolation\Analysis_Folder\Control\SPP'
#analysisFolder = base_path + r'\Isolation_Experiments\Python_Analysis_Short_Isolation\Analysis_Folder\Control\SP'
#analysisFolder = base_path + r'\Isolation_Experiments\Python_Analysis_Short_Isolation\Analysis_Folder\Control\NP'
#analysisFolder = base_path + r'\Isolation_Experiments\Python_Analysis_Short_Isolation\Analysis_Folder\Control\MP'
#analysisFolder = base_path + r'\Isolation_Experiments\Python_Analysis_Short_Isolation\Analysis_Folder\Control\MPP'


#analysisFolder = base_path + r'\Isolation_Experiments\Python_Analysis_Short_Isolation\Analysis_Folder\48h\All'
#analysisFolder = base_path + r'\Isolation_Experiments\Python_Analysis_Short_Isolation\Analysis_Folder\48h\SPP'
#analysisFolder = base_path + r'\Isolation_Experiments\Python_Analysis_Short_Isolation\Analysis_Folder\48h\SP'
#analysisFolder = base_path + r'\Isolation_Experiments\Python_Analysis_Short_Isolation\Analysis_Folder\48h\NP'
#analysisFolder = base_path + r'\Isolation_Experiments\Python_Analysis_Short_Isolation\Analysis_Folder\48h\MP'
#analysisFolder = base_path + r'\Isolation_Experiments\Python_Analysis_Short_Isolation\Analysis_Folder\48h\MPP'

#analysisFolder = base_path + r'\Isolation_Experiments\Python_Analysis_Short_Isolation\Analysis_Folder\Control\MPP_test'
#analysisFolder = base_path + r'\Isolation_Experiments\Python_Analysis_Short_Isolation\Analysis_Folder\Control\SPP_test'
#analysisFolder = base_path + r'\Isolation_Experiments\Python_Analysis_Short_Isolation\Analysis_Folder\Control\NP_test'



#analysisFolder = base_path + r'\Isolation_Experiments\Python_Analysis_Short_Isolation\Analysis_Folder\24h\All'
#analysisFolder = base_path + r'\Isolation_Experiments\Python_Analysis_Short_Isolation\Analysis_Folder\24h\SPP'
#analysisFolder = base_path + r'\Isolation_Experiments\Python_Analysis_Short_Isolation\Analysis_Folder\24h\SP'
#analysisFolder = base_path + r'\Isolation_Experiments\Python_Analysis_Short_Isolation\Analysis_Folder\24h\NP'
#analysisFolder = base_path + r'\Isolation_Experiments\Python_Analysis_Short_Isolation\Analysis_Folder\24h\MP'
#analysisFolder = base_path + r'\Isolation_Experiments\Python_Analysis_Short_Isolation\Analysis_Folder\24h\MPP'

#analysisFolder = base_path + r'\Isolation_Experiments\Python_Analysis_Long_Isolation_New_Script3\Analysis_Folder\Isolated\All'
analysisFolder = base_path + r'\Isolation_Experiments\Python_Analysis_Long_Isolation_New_Script3\Analysis_Folder\Controls\All'



#analysisFolder = base_path + r'\Isolation_Experiments\Python_Analysis_Short_Isolation\Analysis_Folder\Control\All'
#analysisFolder = base_path + r'\Isolation_Experiments\Python_Analysis_Short_Isolation\Analysis_Folder\24h\All'
#analysisFolder = base_path + r'\Isolation_Experiments\Python_Analysis_Short_Isolation\Analysis_Folder\48h\All'

#analysisFolder = base_path + r'\Isolation_Experiments\Python_Analysis_Long_Isolation_New_Script3\Analysis_Folder\Controls\All'
#analysisFolder = base_path + r'\Isolation_Experiments\Python_Analysis_Long_Isolation_New_Script3\Analysis_Folder\Isolated\All'

#analysisFolder = base_path + r'\Isolation_Experiments\Social_Brain_Areas_Analisys\Analysis_Folder\Wt_All_No_SC'

#analysisFolder = base_path + r'\Isolation_Experiments\Social_Brain_Areas_Analisys\Analysis_Folder\Wt_All_No_SC'

#analysisFolder = base_path + r'\Isolation_Experiments\Python_Analysis_Long_Isolation_New_Script3\Analysis_Folder\Controls\All'
#analysisFolder = base_path + r'\Isolation_Experiments\Python_Analysis_Long_Isolation_New_Script3\Analysis_Folder\Controls\SPP'
#analysisFolder = base_path + r'\Isolation_Experiments\Python_Analysis_Long_Isolation_New_Script3\Analysis_Folder\Controls\SP'
#analysisFolder = base_path + r'\Isolation_Experiments\Python_Analysis_Long_Isolation_New_Script3\Analysis_Folder\Controls\NP'
#analysisFolder = base_path + r'\Isolation_Experiments\Python_Analysis_Long_Isolation_New_Script3\Analysis_Folder\Controls\MP'
#analysisFolder = base_path + r'\Isolation_Experiments\Python_Analysis_Long_Isolation_New_Script3\Analysis_Folder\Controls\MPP'


#analysisFolder = base_path + r'\Isolation_Experiments\Python_Analysis_Long_Isolation_New_Script3\Analysis_Folder\Isolated\All'
#analysisFolder = base_path + r'\Isolation_Experiments\Python_Analysis_Long_Isolation_New_Script3\Analysis_Folder\Isolated\MPP'
#analysisFolder = base_path + r'\Isolation_Experiments\Python_Analysis_Long_Isolation_New_Script3\Analysis_Folder\Isolated\MP'
#analysisFolder = base_path + r'\Isolation_Experiments\Python_Analysis_Long_Isolation_New_Script3\Analysis_Folder\Isolated\NP'
#analysisFolder = base_path + r'\Isolation_Experiments\Python_Analysis_Long_Isolation_New_Script3\Analysis_Folder\Isolated\SP'
#analysisFolder = base_path + r'\Isolation_Experiments\Python_Analysis_Long_Isolation_New_Script3\Analysis_Folder\Isolated\SPP'

#analysisFolder = base_path + r'\Isolation_Experiments\Social_Brain_Areas_Analisys\Analysis_Folder\Wt_All'
#analysisFolder = base_path + r'\Isolation_Experiments\Python_Analysis_Long_Isolation_New_Script3\Analysis_Folder\Controls\All'
#analysisFolder = base_path + r'\Isolation_Experiments\Python_Analysis_Long_Isolation_New_Script3\Analysis_Folder\Isolated\All'

#analysisFolder = base_path + r'\Isolation_Experiments\Python_Analysis_All_No_SC\Analysis_Folder\Wt_No_SC'
#analysisFolder = base_path + r'\Isolation_Experiments\Python_Analysis_All_No_SC\Analysis_Folder\Isolated_No_SC'

# Freeze time threshold
freeze_threshold = 500

# Find all the npz files saved for each group and fish with all the information
npzFiles = glob.glob(analysisFolder+'\*.npz')

#Calculate how many files
numFiles = np.size(npzFiles, 0)

VPI_NS_ALL = np.zeros(numFiles)
VPI_S_ALL = np.zeros(numFiles)

SPI_NS_ALL = np.zeros(numFiles)
SPI_S_ALL = np.zeros(numFiles)

BPS_NS_ALL = np.zeros(numFiles)
BPS_S_ALL = np.zeros(numFiles)

Distance_NS_ALL = np.zeros(numFiles)
Distance_S_ALL = np.zeros(numFiles)

Freezes_NS_ALL = np.zeros(numFiles)
Freezes_S_ALL = np.zeros(numFiles)

OrtHist_NS_NSS_ALL = np.zeros((numFiles,36))
OrtHist_NS_SS_ALL = np.zeros((numFiles,36))
OrtHist_S_NSS_ALL = np.zeros((numFiles,36))
OrtHist_S_SS_ALL = np.zeros((numFiles,36))

Bouts_NS_ALL = np.zeros((0,10))
Bouts_S_ALL = np.zeros((0,10))
Pauses_NS_ALL = np.zeros((0,10))   
Pauses_S_ALL = np.zeros((0,10))


#Go through all the files contained in the analysis folder
for f, filename in enumerate(npzFiles):

    #Load each npz file
    dataobject = np.load(filename)
    
    #Extract from the npz file
    VPI_NS = dataobject['VPI_NS']    
    VPI_S = dataobject['VPI_S']   
    SPI_NS = dataobject['SPI_NS']    
    SPI_S = dataobject['SPI_S']   
    BPS_NS = dataobject['BPS_NS']   
    BPS_S = dataobject['BPS_S']
    Distance_NS = dataobject['Distance_NS']   
    Distance_S = dataobject['Distance_S']   
    OrtHist_ns_NonSocialSide = dataobject['OrtHist_NS_NonSocialSide']
    OrtHist_ns_SocialSide = dataobject['OrtHist_NS_SocialSide']
    OrtHist_s_NonSocialSide = dataobject['OrtHist_S_NonSocialSide']
    OrtHist_s_SocialSide = dataobject['OrtHist_S_SocialSide']
    Bouts_NS = dataobject['Bouts_NS']   
    Bouts_S = dataobject['Bouts_S']
    Pauses_NS = dataobject['Pauses_NS']   
    Pauses_S = dataobject['Pauses_S']
    
    # Count Freezes
    Freezes_NS_ALL[f] = np.sum(Pauses_NS[:,8] > freeze_threshold)
    Freezes_S_ALL[f] = np.sum(Pauses_S[:,8] > freeze_threshold)
    
    #Make an array with all summary stats
    VPI_NS_ALL[f] = VPI_NS
    VPI_S_ALL[f] = VPI_S
    SPI_NS_ALL[f] = SPI_NS
    SPI_S_ALL[f] = SPI_S
    BPS_NS_ALL[f] = BPS_NS
    BPS_S_ALL[f] = BPS_S
    Distance_NS_ALL[f] = Distance_NS
    Distance_S_ALL[f] = Distance_S
    OrtHist_NS_NSS_ALL[f,:] = OrtHist_ns_NonSocialSide
    OrtHist_NS_SS_ALL[f,:] = OrtHist_ns_SocialSide
    OrtHist_S_NSS_ALL[f,:] = OrtHist_s_NonSocialSide
    OrtHist_S_SS_ALL[f,:] = OrtHist_s_SocialSide
    
    # Somehow concat all Pauses/Bouts
    Bouts_NS_ALL = np.vstack([Bouts_NS_ALL, Bouts_NS])
    Bouts_S_ALL = np.vstack([Bouts_S_ALL, Bouts_S])
    Pauses_NS_ALL = np.vstack([Pauses_NS_ALL, Pauses_NS])
    Pauses_S_ALL = np.vstack([Pauses_S_ALL, Pauses_S])

# ----------------
# VPI Summary Plot

#Make histogram and plot it with lines 
a_ns,c=np.histogram(VPI_NS_ALL,  bins=8, range=(-1,1))
a_s,c=np.histogram(VPI_S_ALL,  bins=8, range=(-1,1))
centers = (c[:-1]+c[1:])/2

#Normalize by tot number of fish
Tot_Fish_NS=numFiles

a_ns_float = np.float32(a_ns)
a_s_float = np.float32(a_s)

a_ns_nor_medium=a_ns_float/Tot_Fish_NS
a_s_nor_medium=a_s_float/Tot_Fish_NS 
 
plt.figure()
plt.subplot(1,3,1)
plt.plot(centers, a_ns_nor_medium, color=[0.5,0.5,0.5,1.0], linewidth=4.0)
plt.plot(centers, a_s_nor_medium, color=[1.0,0.0,0.0,0.5], linewidth=4.0)
plt.title('Non Social/Social VPI', fontsize=12)
plt.xlabel('Preference Index (PI_)', fontsize=12)
plt.ylabel('Rel. Frequency', fontsize=12)
plt.axis([-1.1, 1.1, 0, 0.5])
pl.yticks([0, 0.1, 0.2, 0.3, 0.4, 0.5], fontsize=12)
pl.xticks([-1, -0.5, 0, 0.5, 1.0], fontsize=12)

bar_width=0.25
plt.subplot(1,3,2)
plt.bar(centers, a_ns_nor_medium, width=0.25, color=[0.5,0.5,0.5,1.0], linewidth=4.0)
plt.title('Non Social VPI', fontsize=12)
plt.xlabel('Preference Index (PI_)', fontsize=12)
plt.ylabel('Rel. Frequency', fontsize=12)
plt.axis([-1.1, 1.1, 0, 0.5])
pl.yticks([0, 0.1, 0.2, 0.3, 0.4, 0.5], fontsize=12)
pl.xticks([-1, -0.5, 0, 0.5, 1.0], fontsize=12)

plt.subplot(1,3,3)
plt.bar(centers, a_s_nor_medium, width=0.25, color=[1.0,0.0,0.0,1.0], linewidth=4.0)
plt.title('Social VPI', fontsize=12)
plt.xlabel('Preference Index (PI_)', fontsize=12)
plt.ylabel('Rel. Frequency', fontsize=12)
plt.axis([-1.1, 1.1, 0, 0.5])
pl.yticks([0, 0.1, 0.2, 0.3, 0.4, 0.5], fontsize=12)
pl.xticks([-1, -0.5, 0, 0.5, 1.0], fontsize=12)


# ----------------
# SPI Summary Plot

#Make histogram and plot it with lines 
a_ns,c=np.histogram(SPI_NS_ALL,  bins=8, range=(-1,1))
a_s,c=np.histogram(SPI_S_ALL,  bins=8, range=(-1,1))
centers = (c[:-1]+c[1:])/2

#Normalize by tot number of fish
Tot_Fish_NS=numFiles

a_ns_float = np.float32(a_ns)
a_s_float = np.float32(a_s)

a_ns_nor_medium=a_ns_float/Tot_Fish_NS
a_s_nor_medium=a_s_float/Tot_Fish_NS 
 
plt.figure()
plt.subplot(1,3,1)
plt.plot(centers, a_ns_nor_medium, color=[0.5,0.5,0.5,1.0], linewidth=4.0)
plt.plot(centers, a_s_nor_medium, color=[1.0,0.0,0.0,0.5], linewidth=4.0)
plt.title('Non Social/Social SPI', fontsize=12)
plt.xlabel('Preference Index (PI_)', fontsize=12)
plt.ylabel('Rel. Frequency', fontsize=12)
plt.axis([-1.1, 1.1, 0, 0.5])
pl.yticks([0, 0.1, 0.2, 0.3, 0.4, 0.5], fontsize=12)
pl.xticks([-1, -0.5, 0, 0.5, 1.0], fontsize=12)

bar_width=0.25
plt.subplot(1,3,2)
plt.bar(centers, a_ns_nor_medium, width=0.25, color=[0.5,0.5,0.5,1.0], linewidth=4.0)
plt.title('Non Social SPI', fontsize=12)
plt.xlabel('Preference Index (PI_)', fontsize=12)
plt.ylabel('Rel. Frequency', fontsize=12)
plt.axis([-1.1, 1.1, 0, 0.5])
pl.yticks([0, 0.1, 0.2, 0.3, 0.4, 0.5], fontsize=12)
pl.xticks([-1, -0.5, 0, 0.5, 1.0], fontsize=12)

plt.subplot(1,3,3)
plt.bar(centers, a_s_nor_medium, width=0.25, color=[1.0,0.0,0.0,1.0], linewidth=4.0)
plt.title('Social SPI', fontsize=12)
plt.xlabel('Preference Index (PI_)', fontsize=12)
plt.ylabel('Rel. Frequency', fontsize=12)
plt.axis([-1.1, 1.1, 0, 0.5])
pl.yticks([0, 0.1, 0.2, 0.3, 0.4, 0.5], fontsize=12)
pl.xticks([-1, -0.5, 0, 0.5, 1.0], fontsize=12)


# ----------------
# BPS Summary Plot

# Make histogram and plot it with lines 
a_ns,c=np.histogram(BPS_NS_ALL,  bins=16, range=(0,10))
a_s,c=np.histogram(BPS_S_ALL,  bins=16, range=(0,10))
centers = (c[:-1]+c[1:])/2

#Normalize by tot number of fish
Tot_Fish_NS=numFiles

a_ns_float = np.float32(a_ns)
a_s_float = np.float32(a_s)

a_ns_nor_medium=a_ns_float/Tot_Fish_NS
a_s_nor_medium=a_s_float/Tot_Fish_NS 
 
plt.figure()
plt.subplot(1,3,1)
plt.plot(centers, a_ns_nor_medium, color=[0.5,0.5,0.5,1.0], linewidth=4.0)
plt.plot(centers, a_s_nor_medium, color=[1.0,0.0,0.0,0.5], linewidth=4.0)
plt.title('Non Social/Social BPS', fontsize=12)
plt.xlabel('Bouts per Second (BPS)', fontsize=12)
plt.ylabel('Rel. Frequency', fontsize=12)
plt.axis([-0.1, 10.1, 0, 0.5])
pl.yticks([0, 0.1, 0.2, 0.3, 0.4, 0.5], fontsize=12)
pl.xticks([0, 5, 10], fontsize=12)

bar_width=0.5
plt.subplot(1,3,2)
plt.bar(centers, a_ns_nor_medium, width=bar_width, color=[0.5,0.5,0.5,1.0], linewidth=4.0)
plt.title('Non Social BPS', fontsize=12)
plt.xlabel('Bouts per Second (BPS)', fontsize=12)
plt.ylabel('Rel. Frequency', fontsize=12)
plt.axis([-0.1, 10.1, 0, 0.5])
pl.yticks([0, 0.1, 0.2, 0.3, 0.4, 0.5], fontsize=12)
pl.xticks([0, 5, 10], fontsize=12)

plt.subplot(1,3,3)
plt.bar(centers, a_s_nor_medium, width=bar_width, color=[1.0,0.0,0.0,1.0], linewidth=4.0)
plt.title('Social BPS', fontsize=12)
plt.xlabel('Bouts per Second (BPS)', fontsize=12)
plt.ylabel('Rel. Frequency', fontsize=12)
plt.axis([-0.1, 10.1, 0, 0.5])
pl.yticks([0, 0.1, 0.2, 0.3, 0.4, 0.5], fontsize=12)
pl.xticks([0, 5, 10], fontsize=12)

# ----------------
# Bouts Summary Plot
plt.figure()
bar_width=0.005

# NS
visible_bouts = np.where(Bouts_NS_ALL[:,9] == 1)[0]
non_visible_bouts = np.where(Bouts_NS_ALL[:,9] == 0)[0]
plt.subplot(221)
bout_durations_ns, c = np.histogram(Bouts_NS_ALL[non_visible_bouts,8], bins=51, range=(0,50))
centers = (c[:-1]+c[1:])/2
plt.bar(centers/100, bout_durations_ns, width=bar_width, color=[0.5,0.5,0.5,1.0], linewidth=4.0)
plt.title('Non Social Bout Durations (non-visible)', fontsize=12)
plt.ylabel('Rel. Frequency', fontsize=12)
plt.subplot(223)
bout_durations_ns, c = np.histogram(Bouts_NS_ALL[visible_bouts,8], bins=51, range=(0,50))
centers = (c[:-1]+c[1:])/2
plt.bar(centers/100, bout_durations_ns, width=bar_width, color=[0.5,0.5,0.5,1.0], linewidth=4.0)
plt.title('Non Social Bout Durations (visible)', fontsize=12)
plt.xlabel('Bout Durations (sec)', fontsize=12)
plt.ylabel('Rel. Frequency', fontsize=12)
# S
visible_bouts = np.where(Bouts_S_ALL[:,9] == 1)[0]
non_visible_bouts = np.where(Bouts_S_ALL[:,9] == 0)[0]
plt.subplot(222)
bout_durations_s, c = np.histogram(Bouts_S_ALL[non_visible_bouts,8], bins=51, range=(0,50))
centers = (c[:-1]+c[1:])/2
plt.bar(centers/100, bout_durations_s, width=bar_width, color=[1.0,0.5,0.5,1.0], linewidth=4.0)
plt.title('Social Bout Durations (non-visible)', fontsize=12)
plt.ylabel('Rel. Frequency', fontsize=12)
plt.subplot(224)
bout_durations_s, c = np.histogram(Bouts_S_ALL[visible_bouts,8], bins=51, range=(0,50))
centers = (c[:-1]+c[1:])/2
plt.bar(centers/100, bout_durations_s, width=bar_width, color=[1.0,0.5,0.5,1.0], linewidth=4.0)
plt.title('Social Bout Durations (visible)', fontsize=12)
plt.xlabel('Bout Durations (sec)', fontsize=12)
plt.ylabel('Rel. Frequency', fontsize=12)

# ----------------
# All Bouts Summary Plot
plt.figure()
plt.subplot(1,2,1)
plt.plot(Bouts_NS_ALL[:, 1], Bouts_NS_ALL[:, 2], '.', Color=[0.0, 0.0, 0.0, 0.002])
plt.axis([0, 17, 0, 42])
plt.gca().invert_yaxis()
    
plt.subplot(1,2,2)
plt.plot(Bouts_S_ALL[:, 1], Bouts_S_ALL[:, 2], '.', Color=[0.0, 0.0, 0.0, 0.002])
plt.axis([0, 17, 0, 42])
plt.gca().invert_yaxis()

# ----------------
# Long Pauses Summary Plot
plt.figure()
plt.subplot(1,2,1)
long_pauses_ns = np.where(Pauses_NS_ALL[:,8] > freeze_threshold)[0]
num_long_pauses_per_fish_ns = len(long_pauses_ns)/numFiles
plt.title('NS: #Long Pauses = ' + format(num_long_pauses_per_fish_ns, '.4f'))
plt.plot(Pauses_NS_ALL[long_pauses_ns, 1], Pauses_NS_ALL[long_pauses_ns, 2], 'o', Color=[0.0, 0.0, 0.0, 0.2])
plt.axis([0, 17, 0, 42])
plt.gca().invert_yaxis()
    
plt.subplot(1,2,2)
long_pauses_s = np.where(Pauses_S_ALL[:,8] > freeze_threshold)[0]
num_long_pauses_per_fish_s = len(long_pauses_s)/numFiles
plt.title('S: #Long Pauses = ' + format(num_long_pauses_per_fish_s, '.4f'))
plt.plot(Pauses_S_ALL[long_pauses_s, 1], Pauses_S_ALL[long_pauses_s, 2], 'o', Color=[0.0, 0.0, 0.0, 0.2])
plt.axis([0, 17, 0, 42])
plt.gca().invert_yaxis()

# ----------------
# VPI vs BPS Summary Plot 
plt.figure()
plt.subplot(1,2,1)
plt.title('VPI vs BPS (NS)')
plt.plot(VPI_NS_ALL, BPS_NS_ALL, 'o', Color=[0.0, 0.0, 0.0, 0.5])
plt.xlabel('Visual Preference Index (VPI)', fontsize=12)
plt.ylabel('Bouts per Second', fontsize=12)
plt.axis([-1.1, 1.1, 0, max(BPS_NS_ALL)+0.5])
pl.xticks([-1, -0.5, 0, 0.5, 1.0], fontsize=12)
    
plt.subplot(1,2,2)
plt.title('VPI vs BPS (S)')
plt.plot(VPI_S_ALL, BPS_S_ALL, 'o', Color=[0.0, 0.0, 0.0, 0.5])
plt.xlabel('Visual Preference Index (VPI)', fontsize=12)
plt.axis([-1.1, 1.1, 0,  max(BPS_S_ALL)+0.5])
pl.xticks([-1, -0.5, 0, 0.5, 1.0], fontsize=12)

# ----------------
# VPI vs Distance Traveled Summary Plot 
plt.figure()
plt.subplot(1,2,1)
plt.title('VPI vs Distance Traveled (NS)')
plt.plot(VPI_NS_ALL, Distance_NS_ALL, 'o', Color=[0.0, 0.0, 0.0, 0.5])
plt.xlabel('Visual Preference Index (VPI)', fontsize=12)
plt.ylabel('Distance (mm)', fontsize=12)
plt.axis([-1.1, 1.1, 0, max(Distance_NS_ALL)+0.5])
pl.xticks([-1, -0.5, 0, 0.5, 1.0], fontsize=12)
    
plt.subplot(1,2,2)
plt.title('VPI vs Distance Traveled (S)')
plt.plot(VPI_S_ALL, Distance_S_ALL, 'o', Color=[0.0, 0.0, 0.0, 0.5])
plt.xlabel('Visual Preference Index (VPI)', fontsize=12)
plt.axis([-1.1, 1.1, 0,  max(Distance_S_ALL)+0.5])
pl.xticks([-1, -0.5, 0, 0.5, 1.0], fontsize=12)

# ----------------
# VPI vs Number of Long Pauses Summary Plot 
plt.figure()
plt.subplot(1,2,1)
plt.title('VPI vs Freezes (NS)')
plt.plot(VPI_NS_ALL, Freezes_NS_ALL, 'o', Color=[0.0, 0.0, 0.0, 0.5])
plt.xlabel('Visual Preference Index (VPI)', fontsize=12)
plt.ylabel('Freezes (count)', fontsize=12)
plt.axis([-1.1, 1.1, -1, max(Freezes_NS_ALL)+0.5])
pl.xticks([-1, -0.5, 0, 0.5, 1.0], fontsize=12)
    
plt.subplot(1,2,2)
plt.title('VPI vs Freezes (S)')
plt.plot(VPI_S_ALL, Freezes_S_ALL, 'o', Color=[0.0, 0.0, 0.0, 0.5])
plt.xlabel('Visual Preference Index (VPI)', fontsize=12)
plt.axis([-1.1, 1.1, -1, max(Freezes_S_ALL)+0.5])
pl.xticks([-1, -0.5, 0, 0.5, 1.0], fontsize=12)



# ----------------
# ORT_HIST Summary Plot

# Accumulate all histogram values and normalize
Accum_OrtHist_NS_NSS_ALL = np.sum(OrtHist_NS_NSS_ALL, axis=0)
Accum_OrtHist_NS_SS_ALL = np.sum(OrtHist_NS_SS_ALL, axis=0)
Accum_OrtHist_S_NSS_ALL = np.sum(OrtHist_S_NSS_ALL, axis=0)
Accum_OrtHist_S_SS_ALL= np.sum(OrtHist_S_SS_ALL, axis=0)

Norm_OrtHist_NS_NSS_ALL = Accum_OrtHist_NS_NSS_ALL/np.sum(Accum_OrtHist_NS_NSS_ALL)
Norm_OrtHist_NS_SS_ALL = Accum_OrtHist_NS_SS_ALL/np.sum(Accum_OrtHist_NS_SS_ALL)
Norm_OrtHist_S_NSS_ALL = Accum_OrtHist_S_NSS_ALL/np.sum(Accum_OrtHist_S_NSS_ALL)
Norm_OrtHist_S_SS_ALL = Accum_OrtHist_S_SS_ALL/np.sum(Accum_OrtHist_S_SS_ALL)

# Plot Summary
xAxis = np.arange(-np.pi,np.pi+np.pi/18.0, np.pi/18.0)
#plt.figure('Summary: Orientation Histograms')
plt.figure()

ax = plt.subplot(221, polar=True)
plt.title('NS - Non Social Side')
plt.plot(xAxis, np.hstack((Norm_OrtHist_NS_NSS_ALL, Norm_OrtHist_NS_NSS_ALL[0])), linewidth = 3)

ax = plt.subplot(222, polar=True)
plt.title('NS - Social Side')
plt.plot(xAxis, np.hstack((Norm_OrtHist_NS_SS_ALL, Norm_OrtHist_NS_SS_ALL[0])), linewidth = 3)

ax = plt.subplot(223, polar=True)
plt.title('S - Non Social Side')
plt.plot(xAxis, np.hstack((Norm_OrtHist_S_NSS_ALL, Norm_OrtHist_S_NSS_ALL[0])), linewidth = 3)

ax = plt.subplot(224, polar=True)
plt.title('S - Social Side')
plt.plot(xAxis, np.hstack((Norm_OrtHist_S_SS_ALL, Norm_OrtHist_S_SS_ALL[0])), linewidth = 3)


#------------------------
# Behaviour Summary plots
plt.figure()

# VPI
plt.subplot(2,2,1)
plt.title('VPI')
s1 = pd.Series(VPI_NS_ALL, name='NS')
s2 = pd.Series(VPI_S_ALL, name='S')
df = pd.concat([s1,s2], axis=1)
sns.barplot(data=df, orient="v", saturation=0.1, color=[0.75,0.75,0.75,1], ci=95, capsize=0.05, errwidth=2)
sns.stripplot(data=df, orient="v", size=4, jitter=True, edgecolor="gray")

# BPS
plt.subplot(2,2,2)
plt.title('BPS')
s1 = pd.Series(BPS_NS_ALL, name='NS')
s2 = pd.Series(BPS_S_ALL, name='S')
df = pd.concat([s1,s2], axis=1)
sns.barplot(data=df, orient="v", saturation=0.1, color=[0.75,0.75,0.75,1], ci=95, capsize=0.05, errwidth=2)
sns.stripplot(data=df, orient="v", size=4, jitter=True, edgecolor="gray")

# Distance
plt.subplot(2,2,3)
plt.title('Distance Traveled')
s1 = pd.Series(Distance_NS_ALL, name='NS')
s2 = pd.Series(Distance_S_ALL, name='S')
df = pd.concat([s1,s2], axis=1)
sns.barplot(data=df, orient="v", saturation=0.1, color=[0.75,0.75,0.75,1], ci=95, capsize=0.05, errwidth=2)
sns.stripplot(data=df, orient="v", size=4, jitter=True, edgecolor="gray")

# Freezes
plt.subplot(2,2,4)
plt.title('Freezes')
s1 = pd.Series(Freezes_NS_ALL, name='NS')
s2 = pd.Series(Freezes_S_ALL, name='S')
df = pd.concat([s1,s2], axis=1)
sns.barplot(data=df, orient="v", saturation=0.1, color=[0.75,0.75,0.75,1], ci=95, capsize=0.05, errwidth=2)
sns.stripplot(data=df, orient="v", size=4, jitter=True, edgecolor="gray")


# FIN
