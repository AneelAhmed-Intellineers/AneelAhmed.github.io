from rest_framework.routers import DefaultRouter

from.views import EquityView


router = DefaultRouter()

router.register('', EquityView, basename='home')
urlpatterns = router.urls