#include<stdio.h>
void swap(int* i, int* j){
    int temp = *i;
    *i = *j;
    *j = temp;
}

int partition(int arr[], int low, int high){
    int pivot = arr[high];
    int i = low - 1;

    for(int j=low;j<high;j++){
        if (arr[j] <= pivot) {
            i++;
            swap(&arr[i], &arr[j]);
        }
    }
    i++;
    swap(&arr[i], &arr[high]);
    return i;
}

void quickSort(int arr[], int low, int high){
    if(low < high){
        int pidx = partition(arr, low, high);

        quickSort(arr, low, pidx-1);
        quickSort(arr, pidx+1, high);
    }
}

void showArray(int arr[], int n){
    for(int i=0;i<n;i++) printf("%d\t" , arr[i]);
    printf("\n");
}

int main(){
    int n;
    printf("Enter the number of elements in the array : \n");
    scanf("%d",&n);

    int arr[n];
    printf("Enter the elements in the Array : \n");
    for(int i=0;i<n;i++) scanf("%d", &arr[i]);

    printf("Original Array : \n");
    showArray(arr,n);

    quickSort(arr, 0, n-1);
    printf("After Sorting the Array : \n");
    showArray(arr,n);
    return 0;
}