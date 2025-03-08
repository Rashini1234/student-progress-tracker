# Student Progress Tracker

## Overview
The **Student Progress Tracker** is a Python-based command-line interface (CLI) system designed to track and manage student performance. The tool allows staff and students to input credit values for **pass**, **defer**, and **fail** categories, categorizing the results into **Progress**, **Progress (module trailer)**, **Do not progress (module retriever)**, or **Exclude**. The system also includes a histogram to visualize the distribution of results and stores the outcomes in a text file for further review.

## Features
- **CLI Interface:** Easy-to-use command-line interface for staff and students to input their credit values.
- **Categorization:** Automatically categorizes student results based on the input credit values into four categories: 
  - **Progress**
  - **Progress (module trailer)**
  - **Do not progress (module retriever)**
  - **Exclude**
- **Histogram:** Generates a histogram to visualize the distribution of outcomes.
- **File Handling:** Stores the results in a text file for later review and analysis.

## Tech Stack
- **Python**
  
## Usage
1. Run the program using Python.
2. Input the credit values for **pass**, **defer**, and **fail**.
3. The program will categorize the results based on predefined criteria:
   - If the total credits sum to 120 and pass value equals 120 with no deferrals or failures, the result will be **Progress**.
   - If the pass value is 100 with deferrals and no failures, the result will be **Progress (module trailer)**.
   - If the pass value is 80 or less with deferrals and failures, the result will be **Do not progress (module retriever)**.
   - If the pass value is 40 or less with fail value being above 80, the result will be **Exclude**.
4. Results will be displayed, and the program will optionally generate a histogram to represent the outcomes.
5. Results will be saved in a text file for further analysis.
