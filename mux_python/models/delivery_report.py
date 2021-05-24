# coding: utf-8

"""
    Mux API

    Mux is how developers build online video. This API encompasses both Mux Video and Mux Data functionality to help you build your video-related projects better and faster than ever before.   # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import inspect
import pprint
import re  # noqa: F401
import six

from mux_python.configuration import Configuration


class DeliveryReport(object):
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
        'live_stream_id': 'str',
        'asset_id': 'str',
        'passthrough': 'str',
        'created_at': 'str',
        'deleted_at': 'str',
        'asset_state': 'str',
        'asset_duration': 'float',
        'delivered_seconds': 'float'
    }

    attribute_map = {
        'live_stream_id': 'live_stream_id',
        'asset_id': 'asset_id',
        'passthrough': 'passthrough',
        'created_at': 'created_at',
        'deleted_at': 'deleted_at',
        'asset_state': 'asset_state',
        'asset_duration': 'asset_duration',
        'delivered_seconds': 'delivered_seconds'
    }

    def __init__(self, live_stream_id=None, asset_id=None, passthrough=None, created_at=None, deleted_at=None, asset_state=None, asset_duration=None, delivered_seconds=None, local_vars_configuration=None):  # noqa: E501
        """DeliveryReport - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._live_stream_id = None
        self._asset_id = None
        self._passthrough = None
        self._created_at = None
        self._deleted_at = None
        self._asset_state = None
        self._asset_duration = None
        self._delivered_seconds = None
        self.discriminator = None

        if live_stream_id is not None:
            self.live_stream_id = live_stream_id
        if asset_id is not None:
            self.asset_id = asset_id
        if passthrough is not None:
            self.passthrough = passthrough
        if created_at is not None:
            self.created_at = created_at
        if deleted_at is not None:
            self.deleted_at = deleted_at
        if asset_state is not None:
            self.asset_state = asset_state
        if asset_duration is not None:
            self.asset_duration = asset_duration
        if delivered_seconds is not None:
            self.delivered_seconds = delivered_seconds

    @property
    def live_stream_id(self):
        """Gets the live_stream_id of this DeliveryReport.  # noqa: E501

        Unique identifier for the live stream that created the asset.  # noqa: E501

        :return: The live_stream_id of this DeliveryReport.  # noqa: E501
        :rtype: str
        """
        return self._live_stream_id

    @live_stream_id.setter
    def live_stream_id(self, live_stream_id):
        """Sets the live_stream_id of this DeliveryReport.

        Unique identifier for the live stream that created the asset.  # noqa: E501

        :param live_stream_id: The live_stream_id of this DeliveryReport.  # noqa: E501
        :type live_stream_id: str
        """

        self._live_stream_id = live_stream_id

    @property
    def asset_id(self):
        """Gets the asset_id of this DeliveryReport.  # noqa: E501

        Unique identifier for the asset.  # noqa: E501

        :return: The asset_id of this DeliveryReport.  # noqa: E501
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        """Sets the asset_id of this DeliveryReport.

        Unique identifier for the asset.  # noqa: E501

        :param asset_id: The asset_id of this DeliveryReport.  # noqa: E501
        :type asset_id: str
        """

        self._asset_id = asset_id

    @property
    def passthrough(self):
        """Gets the passthrough of this DeliveryReport.  # noqa: E501

        The `passthrough` value for the asset.  # noqa: E501

        :return: The passthrough of this DeliveryReport.  # noqa: E501
        :rtype: str
        """
        return self._passthrough

    @passthrough.setter
    def passthrough(self, passthrough):
        """Sets the passthrough of this DeliveryReport.

        The `passthrough` value for the asset.  # noqa: E501

        :param passthrough: The passthrough of this DeliveryReport.  # noqa: E501
        :type passthrough: str
        """

        self._passthrough = passthrough

    @property
    def created_at(self):
        """Gets the created_at of this DeliveryReport.  # noqa: E501

        Time at which the asset was created. Measured in seconds since the Unix epoch.  # noqa: E501

        :return: The created_at of this DeliveryReport.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this DeliveryReport.

        Time at which the asset was created. Measured in seconds since the Unix epoch.  # noqa: E501

        :param created_at: The created_at of this DeliveryReport.  # noqa: E501
        :type created_at: str
        """

        self._created_at = created_at

    @property
    def deleted_at(self):
        """Gets the deleted_at of this DeliveryReport.  # noqa: E501

        If exists, time at which the asset was deleted. Measured in seconds since the Unix epoch.  # noqa: E501

        :return: The deleted_at of this DeliveryReport.  # noqa: E501
        :rtype: str
        """
        return self._deleted_at

    @deleted_at.setter
    def deleted_at(self, deleted_at):
        """Sets the deleted_at of this DeliveryReport.

        If exists, time at which the asset was deleted. Measured in seconds since the Unix epoch.  # noqa: E501

        :param deleted_at: The deleted_at of this DeliveryReport.  # noqa: E501
        :type deleted_at: str
        """

        self._deleted_at = deleted_at

    @property
    def asset_state(self):
        """Gets the asset_state of this DeliveryReport.  # noqa: E501

        The state of the asset.  # noqa: E501

        :return: The asset_state of this DeliveryReport.  # noqa: E501
        :rtype: str
        """
        return self._asset_state

    @asset_state.setter
    def asset_state(self, asset_state):
        """Sets the asset_state of this DeliveryReport.

        The state of the asset.  # noqa: E501

        :param asset_state: The asset_state of this DeliveryReport.  # noqa: E501
        :type asset_state: str
        """
        allowed_values = ["ready", "errored", "deleted"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and asset_state not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `asset_state` ({0}), must be one of {1}"  # noqa: E501
                .format(asset_state, allowed_values)
            )

        self._asset_state = asset_state

    @property
    def asset_duration(self):
        """Gets the asset_duration of this DeliveryReport.  # noqa: E501

        The duration of the asset in seconds.  # noqa: E501

        :return: The asset_duration of this DeliveryReport.  # noqa: E501
        :rtype: float
        """
        return self._asset_duration

    @asset_duration.setter
    def asset_duration(self, asset_duration):
        """Sets the asset_duration of this DeliveryReport.

        The duration of the asset in seconds.  # noqa: E501

        :param asset_duration: The asset_duration of this DeliveryReport.  # noqa: E501
        :type asset_duration: float
        """

        self._asset_duration = asset_duration

    @property
    def delivered_seconds(self):
        """Gets the delivered_seconds of this DeliveryReport.  # noqa: E501

        Total number of delivered seconds during this time window.  # noqa: E501

        :return: The delivered_seconds of this DeliveryReport.  # noqa: E501
        :rtype: float
        """
        return self._delivered_seconds

    @delivered_seconds.setter
    def delivered_seconds(self, delivered_seconds):
        """Sets the delivered_seconds of this DeliveryReport.

        Total number of delivered seconds during this time window.  # noqa: E501

        :param delivered_seconds: The delivered_seconds of this DeliveryReport.  # noqa: E501
        :type delivered_seconds: float
        """

        self._delivered_seconds = delivered_seconds

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
        if not isinstance(other, DeliveryReport):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeliveryReport):
            return True

        return self.to_dict() != other.to_dict()
