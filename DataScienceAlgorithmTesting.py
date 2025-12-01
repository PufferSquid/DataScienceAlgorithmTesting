import DataScienceAlgorithmTesting
import SchedulingAlgorithms
import SearchingAlgorithms
import SortingAlgorithms
import pandas as pd
import numpy as np
import math
import time
import tracemalloc


# Load the 'Data' sheet from the Excel file into a DataFrame
df = pd.read_excel('241003 Assignment Data (2025).xlsx', sheet_name='Data')

# Optional: Clean or prepare the data (e.g., convert 'Time' to numeric if needed)
df['Time'] = pd.to_numeric(df['Time'], errors='coerce')


# returned as dictionary without being transposed
"""
def GetGraphData():
    df_graph = pd.read_excel('241003 Assignment Data (2025).xlsx', sheet_name='SimplifiedGraph')
    df_graph = df_graph.set_index('NodeX')
    return_dict = {}

    for node, row in df_graph.iterrows():
        cleaned_values = [value for value in row if not pd.isna(value)]
        return_dict[node] = cleaned_values

    return return_dict
"""

# returns transposed df of dictionaries
def GetGraphData():

    df_graph = pd.read_excel('241003 Assignment Data (2025).xlsx', sheet_name='SimplifiedGraph')
    df_clean = df_graph.copy()
    df_clean = df_clean.set_index('NodeX')  # Set NodeX as index
    df_clean = df_clean.fillna(0)

    #Create a copy of the upper triangular part of the matrix (the non 0s)
    upper_triangle = df_clean.copy()
    
    # Get the lower triangular part by transposing (very handy pandas function)
    lower_triangle = upper_triangle.transpose()
    
    # use maximum to handle the diagonal (keep 0s on diagonal)
    symmetric_df = upper_triangle.combine(lower_triangle, np.maximum)

    # return the symmetrical df (by default, the matrix upper triangle has values, and 0s diagonally, but nan for the rest so we have to transpose it and combine)
    return symmetric_df


def ConvertDfToGraphDict(symmetric_df):
    graph_dict = {}
    
    # Get all node IDs from DataFrame index
    nodes = symmetric_df.index.tolist()
    
    for node_i in nodes:
        graph_dict[node_i] = {}
        for node_j in nodes:
            cost = symmetric_df.loc[node_i, node_j]
            # Only include connections with positive cost and not to self
            if cost > 0 and node_i != node_j:
                graph_dict[node_i][node_j] = int(cost)
    
    return graph_dict


# TEST Merge Sort
def testMergeSort(packet_lengths):
    start_time = time.perf_counter()
    tracemalloc.start()
    result = SortingAlgorithms.mergeSort(packet_lengths, 0, len(packet_lengths) - 1)
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    end_time = time.perf_counter()  
    elapsed = end_time - start_time

    print()
    print("===Merge Sort algorithm performance test===")
    print(f"Result: {result}")
    print(f"Start time: {start_time}")
    print(f"End time: {end_time}")
    print(f"Elapsed time: {elapsed}")
    print(f"Peak memory allocated: {peak}")


# TEST Bucket Sort
def testBucketSort(packet_lengths):
    start_time = time.perf_counter()
    tracemalloc.start()
    result = SortingAlgorithms.bucketSort(packet_lengths)
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    end_time = time.perf_counter()  
    elapsed = end_time - start_time

    print()
    print("===Bucket Sort algorithm performance test===")
    print(f"Result: {result}")
    print(f"Start time: {start_time}")
    print(f"End time: {end_time}")
    print(f"Elapsed time: {elapsed}")
    print(f"Peak memory allocated: {peak}")


# TEST Linear Search
def testLinearSearch(target_value, sorted_packet_lengths):
    start_time = time.perf_counter()
    tracemalloc.start()
    result = SearchingAlgorithms.linearSearch(sorted_packet_lengths, target_value)
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    end_time = time.perf_counter()  
    elapsed = end_time - start_time

    print()
    print("===Linear Search algorithm performance test===")
    print(f"Result index at: {result}")
    print(f"Start time: {start_time}")
    print(f"End time: {end_time}")
    print(f"Elapsed time: {elapsed}")
    print(f"Peak memory allocated: {peak}")


# TEST Binary Search
def testBinarySearch(target_value, sorted_packet_lengths):
    start_time = time.perf_counter()
    tracemalloc.start()
    result = SearchingAlgorithms.binarySearch(sorted_packet_lengths, target_value)
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    end_time = time.perf_counter()  
    elapsed = end_time - start_time

    print()
    print("===Binary Search algorithm performance test===")
    print(f"Result index at: {result}")
    print(f"Start time: {start_time}")
    print(f"End time: {end_time}")
    print(f"Elapsed time: {elapsed}")
    print(f"Peak memory allocated: {peak}")


# TEST Dijkstra
def testDijkstra(df_to_dict):
    start_time = time.perf_counter()
    tracemalloc.start()
    result = SchedulingAlgorithms.Dijkstra(df_to_dict, 1)
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    end_time = time.perf_counter()  
    elapsed = end_time - start_time

    print()
    print("===Dijkstra's algorithm performance test===")
    print(f"Result: {result}")
    print(f"Start time: {start_time}")
    print(f"End time: {end_time}")
    print(f"Elapsed time: {elapsed}")
    print(f"Peak memory allocated: {peak}")


# TEST Bellman-Ford
def testBellmanFord(df_to_dict):
    start_time = time.perf_counter()
    tracemalloc.start()
    result = SchedulingAlgorithms.BellmanFord(df_to_dict, 1)
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    end_time = time.perf_counter()  
    elapsed = end_time - start_time

    print()
    print("===Bellman-Ford algorithm performance test===")
    print(f"Result: {result}")
    print(f"Start time: {start_time}")
    print(f"End time: {end_time}")
    print(f"Elapsed time: {elapsed}")
    print(f"Peak memory allocated: {peak}")


print()

df_to_dict = ConvertDfToGraphDict(GetGraphData())
packet_lengths = df['Length'].tolist()
sorted_packet_lengths = df['Length'].tolist().copy()
sorted_packet_lengths = SortingAlgorithms.mergeSort(sorted_packet_lengths, 0, len(sorted_packet_lengths) - 1)

print(df)
#print(packet_lengths)
#print(sorted_packet_lengths)
# Run the tests
testMergeSort(packet_lengths)
testBucketSort(packet_lengths)
testLinearSearch(54, sorted_packet_lengths)
testBinarySearch(708, sorted_packet_lengths)
testDijkstra(df_to_dict)
testBellmanFord(df_to_dict)