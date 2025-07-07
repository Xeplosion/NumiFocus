# NumiFocus

**NumiFocus** — *Numerical Utility for Money, Investments, Financial Oversight, Capital Utilization & Strategy* — is an intelligent, all-in-one financial assistant designed to bring clarity and control to both personal and investment finances.

It offers robust tools for budgeting, generates detailed reports on transactions and expenditures, and features a neural network-driven engine for analyzing market data and managing investment portfolios. Whether you're tracking daily expenses or optimizing long-term asset strategies, NumiFocus helps streamline financial decision-making through automation, insight, and precision.

---

## Table of Contents

- [NumiFocus](#numifocus)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
    - [Key Features](#key-features)
  - [Features Overview](#features-overview)
    - [1. **Transaction Data Processing \& Report Generation**](#1-transaction-data-processing--report-generation)
    - [2. **Neural Network for Stock and Investment Analysis**](#2-neural-network-for-stock-and-investment-analysis)
    - [3. **Investment Decision Support**](#3-investment-decision-support)
    - [4. **Google Sheets Integration for Real-Time Reporting**](#4-google-sheets-integration-for-real-time-reporting)
    - [Conclusion](#conclusion)
  - [Installation \& Startup](#installation--startup)
    - [1. Clone the Repository](#1-clone-the-repository)
    - [Install Dependencies](#install-dependencies)
    - [Launch NumiFocus](#launch-numifocus)
    - [🔔 Note](#-note)
  - [Getting Started with NumiFocus](#getting-started-with-numifocus)
    - [Uploading Transaction Data](#uploading-transaction-data)
    - [Logging Bills \& Expenses](#logging-bills--expenses)
    - [Report Generation](#report-generation)

---

## Introduction

Welcome to **NumiFocus** — your all-in-one solution for intelligent financial management and stock analysis. NumiFocus combines powerful tools for managing personal budgets, tracking transactions, and generating insightful financial reports, with advanced neural network models for stock evaluation and portfolio optimization. Whether you're looking to optimize your spending, make informed investment decisions, or simply gain deeper insights into your financial situation, NumiFocus offers an intuitive platform to help you achieve your goals.

### Key Features

- **Budgeting & Transaction Tracking:** Easily manage your budget, log transactions, and generate reports to monitor your spending habits.
- **Investment Portfolio Management:** Analyze stocks and optimize portfolios using cutting-edge AI-driven models and financial metrics.
- **Stock Analysis Engine:** Leverage a hybrid multi-modal neural network for evaluating stock performance, profitability, and risk-adjusted returns.
- **Advanced Financial Metrics:** Access a comprehensive suite of financial metrics, including valuation, profitability, momentum, and growth indicators.
- **Customizable Reporting:** Generate tailored reports that suit your needs, with support for recurring data and real-time financial insights.

Whether you're a seasoned investor or just starting, **NumiFocus** helps you make smarter financial decisions with data-driven insights and automation. Let's dive into the features and see how **NumiFocus** can empower your financial strategy.

---

## Features Overview

**NumiFocus** combines powerful tools for personal financial management and advanced stock analysis. Below is an overview of its key features and how they work together to provide users with an intuitive and intelligent platform for managing budgets, tracking transactions, and optimizing investments.

### 1. **Transaction Data Processing & Report Generation**

**NumiFocus** integrates seamlessly with the **Google Drive API** to process transaction data from multiple banks. By uploading data through **Google Forms**, users can easily submit their CSV transaction records and bills paid throughout the month. Here's how it works:

- **Transaction Data Upload:** Users upload their CSV files containing bank transaction data and monthly bills through **Google Forms**.
- **Google Drive API Integration:** The app uses the Google Drive API to retrieve and store these files in a secure, accessible location.
- **Data Formatting:** The transaction data is processed into a consistent format, allowing for easy analysis, filtering, and reporting. NumiFocus ensures that all bank data is standardized for seamless integration and use.
- **Google Sheets API:** Automatically fills out Google Sheets with the processed transaction data. The intuitive interface of Google Sheets then provides an easy-to-use platform for generating custom financial reports, such as:
  - **Spending habits analysis**
  - **Budget recommendations**
  - **Monthly expenditure breakdowns**
  - **Transaction summaries**

This feature makes it simple for users to stay on top of their finances, analyze their spending, and create comprehensive reports without the need for manual data entry or complicated financial software.

---

### 2. **Neural Network for Stock and Investment Analysis**

The heart of **NumiFocus**'s investment analysis tools is its **hybrid multi-modal neural network**, designed to evaluate stocks, estimate returns, and assess various investment parameters. The neural network provides insightful analysis and data-driven predictions based on various financial metrics and technical indicators.

- **Stock Valuation Metrics:** Uses traditional valuation metrics like P/E, P/B, and EV/EBITDA to estimate the underlying value of stocks.
- **Profitability and Efficiency Metrics:** Analyzes profitability (ROE, Gross Margin) and efficiency (Earnings Growth Rate, PEG Ratio, Asset Turnover) to determine a company's financial health.
- **Momentum and Technical Indicators:** Includes analysis of key indicators such as SMA, EMA, RSI, MACD, and Beta, allowing the neural network to forecast stock price momentum and volatility.
- **Risk-Adjusted Return Metrics:** Assesses risk-adjusted returns using metrics like Sharpe and Treynor ratios to help users make informed decisions based on their risk tolerance.
- **Expected Volatility & Investment Outcomes:** The neural network also calculates the **expected volatility** of stocks and estimates the probability of different investment outcomes, aiding users in evaluating the risk and potential return on their investments.

---

### 3. **Investment Decision Support**

NumiFocus takes the guesswork out of stock trading and portfolio management by providing critical data insights and estimates that help users make more informed decisions:

- **Estimated Investment Returns:** The neural network forecasts the likely returns on different types of investments, providing users with expected profit ranges.
- **Probability of Investment Outcomes:** Estimates the probability of various investment outcomes, helping users assess the likelihood of success or failure.
- **Volatility Calculations:** Predicts the expected volatility of investments, offering insights into the potential risks involved.

With these features, **NumiFocus** helps investors optimize their portfolios by analyzing complex data and delivering actionable insights to guide their financial strategies.

---

### 4. **Google Sheets Integration for Real-Time Reporting**

**NumiFocus** also utilizes **Google Sheets API** to streamline data management and reporting. Once the transaction data is processed and uploaded, users can quickly access the data in a **Google Sheet** that provides:

- **Intuitive Report Generation:** Users can easily create custom reports from their transaction data, analyze spending habits, and track monthly budgets.
- **Dynamic Financial Dashboards:** The data is organized in easy-to-read tables that update automatically, allowing for real-time analysis of spending, investments, and financial trends.
- **Budget Recommendations:** Based on the analysis of transaction data, **NumiFocus** generates actionable budget recommendations to help users optimize their spending habits.

---

### Conclusion

With **NumiFocus**, users can easily upload and process their transaction data, analyze their spending habits, and optimize their investment strategies. Through integration with **Google Drive** and **Google Sheets**, the platform simplifies financial tracking and reporting, while the powerful **neural network** delivers deep insights into investment potential, profitability, and risk.

By combining robust data processing, real-time reporting, and advanced AI-driven stock analysis, **NumiFocus** empowers users to take full control of their financial journey.

---

## Installation & Startup

Follow these steps to set up and run **NumiFocus** on your local machine:

### 1. Clone the Repository

```bash
git clone https://github.com/Xeplosion/NumiFocus.git
cd NumiFocus
```

### Install Dependencies

Make sure that you have Python 3.10 or higher installed, then run:

```bash
pip install -r requirements.txt
```

💡 Tip: It's recommended to use a virtual environment to manage dependencies:

```bash
python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate
```

### Launch NumiFocus

Once the dependencies are installed, you can start the application with:

```bash
python main.py
```

### 🔔 Note

To enable budgeting and transaction report features, you’ll need to set up your own Google Cloud project and credentials. If you choose not to, NumiCore will still function normally for portfolio analysis and stock evaluation.

---

## Getting Started with NumiFocus

Getting started with **NumiFocus** is easy and simple. Follow the steps below to set up your environment, upload transaction data, log bills and expenses, and start generating reports. Let’s dive in!

### Uploading Transaction Data

To get started with tracking your transactions and managing your finances, you’ll first need to upload your transaction data. NumiFocus integrates with **Google Forms** for easy submission of CSV transaction records. Here’s how to upload your data:

1. **Prepare Your Transaction CSV Files:**
   - Download or export your bank transaction data and bills from your bank’s online platform.
   - Download one months worth of data at a time, allowing 7 days of overlap for last months pending transactions.
   Example: *from 04-25-2025 to 06-01-2025.*
   - Ensure the data is in CSV format for easy processing.
   - Name the file to match NumiFocus conventions *name_account_date-start_to_date-end.csv*. All text should be lowercase, with hyphens separating the dates.
   Example: *foster_checking_04-25-2025_to_06-01-2025*.

2. **Upload via Google Forms:**
   - Go to the <ins>[**NumiFocus Transaction Data**](https://forms.gle/EE1EpxchkiC3n96L6)</ins> Google Form.
   - Fill in the form and attach your CSV file(s).
   - Submit the form to upload the files.

3. **Automatic Data Processing:**
   - NumiFocus uses the *Google Drive API* to retrieve and process your uploaded files.
   - Your transaction data will be automatically formatted and stored for easy access.

4. **Access Your Data in Google Sheets:**
   - Once the data is processed, it will be available in the <ins>[**Couples Finance**](https://docs.google.com/spreadsheets/d/12skIju98UNf9QH6OCUuMVELN2SOfYZp-ZjK9IQwxFlc/edit?usp=sharing)</ins> Google Sheet document.
   - This allows you to manage and review your transaction data.

---

### Logging Bills & Expenses

To keep track of your regular expenses like bills and subscriptions, follow these steps:

1. **Upload via Google Forms**
   - Navigate to the [**NumiFocus Bills & Expenses**](https://forms.gle/r7oBKnJJpXmgZT8e8) Google Form.
   - Fill out all necessary data.
   - If there is no available option for the bill or expense paid, select *"Other"*. The next time that you use the form, an option will be present.

2. **Access Your Data in Google Sheets:**
   - Once the data is processed, it will be available in the <ins>[**Couples Finance**](https://docs.google.com/spreadsheets/d/12skIju98UNf9QH6OCUuMVELN2SOfYZp-ZjK9IQwxFlc/edit?usp=sharing)</ins> Google Sheet document.
   - This allows you to manage and review your transaction data.

---

### Report Generation

Generating reports from your transaction data has never been easier. Follow these steps to create custom reports and gain insights into your spending:

1. **Access the “Reports” Section:**
   - Reports can be created using the <ins>[**Couples Finance**](https://docs.google.com/spreadsheets/d/12skIju98UNf9QH6OCUuMVELN2SOfYZp-ZjK9IQwxFlc/edit?usp=sharing)</ins> Google Sheet document.

2. **Choose Your Report Type:**
   - Select from various report types, including:
     - **Spending Habits Analysis**
     - **Monthly Expenditure Breakdown**
     - **Budget Recommendations**

3. **Customize Your Report:**
   - Choose the time period (weekly, monthly, or custom date range) for your report.
   - You can filter data by categories such as groceries, rent, and utilities.

4. **View & Download Your Report:**
   - Once the report is generated, you can view it within the Google Sheets page or download it for further analysis.

---

By following these simple steps, you’ll be able to start using **NumiFocus** to manage your finances and investments efficiently. Use the **Google Sheets** integration to track and generate reports based on your uploaded data.
