#include <iostream>
using namespace std;
int main( int argc, char *argv[] ) {
    int a, b;
    a = *argv[3] - '0';
    b = *argv[4] - '0';
    cout << a + b << "\n";
}