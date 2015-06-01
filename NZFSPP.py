import re

# The New Zealand Fire Service (NZFS) uses a specific pager message format
# (UNIT123, UNIT1234) 111-STRU (Alarm Type SMOKE) (Box 123) SOME BUILDING SOME ADDRESS. (XStr A STREET) .JOB DETAILS. #F12345
# the fields (Alarm Type *) and (Box *) are optional and do not appear in every message.


class PagerMessage:

    def __init__(self, message):
        self.message = message

    def appliances(self):
        # Matches appliance names using the consistent four uppercase letters followed by three - four numbers.
        appliances = ','.join(re.findall(r'\w[A-Z]{3}\d[0-9]{2,3}', self.message))
        return appliances

    def source(self):
        # Matches source and job type using the - as a guide, this section is always proceeded by the trucks on the job
        # therefore is always proceeded by a ) and a space. Allows between 3-9 characters either side of the - this is
        # to allow such variations as 111-RESC, CAA-AIRCRAFT etc.
        source = ''.join(re.findall(r'\) ([A-Za-z1-9]{2,8}-[A-Za-z1-9]{2,8})', self.message))
        return source

    def address(self):
        # Gets address by starting at (but ignoring) the job source e.g. -RESC and capturing everything until the next . period
        # the end of the address section always has a period. Uses ?; to ignore up to two sets of brackets that may appear in
        # the string for things such as box numbers or alarm types.
        address = ''.join(re.findall(r'-[A-Z1-9]{2,8}(?: \(Alarm .*?\))?(?: \(Box .*\))? (.*?)\. \(', self.message))
        return address

    def xstr(self):
        # Finds the specified cross streets as they are always within () brackets, each bracket has a space immediately
        # before or after and the work XStr is always present.
        xstr = ''.join(re.findall(r' \((XStr.*?)\) ', self.message))
        return xstr

    def details(self):
        # The job details / description is always contained between two . periods e.g.  .42YOM CARDIAC ARREST.  each period
        # has a space either immediately before or after.
        job_details = ''.join(re.findall(r' \.(.*?)\. ', self.message))
        return job_details

    def job_number(self):
        # Job number is always in the format #F followed by seven digits.  The # is always proceeded by a space.  Allowed
        # between 1 and 8 digits for future proofing.
        job_number = ''.join(re.findall(r' (#F\d{0,7})', sInput))
        return job_number

    def additional_details(self):
        # Get optional Alarm type which is always presented with a space (Alarm
        alarm_detials = ''.join(re.findall(r' \((Alarm .*?)\) ', sInput))

        # Get optional Box type which is always presented with a space (Box
        box_details = ''.join(re.findall(r' (\(Box .*?\))', sInput))

        if alarm_detials != "" and box_details != "":
            ad_info = alarm_detials + ", " + box_details
        elif alarm_detials != "" and box_details == "":
            ad_info = alarm_detials
        elif alarm_detials == "" and box_details != "":
            ad_info = box_details

        return ad_info
