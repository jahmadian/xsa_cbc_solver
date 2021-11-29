import pulp
import networkx as nx


def pulp_solver(solve=1):
    model = pulp.LpProblem("Profit maximising problem", pulp.LpMaximize)
    A = pulp.LpVariable('A', lowBound=0, cat='Integer')
    B = pulp.LpVariable('B', lowBound=0, cat='Integer')

    # Objective function
    model += 30000 * A + 45000 * B, "Profit"

    # Constraints
    model += 3 * A + 4 * B <= 30
    model += 5 * A + 6 * B <= 60
    model += 1.5 * A + 3 * B <= 21
    solver = pulp.PULP_CBC_CMD(msg=True)
    # Solve the problem
    er1 = ""
    if solve == 1:
        try:
            model.solve(solver)
        except OSError as error:
            print(error)
            er1 = "   =====-------" + str(error)

    print('The status of the solution is', pulp.LpStatus[model.status])

    # Print our decision variable values
    print("Production of Car A = {}".format(A.varValue))
    print("Production of Car B = {}".format(B.varValue))

    # Print our objective function value
    print(pulp.value(model.objective))

    msg = 'The status of the solution is ' + str(
        pulp.LpStatus[model.status]) + '\n <br> ' + "Production of Car A = {}".format(
        A.varValue) + '\n <br> ' + "Production of Car B = {}".format(B.varValue) + '\n <br> ' + str(pulp.value(model.objective)) + \
          '\n <br> ' + er1

    return msg
