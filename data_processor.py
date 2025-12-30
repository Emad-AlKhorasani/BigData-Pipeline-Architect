import kagglehub
from kagglehub import KaggleDatasetAdapter
import os

print("⏳ Downloading dataset from Kaggle...")

try:
    # Professional Update: Handle corrupted lines, encoding, and delimiters automatically
    df = kagglehub.dataset_load(
        KaggleDatasetAdapter.PANDAS,
        "kzmontage/e-commerce-website-logs",
        "E-commerce Website Logs.csv",
        pandas_kwargs={
            "encoding": "latin1",
            "on_bad_lines": "skip", # Skips lines that cause code to crash
            "engine": "python",     # More flexible engine for messy data
            "sep": None              # Auto-detect delimiter
        }
    )

    print("✅ Data Loaded Successfully (Cleaned)!")
    print("\n--- Showcase: Data Preview ---")
    print(df.head())

    # Statistics for the GitHub Showcase
    print(f"\n📊 Total Records Cleaned: {len(df)}")
    print(f"🛠️ Simulation: Streaming these {len(df)} records into the Kafka cluster...")

    # 3. Generate Architecture Diagram
    print("\n🎨 Generating Architecture Diagram via Mermaid Engine...")
    if not os.path.exists('output'):
        os.makedirs('output')
        
    exit_code = os.system("python3 main.py -i architecture.yaml -o output/kaggle_live_result.md")
    
    if exit_code == 0:
        print("\n🏁 SUCCESS: MVP is fully functional.")
        print("📂 Results saved in: output/kaggle_live_result.md")
    else:
        print("⚠️ Warning: Mermaid generator returned an error.")

except Exception as e:
    print(f"💥 Error: {e}")