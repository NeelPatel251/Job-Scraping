from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from LLM import extract_job_description, json_file_create
import asyncio

# Configuration
# EMAIL = "basegar197@frisbook.com"
# PASSWORD = "basegar197@123"
JOB_TITLE = "Full Stack Developer"
LOCATION = "Ahmedabad, India"
SORT_BY_OPTION = "most_recent" # Options: "most_recent", "most_relevant"
DATE_POSTED = "past_month"  # Options: "any_time", "past_month", "past_week", "past_24_hours"
JOB_TYPE = ["Full_Time", "Part_Time"]  # Options: "Full_Time", "Part_Time", "Contract", "Internship"
WORK_PLACE_TYPE = ["On_Site", "Hybrid", "Remote"]  # Options: "On_Site", "Hybrid", "Remote"

def initialize_driver():
    """Initialize Chrome WebDriver with options."""
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 10)
    return driver, wait


# def login_to_linkedin(driver):
#     """Login to LinkedIn with provided credentials."""
#     driver.get("https://www.linkedin.com/login")
#     time.sleep(2)
    
#     driver.find_element(By.ID, "username").send_keys(EMAIL)
#     driver.find_element(By.ID, "password").send_keys(PASSWORD + Keys.RETURN)
#     time.sleep(3)
#     print("[INFO] Logged in to LinkedIn.")


def navigate_to_jobs(driver):
    """Navigate to LinkedIn Jobs section."""
    jobs_link = driver.find_element(By.CSS_SELECTOR, 'a[href="https://www.linkedin.com/jobs/?"]')
    jobs_link.click()
    time.sleep(5)
    print("[INFO] Navigated to Jobs section.")


def enter_search_criteria(driver):
    """Enter job title and location in search fields."""
    # Enter Job Title
    job_input = driver.find_element(By.XPATH, "//input[starts-with(@id, 'jobs-search-box-keyword-id-ember')]")
    job_input.clear()
    job_input.send_keys(JOB_TITLE)
    time.sleep(1)
    
    # Enter Location
    location_input = driver.find_element(By.XPATH, "//input[starts-with(@id, 'jobs-search-box-location-id-ember')]")
    location_input.clear()
    location_input.send_keys(LOCATION)
    time.sleep(1)
    location_input.send_keys(Keys.RETURN)
    time.sleep(3)
    print(f"[INFO] Entered search criteria: {JOB_TITLE} in {LOCATION}")


def open_filters_modal(driver):
    """Open the 'All filters' modal."""
    try:
        all_filters_btn = driver.find_element(By.XPATH, "//button[contains(@aria-label, 'Show all filters')]")
        all_filters_btn.click()
        print("[INFO] Clicked 'All filters' button.")
        time.sleep(2)
    except Exception as e:
        print("[ERROR] Error opening filter modal:", e)


def apply_sort_filter(driver, sort_by="most_recent"):
    """Apply sort filter (most recent or most relevant)."""
    SORT_OPTIONS = {
        "most_recent": "advanced-filter-sortBy-DD",
        "most_relevant": "advanced-filter-sortBy-R"
    }

    sort_id = SORT_OPTIONS.get(sort_by.lower())
    if not sort_id:
        print(f"[ERROR] Invalid sort_by value: {sort_by}")
        return

    try:
        sort_radio = driver.find_element(By.ID, sort_id)
        driver.execute_script("arguments[0].click();", sort_radio)
        print(f"[INFO] Selected '{sort_by.replace('_', ' ').title()}' radio button.")
        time.sleep(2)
    except Exception as e:
        print(f"[ERROR] Failed to select '{sort_by}' radio button:", e)


def apply_date_posted_filter(driver, date_filter):
    """Apply date posted filter."""
    DATE_OPTIONS = {
        "any_time": "advanced-filter-timePostedRange-",
        "past_month": "advanced-filter-timePostedRange-r2592000",
        "past_week": "advanced-filter-timePostedRange-r604800",
        "past_24_hours": "advanced-filter-timePostedRange-r86400"
    }

    date_id = DATE_OPTIONS.get(date_filter.lower())
    if not date_id:
        print(f"[ERROR] Invalid date_filter value: {date_filter}")
        return

    try:
        date_radio = driver.find_element(By.ID, date_id)
        driver.execute_script("arguments[0].click();", date_radio)
        print(f"[INFO] Selected '{date_filter.replace('_', ' ').title()}' radio button.")
        time.sleep(2)
    except Exception as e:
        print(f"[ERROR] Failed to select '{date_filter}' radio button:", e)


def apply_job_type_filter(driver, job_types):
    """Apply job type filter (Full-time, Part-time, etc.)."""
    JOB_TYPE_OPTIONS = {
        "Full_Time": "advanced-filter-jobType-F",
        "Part_Time": "advanced-filter-jobType-P",
        "Contract": "advanced-filter-jobType-C",
        "Internship": "advanced-filter-jobType-I"
    }

    for job_type in job_types:
        job_type_id = JOB_TYPE_OPTIONS.get(job_type)
        if not job_type_id:
            print(f"[ERROR] Invalid job_type value: {job_type}")
            continue
        
        try:
            job_type_checkbox = driver.find_element(By.ID, job_type_id)
            driver.execute_script("arguments[0].click();", job_type_checkbox)
            print(f"[INFO] Selected '{job_type.replace('_', ' ').title()}' checkbox.")
            time.sleep(2)
        except Exception as e:
            print(f"[ERROR] Failed to select '{job_type}' checkbox:", e)


