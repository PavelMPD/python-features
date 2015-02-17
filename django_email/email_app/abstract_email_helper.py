from abc import ABCMeta, abstractmethod


class AbstractEmailHelper():
    __metaclass__ = ABCMeta

    @abstractmethod
    def send_info_email(self):
        """Send information email"""