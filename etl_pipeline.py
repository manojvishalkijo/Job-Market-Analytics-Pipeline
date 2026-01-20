import pandas as pd
import random
from faker import Faker
import sqlite3
import datetime
import re

fake = Faker('en_IN')

def generate_mock_job_data(num_records=500):
    print(f"--- Phase 1: Generating {num_records} mock job records ---")
    
    job_titles = ['Data Analyst', 'Senior Data Analyst', 'Data Scientist', 'Machine Learning Engineer', 
                  'Python Developer', 'Business Analyst', 'Data Engineer', 'Junior Data Analyst']
    
    skills_pool = ['SQL', 'Python', 'Excel', 'Tableau', 'PowerBI', 'AWS', 'Azure', 'Java', 'React', 
                   'Spark', 'Hadoop', 'Machine Learning', 'Statistics', 'Snowflake']
    
    locations = ['Bangalore', 'Bengaluru', 'Pune', 'Hyderabad', 'Mumbai', 'Delhi', 'Remote', 'Gurgaon', 'Noida', 'Chennai']
    
    data = []
    
    for _ in range(num_records):
        job = {
            'job_id': fake.uuid4(),
            'job_title': random.choice(job_titles),
            'company_name': fake.company(),
            'location': random.choice(locations),
            'posted_date': fake.date_between(start_date='-30d', end_date='today'),
        }
        
        if random.random() < 0.15:
            job['salary_range'] = "Not Disclosed"
        else:
            min_sal = random.randint(3, 15)
            max_sal = min_sal + random.randint(2, 10)
            job['salary_range'] = f"₹{min_sal}-{max_sal} LPA"
            
        job_skills = random.sample(skills_pool, k=random.randint(3, 6))
        job['skills_required'] = ", ".join(job_skills)
        
        data.append(job)
        
    df = pd.DataFrame(data)
    print("Data Extraction Complete. Head of raw data:")
    print(df.head(), "\n")
    return df

def clean_job_data(df):
    print("--- Phase 2: Cleaning and Transforming Data ---")
    
    df['location'] = df['location'].str.lower().str.strip()
    df['location'] = df['location'].replace({'bengaluru': 'bangalore'})
    
    def parse_salary(salary_str):
        if pd.isna(salary_str) or "not disclosed" in salary_str.lower():
            return None, None
        
        match = re.findall(r'(\d+)', salary_str)
        if len(match) >= 2:
            return float(match[0]), float(match[1])
        elif len(match) == 1:
            return float(match[0]), float(match[0])
        return None, None

    salary_data = df['salary_range'].apply(lambda x: parse_salary(x))
    df['min_salary'] = [x[0] for x in salary_data]
    df['max_salary'] = [x[1] for x in salary_data]
    
    df['skills_required'] = df['skills_required'].apply(lambda x: ", ".join([s.strip() for s in x.split(',')]))
    
    df.dropna(subset=['job_id'], inplace=True)
    
    print("Transformation Complete. Data types:")
    print(df.dtypes, "\n")
    return df

def save_to_database(df, db_name='jobs_market.db'):
    print(f"--- Phase 3: Loading data into {db_name} ---")
    try:
        conn = sqlite3.connect(db_name)
        df.to_sql('job_postings', conn, if_exists='replace', index=False)
        conn.close()
        print("Data loaded successfully into table 'job_postings'.\n")
    except Exception as e:
        print(f"Error loading database: {e}")

def run_analysis_and_export(db_name='jobs_market.db', output_csv='cleaned_jobs_for_dashboard.csv'):
    print("--- Phase 4: Analysis & Export ---")
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    print("\n[Analysis 1] Top 5 Most Demanded Skills (Processed via Python from DB data):")
    cursor.execute("SELECT skills_required FROM job_postings")
    rows = cursor.fetchall()
    all_skills = []
    for row in rows:
        if row[0]:
            skills = [s.strip() for s in row[0].split(',')]
            all_skills.extend(skills)
            
    from collections import Counter
    top_5_skills = Counter(all_skills).most_common(5)
    for skill, count in top_5_skills:
        print(f"  - {skill}: {count} postings")

    print("\n[Analysis 2] Average Salary for 'Data Analyst' roles (SQL):")
    query_avg_sal = """
    SELECT AVG((min_salary + max_salary) / 2) as avg_package
    FROM job_postings
    WHERE job_title LIKE '%Data Analyst%' 
      AND min_salary IS NOT NULL;
    """
    cursor.execute(query_avg_sal)
    result_avg = cursor.fetchone()
    if result_avg and result_avg[0]:
        print(f"  - Average Package: ₹{result_avg[0]:.2f} LPA")
    else:
        print("  - No salary data available for Data Analysts.")

    print("\n[Analysis 3] Location with highest job postings (SQL):")
    query_loc = """
    SELECT location, COUNT(*) as count
    FROM job_postings
    GROUP BY location
    ORDER BY count DESC
    LIMIT 1;
    """
    cursor.execute(query_loc)
    result_loc = cursor.fetchone()
    if result_loc:
        print(f"  - {result_loc[0].title()} ({result_loc[1]} postings)")

    print(f"\nExporting data to {output_csv}...")
    df = pd.read_sql_query("SELECT * FROM job_postings", conn)
    df.to_csv(output_csv, index=False)
    print("Export Complete.")
    
    conn.close()

if __name__ == "__main__":
    try:
        raw_df = generate_mock_job_data(num_records=500)
        clean_df = clean_job_data(raw_df)
        save_to_database(clean_df)
        run_analysis_and_export()
        print("\n=== ETL Job Completed Successfully ===")
        
    except ImportError as e:
        print("Error: Missing libraries. Please install required packages:")
        print("pip install pandas faker")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
