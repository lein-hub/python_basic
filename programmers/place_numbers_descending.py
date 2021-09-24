def solution(n):
    stringified_number_list = list(str(n))
    stringified_number_list.sort(reverse=True)
    stringified_number_order_by_descending = ''.join(stringified_number_list)

    return int(stringified_number_order_by_descending)
