# Internship Request Scraping and Analysis Web App

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Technologies Used](#technologies-used)
6. [Project Structure](#project-structure)

## Introduction
This web application scrapes data from various websites to collect internship requests. It then analyzes this data and presents visual charts to help users gain insights. The application also provides an option to download the analyzed data in XLSX or CSV format for further use.

## Features
- **Data Scraping**: Collects internship request data from specified websites.
- **Data Analysis**: Analyzes the scraped data and generates visual charts.
- **Export Functionality**: Allows users to download the data as XLSX or CSV.
- **Interactive Charts**: Provides dynamic and interactive visualizations.
- **Search Functionality**: Enables users to search and filter data in real-time.

## Installation
Follow these steps to set up the project on your local machine:

### Prerequisites
- Python 3.x
- pip (Python package installer)

### Steps
1. **Clone the Repository**:
    ```bash
    git clone https://github.com/DarkShadowG17/StageScrap
    cd StageScrap
    ```

2. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Application**:
    ```bash
    flask run
    ```

## Usage
1. **Access the Web Application**:
    Open your web browser and go to `http://127.0.0.1:5000`.

2. **Scraping Data**:
    - Log In.
    - Select the wanted site on sites section.

3. **Viewing and Analyzing Data**:
    - Log in to the dashboard.
    - Filter and find specific entries.
    - Visualize the data using the provided charts.

4. **Exporting Data**:
    - Click on the 'Export Data' button.
    - Choose the format (XLSX or CSV) and download the file.

## Technologies Used
- **Backend**: Flask
- **Frontend**: HTML, TailwindCSS, JavaScript, Bootstrap
- **Data Visualization**: ApexCharts, Plotly
- **Data Scraping**: MechanicalSoup, Requests
- **Data Export**: pandas, XlsxWriter, csv

## Project Structure
|   .gitignore
|   app.py
|   package-lock.json
|   package.json
|   README.md
|   requirements.txt
|     
+---models
|   |   csv.py
|   |   scrapMarocAnnonces.py
|   |   scrapMAStage.py
|   |   scrapStagiaires.py
|   |   xlsx.py
|   |   __init__.py
|        
+---node_modules
|                            
+---static
|   +---assets
|   |       chart.js
|   |       constants.js
|   |       dark-mode.js
|   |       index.js
|   |       sidebar.js
|   |       style.css
|   |       
|   +---css
|   |       bootstrap-grid.css
|   |       style.css
|   |       
|   +---dist
|   |   |   main.bundle.js
|   |   |   main.bundle.js.map
|   |   |   main.css
|   |   |   main.css.map
|   |   |   
|   |   \---css
|   |           output.css
|   |           
|   +---images      
|   |       
|   \---js
|           script.js
|           
+---templates
|   |   dashboard.html
|   |   index.html
|   |   
|   +---accounts
|   |       profile.html
|   |       profileChanged.html
|   |       profileError.html
|   |       profileErrorEmail.html
|   |       
|   +---includes
|   |       head.html
|   |       navigation.html
|   |       scripts.html
|   |       sidebar.html
|   |       
|   +---layouts
|   |       base.html
|   |       
|   \---pages
|           marocAnnonces.html
|           stagiaire.html
|           
+---views
|   |   dashboard.py
|   |   downloadCsv.py
|   |   downloadXlsx.py
|   |   graphData.py
|   |   latestData.py
|   |   profile.py
|   |   sites.py
|   |   user.py
|   |   __init__.py
     
