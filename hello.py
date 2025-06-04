from preswald import connect, get_df, query, table, text, plotly
import plotly.express as px

# Initialize connection
connect()

# Load dataset
df = get_df("vgsales")

# Title and description
text("# 🎮 Video Game Sales Analysis")
text("Explore global video game sales data across platforms, genres, and years")

# Query interesting insights with best-selling games
text("## —Best Selling Games by Platform")
platform_sql = """
    WITH RankedGames AS (
        SELECT 
            Platform,
            Name as Best_Selling_Game,
            CAST(Global_Sales AS FLOAT) as Game_Sales,
            ROW_NUMBER() OVER (PARTITION BY Platform ORDER BY CAST(Global_Sales AS FLOAT) DESC) as rn
        FROM vgsales
    )
    SELECT 
        p.Platform,
        COUNT(*) as Total_Games,
        CAST(SUM(CAST(v.Global_Sales AS FLOAT)) AS DECIMAL(10,2)) as Total_Sales,
        r.Best_Selling_Game,
        CAST(r.Game_Sales AS DECIMAL(10,2)) as Best_Game_Sales
    FROM vgsales v
    JOIN (SELECT DISTINCT Platform FROM vgsales) p ON p.Platform = v.Platform
    JOIN RankedGames r ON r.Platform = p.Platform AND r.rn = 1
    GROUP BY p.Platform, r.Best_Selling_Game, r.Game_Sales
    ORDER BY Total_Sales DESC
"""
platform_stats = query(platform_sql, "vgsales")
table(platform_stats, title="Platform Performance & Best Sellers")

# Create a visualization for genre distribution
text("## Genre Distribution")
genre_sql = """
    SELECT Genre,
           COUNT(*) as Game_Count
    FROM vgsales
    GROUP BY Genre
    ORDER BY Game_Count DESC
"""
genre_data = query(genre_sql, "vgsales")

# Convert query result to DataFrame for plotting
genre_df = genre_data.copy()
fig1 = px.pie(data_frame=genre_df, values='Game_Count', names='Genre', 
              title='Distribution of Games by Genre')
plotly(fig1)

# Time trend visualization
text("## Games Released by Year")
year_sql = """
    SELECT Year,
           COUNT(*) as Games_Released
    FROM vgsales
    WHERE Year IS NOT NULL
    GROUP BY Year
    ORDER BY Year
"""
year_data = query(year_sql, "vgsales")
fig2 = px.line(data_frame=year_data, x='Year', y='Games_Released',
               title='Number of Games Released Each Year')
plotly(fig2)

# Top publishers table
text("## Top Game Publishers")
publisher_sql = """
    SELECT Publisher,
           COUNT(*) as Games_Published,
           CAST(SUM(CAST(Global_Sales AS FLOAT)) AS DECIMAL(10,2)) as Total_Sales
    FROM vgsales
    GROUP BY Publisher
    ORDER BY Total_Sales DESC
    LIMIT 10
"""
publisher_data = query(publisher_sql, "vgsales")
table(publisher_data, title="Top 10 Publishers")

# Footer
text("---")
text("*Created by Prarthan Agarwal*")