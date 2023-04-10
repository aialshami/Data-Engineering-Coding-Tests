# The below function doesn't work correctly. It should sum all the numbers at the
# current time. For example, 01:02:03 should return 6. Improve and fix the function,
# and write unit test(s) for it. Use any testing framework you're familiar with.


# [TODO]: fix the function
import datetime as dt

def sum_current_time(time_str: str) -> int:
    """Expects data in the format HH:MM:SS"""
    check_time_is_valid(time_str)
    list_of_nums = time_str.split(":")
    for i, num in enumerate(list_of_nums):
        list_of_nums[i] = int(num)
    print(list_of_nums)
    return sum(list_of_nums)



def check_time_is_valid(time_str:str):
    """checks that the time string is in the correct format"""
    try:
        time = dt.datetime.strptime(time_str, '%H:%M:%S')
    except:
        raise ValueError("Invalid time")

if __name__ == "__main__":
    
    time_str = str(dt.datetime.now().time())[:8]
    print(sum_current_time(time_str))
    