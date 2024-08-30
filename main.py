
def diagonalDifference(arr):

    left = 0
    right = 0
    length = len(arr[0])

    for i in range(length):
        left += arr[i][i]
        right += arr[i][length - i - 1]

    print (abs(left - right))
if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    diagonalDifference(arr)