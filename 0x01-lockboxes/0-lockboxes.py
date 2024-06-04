#!/usr/bin/python3
"""
0-lockboxes.py - canUnlockAll Module
"""


def canUnlockAll(boxes):
    """A method that determines if all boxes can be opened"""
    if not boxes or type(boxes) is not list:
        return False

    unlocked_boxes = [0]

    for i in unlocked_boxes:
        for key in boxes[i]:
            if key not in unlocked_boxes and key < len(boxes):
                unlocked_boxes.append(key)

    return len(unlocked_boxes) == len(boxes)
