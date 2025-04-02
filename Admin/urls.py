from django.urls import path
from Admin import views
app_name="Admin"

urlpatterns = [

    path('Add/', views.Add , name='Add'),
    path('Largest/', views.Largest , name='Largest'),
    path('calculator/', views.calculator , name='calculator'),
    path('reg/', views.reg , name='reg'),
    path('district/', views.district , name='district'),
    path('category/', views.category , name='category'),
    path('delcategory/<int:id>', views.delcategory, name='delcategory'),
    path('editcategory/<int:id>', views.editcategory, name='editcategory'),
    path('deldistrict/<int:id>', views.deldistrict, name='deldistrict'),
    path('editdistrict/<int:id>', views.editdistrict, name='editdistrict'),
    path('Adminreg/', views.Adminreg, name='Adminreg'),
    path('adminprofile/', views.adminprofile, name='adminprofile'),
    path('delAdminreg/<int:id>', views.delAdminreg, name='delAdminreg'),
    path('editAdminreg/<int:id>', views.editAdminreg, name='editAdminreg'),
    path('place/', views.place , name='place'),
    path('delplace/<int:id>', views.delplace, name='delplace'),
    path('Subcategory/', views.Subcategory , name='Subcategory'),
    path('delsub/<int:id>', views.delsub, name='delsub'),
    path('editplace/<int:id>', views.editplace, name='editplace'),
    path('editSubcategory/<int:id>', views.editSubcategory, name='editSubcategory'),
    path('verification/', views.verification, name='verification'),
    path('useraccept/<int:id>', views.useraccept, name='useraccept'),
    path('userreject/<int:id>', views.userreject, name='userreject'),
        
    path('dverification/', views.dverification, name='dverification'),
    path('deliveryaccept/<int:id>', views.deliveryaccept, name='deliveryaccept'),
    path('deliveryreject/<int:id>', views.deliveryreject, name='deliveryreject'),



    path('product/', views.product, name='product'),
    path('ajaxsubcategory/', views.ajaxsubcategory, name='ajaxsubcategory'),
    path('newartist/', views.newartist, name='newartist'),
    path('artistaccept/<int:id>', views.artistaccept, name='artistaccept'),
    path('artistreject/<int:id>', views.artistreject, name='artistreject'),
    path('acceptedartist/', views.acceptedartist, name='acceptedartist'),
    path('rejectedartist/', views.rejectedartist, name='rejectedartist'),
    path('adminhomepage/', views.adminhomepage , name='adminhomepage'),
    path('addevent/', views.addevent , name='addevent'),
    path('delevent/<int:id>', views.delevent , name='delevent'),
    path('viewfeedback/',views.viewfeedback,name="viewfeedback"),
    path('complaint/',views.complaint,name="complaint"),
    path('viewartwok/',views.viewartwok,name="viewartwok"),
    path('delartwork/<int:id>', views.delartwork , name='delartwork'),


    path('reply/<int:id>', views.reply , name='reply'),
    path('replayedcomplaint/', views.replayedcomplaint , name='replayedcomplaint'),
    path('viewticketbooking/<int:id>', views.viewticketbooking , name='viewticketbooking'),
    path('logout/',views.logout,name="logout"),
]