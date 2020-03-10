#!/bin/python3import math
import os
import random
import re
import sys


class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node


def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)


#
# Complete the 'removeKthLinkedListNode' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts following parameters:
#  1. INTEGER_SINGLY_LINKED_LIST head
#  2. INTEGER k
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next


def removeKthLinkedListNode(head, k):

    # get the length of the linked list first
    len = 0
    node = head
    while node:
        len += 1
        node = node.next

    if k > len:
        return head

    # get the kth from the tail:
    k_tail = len-k
    # set up a counter

    # reset the head
    node = head

    # if we need to remove the head
    if k_tail == 0:
        old_head = head
        new_head = node.next
        old_head.next = None
        head = new_head
        return head

    count = 0
    # traverse to the k-1th node
    while count < k_tail-1:
        node = node.next
        count += 1

    # remove the kth node:
    prev_node = node
    kth_node = prev_node.next
    next_node = kth_node.next
    # this is the line that removes the node
    prev_node.next = next_node

    return head

    #point (k-1).next = k+1
    # k.next=null
