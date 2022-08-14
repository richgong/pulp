from pulp import LpMaximize, LpProblem, LpStatus, lpSum, LpVariable


model = LpProblem(name="small-problem", sense=LpMaximize)

x = LpVariable(name="x", lowBound=0)
y = LpVariable(name="y", lowBound=0)

# expression = 2 * x + 4 * y
# constraint = 2 * x + 4 * y >= 8

model += (2 * x + y <= 20, "red_constraint")
model += (4 * x - 5 * y >= -10, "blue_constraint")
model += (-x + 2 * y >= -2, "yellow_constraint")
model += (-x + 5 * y == 15, "green_constraint")

# Add the objective function to the model
obj_func = x + 2 * y
model += obj_func
