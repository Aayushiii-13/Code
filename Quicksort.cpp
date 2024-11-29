#include<iostream>
#include<algorithm> //Provides functions for common data manipulation tasks.
#include<cstdlib> //General-purpose utilities like random numbers.
#include<ctime> //Utilities for working with time, often paired with cstdlib.
#include<chrono> //measuring Exceution time 
using namespace std;
using namespace chrono;

void generateRandomArray(int arr[], int SIZE) {
    srand(time(0));
    for (int i = 0; i < SIZE; i++) {
        arr[i] = rand() % 10000;
    }
}

int partition(int arr[], int low, int high) {
    int pivot = arr[high];
    int i = low - 1;

    for (int j = low; j < high; j++) {
        if (arr[j] < pivot) {
            i++;
            swap(arr[i], arr[j]);
        }
    }
    swap(arr[i + 1], arr[high]);
    return i + 1;
}

void quickSort(int arr[], int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}

// Function to analyze performance of Quick Sort
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
    analyzePerformance(quickSort, arr, SIZE, "Quick Sort");

    cout << "Array after sorting:" << endl;
    for (int i = 0; i < SIZE; i++) cout << arr[i] << " ";
    cout << endl;

    return 0;
}
