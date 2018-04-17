# -*- coding: utf-8 -*-
"""
Created on  Feb 27 2018

@author: frederic

Scaffholding code for CAB320 Assignment One

This is the only file that you have to modify and submit for the assignment.

"""

import numpy as np

import itertools

import generic_search

from assignment_one import (TetrisPart, AssemblyProblem, offset_range, 
                            display_state, 
                            make_state_canonical, play_solution, 
                            load_state, make_random_state
                            )
#tetrispart = TetrisPart()

# ---------------------------------------------------------------------------

def print_the_team():
    '''
    Print details of the members of your team 
    (full name + student number)
    '''
    
    #raise NotImplementedError

    print('Kunxian Liu, 9158090')
#    print('Grace Hopper, 12340002')
#    print('Maryam Mirzakhani, 12340003')
    
# ---------------------------------------------------------------------------
        
def appear_as_subpart(some_part, goal_part):
    '''    
    Determine whether the part 'some_part' appears in another part 'goal_part'.
    
    Formally, we say that 'some_part' appears in another part 'goal_part',
    when the matrix representation 'S' of 'some_part' is a a submatrix 'M' of
    the matrix representation 'G' of 'goal_part' and the following constraints
    are satisfied:
        for all indices i,j
            S[i,j] == 0 or S[i,j] == M[i,j]
            
    During an assembly sequence that does not use rotations, any part present 
    on the workbench has to appear somewhere in a goal part!
    
    @param
        some_part: a tuple representation of a tetris part
        goal_part: a tuple representation of another tetris part
        
    @return
        True if 'some_part' appears in 'goal_part'
        False otherwise    
    '''
    
    #raise NotImplementedError
    #return TetrisPart.get_height
    #return TetrisPart.get_width

    ps = np.array(some_part)  #
    pg = np.array(goal_part)
    
    psT = TetrisPart(ps)
    pgT = TetrisPart(pg)
    
    ps_h = psT.get_height()
    ps_w = psT.get_width()
    #get rows and cols from some_part
        
    pg_h = pgT.get_height()
    pg_w = pgT.get_width()
    #get rows and cols from goal_part
        
    #for each col of each row in goal_part
    for i in range(pg_h-ps_h+1):
        for j in range(pg_w-ps_w+1):
        #if the first index of some part matches a index of goal part  
            if ps[0][0] == pg[i][j]:
                #numpy function of extracting a matrix from a large matrix.
                def submatrix ( matrix, startRow, startCol, size1, size2):
                    return pg[startRow:startRow+size1,startCol:startCol+size2]
                    #form matrix for comparison 
                pm = submatrix (pg, i, j, ps_h,ps_w)
                #
                ps_nonzero_index = np.nonzero(ps)
                #
                ps_nonzero=ps[ps_nonzero_index]
                pm_nonzero=pm[ps_nonzero_index]
                #comparing if the selected matrix from goal part is equal to some part.
                if np.array_equal(ps_nonzero,pm_nonzero):
                    return True# return true if appears
    return False

# ---------------------------------------------------------------------------
        
def cost_rotated_subpart(some_part, goal_part):
    '''    
    Determine whether the part 'some_part' appears in another part 'goal_part'
    as a rotated subpart. If yes, return the number of 'rotate90' needed, if 
    no return 'np.inf'
    
    The definition of appearance is the same as in the function 
    'appear_as_subpart'.
                   
    @param
        some_part: a tuple representation of a tetris part
        goal_part: a tuple representation of another tetris part
    
    @return
        the number of rotation needed to see 'some_part' appear in 'goal_part'
        np.inf  if no rotated version of 'some_part' appear in 'goal_part'
    
    '''
    '''
    compare subpart to goal_part
    do you need to rotate?
    no? -> sub_part == goal part
    rotate_counter=np.inf
    yes-> rotate-> (assignment_one) -> assignment_one.rotate90()
    rotate_counter=rotate_counter+1
    loop until sub_part == goal_part OR rotate_counter == 4 (360deg)
    '''
#    raise NotImplementedError
    rotate_counter = 0
    
    while rotate_counter < 4:
        ps = np.array(some_part)  #
        pg = np.array(goal_part)
    
        psT = TetrisPart(ps)
        pgT = TetrisPart(pg)
        
        if appear_as_subpart(ps,pg) == False:
            psT.rotate90()
            rotate_counter += 1
        #do rotation
        #com
    
    
# ---------------------------------------------------------------------------

