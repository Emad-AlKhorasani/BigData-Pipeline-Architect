🚀 BigData Pipeline Flow Architect (Kaggle Automation)
🌟 Overview

This project represents a practical Minimum Viable Product (MVP) for a Data Engineer. It automates the link between fetching real-world data via the Kaggle API and documenting system infrastructure. The tool doesn't just draw diagrams; it processes actual data and designs its flow (Data Pipeline).
📸 Execution Evidence

To ensure credibility, here is a screenshot showing the tool successfully fetching and automatically cleaning 26,206 records of e-commerce logs:
🛠️ Tech Stack

    Ingestion Layer: Utilizing kagglehub to fetch raw data.

    Processing Layer: Utilizing Pandas to handle encoding errors and skip corrupted data (Bad lines).

    Architecture-as-Code: A custom engine built with Python to convert YAML files into Mermaid.js diagrams.

🏗️ Planned Pipeline Architecture

The architectural diagram represents a production-grade flow consisting of:

    Apache Kafka: For handling data streams (Stream Buffer).

    Apache Spark: For large-scale transformations and cleaning (ETL).

    HDFS & Hive: For storing data in Parquet format and building a Data Warehouse.

    Metabase/Tableau: For final visual analysis.

📂 Project Files

    main.py: The software engine for generating diagrams.

    data_processor.py: Code for fetching and cleaning data.

    architecture.yaml: The configuration file that defines the system structure.

    requirements.txt: Necessary libraries for operation.


    🚀 Execution
    # Install libraries
    pip install -r requirements.txt

    # Run the tool
    python3 data_processor.py