# Data Engineering Portfolio

A curated collection of end-to-end data engineering projects showcasing skills in:

- Python
- Airflow
- APIs & ETL
- Cloud platforms (AWS, GCP)
- SQL & NoSQL databases
- Web scraping
- Data modeling
- Automation

---

## 🔧 Projects

| Project Name | Description | Tools | Highlights |
| ------------ | ----------- | ------ | ---------- |
| [cloud-etl-modernization-airflow-aws](https://github.com/bashoori/cloud-etl-modernization-airflow-aws) | End-to-end Airflow-based ETL pipeline project with mock API data ingestion, transformation, and orchestration on Docker. | Airflow, Python, Docker, Pandas, SQLite, Mockaroo | Auto-ingests ad data, transforms to star schema, runs in dev container with webserver auto-started. |
| [AWS-lambda-linkedin-scraper](./AWS-lambda-linkedin-scraper) | Serverless LinkedIn scraper using AWS Lambda + Python. | AWS Lambda, Python, BeautifulSoup, S3 | Scalable, cost-effective scraping using headless automation. |
| [customer-insights-pipeline](./customer-insights-pipeline) | Customer analytics ETL using Pandas and SQL. | Python, Pandas, SQLite/PostgreSQL, AWS S3 | Unifies multi-source data into star-schema-ready analytics. |
| [ebay-product-tracker](./ebay-product-tracker) | Web scraper tracking product prices and availability over time. | Python, eBay API, SQLite, Pandas | Scheduled collection for historical trend analysis. |
| [healthcare-FHIR-data-pipeline](./healthcare-FHIR-data-pipeline) | ETL pipeline processing synthetic healthcare data from FHIR standard format. | Python, Pandas, SQLite, Synthea | Parses FHIR-compliant records into structured format. |
| [linkedin-job-scraper](./linkedin-job-scraper) | Job listing scraper using Playwright and BeautifulSoup. | Python, Selenium/Playwright, BeautifulSoup | Handles dynamic rendering and pagination. |
| [patient-engagement-pipeline](./patient-engagement-pipeline) | Simulates patient engagement data flow and analytics. | SQL, Python, Tableau | ETL workflows enabling executive-level insights. |
| [pyspark-sales-pipeline](./pyspark-sales-pipeline) | Scalable ETL pipeline using PySpark for sales data. | PySpark, Databricks, Delta Lake, AWS S3 | Modular pipeline for ingesting and transforming sales KPIs. |
| [vitaltrack-wellness-pipeline](./vitaltrack-wellness-pipeline) | ETL and dashboard for personal health tracking data. | Python, Pandas, AWS S3 | Simulates real-time processing of wearable fitness logs. |
| [vpl_scraper](./vpl_scraper) | Python scraper for Vancouver Public Library metadata. | Python, Requests, BeautifulSoup | Offline HTML parsing and Excel export with pandas. |
| [airflow-windows-to-dag-migration](./airflow-windows-to-dag-migration) | Migrates a legacy Windows-scheduled backup script into a modular Apache Airflow DAG using Docker and Python. | Airflow, Python, Docker | Real-world DAG that simulates .bat or .py script automation with volume-mounted file backup. |

---

## 📁 Structure

Each folder is a standalone project with:

- `README.md` explaining the goal
- Scripts / DAGs / notebooks
- Dockerfiles or setup instructions (when applicable)

---

## 🧠 Goals

This portfolio is meant to:

- Demonstrate practical data engineering skills
- Serve as a learning resource for aspiring data engineers
- Showcase hands-on experience with real tools

---

## 🔗 Author

**[Bita Ashoori](https://github.com/bashoori)**  
Connect on [LinkedIn](https://linkedin.com/in/bashoori)
