from javax.swing import JScrollPane

# internal imports
from path_patterns_table import PathPatternsTable


class PathPatternsPanel(JScrollPane):
    def __init__(self):
        super(PathPatternsPanel, self).__init__(PathPatternsTable())
