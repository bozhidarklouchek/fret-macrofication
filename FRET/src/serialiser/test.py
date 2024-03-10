def sort_lists_from_bottom_to_top(input_list):
    if isinstance(input_list, list):
        # Sort each sublist excluding the first element
        sorted_sublists = [sort_lists_from_bottom_to_top(sublist[1:]) for sublist in input_list]
        
        # Extract the first element of each sublist
        first_elements = [sublist[0] for sublist in input_list]
        
        # Combine the first elements with the sorted sublists
        sorted_result = [[first] + sublist for first, sublist in zip(first_elements, sorted_sublists)]
        
        # Sort the combined lists based on the first element
        return sorted(sorted_result, key=lambda x: x[0])
    else:
        return input_list

# Example usage:
nested_list = [[4, 2, 3], [1, 5, 6], [9, 8, 7]]
sorted_nested_list = sort_lists_from_bottom_to_top(nested_list)
print("Sorted List:")
print(sorted_nested_list)
