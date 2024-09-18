import importlib
import inspect
from django.apps import AppConfig
from calculation.apps import CALCULATION_RULES
from calculation.apps import read_all_calculation_rules

MODULE_NAME = 'calcrule_social_protection'
DEFAULT_CFG = {
    'calculate_business_event': 'calcrule_social_protection.calculate',
    'code_length': 8
}




class CalcruleSocialProtectionConfig(AppConfig):
    name = MODULE_NAME

    calculate_business_event = None
    code_length = None

    def ready(self):
        from core.models import ModuleConfiguration
        cfg = ModuleConfiguration.get_or_default(MODULE_NAME, DEFAULT_CFG)
        read_all_calculation_rules(MODULE_NAME, CALCULATION_RULES )
        self.__load_config(cfg)

    @classmethod
    def __load_config(cls, cfg):
        """
        Load all config fields that match current AppConfig class fields, all custom fields have to be loaded separately
        """
        for field in cfg:
            if hasattr(CalcruleSocialProtectionConfig, field):
                setattr(CalcruleSocialProtectionConfig, field, cfg[field])
