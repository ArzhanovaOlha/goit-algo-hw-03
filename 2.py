from turtle import *
  
def koch_curve(size, order): 
    if order == 0: 
        forward(size) 
        return
    size /= 3.0
    koch_curve(size, order-1) 
    left(60) 
    koch_curve(size, order-1) 
    right(120) 
    koch_curve(size, order-1) 
    left(60) 
    koch_curve(size, order-1) 

def draw_koch_curve(order, size=300):  
    speed(0)                    
    penup()                      
    backward(size/2.0) 
    pendown()            
    for i in range(3):     
        koch_curve(size, order)
        right(120) 
      
    mainloop()  
    
draw_koch_curve(4)