/*
CoderPad provides a basic SQL sandbox with the following schema.
You can also use commands like `show tables` and `desc sales`

products                              sales
+------------------+---------+        +------------------+---------+
| product_id       | int     |------->| product_id       | int     |
| product_class_id | int     |  +---->| store_id         | int     |
| brand_name       | varchar |  |  +->| customer_id      | int     |
| product_name     | varchar |  |  |  | promotion_id     | int     |
| price            | int     |  |  |  | store_sales      | decimal |
+------------------+---------+  |  |  | store_cost       | decimal |
                                |  |  | units_sold       | decimal |
                                |  |  | transaction_date | date    |
                                |  |  +------------------+---------+
                                |  | 
stores                          |  |  customers
+-------------------+---------+ |  |  +---------------------+---------+
| store_id          | int     |-+  +--| customer_id         | int     |
| type              | varchar |       | first_name          | varchar |
| name              | varchar |       | last_name           | varchar |
| state             | varchar |       | state               | varchar |
| first_opened_date | datetime|       | birthdate           | date    |
| last_remodel_date | datetime|       | education           | varchar |
| area_sqft         | int     |       | gender              | varchar |
+-------------------+---------+       | date_account_opened | date    |
                                      +---------------------+---------+ 
*/

/*
CoderPad provides a basic SQL sandbox with the following schema.
You can also use commands like `show tables` and `desc sales`

products                              sales
+------------------+---------+        +------------------+---------+
| product_id       | int     |------->| product_id       | int     |
| product_class_id | int     |  +---->| store_id         | int     |
| brand_name       | varchar |  |  +->| customer_id      | int     |
| product_name     | varchar |  |  |  | promotion_id     | int     |
| price            | int     |  |  |  | store_sales      | decimal |
+------------------+---------+  |  |  | store_cost       | decimal |
                                |  |  | units_sold       | decimal |
                                |  |  | transaction_date | date    |
                                |  |  +------------------+---------+
                                |  | 
stores                          |  |  customers
+-------------------+---------+ |  |  +---------------------+---------+
| store_id          | int     |-+  +--| customer_id         | int     |
| type              | varchar |       | first_name          | varchar |
| name              | varchar |       | last_name           | varchar |
| state             | varchar |       | state               | varchar |
| first_opened_date | datetime|       | birthdate           | date    |
| last_remodel_date | datetime|       | education           | varchar |
| area_sqft         | int     |       | gender              | varchar |
+-------------------+---------+       | date_account_opened | date    |
                                      +---------------------+---------+ 
*/



/* 
Question 5a:  
How many products had more than 5 total units sold? 

Expected Output:
+----------------+
| count_products |
+----------------+
|            127 |
+----------------+
*/
select count(product_id) from sales where units_sold > 5

















/* 
Question 4:  
Find the youngest and oldest customers who have bought at least 1 product, segmented by gender.

Expected Output:
+--------+------------------------+--------------------+
| gender | earliest_born_customer | last_born_customer |
+--------+------------------------+--------------------+
|      F |             1928-09-02 |         1994-06-13 |
|      M |             1927-03-02 |         1995-06-20 |
+--------+------------------------+--------------------+

select c.gender, min(c.birthdate), max(c.birthdate)
from sales s
join customers c on s.customer_id = c.customer_id
group by c.gender










/* 
Question 3:  
In how many different states are our stores located in?

Expected Output:
+---------------------+
| count_unique_states |
+---------------------+
|                   3 |
+---------------------+

select count(distinct state) from stores




























/* 
Question 2: 
What percent of our customer base is male?

Expected Output:
+----------+
| pct_male |
+----------+
| 48.6667  |
+----------+

select
  count( if( c.gender = 'M', True, NULL)) / count(*) cn
from customers c



























/* 
Question 1:  
Lists the states with at least 25,000 total square feet of store space

Expected Output:
+-------+-----------------+ 
| state | total_area_sqft | 
+-------+-----------------+ 
| CA    |           46076 | 
| OR    |           27694 | 
+-------+-----------------+


select s.state, sum(area_sqft) sm from stores s group by state having sm >= 25000


