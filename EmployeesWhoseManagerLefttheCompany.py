"""+-------------+----------+
| Column Name | Type     |
+-------------+----------+
| employee_id | int      |
| name        | varchar  |
| manager_id  | int      |
| salary      | int      |
+-------------+----------+
In SQL, employee_id is the primary key for this table.
This table contains information about the employees, their salary, and the ID of their manager. Some employees do not have a manager (manager_id is null).


Find the IDs of the employees whose salary is strictly less than $30000 and whose manager left the company. When a manager leaves the company, their information is deleted from the Employees table, but the reports still have their manager_id set to the manager that left.

Return the result table ordered by employee_id.

The result format is in the following example."""

import pandas as pd


data = [[3, 'Mila', 9, 60301], [12, 'Antonella', None, 31000], [13, 'Emery', None, 67084], [1, 'Kalel', 11, 21241], [9, 'Mikaela', None, 50937], [11, 'Joziah', 6, 28485]]
employees = pd.DataFrame(data, columns=['employee_id', 'name', 'manager_id', 'salary']).astype({'employee_id':'Int64', 'name':'object', 'manager_id':'Int64', 'salary':'Int64'})

def find_employees(employees: pd.DataFrame) -> pd.DataFrame:
    ## Approach 1
    # filtered_employees= employees[(employees['salary']<30000) & (employees['manager_id'].notnull())]
    #
    # invalid_employees = filtered_employees[~ filtered_employees['manager_id'].isin(employees['employee_id'])]
    #
    # return invalid_employees[['employee_id']].sort_values(by='employee_id')

    ## Approach 2:
    return employees[~(employees['manager_id'].isin(employees['employee_id']))
                     & (employees['salary'] < 30000)].dropna()[['employee_id']].sort_values(by='employee_id')


print(find_employees(employees))