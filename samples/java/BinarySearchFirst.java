    public int binarySearchFirst(int[] values, int target) {
        int start = 0, end = values.length - 1;

        int matchIndex = -1;
        while(start <= end) {
            int mid = start + (end - start) / 2;
            if(values[mid] == target) {
                matchIndex = mid;
                end = mid - 1;
            } else if(target < values[mid]) {
                end = mid - 1;
            } else {
                start = mid + 1;
            }
        }
        return matchIndex;
    }
