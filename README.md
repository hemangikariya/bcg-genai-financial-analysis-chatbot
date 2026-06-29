# BCG GenAI Job Simulation

This repository contains my solutions for the **BCG GenAI Job Simulation**. The project focuses on financial data analysis and the development of a rule-based financial chatbot using Python.

---

## Project Overview

The project is divided into two tasks:

### Task 1 – Financial Data Analysis

In this task, financial data was manually extracted from the SEC EDGAR 10-K filings of Microsoft, Apple, and Tesla for the years **2023–2025**.

The extracted data was analyzed using **Python** and **Pandas** to identify financial trends and prepare the dataset for chatbot integration.

### Objectives

- Extract financial data from SEC 10-K reports
- Organize data into CSV format
- Analyze financial performance
- Calculate Year-over-Year (YoY) growth
- Prepare clean data for chatbot development

### Financial Metrics

- Total Revenue
- Net Income
- Total Assets
- Total Liabilities
- Operating Cash Flow

### Technologies Used

- Python
- Pandas
- Jupyter Notebook

---

## Task 2 – Rule-Based Financial Chatbot

The second task involved developing a simple financial chatbot capable of answering predefined financial questions using the analyzed dataset.

The chatbot retrieves information directly from the CSV file and responds using rule-based logic.

### Features

- Revenue lookup
- Net Income lookup
- Operating Cash Flow lookup
- Company financial summary
- Revenue comparison
- Highest Revenue finder
- Highest Net Income finder
- Help menu
- Error handling
- Exit command

### Sample Queries

- What is Microsoft's revenue in 2025?
- What is Apple's net income in 2025?
- Show Tesla operating cash flow in 2025.
- Compare Microsoft and Apple revenue.
- Which company has the highest revenue?
- Which company has the highest net income?
- Microsoft summary

---

## Project Structure

```text
BCG-GenAI/
│
├── Task-1/
│   ├── BCG_Task1.ipynb
│   ├── financial_data.csv
│   └── financial_data_cleaned.csv
│
├── Task-2/
│   ├── chatbot.py
│   ├── financial_data.csv
│   └── requirements.txt
│
└── README.md
```

---

## How to Run

### Task 1

1. Open the Jupyter Notebook.
2. Install the required libraries (if needed).
3. Run all notebook cells.
4. Analyze the generated results.

### Task 2

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the chatbot:

```bash
python chatbot.py
```

---

## Future Improvements

- Natural Language Processing (NLP)
- AI-powered conversational responses
- Web-based chatbot interface
- Data visualization support
- Voice interaction

---
**Hemangi Kariya**

BCG GenAI Job Simulation
