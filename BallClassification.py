from sklearn import tree

def MysterioML(weight,surface):
  BallsFeatures = [[35,1],[47.1],[90,0],[48,1],[90,0],[35,1],[92,0],[35,1],[35,1],[35,1],[96,0],[43,1],[110,0],
                  [35,1],[95,0]]
  
  Names = [1,1,2,1,2,1,2,1,1,1,2,1,2,1,2]
  
  clf = tree.DecesionTreeClassifier()
  
  clf = clf.fit(BallsFeature,Names)
  
  result = clf.predict([[weight,surface]])
  
  if result == 1:
    print("Your object looks like Tennis Ball")
    
  elif result == 2:
    print("Your object looks like Cricket Ball")
    
def main():
  print("-------------Machine Learning------------")
  
  print("Enter weight of object")
  weight = input()
  
  print("What is ye surface type of your object Rough or smooth")
  
  surface = input()
  if surface.lower() == "rough":
    surface = 1
  elif surface.lower() == "smooth":
    surface = 0
  else:
    print("Error:Wrong input")
    exit()
  MysterioML(weight,surface)
if __name__ == "__main__":
  main()
