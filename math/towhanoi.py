from datetime import datetime



def moveTower(height, fromPole, toPole, withPole):
	if height >= 1:
		moveTower(height-1, fromPole, withPole, toPole)
		moveDisk(height, fromPole, toPole)
		moveTower(height-1, withPole, toPole, fromPole)

def moveDisk(d, fp, tp):
	print "Moving disk ",d, " from ", fp, " to ", tp

n = input("Enter number of disks\n")
start = datetime.now()
moveTower(n, "A", "B", "C")
print datetime.now() - start