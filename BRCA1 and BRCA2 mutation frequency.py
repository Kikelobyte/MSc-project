Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import pandas as pd
>>> # Step 1: Load the mutation data
... df = pd.read_csv(r"C:\Users\kikel\Desktop\PROJECT\mutations .csv")
>>> # Inspect the columns
... print("Columns in the file:", df.columns)
Columns in the file: Index(['STUDY_ID', 'SAMPLE_ID', 'BRCA1', 'BRCA2'], dtype='object')
>>> print(df.head())
                       STUDY_ID        SAMPLE_ID BRCA1 BRCA2
0  brca_tcga_pan_can_atlas_2018  TCGA-3C-AAAU-01    WT    WT
1  brca_tcga_pan_can_atlas_2018  TCGA-3C-AALI-01    WT    WT
2  brca_tcga_pan_can_atlas_2018  TCGA-3C-AALJ-01    WT    WT
3  brca_tcga_pan_can_atlas_2018  TCGA-3C-AALK-01    WT    WT
4  brca_tcga_pan_can_atlas_2018  TCGA-4H-AAAK-01    WT    WT
>>> KeyboardInterrupt
>>> # Determine mutation status (anything other than 'WT' is considered a mutation)
... BRCA1_mutated = df['BRCA1'] != 'WT'
>>> BRCA2_mutated = df['BRCA2'] != 'WT'
>>> # Count mutations
... brca1_mut_count = BRCA1_mutated.sum()
>>> brca2_mut_count = BRCA2_mutated.sum()
>>> # Total samples
... total_samples = len(df)
>>> # Calculate frequencies (as percentages)
... brca1_freq = (brca1_mut_count / total_samples) * 100
>>> brca2_freq = (brca2_mut_count / total_samples) * 100
>>> # Print results
... print(f"Total samples: {total_samples}")
Total samples: 994
>>> print(f"BRCA1 mutations: {brca1_mut_count} ({brca1_freq:.2f}%)")
BRCA1 mutations: 27 (2.72%)
>>> print(f"BRCA2 mutations: {brca2_mut_count} ({brca2_freq:.2f}%)")
BRCA2 mutations: 28 (2.82%)
