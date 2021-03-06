import time


def left_rotation(arr, number_rotation):
    """
        Return the array with desired number of rotation
        from left to right
    """
    for _ in range(number_rotation):
        target = arr[0]
        arr.remove(target)
        arr.append(target)
    return arr


def leftrotation(arr, number_rotation):
    return (arr[number_rotation:]+arr[:number_rotation])


if __name__ == '__main__':
    
    arr = [1, 2, 3, 4, 5]
    number_rotation = 4
    start_time = time.time()
    print(left_rotation(arr, number_rotation))
    end_time = time.time()
    print("time is {}".format(end_time-start_time))

    # print(leftrotation(arr, number_rotation))

    # print(f" {time.time() - start_time} seconds")
