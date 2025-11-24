'''Task Description #5
    Student need to write code to calculate sum of add 
    number and even numbers in the list'''


def calculate_odd_even_sum(numbers_list): 
    odd_sum = 0
    even_sum = 0

    
    for num in numbers_list:
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num
            
    return odd_sum, even_sum


list_num = [2, 3, 4, 5, 6, 7, 8, 9]

odd_sum, even_sum = calculate_odd_even_sum(list_num) 

print(f"List: {list_num}")
print(f"The sum of odd numbers is {odd_sum}")
print(f"The sum of even numbers is {even_sum}")