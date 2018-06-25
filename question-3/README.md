# Dependencies
This solution depends on two external libraries:

1. pydash
2. intervaltree

You can install them by running the following command:
```shell
pip install pydash intervaltree
```

# Assumptions
* The solutions assumes a specific representation for the time interval values. In particular time intervals are expected to be a tuple (x, y) where the values for x and y are (hh:mm * 100). E.g. if the interval is (12:15, 16:00) then the solution expects the input to be (1215, 1600).
* The solution doesn't include validation of the input time intervals.