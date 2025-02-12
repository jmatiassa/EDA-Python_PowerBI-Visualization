# EDA-Python_PowerBI-Visualization
EDA|PYTHON|DATA CLEANING|PANDAS|VISUALIZATION|POWER BI|

## Content:
### Project purpose
This project is a demonstration of analytical skills to transform raw data into actionable insights that can help make valuable business decisions. A sales dataset from a retail company that sells technological products, such as smartphones, laptops, and so on, is going to be analyzed. The hard skills that are relevant to this project are the use of the pandas library in Python and the use of Power BI as a business intelligence tool.

### EDA in Python
Below there is going to be explained the process that has been followed to transform the data:

1. Raw data:
The main datasource of this project is Sales Data.csv. This dataframe is a mock dataframe that has been downloaded from kaggle in order to practice. The columns are:
- Order ID: ID of each transaction
- Product: The item sold
- Quantity ordered: amount of units sold
- Price each: unit price
- Order date: date of the sale
- Purchase address: the address of the sale
- Month: number of the month
- Sales: amount of the sale
- City: name of the city
- Hour: hour when the product was sold
2. Transforming the data:

  Data has been transformed in order to adjust it to the purpose of the analysis. The steps followed are the next:
  
1. Drop duplicates
2. Date column to datetime
3. Change Price Each into Unit Price
4. Transform adress column into separate columns: Adres Number, Street, City, State, Zip Code

This work is done in 1Transforming.ipynb file and the output is sales_transformed.csv

3. Merge data with the product category dataset

In order to provide more data and show more transformation options in Pandas it has been created a dataset that contains the product categories that every product has.
This work is done in 2Merge.ipynb file and the output is DataMerged.c

4.Statistics

Before the analysis in power bi it has been created a preeliminar analysis that determines the causalities between variables and inferential statistics. These results will determine the perspective of the analysis of the power bi dashboard.
The analysis are:
- Anova analysis of categorical variables:Conclussions of the analysis: The type of product, product category and Hour have significative impact on the sales. Analysing these variables may have impact on optimizing the revenue
- Preelliminar calculation of some metrics and dashboard design
The work is done in 3Statistics.ipynb file and the outputs are Sales_BI.csv and anova_stats.csv

### Dashboard visualization in Power BI

There have been implemented 2 use cases in Power bi: sales overview and profitability analysis.

#### Sales overview:

In sales overview there is the general information that shows the evolution of the sales of the company and the main caracteristics of this.

Kpis: 

1.1 Total Revenue: Sum of the revenue of the sales
1.2 Total Aquisition Cost: Sum of the cost of the units sold
1.3 Total Gross Profit: Difference between Total Revenue and Total aquisition cost
1.4 %Gross Margin: Expression of total gross profit in %
2.1 Nº Sales: Nº of transactions completed
2.2. Nº Units Sold: Nº of units that have been sold
2.3 Nº Units per Sale: Mean of the number of units that have been sold per transaction in average
2.4 Avg Gross Profit per Sale:

Distributions:

1.1 Temporal evolution of sales
1.2 Nº Sales per Hour
1.3 Statistical significance on Sales
2.1 Nº Sales by Product Category
2.2 Nº Sales by Category
2.3 Geographical Sales Map

#### Sales profitability:

In sales profitability there is the general informmation that shows the informarion about the profitability streams of the company. According to the analysis of which were the variables that most affect to revenue, the distributions have been created to discover insights that can have impacto on business.

Kpis:

1.1 Total Revenue: Sum of the revenue of the sales
1.2 Total Aquisition Cost: Sum of the cost of the units sold
1.3 Total Gross Profit: Difference between Total Revenue and Total aquisition cost
1.4 %Gross Margin: Expression of total gross profit in %
2.1 Nº Sales: Nº of transactions completed
2.2. Aavg Gross Profitper unit:Mean of the profit that every unit is generating
2.3 Avg Gross Profit per Sale: Mean of the profit that every transaction is generating
2.4 Avg Gross Profit per month: Mean of the profit that the company is generating per month

Distributions:
1.1 Gross Profit by Hour
1.2 Temporal distribution of Gross Margin per Unit
1.3 Distriburion of Product Category by Gross margin per unit
2.1 Distribution of Profitability by Product Category
2.2 Distribution of Profitability by Product
2.3 Distribution of Product by gross margin per unit


#### Filter Panel:

In addition to the dashboards it has been created a filter panel where can be applied dynamic filters. This filter page has been created with markdowns for both pages.

Filters:

- Date
- Hour
- Product Category
- Product
- State
- City


### Analysis of the results

In order to show the functionality it has been conducted an analysis so that it can be validity of the bi tool demonstrated.


Objective of the analysis: determine how can the retail company increase their profitability over the time.

#### Descriptive analysis

The retail company has been selling technological products for one year, from Ganuary 2019 to Genuary 2020. During this period of time it has reached the following results:

- Total revenue of 34.49K €
- Total aquisition cost of 25K €
- Total gross profit of 9 Million €.
  
To reach that results the company has sold 209K units of its products, earing 53,20 € per sale on average

Sales have shown an increasing trend, but it has not been gradual, as between April and October, sales decreased and fell below the average from June to October. External factors that could explain this variation in sales are unknown. However, the statistical significance table shows that there is no strong relationship between the monthly trend and the sales. Therefore, it is not recommended to make any decisions based on the temporal analysis at this time.

![image](https://github.com/user-attachments/assets/6ae60222-6251-4eb1-87be-e8873d02b3a6)


This is not the case for the time frame, as the statistical table does show significance of the hours on sales. In the graph, we can see that the early morning hours, between 00:00 and 9:00 AM, accumulate sales figures lower than the average. Between 9:00 AM and 10:00 PM, sales exceed the average, with peaks between 10:00 AM and 2:00 PM, and between 5:00 PM and 9:00 PM

![image](https://github.com/user-attachments/assets/35cd16d5-11c8-41f4-9509-e1a87629d767)

With this information, it is possible to understand when the company sells the most, and it can lead to lines of analysis to determine when products should be promoted.

Regarding products and product categories, they also have statistical significance in sales. This means that some products are more successful than others. The sale of headphones and earbuds, accessories, and batteries represents more than 70% of sales. One hypothesis to investigate is whether these products, which the company sells the most, are also the most profitable.

![image](https://github.com/user-attachments/assets/177ee81b-4031-43e2-b036-d8138044f5f9)



#### Identification of Improvement Opportunities

The profit margin evolves in tandem with sales. This can be observed by comparing charts 1.1 from both pages. However, if we analyze the temporal evolution of the profit margin per sale, we can see that there is no upward trend, meaning that profitability is not increasing over time.

![image](https://github.com/user-attachments/assets/0632ee27-4175-403e-b239-a432f5adec9a)

An optimization of the product catalog with a product strategy is the selected approach to improve the profitability and gross profit. To do that it has been created an additional dashboard: Product Matrix. This matrix shows which are the products that are exceptional for the company, which are having good results and which must be optimized or even substituted. This project is not foccused on having a deep analysis so it won't be taken strategic decisions. Despite that, this panel shows the most relevant information of the products with the existing data and it could help any business to make strategic decisions.

![image](https://github.com/user-attachments/assets/286c2d9f-7b81-412a-8a57-a67ad6f072dc)


