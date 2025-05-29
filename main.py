from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from LLM import extract_job_description
import asyncio
import json
from utils import (initialize_driver, 
                   login_to_linkedin, 
                   navigate_to_jobs, 
                   enter_search_criteria, 
                   open_filters_modal, 
                   apply_date_posted_filter,
                   apply_job_type_filter,
                   apply_sort_filter,
                   apply_workplace_type_filter,
                   show_results,
                   click_each_job_list_item,
                   process_job_descriptions,
                   process_job_descriptions_into_Json
                   )

# Configuration
JOB_TITLE = "Full Stack Developer"
LOCATION = "Ahmedabad, India"
SORT_BY_OPTION = "most_recent" # Options: "most_recent", "most_relevant"
DATE_POSTED = "past_month"  # Options: "any_time", "past_month", "past_week", "past_24_hours"
JOB_TYPE = ["Full_Time", "Part_Time"]  # Options: "Full_Time", "Part_Time", "Contract", "Internship"
WORK_PLACE_TYPE = ["On_Site", "Hybrid", "Remote"]  # Options: "On_Site", "Hybrid", "Remote"

def main():
    """Main function to execute the LinkedIn job search automation."""
    json_file_Jds = None 
    # Initialize WebDriver
    driver, wait = initialize_driver()
    
    try:
        # Login to LinkedIn
        login_to_linkedin(driver)
        
        time.sleep(10) # To solve the puzzle

        # Navigate to Jobs section
        navigate_to_jobs(driver)
        
        # Enter search criteria
        enter_search_criteria(driver)
        
        # Open filters modal
        open_filters_modal(driver)
        
        # Apply filters
        apply_sort_filter(driver, sort_by=SORT_BY_OPTION)
        apply_date_posted_filter(driver, date_filter=DATE_POSTED)
        apply_job_type_filter(driver, job_types=JOB_TYPE)
        apply_workplace_type_filter(driver, workplace_types=WORK_PLACE_TYPE)
        
        # Show results
        show_results(driver)

        
        # Click each job list item
        job_descriptions_to_process = click_each_job_list_item(driver)

        # Process job descriptions
        Company_Job_Description = []
        Raw_JD_List = process_job_descriptions(job_descriptions_to_process, Company_Job_Description)

        # convert it into Json
        json_file_Jds = process_job_descriptions_into_Json(Raw_JD_List)
        
    except Exception as e:
        print(f"[ERROR] An error occurred: {e}")
    finally:
        # Close the driver
        driver.quit()
        print("[INFO] Browser closed.")

    return json_file_Jds

if __name__ == "__main__":
    json_file_content = main()

    with open("combined_jobs2.json", "w", encoding="utf-8") as f:
        json.dump(json_file_content, f, indent=4, ensure_ascii=False)

    print("Combined JSON saved to combined_jobs.json")