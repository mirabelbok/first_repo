import pandas as pd

# Load your Excel file (update the filename if needed)
df = pd.read_excel("Mantamonis_bacterial_contamination_analysis.xlsx")

# Filter the dataset to only "contig ID" and "Seq Coverage"
filtered = df[["contig ID", "Seq Coverage"]]

# Sort by "Seq Coverage" in descending order
filtered_sorted = filtered.sort_values(by="Seq Coverage", ascending=False)

# Save to /first_repo as 'filtered_mantamonis.xlsx'
filtered_sorted.to_excel("filtered_mantamonis.xlsx", index=False)
