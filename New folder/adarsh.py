# def addition (n1: int,n2:int)->int:
#     """this functin take two arguments and return total"""
#     total = n1 + n2
#     return total

# def mul(n1,n2):
#     return n1*n2

# if __name__=="__main__":
#     print(addition(12,13))

#     print("name of this file is",__name__)


# number_list = [12,13,15,16,24,31,25,65,78,45,98,11]

def find_large_number(number_list: list[float]) -> float:

    if not isinstance(number_list, list):
        raise TypeError("Input must be a list of numbers.")
    
    if not number_list:
        raise ValueError("List cannot be empty.")
    
    for num in number_list:
        if not isinstance(num, (int, float)):
            raise TypeError("All elements must be numeric.")
    
    large_num = number_list[0] 
    for num in number_list:
        if num > large_num:
            large_num = num
            
    return large_num

if __name__ == "__main__":
    try:
        user_input = input("Enter the numbers separated by spaces: ")

        number_list = [float(item) for item in user_input.split()]
        
        result = find_large_number(number_list)
        print(f"The largest number in the list is: ",result)
    except ValueError as e:
        print(e)
    except TypeError as e:
        print(e)

