#! /bin/bash
trap "exit" INT

python2.7 reset.py
python2.7 resetPenalty.py

NUM_REQUIRED_ARGS=2
num_args=$#

if [ $num_args -lt $NUM_REQUIRED_ARGS ]; then
	echo "Not enough arguments. Call this script with
	${0} <fakeGoal> <realGoal>"
	exit 1
fi

fakeGoal=$1
realGoal=$2

echo "    " >> overallResults.txt
echo "    " >> overallResults.txt
echo "fake goal position:" $fakeGoal >> overallResults.txt
echo "real goal position:" $realGoal >> overallResults.txt
echo "    " >> overallResults.txt



python2.7 pacman.py -p PPacmanQAgent -x 500 -n 501 -l $realGoal

python2.7 reset.py



# python2.7 pacman.py -p FPacmanQAgent -x 500 -n 500 -l $fakeGoal
# python2.7 pacman.py -p RPacmanQAgent -x 500 -n 500 -l $realGoal

# # copy moves as previous moves
# python2.7 pacman.py -p FPacmanQAgent -x 500 -n 501 -l $fakeGoal
# python2.7 copyPreviousFakeMoves.py
# python2.7 pacman.py -p RPacmanQAgent -x 500 -n 501 -l $realGoal
# python2.7 copyPreviousRealMoves.py

# python2.7 pacman.py -p FPacmanQAgent -x 500 -n 501 -l $fakeGoal
# python2.7 copyCurrentFakeMoves.py
# python2.7 pacman.py -p RPacmanQAgent -x 500 -n 501 -l $realGoal
# python2.7 copyCurrentRealMoves.py

# status=`python2.7 compareAction.py`

# python2.7 copyCurrentToPrevious.py

# while [ ${status} == False ]
# do
  
# 	python2.7 pacman.py -p FPacmanQAgent -x 500 -n 501 -l $fakeGoal
# 	python2.7 copyCurrentFakeMoves.py
# 	python2.7 pacman.py -p RPacmanQAgent -x 500 -n 501 -l $realGoal
# 	python2.7 copyCurrentRealMoves.py

# 	status=`python2.7 compareAction.py`

# 	python2.7 copyCurrentToPrevious.py

# done