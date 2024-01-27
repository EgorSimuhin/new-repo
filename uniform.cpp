#include <iostream>
using namespace std;
int main() {
    setlocale(LC_ALL, "RU");
    int f, g, nod = 1;
    cin >> f >> g;
    for(int u = 1; u <= g; u++) {
        if(f % u == 0 && g % u == 0) {
            nod = u;
        }
    }
    cout << "НОД - " << nod;
    cout << endl << "Это Инженерка"; 
    return 0;
}