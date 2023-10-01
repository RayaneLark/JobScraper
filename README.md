# JobScraper Script

## Overview

The JobScraper script is a Python-based tool that allows users to search and retrieve job postings from two popular job listing platforms: **Indeed** and **LinkedIn**. This script is designed to streamline the process of finding job opportunities for a specific job position in a specified location. It can automatically gather job listings, format the data, and send the results to an email address.

## Key Features

### 1. Initial Setup

1. Create a `.env` file: Before using the script, you need to create a `.env` file to securely store your email credentials. The `.env` file should contain the following information:

    EMAIL_SENDER=your_email@gmail.com
    EMAIL_PASSWORD=your_email_password
    EMAIL_RECEIVER=recipient_email@example.com


    Replace `your_email@gmail.com` with your Gmail address and `your_email_password` with the **App Password** or **OAuth2 Token** generated for your Gmail account. Storing your email credentials in the `.env` file ensures their security.

2. Run the command ```pip install -r requirements.txt``` to install all the dependecies used in the script.


### 2. Input Parameters

- **Job Name:** The user is prompted to enter the job title or position they are interested in.
- **Country:** The desired country or location for job searching.
- **Location:** The specific location or city for job searching.
- **Number of Results:** The user can specify the number of job listings they want to retrieve.

### 3. Data Scraping

- The script utilizes the 'jobspy' library to scrape job postings from LinkedIn and Indeed.
- It sends a search query to both platforms, collects job listings, and compiles the results.

### 4. Data Formatting

- The scraped job data is structured into a pandas DataFrame for easy manipulation.
- The script formats the output for better readability.

### 5. Saving Results

- The script saves the job listings as both a CSV (Comma-Separated Values) file and an Excel file (XLSX).
- The file names include the current date to organize the data.

### 6. Email Notification

- The script sends an email notification to the user.
- It includes a subject line mentioning the date of the job search.
- The email body provides a brief message with instructions on accessing the attached job listings.

## Usage

1. Create a .env file an put your email and password.
2. Execute the command ```pip install -r requirements.txt```
3. Run the file ```setup.py```.
4. Provide input parameters, including the job name, country, location, and the number of results desired.
5. The script will perform the following steps:
   - Scrape job postings from LinkedIn and Indeed.
   - Structure the data into a DataFrame.
   - Save the data as CSV and Excel files.
   - Send an email notification with attached files.
6. Check your email for the job listings and access the attachments.

## Dependencies

- **Python:** The script is written in Python, so you need a Python environment to run it.
- **jobspy Library:** Used for web scraping job postings.
- **pandas Library:** Used for data manipulation and formatting.
- **openpyxl Library:** Used for handling Excel files.
- **smtplib Library:** Used for sending emails.
- **decouple Library:** Used for managing sensitive data like email credentials.

## Notes

- Ensure that you have the necessary libraries installed before running the script.
- Review the email configuration to ensure successful delivery.


Happy job hunting!
