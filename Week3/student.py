from random import randint


class Student(object):
    """Represents a student."""

    def __init__(self, student_name="", numberOfScores=3):
        """All scores are initially 0."""
        self.student_name = student_name
        self.scoreList = [0, 0, 0]
        self.numberOfScores = numberOfScores
        self.highScore = 0
        self.lowestScore = 0

    def display(self):
        self.getLowestScore()
        self.getHighScore()
        print("Name: ", self.student_name)
        print("Scores: ", self.scoreList)
        print("Highest Score: ", self.highScore)
        print("Lowest Score: ", self.lowestScore)
        print("Average: %.2f" % self.getAverage())
        print()

    def getNumberOfScores(self):
        return self.numberOfScores

    def getName(self):
        return self.student_name

    def setScore(self, i, score):
        self.scoreList[i] = score

    def getScore(self, i):
        return self.scoreList[i]

    def getAverage(self):
        sum = 0
        for i in range(len(self.scoreList)):
            sum += self.scoreList[i]
        return sum / self.numberOfScores

    def getHighScore(self):
        for i in range(len(self.scoreList)):
            if self.scoreList[i] > self.highScore:
                self.highScore = self.scoreList[i]

    def getLowestScore(self):
        self.lowestScore = 100
        for i in range(len(self.scoreList)):
            if (self.scoreList[i]) < self.lowestScore:
                self.lowestScore = self.scoreList[i]


def main(numScores=3):
    """Tests sorting."""
    # Create the list and put 5 students into it
    students = list()
    names = ("Juan", "Bill", "Stacy", "Maria", "Charley")
    for name in names:
        s = Student(name, numScores)
        for index in range(numScores):
            s.setScore(index, randint(70, 100))
        students.append(s)
    # Print the contents
    print("The list of students:\n")
    for s in students:
        s.display()


if __name__ == "__main__":
    main()
