# select_all_female_bears_return_name_and_age = """
#     Write your SQL query here
# """

# select_all_bears_names_and_orders_in_alphabetical_order = """
#     Write your SQL query here
# """

# select_all_bears_names_and_ages_that_are_alive_and_order_youngest_to_oldest = """
#     Write your SQL query here
# """

# select_oldest_bear_and_returns_name_and_age = """
#     Write your SQL query here
# """
# select_youngest_bear_and_returns_name_and_age = """
#     Write your SQL query here
# """
# sql_queries.py

# Select all female bears and return their name and age
select_all_female_bears_return_name_and_age = """
SELECT name, age
FROM bears
WHERE sex = 'F';
"""

# Select all bears' names and order them alphabetically
select_all_bears_names_and_orders_in_alphabetical_order = """
SELECT name
FROM bears
ORDER BY name;
"""

# Select all bears' names and ages that are alive and order them from youngest to oldest
select_all_bears_names_and_ages_that_are_alive_and_order_youngest_to_oldest = """
SELECT name, age
FROM bears
WHERE alive = 1
ORDER BY age;
"""

# Select the oldest bear and return its name and age
select_oldest_bear_and_returns_name_and_age = """
SELECT name, age
FROM bears
ORDER BY age DESC
LIMIT 1;
"""

# Select the youngest bear and return its name and age
select_youngest_bear_and_returns_name_and_age = """
SELECT name, age
FROM bears
ORDER BY age
LIMIT 1;
"""