def apply_workplace_type_filter(driver, workplace_types):
    """Apply workplace type filter (On-site, Remote, Hybrid)."""
    WORKPLACE_OPTIONS = {
        "On_Site": "advanced-filter-workplaceType-1",
        "Hybrid": "advanced-filter-workplaceType-3",
        "Remote": "advanced-filter-workplaceType-2"
    }

    for workplace_type in workplace_types:
        workplace_id = WORKPLACE_OPTIONS.get(workplace_type)
        if not workplace_id:
            print(f"[ERROR] Invalid workplace_type value: {workplace_type}")
            continue
        
        try:
            workplace_checkbox = driver.find_element(By.ID, workplace_id)
            driver.execute_script("arguments[0].click();", workplace_checkbox)
            print(f"[INFO] Selected '{workplace_type.replace('_', ' ').title()}' checkbox.")
            time.sleep(2)
        except Exception as e:
            print(f"[ERROR] Failed to select '{workplace_type}' checkbox:", e)


def show_results(driver):
    """Click the 'Show Results' button to apply filters."""
    try:
        show_results_btn = driver.find_element(By.XPATH, "//button[@data-test-reusables-filters-modal-show-results-button='true']")
        driver.execute_script("arguments[0].click();", show_results_btn)
        print("[INFO] Clicked 'Show results' button.")
        time.sleep(5)
    except Exception as e:
        print("[ERROR] Failed to click 'Show results':", e)

# def click_each_job_list_item(driver):
#     """Iterate through each job list item and click to open job details."""
#     try:
#         job_list_container = driver.find_element(By.CLASS_NAME, "WUpyIoStvOvEVowQwyIxAwPHVKUSsGnUXU")
#         job_list_items = job_list_container.find_elements(By.XPATH, ".//li[contains(@class, 'scaffold-layout__list-item')]")
#         print(f"[INFO] Found {len(job_list_items)} job list items.")

#         job_descriptions_to_process = []

#         for index, item in enumerate(job_list_items):
#             try:
#                 driver.execute_script("arguments[0].scrollIntoView(true);", item)
#                 time.sleep(1)  
#                 clickable_div = item.find_element(By.CLASS_NAME, "job-card-container") 

#                 driver.execute_script("arguments[0].click();", clickable_div)
#                 print(f"[INFO] Clicked job item #{index + 1}")
#                 time.sleep(2)  # wait for content to load

#                 detail_container = driver.find_element(By.CLASS_NAME, "jobs-search__job-details--container")
#                 job_text = detail_container.text
#                 print(f"[INFO] Extracted raw text for job #{index + 1}")
#                 job_descriptions_to_process.append(job_text)

#             except Exception as e:
#                 print(f"[ERROR] Failed at job item #{index + 1}: {e}")
#                 continue 

#     except Exception as e:
#         print("[ERROR] Could not locate job list container:", e)
    
#     finally:
#         return job_descriptions_to_process

def click_each_job_list_item(driver):
    job_descriptions_to_process = []
    page_number = 1
    total_jobs_scraped = 0

    while True:
        try:
            print(f"\n[INFO] Processing Page #{page_number}")
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "WUpyIoStvOvEVowQwyIxAwPHVKUSsGnUXU"))
            )
            job_list_container = driver.find_element(By.CLASS_NAME, "WUpyIoStvOvEVowQwyIxAwPHVKUSsGnUXU")
            job_list_items = job_list_container.find_elements(By.XPATH, ".//li[contains(@class, 'scaffold-layout__list-item')]")
            print(f"[INFO] Found {len(job_list_items)} job list items on Page #{page_number}")

            for index, item in enumerate(job_list_items):
                try:
                    driver.execute_script("arguments[0].scrollIntoView(true);", item)
                    time.sleep(1)
                    clickable_div = item.find_element(By.CLASS_NAME, "job-card-container")

                    driver.execute_script("arguments[0].click();", clickable_div)
                    print(f"[INFO] Clicked job #{total_jobs_scraped + 1}")
                    time.sleep(2)

                    detail_container = driver.find_element(By.CLASS_NAME, "jobs-search__job-details--container")
                    job_text = detail_container.text
                    job_descriptions_to_process.append(job_text)
                    total_jobs_scraped += 1

                except Exception as e:
                    print(f"[ERROR] Failed to process job item #{index + 1} on Page #{page_number}: {e}")
                    continue

            try:
                next_button = driver.find_element(By.XPATH, "//button[contains(@class, 'jobs-search-pagination__button--next')]")
                if 'artdeco-button--disabled' in next_button.get_attribute("class"):
                    print("[INFO] Reached the last page. No more jobs to scrape.")
                    break
                else:
                    print(f"[INFO] Moving to Page #{page_number + 1}...")
                    driver.execute_script("arguments[0].click();", next_button)
                    time.sleep(3) 
                    page_number += 1

            except Exception as e:
                print("[INFO] No 'Next' button found or failed to click:", e)
                break

        except Exception as e:
            print(f"[ERROR] Could not process jobs on Page #{page_number}:", e)
            break

    print(f"\nFinished scraping. Total jobs scraped: {total_jobs_scraped}")
    return job_descriptions_to_process


def process_job_descriptions(text_list, result_list):

    for i, job_text in enumerate(text_list):
        try:
            print(f"[INFO] Sending job #{i+1} text to LLM...")
            processed = extract_job_description(job_text)
            result_list.append(processed)
        except Exception as e:
            print(f"[ERROR] Failed to process job #{i+1}: {e}")
    return result_list

def process_job_descriptions_into_Json(job_texts):
    
    all_jobs_json = []

    for i, job_text in enumerate(job_texts):
        try:
            print(f"[INFO] Sending job #{i+1} text to LLM again for json...")
            job_json = json_file_create(job_text)
            if job_json is not None:
                all_jobs_json.append(job_json)
        except Exception as e:
            print(f"[ERROR] Failed to parse job #{i}: {e}")
            continue

    return all_jobs_json


