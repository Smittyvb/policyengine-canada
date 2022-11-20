from policyengine_canada.model_api import *


class climate_action_incentive_pre_rural(Variable):
    value_type = float
    entity = Household
    label = "Canada Climate Action Incentive before rural suplement"
    unit = CAD
    documentation = "Universal amount without adjustment based on AFNI"
    definition_period = YEAR

    formula = sum_of_variables(
        [
            "climate_action_incentive_single_parent",
            "climate_action_incentive_married",
            "climate_action_incentive_basic",
            "climate_action_incentive_children",
        ]
    )
