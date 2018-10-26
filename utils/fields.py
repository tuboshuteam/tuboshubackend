from rest_framework import serializers
from datetime import datetime

from django.core.exceptions import ValidationError



class TimestampField(serializers.DateTimeField):
    """
    Convert a django datetime to/from timestamp.
    """

    def to_representation(self, value):
        """
        Convert the field to its internal representation (aka timestamp)
        :param value: the DateTime value
        :return: a UTC timestamp integer
        """
        # result = super(TimestampField, self).to_representation(value)
        return value.timestamp()

    def to_internal_value(self, value):
        """
        deserialize a timestamp to a DateTime value
        :param value: the timestamp value
        :return: a django DateTime value
        """
        # converted = datetime.fromtimestamp(float('%s' % value))
        # return super(TimestampField, self).to_representation(converted)
        if not value.isdigit():
            raise ValidationError("请输入timestamp")
        return datetime.fromtimestamp(float(value))