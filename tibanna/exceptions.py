import re

# custom exceptions
class AWSEMJobErrorException(Exception):
    """There is an error from a worklow run on the EC2 AWSEM instance."""
    pass


class AWSEMErrorHandler(object):

    class AWSEMError(object):
        def __init__(self, error_type, pattern_in_log):
            self.error_type = error_type
            self.pattern_in_log = pattern_in_log

    ErrorList = [
        AWSEMError('No peak called', 'Exception: File is empty (.+.regionPeak.gz)')
    ]

    #AWSEMErrorExceptionList = [NoPeakException]

    def parse_log(self, log):
        #for ex in self.AWSEMErrorExceptionList:
        for ex in self.ErrorList:
            res = re.search(ex.pattern_in_log, log)
            if res:
                match = res.string[res.regs[0][0]:res.regs[0][1] + 1]
                msg = "%s: %s" % (ex.error_type, match)
                return AWSEMJobErrorException(msg)
        return


class StillRunningException(Exception):
    """EC2 AWSEM instance is still running (job not complete)"""
    pass


class EC2StartingException(Exception):
    """EC2 AWSEM instance is still starting (job not complete)"""
    pass
class DependencyStillRunningException(Exception):
    pass


class DependencyFailedException(Exception):
    pass


class EC2LaunchException(Exception):
    pass


class EC2UnintendedTerminationException(Exception):
    pass


class EC2IdleException(Exception):
    pass


class EC2InstanceLimitException(Exception):
    pass


class EC2InstanceLimitWaitException(Exception):
    pass


class MissingFieldInInputJsonException(Exception):
    pass


class MalFormattedInputJsonException(Exception):
    pass


class MalFormattedPostrunJsonException(Exception):
    pass


class MetricRetrievalException(Exception):
    pass
