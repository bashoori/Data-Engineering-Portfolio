<p align="center">
  <img src="https://avatars.githubusercontent.com/u/72375349?v=4" width="140" />
</p>

# 💼 Bita Ashoori | Data Engineering Portfolio

## 👩‍💻 About Me
I'm a Data Engineer based in Vancouver with over 5 years of experience across data engineering, BI, and analytics. I'm passionate about clean architecture, automation, and helping organizations turn data into meaningful decisions. I'm currently expanding my knowledge in AI and machine learning to complement my strong data pipeline and cloud engineering background.

Welcome! I'm a Data Engineer with over 3 years of experience building and maintaining cloud-based data pipelines, and another 2+ years working as a Business Intelligence Developer and Data Analyst. I have experience in transforming raw data into actionable insights using Python, SQL, AWS (S3, Redshift, Lambda), and Apache Airflow.  

I have a strong track record designing ETL workflows that integrate data from APIs, JSON, and relational databases—delivering scalable, automated, and reliable data solutions. My background in BI and analytics enables me to bridge the gap between technical implementation and business needs, translating complex requirements into efficient data systems within agile environments.  

I'm passionate about solving large-scale data problems through clean architecture, real-time insights, and automation—and enabling organizations to extract true value from their data.

---

## 🚀 Projects

### 🛠️ Airflow AWS Modernization  
[🔗 View Project](https://github.com/bashoori/data-engineering-portfolio/tree/main/airflow-aws-modernization)  
![Airflow](https://img.shields.io/badge/Airflow-017CEE?style=flat&logo=apache-airflow&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-232F3E?style=flat&logo=amazon-aws&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)  
Migrated legacy Windows Task Scheduler jobs into modular Airflow DAGs with Docker and AWS S3.  
This project improves maintainability and scalability of previously manual and error-prone batch processes. It leverages Docker containers to simulate production workflows in a local dev environment.

<p align="center">
  <img src="https://raw.githubusercontent.com/bashoori/repo/master/airflow-aws-modernization/etl2.png" alt="Airflow AWS Diagram" width="700" style="border: 1px solid #ccc; border-radius: 6px;" />
</p>

---

### ⚡ Real-Time Marketing Pipeline  
[🔗 View Project](https://github.com/bashoori/data-engineering-portfolio/tree/main/real-time-marketing-pipeline)  
![PySpark](https://img.shields.io/badge/PySpark-E34F26?style=flat&logo=apachespark&logoColor=white)
![Databricks](https://img.shields.io/badge/Databricks-E0214E?style=flat&logo=databricks&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat&logo=github-actions&logoColor=white)  
Real-time campaign ETL with PySpark and Databricks, deployed via GitHub Actions.  
Built to simulate real-time ingestion of ad data, this pipeline automates scheduling and deployment via CI/CD, ensuring quick feedback loops and error handling.

<p align="center">
  <img src="https://raw.githubusercontent.com/bashoori/repo/master/real-time-marketing-pipeline/image1.png" alt="Real-Time Pipeline Diagram" width="700" style="border: 1px solid #ccc; border-radius: 6px;" />
</p>

---

### ☁️ Cloud ETL Modernization  
[🔗 View Project](https://github.com/bashoori/data-engineering-portfolio/tree/main/cloud-etl-modernization-airflow-aws)  
![Airflow](https://img.shields.io/badge/Airflow-017CEE?style=flat&logo=apache-airflow&logoColor=white)
![Redshift](https://img.shields.io/badge/AWS_Redshift-4053D6?style=flat&logo=amazon-redshift&logoColor=white)
![CloudWatch](https://img.shields.io/badge/AWS_CloudWatch-FF4F8B?style=flat&logo=amazon-aws&logoColor=white)  
Rebuilt legacy ETL workflows on Airflow + AWS for scalable processing and monitoring.  
Implements data quality checks and logging to CloudWatch for better observability. Redshift is used as the destination warehouse with SQL-based transformations.

<p align="center">
  <img src="https://raw.githubusercontent.com/bashoori/repo/master/cloud-etl-Modernization/etl31.png" alt="Cloud ETL Diagram" width="700" style="border: 1px solid #ccc; border-radius: 6px;" />
</p>

---

### 🏥 FHIR Healthcare Pipeline  
[🔗 View Project](https://github.com/bashoori/data-engineering-portfolio/tree/main/healthcare-FHIR-data-pipeline)  
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![FHIR](https://img.shields.io/badge/FHIR-DF3E51?style=flat&logo=fhir&logoColor=white)  
Parsed synthetic FHIR-compliant patient data into structured tables using Python.  
This project mimics real-world healthcare data ingestion, processing FHIR JSON into relational models to support downstream analysis and dashboarding.

<p align="center">
  <img src="https://raw.githubusercontent.com/bashoori/repo/master/healthcare-FHIR-data-pipeline/etl4.png" alt="FHIR Pipeline Diagram" width="700" style="border: 1px solid #ccc; border-radius: 6px;" />
</p>

---

### 🔍 LinkedIn Scraper (Lambda)  
[🔗 View Project](https://github.com/bashoori/data-engineering-portfolio/tree/main/linkedIn-job-scraper)  
![AWS Lambda](https://img.shields.io/badge/AWS_Lambda-FF9900?style=flat&logo=amazon-aws&logoColor=white)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-2C8EBB?style=flat&logo=python&logoColor=white)  
Serverless job scraper storing results in AWS S3.  
Built with Lambda, this solution automates job search scraping from LinkedIn using headless requests and parses results to structured CSV for storage and downstream use.

<p align="center">
  <img src="https://raw.githubusercontent.com/bashoori/repo/master/linkedIn-job-scraper/etl5.png" alt="LinkedIn Scraper Diagram" width="700" style="border: 1px solid #ccc; border-radius: 6px;" />
</p>

---

### 📈 PySpark Sales Pipeline  
[🔗 View Project](https://github.com/bashoori/data-engineering-portfolio/tree/main/pyspark-sales-pipeline)  
![PySpark](https://img.shields.io/badge/PySpark-E34F26?style=flat&logo=apachespark&logoColor=white)
![Delta Lake](https://img.shields.io/badge/Delta_Lake-0F9D58?style=flat&logo=databricks&logoColor=white)
![S3](https://img.shields.io/badge/S3-569A31?style=flat&logo=amazon-aws&logoColor=white)  
Built a scalable ETL pipeline to ingest, clean, and report on high-volume sales KPIs.  
It uses Delta Lake for efficient storage and query performance, while PySpark automates transformation logic and outputs analytics-ready datasets.

<p align="center">
  <img src="https://raw.githubusercontent.com/bashoori/repo/master/pyspark-sales-pipeline/etl6.png" alt="PySpark Pipeline Diagram" width="700" style="border: 1px solid #ccc; border-radius: 6px;" />
</p>

---

I'm also an AI enthusiast, continuously exploring how machine learning and artificial intelligence can enhance automation, prediction, and decision-making in data workflows.

## 📁 About This Portfolio

Each project folder includes:
- A `README.md` with description and structure
- Working code and workflows
- Docker or deployment steps
- Sample output or visual diagrams when applicable

---

## 📌 Featured

📄 [Download My Resume](./bita_ashoori_resume.pdf)  
🚀 Currently exploring ML model deployment and real-time analytics use cases.  
📬 Open to freelance and full-time remote opportunities.

---

## 📫 Contact Me

📍 Vancouver, Canada  
🔗 [LinkedIn](https://linkedin.com/in/bashoori)  
💻 [GitHub](https://github.com/bashoori)
