import pulp
from sklearn.metrics import accuracy_score
M = float('Inf')
NUMBER_HOUSES = 3
NUMBER_TANKS = 2
FIXED_CONST_COST_UNIT_VOL = 10
#COST.shape(NUMBER_HOUSES, NUMBER_TANKS)
COST = [[20, 60, 29], [80, 45, 81]]
DEMAND = [15, 20, 10]
SUPPLY = []


#SUPPLY ORIENTED APPROACH
lp_prob0 = pulp.LpProblem("LP0", pulp.LpMinimize)
#variables and bounds
x0 = [[]] #Water transported from jth tank to ith house = x0[j][i]
y0 = [[]] # y0[j][i] = 1 if pipe exists between jth tank and ith house, 0 otherwise
P0 = [0] * NUMBER_TANKS #1 if tank is required at position j, otherwise 0
for j in range(NUMBER_TANKS):
    for i in range(NUMBER_HOUSES):
        print(j,i)
        x0[j].append(pulp.LpVariable(name = 'x{0}{1}'.format(j,i), lowBound = 0, cat = 'Continuous'))
        y0[j].append(pulp.LpVariable(name = 'y{0}{1}'.format(j,i), lowBound = 0, upBound = 1, cat = 'Integer'))

#adding objective
dum = []

for j in range(NUMBER_TANKS): 
    for i in range(NUMBER_HOUSES):
        dum.append(COST[i][j] * y0[j][i] + FIXED_CONST_COST_UNIT_VOL * x0[j][i])

lp_prob0 += pulp.lpSum(line for line in dum)
        
#adding constraints
for i in range(NUMBER_TANKS):
    lp_prob0 += lp.sum(x0[j][i] for j in range(NUMBER_TANKS)) == DEMAND[i]
for j in range(NUMBER_TANKS):
    for i in range(NUMBER_HOUSES):
        lp_prob0 += x[j][i] <= M * y[j][i]
for i in range(NUMBER_HOUSES):
    lp_prob0 += lp.sum(y0[i][j] for j in range(NUMBER_TANKS)) >= 1
status0 = lp_prob0.solve()
if status0 == 1:
    for j in range(NUMBER_TANKS):
        SUPPLY[j] = 0
        for i in range(NUMBER_HOUSES):
            SUPPLY[j] += x0[j][i]
            P0[j] = max(P0[j], y0[j][i])
            
#DEMAND ORIENTED APPROACH
lp_prob = pulp.LpProblem("LP1", pulp.LpMinimize)

#variables and bounds
x = [[]]
y = [[]]
P = []
for i in range(NUMBER_HOUSES):
    for j in range(NUMBER_TANKS):
        x[i].append(pulp.LpVariable('x{0}{1}'.format(i,j), 0, cat = 'Continuous'))
        y[i].append(pulp.LpVariable('y{0}{1}'.format(i,j), 0, cat = 'Binary'))

#adding objective
dum = []

for j in range(NUMBER_TANKS): 
    for i in range(NUMBER_HOUSES):
        dum.append(COST[i][j] * y[j][i] + FIXED_CONST_COST_UNIT_VOL * x[j][i])

lp_prob += pulp.lpSum(line for line in dum)

#adding constraints
for j in range(NUMBER_TANKS):
    lp_prob += lp.sum(x[i][j] for i in range(NUMBER_HOUSES)) == SUPPLY[j]
for i in range(NUMBER_HOUSES):
    for j in range(NUMBER_TANKS):
        lp_prob += x[i][j] <= M * y[i][j]
status = lp_prob.solve()
if status == 1:
    for j in range(NUMBER_TANKS):
        for i in range(NUMBER_HOUSES):
            P[j] = max(P[j], y[i][j])

accuracy_score(np.array(P0), np.array(P))
