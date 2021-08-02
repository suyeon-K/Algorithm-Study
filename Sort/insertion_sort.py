def insertion_sort(num_list):
    bef_n_list = num_list.copy()

    for idx in range(len(bef_n_list)):
        now_idx = idx
        while idx > 0:
            # t = bef_n_list[idx-1]
            # bef_n_list[idx-1] = bef_n_list[idx]
            # bef_n_list[idx] = t

            bef_n_list[idx], bef_n_list[idx-1] = bef_n_list[idx-1], bef_n_list[idx]
            now_idx -=1 

    return []