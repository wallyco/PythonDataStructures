"""
File: bstnode.py
Author: Ken Lambert
"""

class BTNode(object):
    """Represents a node for a linked binary tree."""

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
