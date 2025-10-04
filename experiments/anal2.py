# ======================================
# 1. Cargar librerías
# ======================================
import dask.dataframe as dd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np

# Configuración visual
sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)
'''
# ======================================
# 2. Cargar datos grandes con Dask
# ======================================
# Cambia la ruta al archivo correcto
df = dd.read_csv("./data/OM-RGC_v2.tsv", 
                 sep="\t", 
                 dtype=str,  # todo como string al inicio
                 blocksize="256MB")  # ajusta según RAM

# ======================================
# 3. Estadísticas básicas
# ======================================
# Número de filas y columnas
n_rows, n_cols = df.shape
print("Número de filas:", n_rows)
print("Número de columnas:", n_cols)

# Porcentaje de genes con anotación KO
total_genes = n_rows
genes_with_KO = df["KO"].notnull().sum().compute()
pct_with_KO = (genes_with_KO / total_genes) * 100
print(f"Genes con anotación KO: {pct_with_KO:.2f}%")

# Número de KOs únicos
unique_KOs = df["KO"].nunique().compute()
print("Número de KOs únicos:", unique_KOs)

# ======================================
# 4. KO más frecuentes
# ======================================
top_kos = (
    df["KO"]
    .value_counts()
    .nlargest(20)   # top 20
    .compute()
)

plt.figure(figsize=(12, 6))
sns.barplot(x=top_kos.values, y=top_kos.index, palette="viridis")
plt.title("Top 20 KOs más frecuentes")
plt.xlabel("Frecuencia")
plt.ylabel("KO")
plt.show()

# ======================================
# 5. Histograma de longitud de secuencias
# ======================================
# ⚠️ Si 'sequence' está incluida, puede ser muy pesado. 
# Aquí medimos longitud de secuencia de una muestra
sample_sequences = df["sequence"].sample(frac=0.001).compute()  # 0.1% del dataset
seq_lengths = sample_sequences.str.len()

sns.histplot(seq_lengths, bins=50, kde=False)
plt.title("Distribución de longitudes de genes (muestra 0.1%)")
plt.xlabel("Longitud de secuencia (nt)")
plt.ylabel("Frecuencia")
plt.show()
'''
# ======================================
# 6. PCA exploratoria en perfiles
# ======================================
# Esto requiere usar un archivo de "gene_profile_metaG.tsv.gz" o similar
# Ejemplo con un subset para PCA

profiles = dd.read_csv("./data/gene_profile_metaG.tsv", 
                       sep="\t", 
                       blocksize="256MB",
                       dtype={'TARA_A100001035': 'float64',
                                'TARA_A100001037': 'float64',
                                'TARA_A100001234': 'float64',
                                'TARA_A100001388': 'float64',
                                'TARA_B000000460': 'float64',
                                'TARA_B000000565': 'float64',
                                'TARA_B100000003': 'float64',
                                'TARA_B100000123': 'float64',
                                'TARA_B100000131': 'float64',
                                'TARA_B100000161': 'float64',
                                'TARA_B100000212': 'float64',
                                'TARA_B100000242': 'float64',
                                'TARA_B100000282': 'float64',
                                'TARA_B100000378': 'float64',
                                'TARA_B100000424': 'float64',
                                'TARA_B100000513': 'float64',
                                'TARA_B100000674': 'float64',
                                'TARA_B100000683': 'float64',
                                'TARA_B100000749': 'float64',
                                'TARA_B100000767': 'float64',
                                'TARA_B100000768': 'float64',
                                'TARA_B100000780': 'float64',
                                'TARA_B100000787': 'float64',
                                'TARA_B100000795': 'float64',
                                'TARA_B100000809': 'float64',
                                'TARA_B100000886': 'float64',
                                'TARA_B100000900': 'float64',
                                'TARA_B100000927': 'float64',
                                'TARA_B100000989': 'float64',
                                'TARA_B100001027': 'float64',
                                'TARA_B100001105': 'float64',
                                'TARA_B100001115': 'float64',
                                'TARA_B100001121': 'float64',
                                'TARA_B100001146': 'float64',
                                'TARA_B100001245': 'float64',
                                'TARA_B100001248': 'float64',
                                'TARA_B100001939': 'float64',
                                'TARA_B100001971': 'float64',
                                'TARA_B100001989': 'float64',
                                'TARA_B100002003': 'float64',
                                'TARA_B110000027': 'float64',
                                'TARA_B110000037': 'float64',
                                'TARA_B110000046': 'float64',
                                'TARA_B110000090': 'float64',
                                'TARA_B110000091': 'float64',
                                'TARA_B110000093': 'float64',
                                'TARA_B110000114': 'float64',
                                'TARA_B110000116': 'float64',
                                'TARA_B110000196': 'float64',
                                'TARA_B110000208': 'float64',
                                'TARA_B110000211': 'float64',
                                'TARA_B110000238': 'float64',
                                'TARA_B110000240': 'float64',
                                'TARA_B110000259': 'float64',
                                'TARA_B110000261': 'float64',
                                'TARA_B110000263': 'float64',
                                'TARA_B110000285': 'float64',
                                'TARA_B110000444': 'float64',
                                'TARA_B110000459': 'float64',
                                'TARA_B110000483': 'float64',
                                'TARA_B110000495': 'float64',
                                'TARA_B110000503': 'float64',
                                'TARA_B110000858': 'float64',
                                'TARA_B110000879': 'float64',
                                'TARA_B110000881': 'float64',
                                'TARA_B110000902': 'float64',
                                'TARA_B110000908': 'float64',
                                'TARA_B110000914': 'float64',
                                'TARA_B110000967': 'float64',
                                'TARA_B110000971': 'float64',
                                'TARA_B110000977': 'float64',
                                'TARA_B110001452': 'float64',
                                'TARA_B110001454': 'float64',
                                'TARA_B110001469': 'float64',
                                'TARA_Y100000031': 'float64',
                                'TARA_Y100000287': 'float64'})
print("lectura finalizada")
# Tomar muestra manejable
profiles_sample = profiles.sample(frac=0.01).compute()  # 1% de los datos
profiles_sample = profiles_sample.dropna(axis=1, how="any")

# Estandarizar
X = StandardScaler().fit_transform(profiles_sample.iloc[:, 1:])  # asumiendo col 0 es gene_id

pca = PCA(n_components=2)
coords = pca.fit_transform(X)
print("hola")
plt.scatter(coords[:,0], coords[:,1], alpha=0.5)
plt.title("PCA exploratoria (subset)")
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.show()
'''
# ======================================
# 7. Heatmap de KOs principales en muestras
# ======================================
# Tomamos una tabla KO_metaG_norm.tsv.gz (ejemplo)
ko_profile = dd.read_csv("KO_metaG_norm.tsv.gz", sep="\t", blocksize="256MB")

# Convertir a pandas (solo top 50 KOs para no colapsar RAM)
ko_df = ko_profile.set_index("KO").compute()
top50 = ko_df.sum(axis=1).nlargest(50).index
heatmap_data = ko_df.loc[top50]

sns.heatmap(np.log1p(heatmap_data), cmap="mako")
plt.title("Heatmap de los 50 KOs más abundantes (log transformados)")
plt.xlabel("Muestras")
plt.ylabel("KO")
plt.show()
'''