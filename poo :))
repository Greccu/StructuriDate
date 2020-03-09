#include <iostream>

using namespace std;

class Multime
{
private:

  int v[100], n;
  
public:
  int *get_v (){ return v; }
  int get_n (){ return n; }
  void set_v (int x[100]){
    for (int i = 0; i < n; i++)
      v[i] = x[i];
  }
  void set_n (int m){ m = n; }
  Multime ();
  Multime (int x[], int m);	//constructor de initializare
  Multime (const Multime & m);	//constructor de copiere
  ~Multime ();
  void convert (int x[100], int m);
  void afisare ();
  friend Multime operator + (Multime m1, Multime m2);
  friend Multime operator * (Multime m1, Multime m2);
  friend Multime operator - (Multime m1, Multime m2);
  friend ostream & operator << (ostream & os, const Multime & m);
};

Multime::Multime (){
  n = 0;
}

Multime::Multime(int x[], int m){
  int k = 0, ok;
  for (int i = 0; i < m; i++){
      ok = 1;
      for (int j = 0; j < k; j++)
	if (x[i] == v[j])
	  {
	    ok = 0;
	  }
      if (ok){
	  v[k++] = x[i];
	    }
    }


Multime::Multime(const Multime & m){
  n = m.n;
  for (int i = 0; i < n; i++){
      v[i] = m.v[i];
    }
}

Multime::~Multime (){
  n = 0;
}

void Multime::convert(int x[100], int m){
  int k = 0, ok;
  for (int i = 0; i < m; i++){
      ok = 1;
      for (int j = 0; j < k; j++)
	if (x[i] == v[j]){
	    ok = 0;
	  }
      if (ok){
	  v[k++] = x[i];
	    }
}

Multime operator + (Multime m1, Multime m2){
  int n, m, v[200], *p1, *p2;
  n = m1.get_n () + m2.get_n ();
  m = m1.get_n ();
  p1 = m1.get_v ();
  p2 = m2.get_v ();
  for (int i = 0; i < n; i++){
      if (i < m)
	v[i] = p1[i];
      else
	v[i] = p2[i - m];
    }
  Multime M (v, n);
  M.convert ();
  return M;

}

Multime operator * (Multime m1, Multime m2){
  int v[200], *p1, *p2, k, ok;
  p1 = m1.get_v ();
  p2 = m2.get_v ();
  k = 0;
  for (int i = 0; i < m1.get_n (); i++){
      ok = 0;
      for (int j = 0; j < m2.get_n (); j++){
	  if (p1[i] == p2[j]){
	      ok = 1;
	    }
	}
      if (ok){
	  v[k++] = p1[i];
	}
    }
  Multime M (v, k);
  M.convert ();
  return M;

}

Multime operator - (Multime m1, Multime m2){
  int v[200], *p1, *p2, k, ok;
  p1 = m1.get_v ();
  p2 = m2.get_v ();
  k = 0;
  for (int i = 0; i < m1.get_n (); i++){
      ok = 0;
      for (int j = 0; j < m2.get_n (); j++){
	  if (p1[i] == p2[j]){
	      ok = 1;
	    }
	}
      if (ok == 0){
	  v[k++] = p1[i];
	}
    }
  Multime M (v, k);
  M.convert ();
  return M;

}

void Multime::afisare (){
  for (int i = 0; i < n; i++){
      cout << v[i] << " ";
    }
  cout << "\n";
}


int main (){
  int v[] = { 4, 3, 7, 5, 2, 3, 4, 5, 6, 7, 8 }, n = 11,	//4,3,7,5,2,6,8   - > 4,3,7,5,2,6,11,23,1
    v2[] ={3, 11, 23, 4, 5, 7, 1}, n2 = 7;	//3,11,23,4,5,7,1 - > 4,3,7,5
  Multime Set (v, n);		//                 - > 2,6,8
  Multime Set2 (v2, n2);
  Set.afisare ();
  Set2.afisare ();
  Multime X;
  X = Set + Set2;
  X.afisare ();
  X = Set * Set2;
  X.afisare ();
  X = Set - Set2;
  X.afisare ();

  return 0;
}
