from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static 
from django.contrib.auth import views as auth_views
from .forms import LoginForm,MyPasswordChangeForm, MyPasswordResetForm,MySetPasswordForm
urlpatterns = [
    # path('', views.home),
    ######### front pages connection 
    path('',views.ProductView.as_view(),name='home'),
    path('product-detail/<int:pk>', views.ProductDetailView.as_view() , name='product-detail'),
   
    
    # path('changepassword/', views.change_password, name='changepassword'),
    ######## product details ##########
    path('mobile/', views.mobile, name='mobile'),
    path('mobile/<slug:data>', views.mobile, name='mobiledata'),
    path('laptop/', views.laptops, name='laptops'),
    path('laptop/<slug:data>', views.laptops, name='laptopsdata'),
    path('topwear/', views.topwears, name='topwear'),
    path('topwear/<slug:data>', views.topwears, name='topweardata'),
    path('bottomwear/', views.bottomwears, name='bottomwear'),
    path('bottomwear/<slug:data>', views.bottomwears, name='bottomweardata'),
    

    ####### Accounts ############
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),

    
    
    ######### Action taken on product #############
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.show_cart, name='showcart'),
    path('pluscart/', views.plus_cart),
    path('minuscart/', views.minus_cart),
    path('removecart/', views.remove_cart),
    path('checkout/', views.checkout, name='checkout'),
    path('paymentdone/', views.payment_done, name='paymentdone'),
    path('buy/', views.buy_now, name='buy-now'),
   
   
   
    ###### Login  nd Registration #########
    path('registration/',views.CustomerRegistreationView.as_view(), name='customerregistration'),
    path('accounts/login/',auth_views.LoginView.as_view(template_name='app/login.html',authentication_form=LoginForm),name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    
    
    
     #######   password change #######
    path('passwordchange/',auth_views.PasswordChangeView.as_view(template_name='app/passwordchange.html',form_class=MyPasswordChangeForm, success_url='/passwordchangedone/'),name='passwordchange'),
    path('passwordchangedone/',auth_views.PasswordChangeView.as_view(template_name='app/passwordchangedone.html'),name='passwordchangedone'),
    
    
    #####password reset###########
    path('accounts/password_reset/',auth_views.PasswordResetView.as_view(template_name='app/password_reset.html',form_class=MyPasswordResetForm),name='password_reset'),
    path('accounts/password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='app/password_reset_done.html'),name='password_reset_done'),
    path('accounts/password_reset_confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='app/password_reset_confirm.html',form_class=MySetPasswordForm),name='password_reset_confirm'),    ####### hash id
    path('accounts/password_reset_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='app/password_reset_complete.html'),name='password_reset_complete'),






    # path('login/', views.login, name='login'),
    # path('registration/', views.customerregistration, name='customerregistration'),
    
    
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
