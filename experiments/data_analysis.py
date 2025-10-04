import dask.dataframe as dd
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------------------
# load (auto-detect gzip)
# ---------------------------
df = dd.read_csv(
    "./data/OM-RGC_v2.tsv",  # or .tsv if already unzipped
    sep="\t",
    dtype=str,           # safe for mixed columns
    blocksize="256MB",   # tune for your RAM
    compression="infer"
)

# ---------------------------
# 1) Safe row / column counts
# ---------------------------
# Compute lengths per partition and sum them (works reliably)
partition_lens = df.map_partitions(len).compute()    # array-like of ints (one per partition)
n_rows = int(partition_lens.sum())
n_cols = len(df.columns)

print(f"Rows: {n_rows:,}, Columns: {n_cols}")

# ---------------------------
# 2) Column overview / non-missing counts
# ---------------------------
print("\nColumns:", list(df.columns))

non_missing = df.count().compute()   # OK: per-column non-missing counts
print("\nNon-missing per column:\n", non_missing)

# ---------------------------
# 3) Top taxonomy categories (safe ordering)
# ---------------------------
# Compute the full value_counts into pandas, then take nlargest there
domain_counts = df["Domain"].value_counts(dropna=False).compute()
top_domains = domain_counts.nlargest(10)
print("\nTop Domains:\n", top_domains)

phylum_counts = df["Phylum"].value_counts(dropna=False).compute()
top_phyla = phylum_counts.nlargest(10)
print("\nTop Phyla:\n", top_phyla)

# ---------------------------
# 4) KO annotation coverage example
# ---------------------------
# Count how many rows have a non-missing KO
# (works whether KO column is NaN or empty string; if empty-string is used, handle below)
ko_notnull = df["KO"].notnull().sum().compute()  # counts True values
# if some missing are empty strings, also subtract those:
# string_empty = (df["KO"] == "").sum().compute()
# ko_notnull = ko_notnull - string_empty   # uncomment if necessary

print(f"\nGenes with KO annotation: {ko_notnull:,} / {n_rows:,} "
      f"({100 * ko_notnull / n_rows:.2f}%)")

# ---------------------------
# 5) Plots (use computed pandas Series)
# ---------------------------
plt.figure(figsize=(8, 5))
sns.barplot(x=top_domains.values, y=top_domains.index)
plt.xlabel("Number of genes")
plt.ylabel("Domain")
plt.title("Top 10 Domains")
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))
sns.barplot(x=top_phyla.values, y=top_phyla.index)
plt.xlabel("Number of genes")
plt.ylabel("Phylum")
plt.title("Top 10 Phyla")
plt.tight_layout()
plt.show()