class AssemblyProblem_1(AssemblyProblem):
    '''
    
    Subclass of 'assignment_one.AssemblyProblem'
    
    * The part rotation action is not available for AssemblyProblem_1 *

    The 'actions' method of this class simply generates
    the list of all legal actions. The 'actions' method of this class does 
    *NOT* filtered out actions that are doomed to fail. In other words, 
    no pruning is done in the 'actions' method of this class.
        
    '''

    def __init__(self, initial, goal=None):
        """The constructor specifies the initial state, and possibly a goal
        state, if there is a unique goal.  Your subclass's constructor can add
        other arguments."""
        if goal is None:
            self.goal = AssemblyProblem.goal
        else:
            self.goal = goal
        if initial:
            self.initial = initial
        else:
            self.inital = AssemblyProblem.initial
        self.initial = tuple(self.initial)
        self.goal = tuple(self.goal)
        # Call the parent class constructor.
        # Here the parent class is 'AssemblyProblem' 
        # which itself is derived from 'generic_search.Problem'
        super(AssemblyProblem_1, self).__init__(initial, goal, use_rotation=False)
    
    def actions(self, state):
        """
        Return the actions that can be executed in the given
        state. The result would typically be a list, but if there are
        many actions, consider yielding them one at a time in an
        iterator, rather than building them all at once.
        
        @param
          state : a state of an assembly problem.
        
        @return 
           the list of all legal drop actions available in the 
            state passed as argument.
        
        """
        #Make a copy of the state as a list
        part_list=listt(state)
        # Make an empty array to append all legal actions (pa,pu, offset)
        action_list = []

        for pa,pu in itertools.permutations(part_list,2):
        # returns the permutation of the pa, pu pair
          start, end = offset_range(pa, pu)
          # Returns start, end
          for offset in range(start, end):
            action_list.append((pa, pu, offset))
  
        # This nested for loop will return all permutation of the pairs with a valid offset range[)
        # The range will include the start value and exclude the end value (to help with pythonic indexing)
    
        return action_list
        
    #stacking
     #Yes
    #rotating?
     #No

    def result(self, state, action):
        """
        Return the state (as a tuple of parts in canonical order)
        that results from executing the given
        action in the given state. The action must be one of
        self.actions(state).
        
        @return
          a state in canonical order
        
        """
        # Here a workbench state is a frozenset of parts
        #Extract the values from action
        pa,pu,offset=action
        # Make a new TetrisPart Object with the given action
        new_part = TetrisPart(pa, pu, offset)
        # Make a copy of the state as a list type
        state_list=list(state)
        # Dequeue pa,pu from the list
        state_list.remove(pa)
        state_list.remove(pu)
        # Queue the new_part into the list
        state_list.append(new_part)
        # This effectively "stacks" the pa & pu together at the specified offset
        # Make the state_list canonical to make sure it is in the correct order
        state_list = make_canonical(state_list)
        # Return a tuple of tuples
        return tuple(state_list)
# ---------------------------------------------------------------------------

class AssemblyProblem_2(AssemblyProblem_1):
    '''
    
    Subclass of 'assignment_one.AssemblyProblem'
        
    * Like for AssemblyProblem_1,  the part rotation action is not available 
       for AssemblyProblem_2 *

    The 'actions' method of this class  generates a list of legal actions. 
    But pruning is performed by detecting some doomed actions and 
    filtering them out.  That is, some actions that are doomed to 
    fail are not returned. In this class, pruning is performed while 
    generating the legal actions.
    However, if an action 'a' is not doomed to fail, it has to be returned. 
    In other words, if there exists a sequence of actions solution starting 
    with 'a', then 'a' has to be returned.
        
    '''

    def __init__(self, initial, goal=None):
        """The constructor specifies the initial state, and possibly a goal
        state, if there is a unique goal.  Your subclass's constructor can add
        other arguments."""
        # Call the parent class constructor.
        # Here the parent class is 'AssemblyProblem' 
        # which itself is derived from 'generic_search.Problem'
        super(AssemblyProblem_2, self).__init__(initial, goal)
    
    def actions(self, state):
        """
        Return the actions that can be executed in the given
        state. The result would typically be a list, but if there are
        many actions, consider yielding them one at a time in an
        iterator, rather than building them all at once.
        
        A candidate action is eliminated if and only if the new part 
        it creates does not appear in the goal state.
        """
        #Make an empty list to append pruned actions
        action_list=[]
        # Make a copy of the state as a list
        state_list=list(state)
        
        # Make a similar nested for loop as AssemblyProblem_1
        for pa,pu in itertools.permutations(state_list,2):
          
          start, end = offset_range(pa, pu)
          # Returns start, end
          for offset in range(start, end):
            # Make a TetrisPart of the pa,pu and offset to get a value for TetrisPart.offset
            temp_piece=TetrisPart(pa,pu,offset)
            
            # Pruning
            # If valid piece, append the action
            # Does it appear in the goal state?
            if temp_piece.offset!=None and appear_as_subpart(temp_piece,self.goal):
              action_list.append((pa, pu, offset))
        
        return action_list

# ---------------------------------------------------------------------------

