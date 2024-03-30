from django.urls import path

from measurement.views import MeasurementAPIView, GetPostSensor, GetPutPatchSensor

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    # path('sensors/<pk>', SensorAPIViewUpdate.as_view()),
    path('get_sensors/', GetPostSensor.as_view()),
    path('get_sensors/<pk>/', GetPostSensor.as_view()),
    path('create_sensors/', GetPostSensor.as_view()),
    path('update_sensors/<pk>/', GetPutPatchSensor.as_view()),
    path('edit_measurements/', MeasurementAPIView.as_view()),
    # path('measurements', MeasurementAPIView.as_view()),

]
