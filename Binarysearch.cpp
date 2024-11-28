#include<iostream>
#include<algorithm>
#include<cstdlib>
#include<ctime>
using namespace std;

void generaterandom(int arr[] , int SIZE){
    srand(time(0));
    for(int i = 0; i < SIZE ; i++){
        arr[i] = rand() % 1000 ;

    }
}

int binarysearch(int arr[] , int left, int right , int key){
    while(left <= right){
        int mid  = left + (right - left)/2 ;
        if(arr[mid] == key ){
            return mid ;
        }
        else if (arr[mid] < key){
            left = mid + 1;
        }
        else {
            right = mid - 1;
        }
    }
    return -1 ;
}

int main() {

    const int SIZE = 5000;
    int arr[SIZE];

    generaterandom(arr, SIZE);
    sort(arr, arr + SIZE);


    int key ;
    cout<<"Enter key "<<endl;
    cin>>key;

    int result = binarysearch(arr, 0, SIZE-1 , key );


    if(result != -1){
        cout<<"key is successfully found at index "<<result<<endl;

    }
    else{
        cout<<"key is not there !!"<<endl;
    }

    return 0;
}






























