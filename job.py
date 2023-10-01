from jobspy import scrape_jobs
import pandas as pd
import datetime

def getJob():
    job_name = input("Job name : ")
    country = input("Country : ")
    location = input("Location : ")
    results_wanted = input("Number of results you want : ")

    jobs: pd.DataFrame = scrape_jobs(
        site_name=["indeed", "linkedin"],
        search_term=job_name,
        location=location,
        results_wanted=results_wanted,
        country_indeed=country  # only needed for indeed
    )

    # formatting for pandas
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 50)  # set to 0 to see full job url / desc

    jobs.to_csv(f'jobs_{datetime.datetime.now().strftime("%Y-%m-%d")}.csv', index=False)
    jobs.to_excel(f'jobs_{datetime.datetime.now().strftime("%Y-%m-%d")}.xlsx', index=False)
