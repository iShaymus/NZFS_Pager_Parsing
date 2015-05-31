import re
import sys

sInput = str(sys.argv[1:])

# Matches appliance names using the consistent four uppercase letters followed by three - four numbers.
pTrucks = ','.join(re.findall(r'\w[A-Z]{3}\d[0-9]{2,3}', sInput))

# Matches source and job type using the - as a guide, this section is always proceeded by the trucks on the job
# therefore is always proceeded by a ) and a space. Allows between 3-9 characters either side of the - this is
# to allow such variations as 911-RESC, FAA-AIRCRAFT etc.
pJobSource = ''.join(re.findall(r'\) ([A-Za-z1-9]{2,8}-[A-Za-z1-9]{2,8})', sInput))

# Gets address by starting at (but ignoring) the job source e.g. -RESC and capturing everything until the next . period
# the end of the address section always has a period. Uses ?; to ignore up to two sets of brackets that may appear in
# the string for things such as box numbers or alarm types.
pAddress = ''.join(re.findall(r'-[A-Z1-9]{2,8}(?: \(Alarm .*?\))?(?: \(Box .*\))? (.*?)\. \(', sInput))

# Finds the specified cross streets as they are always within () brackets, each bracket has a space immediately
# before or after and the work XStr is always present.
pCrossStreet = ''.join(re.findall(r' \((XStr.*?)\) ', sInput))

# The job details / description is always contained between two . periods e.g.  .42YOM CARDIAC ARREST.  each period
# has a space either immediately before or after.
pJobDetails = ''.join(re.findall(r' \.(.*?)\. ', sInput))

# Job number is always in the format #F followed by seven digits.  The # is always proceeded by a space.  Allowed
# between 1 and 8 digits for future proofing.
pJobNumber = ''.join(re.findall(r' (#F\d{0,7})', sInput))

# Get optional Alarm type which is always presented with a space (Alarm
pAlarmDetails = ''.join(re.findall(r' \((Alarm .*?)\) ', sInput))

# Get optional Box type which is always presented with a space (Box
pBoxDetails = ''.join(re.findall(r' (\(Box .*?\))', sInput))

print "Responding Trucks:  " + pTrucks
print "Job Source / Type:  " + pJobSource
print "Address:            " + pAddress
print "Cross Streets:      " + pCrossStreet
print "Job Details:        " + pJobDetails
print "Additional Info:    " + pAlarmDetails + ", " + pBoxDetails
print "\n\nJob Number:         " + pJobNumber