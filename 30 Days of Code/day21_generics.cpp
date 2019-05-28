/**
*    Name: printArray
*    Print each element of the generic vector on a new line. Do not return anything.
*    @param A generic vector
**/

template <typename T>
void printArray(const vector<T>& array) {
    for (T elem : array) {
        cout << elem << endl;
    }
}