import sys
from optparse import OptionParser


def readInput(inputFile,islog2):
    inputFH=open(inputFile,"r")
    header = inputFH.readline()
    inputfileLines=inputFH.readlines()
    inputFH.close()
    
    # you will get a matrix
    howManyEntries = dict()
    allvals = dict()
    
    
    for eachline in inputfileLines:
        # walk through every line
        dataVals = eachline.strip().split("\t")
#        print eachline
        # the first column will always have the names
        sys.stderr.write("whereami\n")
        for num in range(1,len(dataVals)):
            # if it hasn't been setup before, it has to be established
            if not dataVals[0] in allvals.keys():
                allvals[dataVals[0]] = list()
                howManyEntries[dataVals[0]] = 1
                # should each one be initialized
                for val in range(0,len(dataVals)-1):
                    allvals[dataVals[0]].append(float(0))
            else:
                if num == 1:
                    howManyEntries[dataVals[0]] += 1
                
            if int(islog2) == 1:
                allvals[dataVals[0]][num-1] += 2**float(dataVals[num])
            else:
                allvals[dataVals[0]][num-1] += float(dataVals[num])
    sys.stderr.write("do i get here\n")
    estimateMatrix(allvals, howManyEntries, header)
    
def estimateMatrix(matrix, numProbes, header):
    
    probeNum = 0
    finalAverage = 0
    
    curNum = 0
    print header,
    for curEntry in matrix.keys():
        curNum += 1
        sys.stderr.write(str(curNum)+"\n")
        print curEntry,
        probeNum = numProbes[curEntry]
        for num in range(0,len(matrix)):
            finalAverage = matrix[curEntry][num]/probeNum
            print "\t", finalAverage,
        print "\n",

    
def main(argv):
    parser = OptionParser()
    parser.add_option("-i", "--input", dest="inputfile", help="input file name")
    parser.add_option("-l", "--islog2",dest="islog2", help="data on log scale?")
    (options, args) = parser.parse_args(argv)

    if len(argv) < 5:
        parser.print_help()
        sys.exit()
    elif len(argv)>5:
        print "Too many arguments"
        sys.exit()
    else:
        readInput(options.inputfile,options.islog2)

    
if __name__ == "__main__":
        main(sys.argv)
