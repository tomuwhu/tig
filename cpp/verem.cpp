#include <iostream>
template <class T>
class verem {
    public:
        int elemszam ;
        class elem {
            public:
                T ertek ;
                elem * kovetkezo ;
        };
        elem * null, * elso ;
        verem() {
            elem * q = new elem;
            elso = q;
            null = q ;
            elemszam = 0 ;
        }
        void verembe(int v) {
            elem * p = new elem;
            p->ertek = v ;
            p->kovetkezo = elso ;
            elso = p ;
            elemszam++ ;
        }
        void uresit() {
            elem * torolni ;	
            while (elemszam) {
                torolni = elso ;
                elso = elso->kovetkezo ;
                delete torolni ;
                elemszam-- ;
            }
        }
        T verembol() {
            if (elemszam) {
                T retv ;
                retv = elso->ertek ;
                elem * torolni ;
                torolni = elso ;
                elso = elso->kovetkezo ;
                delete torolni ;
                elemszam-- ;
                return retv ;
            } else {
                return -1 ;
            }
        }
};
int main() {
    verem<int> v;
    v.verembe(7);
    v.verembe(5);
    v.verembe(2);
    std::cout << v.verembol() << " - " << v.verembol() << " - " << v.verembol();
}