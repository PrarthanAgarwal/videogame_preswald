# 🎮 Video Game Sales Analysis Dashboard

An interactive data analysis dashboard built with Preswald SDK for exploring and visualizing video game sales data. This project demonstrates the power of Preswald for creating engaging, browser-based data applications.

## Project Overview

This dashboard analyzes the `vgsales.csv` dataset containing information about video game sales across different platforms, regions, genres, and publishers. The application features:

- **5 Interactive Visualizations**
- **Multiple Query Tools**  
- **Dynamic Filtering**
- **Real-time Data Updates**

## Features

### Visualizations

1. **📈 Top 10 Best-Selling Games** - Interactive bar chart showing highest-grossing games
2. **🌍 Regional Sales Trends** - Line chart tracking sales over time by region (NA, EU, JP, Other)
3. **🕹️ Platform Market Share** - Pie chart displaying market share by gaming platform
4. **🎯 Genre Popularity Heatmap** - Genre distribution across top gaming platforms
5. **🏢 Publisher Performance Analysis** - Dual bar charts comparing sales vs. game volume

### Interactive Elements

- **Year Range Slider** - Filter data by time period
- **Platform Selector** - Focus on specific gaming platforms
- **Genre Selector** - Analyze particular game genres
- **Best Game by Year Query** - Find top-selling game for any year
- **Platform Comparison Tool** - Side-by-side platform performance metrics

### Data Insights

- Dataset overview with key metrics
- Summary statistics
- Fun facts and notable findings
- Real-time filtering effects across all visualizations

## 📁 Dataset Structure

The `vgsales.csv` dataset contains the following columns:

- `Rank` - Sales ranking
- `Name` - Game title
- `Platform` - Gaming platform (PS4, Xbox, PC, etc.)
- `Year` - Release year
- `Genre` - Game genre (Action, Sports, RPG, etc.)
- `Publisher` - Publishing company
- `NA_Sales` - North America sales (millions)
- `EU_Sales` - Europe sales (millions)
- `JP_Sales` - Japan sales (millions)
- `Other_Sales` - Other regions sales (millions)
- `Global_Sales` - Total worldwide sales (millions)

## Technical Implementation

### Built With
- **Preswald SDK** - Interactive data app framework
- **Plotly** - Advanced data visualizations
- **Pandas** - Data manipulation and analysis
- **Python** - Core programming language

## 🚀 Getting Started

```bash
pip install preswald
```

   ```bash
   preswald run
   ```

## 🎯 Key Insights from the Data

The dashboard reveals several interesting patterns:

- **Nintendo dominance** in best-selling games
- **Regional preferences** vary significantly
- **Platform lifecycles** clearly visible in sales trends
- **Genre popularity** changes over time
- **Publisher strategies** differ in volume vs. revenue focus
