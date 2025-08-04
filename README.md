# Computational Design of an 8-mer Peptide Binder Targeting 5-Hydroxyisourate Hydrolase (PDB ID: 2H6U) Using AfDesign

**Author**: Isarar Siddique  
**Keywords**: AfDesign, AlphaFold2, Peptide Design, PyRosetta, 2H6U, Protein-Peptide Interaction

---

## 🧬 1. Introduction
Peptide therapeutics offer specificity, lower immunogenicity, and rapid development pipelines. In this project, we use **AfDesign**, a peptide hallucination tool based on AlphaFold2, to design an 8-residue peptide binder against 5-hydroxyisourate hydrolase (HIUHase, PDB ID: 2H6U), a target in uric acid degradation.

---

## 🎯 2. Objective
- Design an 8-mer peptide binder using AfDesign.
- Target selected surface-accessible residues on chain A of 2H6U.
- Evaluate binding using AlphaFold2 confidence metrics.
- Optimize peptide torsions via PyRosetta energy minimization.

---

## 🧾 3. Target Protein: 5-Hydroxyisourate Hydrolase

| Feature          | Details                            |
|------------------|-------------------------------------|
| PDB ID           | 2H6U                                |
| Organism         | *Danio rerio* (Zebrafish)          |
| Chain            | A                                  |
| Role             | Uric acid degradation               |
| Hotspot Residues | 10, 11, 52–54, 103, 119             |

---

## 🛠️ 4. AfDesign Setup

| Parameter       | Value      |
|----------------|------------|
| Peptide Length | 8 residues |
| Hotspot Residues | Selected from 2H6U Chain A |
| Recycles       | 0 |
| Multimer       | No |
| Output Models  | 2 |

> Designed Sequence: **LNITARAY**

---

## 📈 5. AlphaFold2 Evaluation

| Metric        | Value   | Interpretation                       |
|---------------|---------|--------------------------------------|
| pLDDT         | 0.9066  | Very high local confidence            |
| PAE (global)  | 0.1325  | Low alignment error                   |
| iPTM          | 0.8886  | Strong peptide-protein interaction    |
| Interface Contacts | 2.074 | Good binding interface              |

---

## 🧪 6. Structural Evaluation

- The peptide binds adjacent to the β-barrel groove of HIUHase.
- Interacts with hotspots (residues 52–54, 103).
- Exhibits stable loop conformation.
- No steric clashes observed in AF2 predictions.

---

## 🔧 7. PyRosetta Backbone Optimization

We used 3 methods for φ/ψ angle optimization:
- **Greedy Search**
- **Metropolis Monte Carlo**
- **Monte Carlo + MinMover**

📁 Code: `pyrosetta_optimization/`

| Method             | Lowest Energy (REU) |
|--------------------|---------------------|
| Greedy             | 1635.71             |
| Metropolis MC      | 1095.79             |
| MC + MinMover      | 16.98               |

> MC + MinMover yielded the best energy minimization.

---

## 📊 8. Visual Comparison

All structures were visualized in PyMOL. Overlay shows best compaction and folding for **MC + MinMover** optimized peptide.

![Structure Comparison](images/structure_comparison.png)

---

## 🔬 9. Applications

- Functional inhibition of HIUHase
- Fluorescent probes for diagnostics
- Benchmark for peptide hallucination pipelines
- Synthetic biology tags

---

## ✅ 10. Conclusion

This project successfully demonstrates the in silico design of a high-confidence peptide binder using AfDesign and PyRosetta optimization. The peptide **LNITARAY** can be synthesized for in vitro validation and therapeutic evaluation.

---

## 📚 11. References

1. Jumper et al. (2021). AlphaFold. *Nature*, 596(7873), 583–589.  
2. Anishchenko et al. (2021). Hallucination design. *Nature*, 600(7889), 547–552.  
3. Chaudhury et al. (2010). PyRosetta. *Bioinformatics*.  
4. PDB Entry: [2H6U](https://www.rcsb.org/structure/2H6U)  

---

## 🗂️ Folder Structure

```bash
afdesign-peptide-2H6U/
├── README.md
├── afdesign_outputs/
│   ├── model_1.pdb
│   └── model_2.pdb
├── pyrosetta_optimization/
│   ├── greedy.py
│   ├── metropolis_mc.py
│   ├── mc_minmover.py
│   ├── low.pdb
│   ├── low2.pdb
│   ├── low3.pdb
├── data/
│   └── target_2H6U.pdb
├── images/
│   └── structure_comparison.png
└── LICENSE
✨ Acknowledgments
AlphaFold & AfDesign authors

RosettaCommons and PyRosetta

Structural Biology & Bioinformatics Community

📬 Contact
Isarar Siddique
📧 isararsiddique@gmail.com
🌐 LinkedIn | ORCID

