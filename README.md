# Dfs_for_flight

Aim:
To find Maximum number of Persons who can travel on the particular day from LAX to JFK.

Input:
1. Id – id of the row
2. Source_City - The Source City of the flight
3. Destination_City - The Destination City of the flight
4. Start_Time - Consist of the starting time of the flight
5. Finish_Time - Consist of the finish time of the flight
6. Capacity – Consist of the number of persons a flight can accommodate.

Algorithm:
We have to find the maximum flow, We use two algorithms to do the process (i.e.) DFS and Ford Fulkerson. DFS is used to find the paths and Ford Fulkerson is used to calculate the maximum flow. We also use activity selection method to get the flight timing without overlapping each other.

Steps to run the code:
1. Copy the code and datasets to the same folder
2. Dataset name is given as data.csv
3. Have attached the code as Python Script and as well as Jupyter Notebook.
