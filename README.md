![Power BI](https://img.shields.io/badge/PowerBI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge)
![Data](https://img.shields.io/badge/Data-10K%2B%20Records-blue?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)

# 🚦 Route Optimization Project — UK Road Network

A Power BI analytics project exploring congestion patterns, travel times, and road performance across the UK.  
This dashboard helps identify bottlenecks, peak‑hour behaviour, and high‑impact road segments for optimization.

---

## 📊 Dashboard Preview

![Dashboard Screenshot](https://raw.githubusercontent.com/teejay7729/Route-Optimization-UK/refs/heads/master/Visuals/Dashboard.png)

---

## 📚 Table of Contents
- [1. Business Problem](#1-business-problem)
- [2. Dataset Overview](#2-dataset-overview)
- [3. Tools & Techniques Used](#3-tools--techniques-used)
- [🧰 Tech Stack](#-tech-stack)
- [🏗️ Detailed Architecture](#️-detailed-architecture)
- [4. Dashboard Features](#4-dashboard-features)
- [5. Key Insights](#5-key-insights)
- [6. Business Impact](#6-business-impact)
- [7. What I Learned](#7-what-i-learned)

---

## 1. Business Problem

UK road networks experience fluctuating congestion, speed, and travel time depending on:
- Road type  
- Time of day  
- Segment characteristics  
- Traffic volume  

**Objective:**  
Build a dashboard that helps planners and analysts:
- Identify congestion hotspots  
- Understand peak travel times  
- Compare performance across road types  
- Highlight critical segments for optimization  
- Support data‑driven transport decisions  

---

## 2. Dataset Overview

The dataset contains **10,000+ road segment records**, including:
- `segment_id`
- `avg_speed_kmh`
- `avg_travel_time_s`
- `congestion_index`
- `total_trips`
- `HourOfDay`
- `highway` (motorway, primary, living street, etc.)

This enables both **segment‑level** and **time‑of‑day** analysis.

---

## 3. Tools & Techniques Used

### 🔧 Tools
- **Python (VS Code)** — preprocessing, cleaning, Parquet export  
- **Power BI** — data modeling, DAX, visuals  
- **Power Query** — final transformations  

### 📐 Techniques
- ETL pipeline (CSV → Python → Parquet → Power BI)  
- KPI design  
- Interactive slicers  
- Insight storytelling  
- Time‑series analysis  
- Congestion pattern analysis  

---

## 🧰 Tech Stack

**Languages & Processing**
- Python (Pandas, NumPy)
- M Query (Power Query)

**Tools & Environments**
- VS Code (Python scripting, ETL)
- Power BI Desktop (Modeling & Visualization)
- Git & GitHub (Version control)

**Data Formats**
- CSV (raw input)
- Parquet (optimized analytics format)

**Analytics & Modeling**
- DAX (Measures & KPIs)
- Data Modeling (Star schema)
- Power Query Transformations

---

## 🏗️ Detailed Architecture

This project uses a hybrid workflow combining Python preprocessing with Power BI analytics.

┌──────────────────────────────────────────────────────────────┐  
│                        Data Source                           │  
│   • UK Road Segment Dataset (CSV)                            │  
└──────────────────────────────────────────────────────────────┘  
                               │  
                               ▼  
┌──────────────────────────────────────────────────────────────┐  
│                     Python Preprocessing                     │  
│   • VS Code (Python)                                         │  
│   • Pandas for cleaning & transformation                     │  
│   • Outlier handling                                         │  
│   • Feature engineering                                      │  
│   • Export to Parquet for optimized analytics                │  
└──────────────────────────────────────────────────────────────┘  
                               │  
                               ▼  
┌──────────────────────────────────────────────────────────────┐  
│                     Power BI Data Layer                      │  
│   • Import Parquet                                            │  
│   • Power Query for final shaping                             │  
│   • Data model (relationships, star schema)                   │  
│   • DAX measures (KPIs, aggregations)                         │  
└──────────────────────────────────────────────────────────────┘  
                               │  
                               ▼  
┌──────────────────────────────────────────────────────────────┐  
│                     Visualization Layer                      │  
│   • KPI Cards                                                │  
│   • Scatter Plot                                             │  
│   • Map Visual                                               │  
│   • Slicers (Road Type, Hour)                                │  
│   • Insights Panel                                           │  
└──────────────────────────────────────────────────────────────┘  
                               │  
                               ▼  
┌──────────────────────────────────────────────────────────────┐  
│                     Insights & Output                        │  
│   • Congestion hotspots                                      │  
│   • Peak travel times                                        │  
│   • High‑impact segments                                     │  
│   • Recommendations for planners                             │  
└──────────────────────────────────────────────────────────────┘  

---

## 4. Dashboard Features

### 🧮 KPI Summary
![KPI](https://raw.githubusercontent.com/teejay7729/Route-Optimization-Project-UK/refs/heads/master/Visuals/KPI.png)

### 📈 Scatter Chart — Trips vs Congestion
![Scatter](https://raw.githubusercontent.com/teejay7729/Route-Optimization-Project-UK/refs/heads/master/Visuals/Scatter.png)

### 💡 Insights Panel
![Insights](https://raw.githubusercontent.com/teejay7729/Route-Optimization-Project-UK/refs/heads/master/Visuals/Insights.png)

![Insights](https://raw.githubusercontent.com/teejay7729/Route-Optimization-Project-UK/refs/heads/master/Visuals/Insight.png)
### 🎛️ Slicer Panel
![Slicer Effective](https://raw.githubusercontent.com/teejay7729/Route-Optimization-Project-UK/refs/heads/master/Visuals/SlicerEffective.png)

---

## 5. Key Insights

- **Segment 259919** shows high congestion + low speed → major bottleneck.  
- **Segment 282272** appears across multiple metrics → critical route.  
- Congestion peaks **7–9 AM** and **5 PM**, matching commuter patterns.  
- Motorways show **higher travel times during peak hours** despite higher speed limits.  
- Scatter plot reveals a **positive correlation** between trips and congestion with notable outliers.  

---

## 6. Business Impact

This dashboard supports:
- Route optimization  
- Traffic management  
- Infrastructure planning  
- Peak‑hour strategy  
- Resource allocation  

It gives decision‑makers a clear, interactive view of where congestion occurs and why.

---

## 7. What I Learned

- Designing a full analytical story in Power BI  
- Combining KPIs, slicers, and visuals into a cohesive dashboard  
- Extracting insights that matter to stakeholders  
- Structuring a portfolio‑ready BI project  