#!/usr/bin/env python

import sys

#
# This program simply represents the identity function.
#

# we want to parse the data into usable components
    
def parseData():
    # First line input: (id \t current, previous, neighbors)
    # Every other line: (id \t iteration, current, previous, neighbors)
    for line in sys.stdin:
        splitLine = line.split("\t")
        nodeId = splitLine[0].split(":")[1]
        data = splitLine[1].strip().split(",")
        # If this is a float
        if '.' in data[0]:
            iteration = int(1)
            curr = float(data[0])
            outlinks = data[2:]
        # If this is a non-float iteration value
        else:
            iteration = int(data[0]) + 1
            curr = float(data[1])
            outlinks = data[2:]
            
        outlinksString = ",".join(outlinks)


        # Other output is simply (node, amountOfRankToAddToNode)

        lengthOutlinks = len(outlinks)
        # If there are no outlinks 
        if lengthOutlinks == 0:
            sys.stdout.write("NodeId:%s\t%i,%f\n" % (nodeId, iteration, curr))
            sys.stdout.write("%s\t%f\n" % (nodeId, curr))
        else:
            sys.stdout.write("NodeID:%s\t%i,%f,%s\n" % (nodeId, iteration, curr, outlinksString))
            for neighbor in outlinks:
                # For each line, we need to pass on the information of previous, the current iteration,
                # and neighbors

                sys.stdout.write("%s\t%f\n" % (neighbor, curr/lengthOutlinks))
        # sys.stdout.write("nodeId: %s, iteration: %i, curr: %f, prev: %f, outlinks: %s \n" % (nodeId, iteration, curr, prev, outlinksString))
        
parseData()
