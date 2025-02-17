# coding: utf-8

"""
    Mux API

    Mux is how developers build online video. This API encompasses both Mux Video and Mux Data functionality to help you build your video-related projects better and faster than ever before.  # noqa: E501

    The version of the OpenAPI document: v1
    Contact: devex@mux.com
    Generated by: https://openapi-generator.tech
"""


import inspect
import pprint
import re  # noqa: F401
import six

from mux_python.configuration import Configuration


class RealTimeTimeseriesDatapoint(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'value': 'float',
        'date': 'str',
        'concurrent_viewers': 'int'
    }

    attribute_map = {
        'value': 'value',
        'date': 'date',
        'concurrent_viewers': 'concurrent_viewers'
    }

    def __init__(self, value=None, date=None, concurrent_viewers=None, local_vars_configuration=None):  # noqa: E501
        """RealTimeTimeseriesDatapoint - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._value = None
        self._date = None
        self._concurrent_viewers = None
        self.discriminator = None

        if value is not None:
            self.value = value
        if date is not None:
            self.date = date
        if concurrent_viewers is not None:
            self.concurrent_viewers = concurrent_viewers

    @property
    def value(self):
        """Gets the value of this RealTimeTimeseriesDatapoint.  # noqa: E501


        :return: The value of this RealTimeTimeseriesDatapoint.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this RealTimeTimeseriesDatapoint.


        :param value: The value of this RealTimeTimeseriesDatapoint.  # noqa: E501
        :type value: float
        """

        self._value = value

    @property
    def date(self):
        """Gets the date of this RealTimeTimeseriesDatapoint.  # noqa: E501


        :return: The date of this RealTimeTimeseriesDatapoint.  # noqa: E501
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this RealTimeTimeseriesDatapoint.


        :param date: The date of this RealTimeTimeseriesDatapoint.  # noqa: E501
        :type date: str
        """

        self._date = date

    @property
    def concurrent_viewers(self):
        """Gets the concurrent_viewers of this RealTimeTimeseriesDatapoint.  # noqa: E501


        :return: The concurrent_viewers of this RealTimeTimeseriesDatapoint.  # noqa: E501
        :rtype: int
        """
        return self._concurrent_viewers

    @concurrent_viewers.setter
    def concurrent_viewers(self, concurrent_viewers):
        """Sets the concurrent_viewers of this RealTimeTimeseriesDatapoint.


        :param concurrent_viewers: The concurrent_viewers of this RealTimeTimeseriesDatapoint.  # noqa: E501
        :type concurrent_viewers: int
        """

        self._concurrent_viewers = concurrent_viewers

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = inspect.getargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RealTimeTimeseriesDatapoint):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RealTimeTimeseriesDatapoint):
            return True

        return self.to_dict() != other.to_dict()
