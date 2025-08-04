import os

structure = {
    "afdesign_outputs": ["model_1.pdb", "model_2.pdb"],
    "pyrosetta_optimization": ["greedy.py", "metropolis_mc.py", "mc_minmover.py", "low.pdb", "low2.pdb", "low3.pdb"],
    "data": ["target_2H6U.pdb"],
    "images": ["structure_comparison.png"]
}

for folder, files in structure.items():
    os.makedirs(folder, exist_ok=True)
    for file in files:
        with open(os.path.join(folder, file), "w") as f:
            f.write(f"# Placeholder for {file}\n")

with open("README.md", "w") as f:
    f.write("# Computational Design of an 8-mer Peptide Binder\n\nDetails coming soon.\n")

with open("LICENSE", "w") as f:
    f.write("MIT License\n\nCopyright (c) 2025")

