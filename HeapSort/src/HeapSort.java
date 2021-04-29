import java.util.*;
import java.io.IOException;
import java.io.FileWriter;
public class HeapSort {
    public void sort(int arr[]) {
        int temp;
        for (int i = arr.length / 2 - 1; i >= 0 ; i--)      //힙 생성
            heapify(arr, arr.length ,i);
        for (int i = arr.length - 1; i > 0; i--) {          //힙에서 요소를 하나씩 추출
            temp = arr[0];
            arr[0] = arr[i];
            arr[i] = temp;
            heapify(arr, i, 0);
        }
    }
    //heapify : 뿌리마디 i에 대한 자식마디
    //n은 힙의 크기, arr[]은 힙 목록
    //최대 힙을 구현하여 정렬함
    void heapify(int arr[], int n, int i) {
        int max = i;                            //max를 뿌리마디의 값으로 초기화
        int temp;
        int l = 2 * i + 1;                      //왼쪽
        int r = 2 * i + 2;                      //오른쪽
        if (l < n && arr[l] > arr[max])
            max = l;                            //왼쪽에 더 큰값이 있을 경우 max를 그 값으로 변경
        if (r < n && arr[r] > arr[max])
            max = r;                            //오른쪽에 더 큰값이 있을 경우 max를 그 값으로 변경
        if (max != i) {                         //가장 큰 값과 뿌리마디의 값이 다를 경우 서로의 위치를 바꿈
            temp = arr[i];
            arr[i] = arr[max];
            arr[max] = temp;
            //재귀적으로 자식마디 생성
            heapify(arr, n, max);
        }
    }
    //sort()메소드와 heapify()메소드의 기본적인 구조는 GeeksforGeeks 사이트를 참고함
    //https://www.geeksforgeeks.org/heap-sort/
    public static void main(String args[]) throws IOException {
        int arr[] = new int[50000];             //abc.txt 데이터 갯수 총 5만개
        int i = 0;
        String x;
        Scanner sc = new Scanner(System.in);
        String str = sc.nextLine();             //입력받을 파일이름 입력
        java.io.File file = new java.io.File(str);
        Scanner inFile = new Scanner (file);
        //파일 입력
        while(inFile.hasNextInt()) {
            arr[i]=inFile.nextInt();            //파일의 값을 배열에 저장
            i++;
        }
        HeapSort ob = new HeapSort();
        ob.sort(arr);
        str = sc.nextLine();                    //출력할 파일이름 입력
        FileWriter newFile = new FileWriter(str);
        for(int j=0;j<arr.length;j++) {
            x= Integer.toString(arr[j]);        //int 값을 문자열로 변환
            newFile.write(x);                   //출력할 파일에 값을 하나씩 입력
            newFile.write("\n");
        }
        newFile.close();
    }
}