class AssemblyProblem_3(AssemblyProblem_1):
    '''
    
    Subclass 'assignment_one.AssemblyProblem'
    
    * The part rotation action is available for AssemblyProblem_3 *

    The 'actions' method of this class simply generates
    the list of all legal actions including rotation. 
    The 'actions' method of this class does 
    *NOT* filter out actions that are doomed to fail. In other words, 
    no pruning is done in this method.
        
    '''

    def __init__(self, initial, goal=None):
        """The constructor specifies the initial state, and possibly a goal
        state, if there is a unique goal.  Your subclass's constructor can add
        other arguments."""
        # Call the parent class constructor.
        # Here the parent class is 'AssemblyProblem' 
        # which itself is derived from 'generic_search.Problem'
        super(AssemblyProblem_3, self).__init__(initial, goal)
        self.use_rotation = True

    
    def actions(self, state):
        """Return the actions that can be executed in the given
        state. The result would typically be a list, but if there are
        many actions, consider yielding them one at a time in an
        iterator, rather than building them all at once.
        
        Rotations are allowed, but no filtering out the actions that 
        lead to doomed states.
        
        """
        #

        raise NotImplementedError

        
    def result(self, state, action):
        """
        Return the state that results from executing the given
        action in the given state. The action must be one of
        self.actions(state).

        The action can be a drop or rotation.        
        """
        # Here a workbench state is a frozenset of parts        
 
        raise NotImplementedError


# ---------------------------------------------------------------------------

class AssemblyProblem_4(AssemblyProblem_3):
    '''
    
    Subclass 'assignment_one.AssemblyProblem3'
    
    * Like for its parent class AssemblyProblem_3, 
      the part rotation action is available for AssemblyProblem_4  *

    AssemblyProblem_4 introduces a simple heuristic function and uses
    action filtering.
    See the details in the methods 'self.actions()' and 'self.h()'.
    
    '''

    def __init__(self, initial, goal=None):
        """The constructor specifies the initial state, and possibly a goal
        state, if there is a unique goal.  Your subclass's constructor can add
        other arguments."""
        # Call the parent class constructor.
        # Here the parent class is 'AssemblyProblem' 
        # which itself is derived from 'generic_search.Problem'
        super(AssemblyProblem_4, self).__init__(initial, goal)

    def actions(self, state):
        """Return the actions that can be executed in the given
        state. The result would typically be a list, but if there are
        many actions, consider yielding them one at a time in an
        iterator, rather than building them all at once.
        
        Filter out actions (drops and rotations) that are doomed to fail 
        using the function 'cost_rotated_subpart'.
        A candidate action is eliminated if and only if the new part 
        it creates does not appear in the goal state.
        This should  be checked with the function "cost_rotated_subpart()'.
                
        """

        raise NotImplementedError
        
        
        
    def h(self, n):
        '''
        This heuristic computes the following cost; 
        
           Let 'k_n' be the number of parts of the state associated to node 'n'
           and 'k_g' be the number of parts of the goal state.
          
        The cost function h(n) must return 
            k_n - k_g + max ("cost of the rotations")  
        where the list of cost of the rotations is computed over the parts in 
        the state 'n.state' according to 'cost_rotated_subpart'.
        
        
        @param
          n : node of a search tree
          
        '''

        raise NotImplementedError

# ---------------------------------------------------------------------------
        
def solve_1(initial, goal):
    '''
    Solve a problem of type AssemblyProblem_1
    
    The implementation has to 
    - use an instance of the class AssemblyProblem_1
    - make a call to an appropriate functions of the 'generic_search" library
    
    @return
        - the string 'no solution' if the problem is not solvable
        - otherwise return the sequence of actions to go from state
        'initial' to state 'goal'
    
    '''

    print('\n++  busy searching in solve_1() ...  ++\n')
    raise NotImplementedError
    
    # assembly_problem = AssemblyProblem_1(initial, goal) # HINT
    

# ---------------------------------------------------------------------------
        
def solve_2(initial, goal):
    '''
    Solve a problem of type AssemblyProblem_2
    
    The implementation has to 
    - use an instance of the class AssemblyProblem_2
    - make a call to an appropriate functions of the 'generic_search" library
    
    @return
        - the string 'no solution' if the problem is not solvable
        - otherwise return the sequence of actions to go from state
        'initial' to state 'goal'
    
    '''

    print('\n++  busy searching in solve_2() ...  ++\n')
    raise NotImplementedError
    

# ---------------------------------------------------------------------------
        
def solve_3(initial, goal):
    '''
    Solve a problem of type AssemblyProblem_3
    
    The implementation has to 
    - use an instance of the class AssemblyProblem_3
    - make a call to an appropriate functions of the 'generic_search" library
    
    @return
        - the string 'no solution' if the problem is not solvable
        - otherwise return the sequence of actions to go from state
        'initial' to state 'goal'
    
    '''

    print('\n++  busy searching in solve_3() ...  ++\n')
    raise NotImplementedError
    
# ---------------------------------------------------------------------------
        
def solve_4(initial, goal):
    '''
    Solve a problem of type AssemblyProblem_4
    
    The implementation has to 
    - use an instance of the class AssemblyProblem_4
    - make a call to an appropriate functions of the 'generic_search" library
    
    @return
        - the string 'no solution' if the problem is not solvable
        - otherwise return the sequence of actions to go from state
        'initial' to state 'goal'
    
    '''

    #         raise NotImplementedError
    print('\n++  busy searching in solve_4() ...  ++\n')
    raise NotImplementedError
        
# ---------------------------------------------------------------------------


    
if __name__ == '__main__':
    appear_as_subpart()
    #cost_rotated_subpart():
    
