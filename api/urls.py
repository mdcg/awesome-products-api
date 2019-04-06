from api.views.products_views import (EditUserProductView, ListProductsView,
                                      ProductDetailsView, UserProductsView)
from api.views.users_views import SignInView, SignUpView
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

urlpatterns = [
    #
    # User
    #
    path('signup', SignUpView.as_view(), name='signup'),
    path('signin', SignInView.as_view(), name='signin'),

    #
    # Products
    #
    path('products', UserProductsView.as_view(), name='user-products'),
    path('products/list', ListProductsView.as_view(), name='products'),
    path('products/<int:product_id>', EditUserProductView.as_view(), name='edit-user-product'),
    path('products/<int:product_id>/details', ProductDetailsView.as_view(), name='product-details'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
