# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView

from measurement.models import Sensor, Measurement
from measurement.serializers import SensorDetailSerializer, MeasurementSerializer
# ListCreateAPIView - get post (read-write)
# RetrieveUpdateAPIView - get put patch (read or update)
# CreateAPIView - post(create only)


class GetPostSensor(ListCreateAPIView):  # first 2 requests
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class GetPutPatchSensor(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class MeasurementAPIView(ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer



