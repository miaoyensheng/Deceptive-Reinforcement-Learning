#! /bin/bash
trap "exit" INT

python2.7 reset.py

NUM_REQUIRED_ARGS=3
num_args=$#

if [ $num_args -lt $NUM_REQUIRED_ARGS ]; then
	echo "Not enough arguments. Call this script with
	${0} <fakeGoal1> <fakeGoal2> <realGoal>"
	exit 1
fi

fakeGoal1=$1
fakeGoal2=$2
realGoal=$3


echo "    " >> overallResults.txt
echo "    " >> overallResults.txt
echo "fake goal 1 position:" $fakeGoal1 >> overallResults.txt
echo "fake goal 2 position:" $fakeGoal2 >> overallResults.txt
echo "real goal position:" $realGoal >> overallResults.txt
echo "    " >> overallResults.txt



python2.7 pacman.py -p PPacmanQAgent -x 1000 -n 1000 -l $realGoal

python2.7 reset.py



python2.7 pacman.py -p FPacmanQAgent -x 500 -n 500 -l $fakeGoal1
python2.7 pacman.py -p F1PacmanQAgent -x 500 -n 500 -l $fakeGoal2
python2.7 pacman.py -p RPacmanQAgent -x 500 -n 500 -l $realGoal




# copy moves as previous moves
python2.7 pacman.py -p FPacmanQAgent -x 500 -n 501 -l $fakeGoal1
python2.7 copyPreviousFakeMoves.py

python2.7 pacman.py -p F1PacmanQAgent -x 500 -n 501 -l $fakeGoal2
python2.7 copyPreviousFakeMoves1.py

python2.7 pacman.py -p RPacmanQAgent -x 500 -n 501 -l $realGoal
python2.7 copyPreviousRealMoves.py




python2.7 pacman.py -p FPacmanQAgent -x 500 -n 501 -l $fakeGoal1
python2.7 copyCurrentFakeMoves.py

python2.7 pacman.py -p F1PacmanQAgent -x 500 -n 501 -l $fakeGoal2
python2.7 copyCurrentFakeMoves1.py

python2.7 pacman.py -p RPacmanQAgent -x 500 -n 501 -l $realGoal
python2.7 copyCurrentRealMoves.py



status=`python2.7 compareAction.py`



python2.7 copyCurrentToPrevious.py

while [ ${status} == False ]
do
  
	python2.7 pacman.py -p FPacmanQAgent -x 500 -n 501 -l $fakeGoal1
	python2.7 copyCurrentFakeMoves.py
	python2.7 pacman.py -p F1PacmanQAgent -x 500 -n 501 -l $fakeGoal2
	python2.7 copyCurrentFakeMoves1.py
	python2.7 pacman.py -p RPacmanQAgent -x 500 -n 501 -l $realGoal
	python2.7 copyCurrentRealMoves.py

	status=`python2.7 compareAction.py`

	python2.7 copyCurrentToPrevious.py

done






















