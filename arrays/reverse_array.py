def reverseArray(array):
    start_index = 0
    end_index = len(array) - 1

    while start_index < end_index:
        array[start_index], array[end_index] = array[end_index], array[start_index]
        start_index += 1
        end_index -= 1
    
    return array
