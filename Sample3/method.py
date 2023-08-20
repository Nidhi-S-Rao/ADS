#Program to get unique elements in list
def unique(input_list):
    unique_elements = []
    for item in input_list:
        if item not in unique_elements:
            unique_elements.append(item)
    return unique_elements


#Program to get duplicates in list
def dups(input_list):
    seen = []
    duplicates = []
    for item in input_list:
        if item in seen and item not in duplicates:
            duplicates.append(item)
        else:
            seen.append(item)
    return duplicates

#Program to split the list
def group(input_list, size):
    grouped_lists = [input_list[i:i + size] for i in range(0, len(input_list), size)]
    return grouped_lists
