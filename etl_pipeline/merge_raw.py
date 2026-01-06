from etl_pipeline.extract_source1 import extract_source1
from etl_pipeline.extract_source2 import extract_source2

# Extract per sumber (RAW)
df_csv_raw = extract_source1()
df_hf_raw = extract_source2()

# GABUNG RAW DATA (BELUM CLEANING)
df = pd.concat(
    [df_csv_raw, df_hf_raw],
    ignore_index=True
)

print("=== DATA GABUNGAN (AWAL TRANSFORM) ===")
print(f"Total baris : {df.shape[0]:,}")
print(f"Total kolom : {df.shape[1]}")

df.head()

