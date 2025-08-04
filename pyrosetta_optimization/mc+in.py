#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 11 13:25:47 2025

@author: sudhanshu
metroplis with simple minimization
"""


from pyrosetta import *
from pyrosetta.rosetta.protocols.minimization_packing import MinMover
import numpy as np
init("--mute all")

kT = 1#0.592 #kcal/mol ## roseta uses 1
maxMove = 10  # degree


movemap = MoveMap()
movemap.set_bb(True)
movemap.set_chi(True)

minm = MinMover()
minm.movemap(movemap)



pose = pose_from_sequence('LNITARAY')
minm.apply(pose)
sf = get_fa_scorefxn()
pose.dump_pdb("start.pdb")
lowestE = sf(pose)
pose.dump_pdb("low3.pdb")
accept = 0

for i in range(10000):   
    
    ## temp pose for modifciation
    temp_Pose = Pose()
    temp_Pose.assign(pose)
    previousE = sf(temp_Pose)
    
    ## Modification   
    randmove1 = (np.random.rand() - 0.5)*maxMove*2
    randomeSite = np.random.randint( len(pose))
    
    if np.random.rand() >0.5:
        originalphi = pose.phi(randomeSite+1)
        ## working in temp pose
        temp_Pose.set_phi(randomeSite+1, originalphi + randmove1) 
    else:
        originalpsi = pose.psi(randomeSite+1)
        ## working in temp pose
        temp_Pose.set_psi(randomeSite+1, originalpsi + randmove1)
    
    
    # Score of modified pose
    minm.apply(temp_Pose)
    newE = sf(temp_Pose) 
    
    
    # acceptance of rejection
    if newE < previousE:
        accept = 1
        
    elif np.random.rand() < np.exp(-(newE - previousE)/kT):
        accept = 1
        
    
    # perform acceptance of rejection
    if accept==1:
        print("New_E=%7.2f Previos_E=%7.2f Lowest_E=%7.2f" % (newE, previousE, lowestE))
        pose.assign(temp_Pose)
        previousE = newE
        pose.dump_pdb("current.pdb")
        
        
        
        if newE  < lowestE:
            pose.dump_pdb("low.pdb")
            lowestE = newE
            
        
    
        
    