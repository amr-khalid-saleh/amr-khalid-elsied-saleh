//شروق فتحي محمد نصور
//سكشن رقم 3
//سكشن بشمهندس احمد الديموكسي
def selection_sort(A):
  n=len(A)
  for j in range(n-1):
      smallest =j
      for i in range(j+1,n):
         if A[i]<A[smallest]:
            smallest=i
      A[j],A[smallest]=A[smallest],A[j]
A=[5,10,6,7,3]
seletion_sort(A)
print("sorted array:",A)
