def interchange(arr):
    arr[0], arr[-1] = arr[-1], arr[0]

def main():
    # Input for arr
    arr_size = int(input())
    arr = list(map(int, input().split()))
    interchange(arr)
    print(" ".join([str(res) for res in arr]))

if __name__ == "__main__":
    main()
