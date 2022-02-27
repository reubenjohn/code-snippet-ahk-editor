
    void countingSort(int[] arr, int limit) {
        int[] freq = new int[limit + 1];
        for(int x: arr)
            freq[x]++;

        int count = 0;
        for(int i = 0; i <= limit; i++)
            for(int j = 0; j < freq[i]; j++)
                arr[count++] = i;
    }
