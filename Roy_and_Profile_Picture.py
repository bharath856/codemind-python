I=int(input())
n=int(input())
for i in range (1,n+1):
  w,h=map(int,input().split())
    
  if w<I or h<I:
      print("UPLOAD ANOTHER")
  else:
     if w==h:
        print("ACCEPTED")
     else:
        print("CROP IT")