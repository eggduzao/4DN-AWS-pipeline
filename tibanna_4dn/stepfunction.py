from .vars import AWS_REGION, AWS_ACCOUNT_NUMBER
from tibanna_ffcommon.stepfunction import StepFunctionFFAbstract


class StepFunctionPony(StepFunctionFFAbstract):

    @property
    def lambda_type(self):
        return 'pony'
