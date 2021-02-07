def test_sort(sort_algorithm):
	""" тестирование алгоритмов сортировки """
    print("Тестируем:", sort_algorithm.__doc__)
    
    print("testcase #1: ", end="")
	A = [4, 2, 5, 1, 3]
	A_sorted = [1, 2, 3, 4, 5]
	sort_algorithm(A)
	print("ok" if A == A_sorted else "fail")
	
	print("testcase #2: ", end="")
	A = list(range(10, 20)) + list(range(0, 10))
	A_sorted = list(range(20))
	sort_algorithm(A)
	print("ok" if A == A_sorted else "fail")
	
	print("testcase #3: ", end="")
	A = [4, 2, 4, 2, 1]
	A_sorted = [1, 2, 2, 4, 4]
	sort_algorithm(A)
	print("ok" if A == A_sorted else "fail")
	
if __name__ == "__main__":
    test sort(insert_sort)
    test sort(choise_sort)
    test sort(bubble_sort)