class Employee:
    company = "Google"

    def getcompany(self):
        print("Company is " + self.company + " and your copany which ?")
        print(f"Company is {self.company} and your copany which ?")
#             ^
#             | 
#             |
#             | 
#             | 
#             | 
#             |
# 
# with f we have to {self.company} for print company
#  
maggie = Employee()

maggie.getcompany()



# print method

# print("Company is " + self.company + " and your copany which ?")
# print(f"Company is {self.company} and your copany which ?")