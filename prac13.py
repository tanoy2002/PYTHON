def arr_sum(bin_arr):
  l, r = 0, len(bin_arr) - 1
  while l <= r:
    m = (l + r) // 2
    if bin_arr[m] == 0:
      l = m + 1
    else:
      r = m - 1

  return len(bin_arr) - l


print(arr_sum([0, 0, 0, 0, 0, 0, 0, 0, 0]))
