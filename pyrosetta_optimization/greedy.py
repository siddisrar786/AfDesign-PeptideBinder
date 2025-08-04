#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 11 14:06:02 2025
@author: sudhanshu
"""

from pyrosetta import *
init()

import numpy as np
from pyrosetta.teaching import PyMOLMover

# Initialize PyMOL mover
pmm = PyMOLMover()
pmm.keep_history(True)

# Create initial pose from sequence
pose = pose_from_sequence('LNITARAY')
sf = get_fa_scorefxn()

# Save starting structure
pose.dump_pdb("start.pdb")

# Score of starting pose
lowestE = sf(pose)
previousE = lowestE

# Total residues in the pose
total_residues = pose.total_residue()

# Run perturbation loop
for i in range(10000):
    randmove = np.random.uniform(-2.5, 2.5)  # Random move between -2.5 and +2.5
    random_site = np.random.randint(2, total_residues)  # Avoid terminal residues (1 and N)

    # Apply random phi or psi torsion change
    if np.random.rand() > 0.5:
        original_phi = pose.phi(random_site)
        pose.set_phi(random_site, original_phi + randmove)
    else:
        original_psi = pose.psi(random_site)
        pose.set_psi(random_site, original_psi + randmove)

    # Score new pose
    currentE = sf(pose)

    # Print energy update
    print(f"[{i}] Previous: {previousE:.2f}, Current: {currentE:.2f}, Lowest: {lowestE:.2f}")

    # Save structure if better
    if currentE < lowestE:
        lowestE = currentE
        pose.dump_pdb('low.pdb')

    # Update PyMOL and store previous energy
    previousE = currentE
    pmm.apply(pose)
