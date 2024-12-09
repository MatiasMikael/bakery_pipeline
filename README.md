## Bakery Sales Analysis Project

## Introduction
This project analyzes bakery sales data to identify trends, most popular items, least sold items, and sales patterns across different times and days. Tools used include Python, Snowflake, SQL, and Tableau Public, with data sourced from Kaggle.

## Tools Used

* Python
* Visual Studio Code (VS Code)
* Snowflake
* SQL
* Tableau Public

## Steps Followed

1. Downloaded the dataset from Kaggle using the Kaggle API and Python.
2. Loaded the dataset into Snowflake for SQL-based analysis.
3. Wrote SQL queries to analyze sales trends, top and least sold items, and sales by time periods.
4. Created visualizations in Tableau Public for selected insights.
5. Saved additional analysis results as CSV files for reference.

## Visualizations and Outputs

* Top 10 most sold items: Highlights the most popular products based on sales count. (File:`top_10_items.png`)
* Top 10 items sold on weekdays and weekends: Compares product popularity between weekdays and weekends. (File: `top_10_items_by_weekday.png`)
* 20 least sold items: Displays products with the lowest sales figures. (File: `least_sold_20_items.png`)

The following data files were left as CSVs due to their simplicity but are included in the repository:

* `sales_by_weekday_weekend.csv`: Shows total sales for weekdays and weekends.

* `sales_by_period_day.csv`: Summarizes sales by different periods of the day (e.g., morning, afternoon).

* `top_10_items_with_datetime_weekday.csv`: Provides a breakdown of top 10 items by date and weekday-weekend classification.

## License

This project and its contents are shared under the MIT License.
The dataset https://www.kaggle.com/datasets/akashdeepkuila/bakery is publicly available under the CC0: Public Domain license.

