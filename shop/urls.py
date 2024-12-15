from django.urls import path,include
from .views import home_view,product_detail,add_to_cart,remove_from_cart,cart_view,checkout,login_view,logout_view,register_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # صفحه اصلی
    path('home/',home_view, name='home'),

    # جزئیات محصول
    path('product/<int:product_id>/',product_detail, name='product_detail'),

    # افزودن محصول به سبد خرید
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),

    # سبد خرید
    path('cart/',cart_view, name='cart_view'),

    # حذف محصول از سبد خرید
    path('remove-from-cart/<int:cart_item_id>/',remove_from_cart, name='remove_from_cart'),

    # صفحه تسویه حساب
    path('checkout/',checkout, name='checkout'),

    # صفحه لاگین
    path('login/',login_view, name='login'),

    # صفحه لاگ اوت
    path('logout/', logout_view, name='logout'),

    # صفحه ثبت نام
    path('register/', register_view, name='register'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
