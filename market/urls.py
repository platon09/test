from django.urls import path, include
from market.views.shop_view import ShopListView, ShopDetailView
from market.views.product_view import ProductListView, ProductDetailView
from market.views.category_view import CategoryListView

urlpatterns = [
    path('', ShopListView.as_view()),
    path('<int:shop_id>/', include([
        path('', ShopDetailView.as_view()),
        path('categories/', CategoryListView.as_view()),
        path('categories/<int:cat_id>/', include([
            path('', ProductListView.as_view()),
            path('<int:prod_id>/', ProductDetailView.as_view()),
        ])),
    ])),
]
