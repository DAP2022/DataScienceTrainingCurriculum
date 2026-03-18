# Possible Projects

**Option A ORFadviser module suite**: Students take their ORFadviser function from M1 and extend it into a full module that: 
1. accepts sequences as file input or user argument,
2. uses NumPy to compute nucleotide composition statistics across a list of sequences,
3. exports results as a CSV readable by pandas, and
4. includes at least one class (e.g., a GeneRecord class with attributes for sequence, ORF status, and translation).
The deliverable is the module, a test notebook demonstrating it on the running sequence, and a 1-page reflection on the design decisions.

**Option B — Comparative data analysis**: Students select a publicly available biological dataset (maternal mortality, ecological survey, gene expression, or their own) and produce a complete analysis notebook that:
1. loads and cleans data with pandas,
2. uses at least two groupby or pivot operations,
3. produces three publication-quality figures with matplotlib,
4. optionally queries a SQLite database they construct from their data.
The deliverable is the annotated notebook exported as a PDF plus a 500-word methods section written as if for a paper. 

**Option C — end-to-end bioinformatics class library**: Students design a small Python package containing at minimum three classes: a GeneRecord class (sequence, gene name, species, with methods for GC content, ORF detection, translation), a ExpressionTable class wrapping a NumPy array with gene names as labels (with methods for row means, column means, and sorting), and a GenomeDatabase class that wraps a SQLite connection and exposes at least two query methods as pandas DataFrames. 
The deliverable is the package directory with an __init__.py, a test notebook demonstrating all three classes on the running sequence and the gene expression data from the course, and a one-page design document explaining the inheritance decisions. This is ambitious!

You are free to suggest your own project of similar effort, and - as usual - if you get stuck, feel free to hand in well explained pseudocode instead of working code. 
