import numpy as np
def eq(A, B, p):
  c = np.sum(A==B)
  s = A.shape[0]
  for e in A.shape[1::]:
    s*= e
  return (c/s)*100>=p

def closest_point_indexes(points, p):
  a = (points-p)**2
  b = np.sum(a,axis=1)
  minn = np.min(b)
  ra = np.arange(b.shape[0])
  return ra[b==minn]
def number_of_inversions(A):
 n = A.shape[0]
 indexes = np.arange(n)
 indexesT = indexes.reshape((n,1))
 AT = A.reshape((n,1))
 inv = np.sum((AT > A) & (indexesT < indexes))
 return inv  

exec(input().strip())