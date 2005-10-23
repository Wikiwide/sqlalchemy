from testbase import PersistTest
import sqlalchemy.util as util
import unittest, sys, os

class thingy(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return "thingy(%d, %s)" % (id(self), self.name)
    def __str__(self):
        return repr(self)
        
class DependencySortTest(PersistTest):
    def testsort(self):
        rootnode = thingy('root')
        node2 = thingy('node2')
        node3 = thingy('node3')
        node4 = thingy('node4')
        subnode1 = thingy('subnode1')
        subnode2 = thingy('subnode2')
        subnode3 = thingy('subnode3')
        subnode4 = thingy('subnode4')
        subsubnode1 = thingy('subsubnode1')
        tuples = [
            (subnode3, subsubnode1),
            (node2, subnode1),
            (node2, subnode2),
            (rootnode, node2),
            (rootnode, node3),
            (rootnode, node4),
            (node4, subnode3),
            (node4, subnode4)
        ]
        head = util.DependencySorter(tuples, []).sort()
        print str(head)

    def testsort2(self):
        node1 = thingy('node1')
        node2 = thingy('node2')
        node3 = thingy('node3')
        node4 = thingy('node4')
        node5 = thingy('node5')
        node6 = thingy('node6')
        node7 = thingy('node7')
        tuples = [
            (node1, node2),
            (node3, node4),
            (node5, node6),
            (node6, node2)
        ]
        head = util.DependencySorter(tuples, [node7]).sort()
        print "\n" + str(head)



if __name__ == "__main__":
    unittest.main()
