#RandomTriangle
#Math 261
#Aiden Ramos

import random as R

while True:    
    user_input = int(input("How many trials would you like to run? "))
    
    for i in range(user_input):
        
    
        #size of sqaure
        SqrSize=5
    
        #function to get the random points
        def Get_Points(size):
            #list to hold random pts
            points=[]
            
            for i in range (3):
                #randomly gets a point x and y
                x=round(R.uniform(0,size+1),2)
                y=round(R.uniform(0,size+1),2)
                #then combines them as a single point
                pt=(x,y)
                #then appends it to the point list
                points.append(pt)
            return points
    
        #distance function
        def Get_Distance(P1,P2):
            #formula to get the distance of a point
            dist_x=P2[0]-P1[0]
            dist_y=P2[1]-P1[1]
            #returns the answer to the user for the point
            return (dist_x**2+dist_y**2)**0.5
    
        #gets the random points
        Pts=Get_Points(5)
        #gets the distance of the points
        #rounds each to two deciaml places
        A=round(Get_Distance(Pts[0],Pts[1]),2)
        B=round(Get_Distance(Pts[1],Pts[2]),2)
        C=round(Get_Distance(Pts[2],Pts[0]),2)
    
        
    
    
        def Get_Perimeter(P1,P2,P3):
            return (P1+P2+P3)
    
        Perimeter=round(Get_Perimeter(A,B,C),2)
    
        
    
        def Get_Area(S1,S2,S3):
            s = ((S1+S2+S3)/2)
            return (s *(s-S1)*(s-S2)*(s-S3))**0.5
    
        Area=round(Get_Area(A,B,C),2)
    
        print(f"\nThe area of triangle {i+1} is {Area}")
        print(f"The perimter of triangle {i+1} is {Perimeter}")
            
            
    print("\nIf you would like to run another simulation, press enter")
    UserStatus=input("If you would lile to quit,enter q: ").lower()
    if UserStatus=="q":
        break


            