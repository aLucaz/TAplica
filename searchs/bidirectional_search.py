def bidirectional_search(problem):
    infinity  = float('inf')
    
    min_edge = problem.find_min_edge()
    gF, gB = {problem.initial : 0}, {problem.goal : 0}
    openF, openB = [problem.initial], [problem.goal]
    closedF, closedB = [], []
    U = infinity

    numBucles = 0

    def extend(U, open_dir, open_other_dir, g_dir, g_other_dir, closed_dir):
        """Extend search in given direction"""
        
        node_state = find_key(C, open_dir, g_dir)

        open_dir.remove(node_state)
        closed_dir.append(node_state)

        for action in problem.actions(node_state):
            path_cost = problem.path_cost(g_dir[node_state], node_state , action)
            if action in open_dir or action in closed_dir:
                if g_dir[action] <= path_cost:
                    continue
                open_dir.remove(action)

            state = action
            g_dir[state] = path_cost
            open_dir.append(state)

            if action in open_other_dir:
                U = min(U, g_dir[action] + g_other_dir[action])

        return U, open_dir, closed_dir, g_dir


    def find_min(open_dir, g):
        """Finds minimum priority, g and f values in open_dir"""
        min_priority, f_min = infinity, infinity
        for node_state in open_dir:
            f_state = g[node_state] + problem.heuristic(node_state)
            priority = max(f_state, 2 * g[node_state])
            min_priority = min(min_priority, priority)
            f_min = min(f_min, f_state)

        return min_priority, f_min, min(g.values())


    def find_key(pr_min, open_dir, g):
        """Finds key in open_dir with value equal to pr_min
        and minimum g value."""
        min_g = infinity
        state = -1
        for node_state in open_dir:
            priority_node = max(g[node_state] + problem.heuristic(node_state), 2*g[node_state])
            if priority_node == pr_min:
                if g[node_state] < min_g:
                    min_g = g[node_state]
                    state = node_state
        return state


    while openF and openB:
        pr_min_f, f_min_f, g_min_f = find_min(openF, gF)
        pr_min_b, f_min_b, g_min_b = find_min(openB, gB)
        C = min(pr_min_f, pr_min_b)
        
        if U <= max(C, f_min_f, f_min_b, g_min_f + g_min_b + min_edge):
            return U, gF , gB , openF , openB , closedF , closedB, numBucles

        numBucles+=1

        #en cada iteracion se debe expandir un nodo con prioridad C, el de menor prioridad
        if C == pr_min_f:
            U, openF, closedF, gF = extend(U, openF, openB, gF, gB, closedF)
        else:            
            U, openB, closedB, gB = extend(U, openB, openF, gB, gF, closedB)

    return infinity