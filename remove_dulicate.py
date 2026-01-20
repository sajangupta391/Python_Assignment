# Question 10


def remove_duplicates(list):
    unique_list = []
    
    for item in list:
        if item not in unique_list:
            unique_list.append(item)
            
    return unique_list

input_1 = [1, 3, 2, 3, 4, 1, 5]
output_1 = remove_duplicates(input_1)
print(f"Input: {input_1}")
print(f"Output: {output_1}")

print("-" * 20)

input_2 = [4, 4, 4, 4]
output_2 = remove_duplicates(input_2)
print(f"Input: {input_2}")
print(f"Output: {output_2}")