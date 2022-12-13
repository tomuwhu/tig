template <class K, class V>
class fa {
public:
    int elemszam ;
    class fapont {
    public:
        K key ;
        V value ;
        fapont * bal, * jobb, * apa;
    };
    fapont * null ;
    fapont * gyoker ;		
    fa() {
        fapont * q=new fapont;
        null=q;
        gyoker = q ;
        elemszam=0 ;
    }
    int beszur(int x,int v) {
        fapont * p,  * papa;
        p=gyoker ;
        papa=null ;
        while (p!=null and p->key!=x) {
            papa=p;
            if (x<p->key) 	p=p->bal;
            else p=p->jobb;
        }
        if (p==null) {
            fapont * ujpont = new fapont;
            if (gyoker==p) gyoker=ujpont ;
            ujpont->key=x ;
            ujpont->value=v ;
            ujpont->bal=null;
            ujpont->jobb=null;
            ujpont->apa=papa;
            if (papa!=null) {
                if (x>papa->key) papa->jobb=ujpont; 
                else  papa->bal=ujpont; 
            }	
            elemszam++ ;
            return 0;	
        } else {
            p->value=v ;
            return 1;
        }	
    } ;
    fapont * keres(int x) {
        fapont * p ;
        p=gyoker ;
        while (p!=null and p->key!=x) {
            if (x<p->key) p=p->bal;
            else p=p->jobb;
        } 
        return p;
    }
    void kiir(fapont * p) {
        if (p!=null) {
            kiir(p->bal) ;
            std::cout << p->key << " -> " << p->value << std::endl;
            kiir(p->jobb) ;
        }	
    }
};