# Tech Talent Market Intelligence Dashboard ETL

This project demonstrates a complete ETL (Extract, Transform, Load) pipeline using Python and SQL. It generates mock job posting data, cleans it, loads it into a SQLite database, and performs analysis.

## Prerequisites

- Python 3.x installed
- pip (Python package manager)

## Setup

1.  **Clone or Download** this project folder.
2.  **Install Dependencies**:
    Open a terminal/command prompt in the project folder and run:
    ```bash
    pip install pandas faker
    ```

## How to Run

1.  **Execute the Pipeline**:
    Run the main script:
    ```bash
    python etl_pipeline.py
    ```

2.  **Check Output**:
    - **Console**: You will see logs for each phase (Generation, Cleaning, Loading, Analysis).
    - **Database**: A `jobs_market.db` SQLite file will be created.
    - **Export**: A `cleaned_jobs_for_dashboard.csv` file will be generated for use in tools like PowerBI.

## Project Structure

- `etl_pipeline.py`: Main Python script containing all ETL logic.
- `jobs_market.db`: Generated SQLite database.
- `cleaned_jobs_for_dashboard.csv`: Exported data for visualization.
