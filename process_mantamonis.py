import pandas as pd

# Load dataset (update the filename if different)
df = pd.read_csv("Mantamonis.csv")

# Filter only the columns we need
df_filtered = df[["contig ID", "Seq Coverage"]]

# Sort by Seq Coverage descending
df_filtered = df_filtered.sort_values(by="Seq Coverage", ascending=False)

# Save the filtered dataset in first_repo
df_filtered.to_csv("filtered_mantamonis.csv", index=False)

