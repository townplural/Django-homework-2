from django.urls import path

from measurement.views import SensorAPIView, MeasurementAPIView

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    # path('sensors/<pk>', SensorAPIViewUpdate.as_view()),
    path('sensors/', SensorAPIView.as_view()),
    path('measurements', MeasurementAPIView.as_view()),
    # path('measurements', MeasurementAPIView.as_view()),

]
