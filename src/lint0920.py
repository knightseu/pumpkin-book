# meeting is a list of tuple (si, ei)
def isConflict(meetings: []):
    meetings.sort()
    prev = meetings[0]
    for meeting in meetings[1:]:
        if prev[1] > meeting[0]:
            return True
        prev = meeting
    return False

print(isConflict([(0, 30), (15, 20), (5, 10)]))
print(isConflict([(0, 4), (15, 20), (5, 10)]))


# A more efficient algorithm, if when range is limited and number of intervals are high.