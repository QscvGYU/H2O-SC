# coding = 'utf-8'
from core.exception_ext.parameter_ex import ParameterException


def validate_host(domain_list: []):
    return domain_list


def validate_ip(ip_list: []):
    return ip_list


class BaseRunner(object,):
    def __int__(self, domain_list: [], ip_list: []):
        self.domain_target_list = validate_host(domain_list)
        self.ip_target_list = validate_ip(ip_list)
        self.check_parameters()

    def check_parameters(self):
        if (not self.domain_target_list) or (not self.ip_target_list):
            raise ParameterException("mast have a target (domain or ip)!")
