Class Student:
  def __init__(self,name,age,grades):
    self.name = name
    self.age = age
    self.grades = grades
  
  def calc_avg(self):
    if not self.grades:
      return 0
    return sum(self.grades_/len(self.grades)

Class Circle:
  def __init__(self,radius):
    self.radius = radius
  def circumference(self)
    return(2*3.14 * self.radius)



#test class circle by calculating circumference
circle = Circle(5) 
print (circle.circumference())
