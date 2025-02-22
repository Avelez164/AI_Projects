# Worked on Project: Antonio Velez
from search import *

class MissCannibalsVariant(Problem):
    def __init__(self, N1=4, N2=4, goal=(0, 0, False)):
        """ Define goal state and initialize a problem """
        initial = (N1, N2, True)
        self.N1 = N1
        self.N2 = N2
        super().__init__(initial, goal)

    def actions(self, state):
        possible_actions = []
        m, c, on_left = state

        if on_left:
            for m_count in range(min(m, 3) + 1):
                for c_count in range(min(c, 3 - m_count) + 1):
                    if m_count + c_count >= 1 and m_count + c_count <= 3:
                        if (m - m_count >= c - c_count or m - m_count == 0) and (self.N1 - m + m_count >= self.N2 - c + c_count or self.N1 - m + m_count == 0):
                            action = 'M' * m_count + 'C' * c_count
                            possible_actions.append(action)
        else:
            for m_count in range(min(self.N1 - m, 3) + 1):
                for c_count in range(min(self.N2 - c, 3 - m_count) + 1):
                    if m_count + c_count >= 1 and m_count + c_count <= 3:
                        if (m + m_count >= c + c_count or m + m_count == 0) and (self.N1 - m - m_count >= self.N2 - c - c_count or self.N1 - m - m_count == 0):
                            action = 'M' * m_count + 'C' * c_count
                            possible_actions.append(action)

        return possible_actions

    def result(self, state, action):
        m, c, on_left = state
        m_count = action.count('M')
        c_count = action.count('C')

        if on_left:
            new_state = (m - m_count, c - c_count, False)
        else:
            new_state = (m + m_count, c + c_count, True)

        return new_state

if __name__ == '__main__':
    mc = MissCannibalsVariant(4, 4)
    #print(mc.actions((3, 3, True))) # Test your code as you develop! This should return ['MC', 'MMM']
    
    path = depth_first_graph_search(mc).solution()
    print(path)
    path = breadth_first_graph_search(mc).solution()
    print(path)