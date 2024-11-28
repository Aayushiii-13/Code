#include<iostream>
#include<cstdlib>
#include<ctime>
#include<chrono>
using namespace std;
using namespace chrono;

void generateRandomArray(int arr[], int SIZE) {
    srand(time(0));
    for (int i = 0; i < SIZE; i++) {
        arr[i] = rand() % 10000;
    }
}

void merge(int arr[], int left, int right, int mid) {
    int n1 = mid - left + 1;
    int n2 = right - mid;

    int L[n1], R[n2];

    for (int i = 0; i < n1; i++) L[i] = arr[left + i];
    for (int i = 0; i < n2; i++) R[i] = arr[mid + 1 + i];

    int i = 0, j = 0, k = left;
    while (i < n1 && j < n2) {
        if (L[i] < R[j]) {
            arr[k++] = L[i++];
        }
        else {
            arr[k++] = R[j++];
        }
    }

    while (i < n1) arr[k++] = L[i++];
    while (j < n2) arr[k++] = R[j++];
}

void mergeSort(int arr[], int left, int right) {
    if (left < right) {
        int mid = left + (right - left) / 2;
        mergeSort(arr, left, mid);
        mergeSort(arr, mid + 1, right);
        merge(arr, left, right, mid);
    }
}

// Function to analyze performance of Merge Sort
void analyzePerformance(void (*sortFunction)(int[], int, int), int arr[], int size, string sortName) {
    int *copyArr = new int[size];
    for (int i = 0; i < size; i++) {
        copyArr[i] = arr[i];
    }

    auto start = high_resolution_clock::now();
    sortFunction(copyArr, 0, size - 1);
    auto stop = high_resolution_clock::now();

    auto duration = duration_cast<milliseconds>(stop - start);
    cout << sortName << " execution time for size " << size << ": " << duration.count() << " ms\n";

    delete[] copyArr;
}

int main() {
    const int SIZE = 10000; // Example size
    int arr[SIZE];

    generateRandomArray(arr, SIZE);

    cout << "Array before sorting:" << endl;
    for (int i = 0; i < SIZE; i++) cout << arr[i] << " ";
    cout << endl;

    // Analyzing performance
    analyzePerformance(mergeSort, arr, SIZE, "Merge Sort");

    cout << "Array after sorting:" << endl;
    for (int i = 0; i < SIZE; i++) cout << arr[i] << " ";
    cout << endl;

    return 0;
}
