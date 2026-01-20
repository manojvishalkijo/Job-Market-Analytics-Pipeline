# 📈 Tech Talent Market Intelligence Dashboard

### 🚀 Project Overview
This project is a comprehensive **Data Analytics & Engineering** solution designed to analyze the current landscape of the technology job market. It demonstrates an end-to-end **ETL (Extract, Transform, Load)** pipeline that generates raw job posting data, cleans and standardizes it, stores it in a relational database, and visualizes actionable insights.

The goal of this project is to simulate a real-world business intelligence workflow: taking raw, unstructured data and turning it into strategic insights for job seekers and recruiters.

### 🏗️ Architecture & Workflow
The project follows a structured data pipeline:
1.  **Extraction:** Generated comprehensive mock datasets (simulating web-scraped data) representing 500+ job postings across various domains.
2.  **Transformation (Cleaning):** Utilized **Pandas** to:
    * Parse complex salary strings into min/max numeric values.
    * Standardize location formats.
    * Explode and count skill keywords for frequency analysis.
3.  **Loading:** Designed a schema and loaded processed data into a **SQLite** relational database.
4.  **Analysis & Visualization:** Executed complex SQL queries to extract KPIs and exported data for **Power BI** dashboarding.

### 📊 Key Features
* **Automated Data Generation:** Custom Python script using `Faker` to simulate realistic job market data.
* **Robust Data Cleaning:** Handles missing values, string parsing, and data type conversion to ensure high data quality.
* **SQL Integration:** demonstrative use of SQL for data storage and analytical querying (aggregations, filtering).
* **Business Insights:** answers critical questions such as:
    * *What are the top 5 most in-demand technical skills?*
    * *How does salary correlate with location?*
    * *What is the average salary spread for Data Analysts vs. Developers?*

  <img width="1919" height="974" alt="image" src="https://github.com/user-attachments/assets/6a285ff2-a727-4006-84d2-c83a45b079d9" />
  <img width="1919" height="979" alt="image" src="https://github.com/user-attachments/assets/c439be74-7dd4-4f79-aa9f-b26b13580460" />

### 🛠️ Tech Stack
* **Language:** Python 3.10+
* **Data Manipulation:** Pandas, NumPy
* **Database:** SQLite3 (SQL)
* **Visualization:** Power BI (for dashboarding), Matplotlib (for static plots)
* **Utilities:** Faker (Data Simulation)

### ⚙️ How to Run
1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Vishal/tech-talent-dashboard.git](https://github.com/Vishal/tech-talent-dashboard.git)
    cd tech-talent-dashboard
    ```
2.  **Install dependencies:**
    ```bash
    pip install pandas faker
    ```
3.  **Run the Pipeline:**
    ```bash
    python src/etl_pipeline.py
    ```
    This will generate the database and export the CSV file.

