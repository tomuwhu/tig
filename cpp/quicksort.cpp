#include <cstdlib>
#include <iostream>
#include <stdio.h>

using namespace std;

// A T[p..r] tömböt két résztömbre osztjuk úgy, hogy az első résztömb minden
// eleme kisebb vagy egyenlő T[q]-nál, a második résztömb minden eleme pedig
// nagyobb vagy egyenlő T[q]-nál.

int Feloszt(int* T, int p, int r){
    int x = T[r];
    int i = p-1;
    for (int j=p; j<=r-1; j++){
        if (T[j]<=x){
            i = i+1;
            int k = T[i];
            T[i] = T[j];
            T[j] = k;
        }
    }
    int v = T[i+1];
    T[i+1] = T[r];
    T[r] = v;
    return i+1;    
}

// A résztömböket a gyorsrendezés rekurzív hívással rendezzük

void Gyorsrendezes(int* T,int p, int r){
    if (p<r){
        int q = Feloszt(T,p,r);
        Gyorsrendezes(T,p,q-1);
        Gyorsrendezes(T,q+1,r);
    }
}

int main(int argc, char *argv[]){

// Beolvasas file-bol
   
    if(argc == 3){
        FILE *f;
        int elemszam;
        int y;
        f = fopen(argv[1], "r");
        fscanf(f,"%d\n",&elemszam);
        int T[elemszam];
        for (int i=1;i<=elemszam;i++){
            fscanf(f,"%d\n",&y);
            T[i]=y;
        }
        fclose (f);

        Gyorsrendezes(T, 1, elemszam);

//Eredmeny kiirasa file-ba
        FILE *f2;
        f2=fopen(argv[2],"w");
        for(int i=1;i<=elemszam;i++){
            fprintf(f2,"%d\n",T[i]);        
        }
        fflush(f2);
        fclose(f2);
        return 0;
    }
    else{
        printf("\nHasznalata: 1. parameter: bemeneti file neve, 2. parameter: kimeneti file neve\n");
        return 1;
    }
}