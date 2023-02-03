from rest_framework.routers import DefaultRouter

from fan_dealership.api.v1.views.Accessories_view import AccessoriesViewSet
from fan_dealership.api.v1.views.Category_view import CategoryViewSet
from fan_dealership.api.v1.views.Fan_dealership_view import Fan_dealershipViewSet
from fan_dealership.api.v1.views.Popularity_view import PopularityViewSet
from purchaser.api.v1.views.Balance_view import BalanceViewSet
from purchaser.api.v1.views.Purchaser_view import PurchaserViewSet
from supplier.api.v1.views.Founder_view import FounderViewSet
from supplier.api.v1.views.Supplier_view import SupplierViewSet

router = DefaultRouter()
router.register(r'accessories', AccessoriesViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'fan_dealership', Fan_dealershipViewSet)
router.register(r'popularity', PopularityViewSet)
router.register(r'balance', BalanceViewSet)
router.register(r'purchaser', PurchaserViewSet)
router.register(r'supplier', SupplierViewSet)
router.register(r'founder', FounderViewSet)

urlpatterns = router.urls
