

lst = [1, 4, 5, 7, 13, 21, 34, 55, 8, 100]

# 6. Xuất tất cả các số lẻ không chia hết cho 5
odd_not_div5 = [x for x in lst if x % 2 != 0 and x % 5 != 0]
print("Số lẻ không chia hết cho 5:", odd_not_div5)

# 7. Xuất tất cả các số Fibonacci
def is_fibonacci(n):
    a, b = 0, 1
    while a <= n:
        if a == n:
            return True
        a, b = b, a + b
    return False

fibonacci_nums = [x for x in lst if is_fibonacci(x)]
print("Các số Fibonacci:", fibonacci_nums)

# 8. Tìm số nguyên tố lớn nhất
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

prime_nums = [x for x in lst if is_prime(x)]
max_prime = max(prime_nums) if prime_nums else None
print("Số nguyên tố lớn nhất:", max_prime)

# 9. Tìm số Fibonacci bé nhất
min_fibonacci = min(fibonacci_nums) if fibonacci_nums else None
print("Số Fibonacci bé nhất:", min_fibonacci)

# 10. Tính trung bình các số lẻ
odd_nums = [x for x in lst if x % 2 != 0]
average_odd = sum(odd_nums) / len(odd_nums) if odd_nums else None
print("Trung bình các số lẻ:", average_odd)

# 11. Tính tích các phần tử là số lẻ không chia hết cho 3 trong mảng
odd_not_div3 = [x for x in lst if x % 2 != 0 and x % 3 != 0]
product_odd_not_div3 = 1
for num in odd_not_div3:
    product_odd_not_div3 *= num
print("Tích các phần tử là số lẻ không chia hết cho 3:", product_odd_not_div3)

# 12. Đổi chỗ 2 phần tử của danh sách
def swap_elements(lst, pos1, pos2):
    lst[pos1], lst[pos2] = lst[pos2], lst[pos1]
    return lst

# Giả sử đổi chỗ phần tử ở vị trí 1 và 3
swapped_lst = swap_elements(lst, 1, 3)
print("Danh sách sau khi đổi chỗ:", swapped_lst)

# 13. Đảo ngược trật tự các phần tử của danh sách
reversed_lst = lst[::-1]
print("Danh sách đảo ngược:", reversed_lst)

# 14. Xuất tất cả các số lớn thứ nhì của danh sách
sorted_lst = sorted(lst)
second_largest = sorted_lst[-2] if len(sorted_lst) > 1 else None
print("Số lớn thứ nhì:", second_largest)

# 15. Tính tổng các chữ số của tất cả các số trong danh sách
def sum_of_digits(n):
    return sum(int(digit) for digit in str(abs(n)))

total_digit_sum = sum(sum_of_digits(x) for x in lst)
print("Tổng các chữ số của tất cả các số:", total_digit_sum)

# 16. Đếm số lần xuất hiện của một số trong danh sách
num_to_count = 5  # Ví dụ, đếm số 5
count_num = lst.count(num_to_count)
print(f"Số {num_to_count} xuất hiện {count_num} lần.")

# 17. Xuất các số xuất hiện n lần trong danh sách
from collections import Counter

n = 2  # Giả sử muốn tìm các số xuất hiện 2 lần
count = Counter(lst)
nums_with_n_occurrences = [num for num, freq in count.items() if freq == n]
print(f"Các số xuất hiện {n} lần:", nums_with_n_occurrences)

# 18. Xuất các số xuất hiện nhiều lần nhất trong danh sách
most_common_count = count.most_common(1)[0][1]  # Lấy tần suất xuất hiện nhiều nhất
most_common_nums = [num for num, freq in count.items() if freq == most_common_count]
print(f"Các số xuất hiện nhiều lần nhất:", most_common_nums)
