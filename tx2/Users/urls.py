from django.conf.urls.defaults import patterns,  url


urlpatterns = patterns('',
        #INDEX PAGES
        url(r'^dashboard/$','Users.Views.UserViews.view_dashboard'),
        url(r'^login/$','Users.Views.UserViewIndex.LoginIndex'),
        url(r'^login/post/$','Users.Views.UserViews.Login'),
        url(r'^logout/$','Users.Views.UserViews.log_out'),
        url(r'^register/$','Users.Views.UserViewIndex.CreateUserIndex'),
        url(r'^register/post/$','Users.Views.UserViews.CreateUserFromSite'),
        url(r'^authenticate/email/(?P<token>\S+)/(?P<refs>\d+)/$','Users.Views.UserViews.AuthenticateUserFromEmail'),
        url(r'^authenticate/resendemail/$','Users.Views.UserViewIndex.ResendAuthenticationEmailIndex'),#TODO
        url(r'^authenticate/resendemail/post/$','Users.Views.UserViews.ResendAuthenticationEmail'), #ResendAuthenticationEmail
        url(r'^password/change/$','Users.Views.UserViewIndex.ChangePassIndex'),
        url(r'^password/change/post/$','Users.Views.UserViews.ChangePass'),
        url(r'^password/reset/$','Users.Views.UserViewIndex.ResetPasswordIndex'),
        url(r'^password/reset/post/$','Users.Views.UserViews.ResetPass'),
        
        # MENU URLS
        url(r'^menu/list/$','Users.Views.MenuViews.ListAllMenu'),
        url(r'^menu/list/delete/$','Users.Views.MenuViews.ListDeletedMenu'),
        url(r'^menu/add/$','Users.Views.MenuViews.AddMenuIndex'),
        url(r'^menu/edit/(?P<MenuId>\d+)/$','Users.Views.MenuViews.EditMenuIndex'),
        url(r'^menu/delete/(?P<MenuId>\d+)/$','Users.Views.MenuViews.DeleteMenuIndex'),
        url(r'^menu/activate/(?P<MenuId>\d+)/$','Users.Views.MenuViews.ActivateMenuIndex'),
        # post-back for logging in 
        
        
        
        
        
        
#        url(r'^admin/$','Users.Views.UserAdminViews.ListAllUsers'),
#        url(r'^admin/(?P<userid>\d+)/edit/$','Users.Views.UserAdminViews.EditUserIndex'),
#        url(r'^admin/(?P<userid>\d+)/edit/edit/$','Users.Views.UserAdminViews.EditUser'),
        
        # MENU URLS #TODO
        url(r'^menu/add/post/$','Users.Views.MenuViews.AddMenu'),
        url(r'^menu/edit/(?P<MenuId>\d+)/post/$','Users.Views.MenuViews.EditMenu'),
        url(r'^menu/delete/(?P<MenuId>\d+)/post/$','Users.Views.MenuViews.Delete'),
        url(r'^menu/activate/(?P<MenuId>\d+)/post/$','Users.Views.MenuViews.Activate'),
    ###########################################################################################
#   url(r'^grouptype/$','Users.Views.GroupTypeViews.GroupTypeIndex'),
#   url(r'^grouptype/create/$','Users.Views.GroupTypeViews.GroupTypeIndex'),
#   url(r'^grouptype/create/new/$','Users.Views.GroupTypeViews.CreateNewGroup'), 
#   
#   url(r'^group/$','Users.Views.GroupViews.GroupIndex',{'__list':'true','__create':'false'}),
#   url(r'^group/create/$','Users.Views.GroupViews.GroupIndex',{'__list':'false','__create':'true'}),
#   url(r'^group/create/new/$','Users.Views.GroupViews.CreateNewGroup'), 
 #   url(r'^group/(?P<gid>\d+)/users/add/$','txUser.Views_Group.AddUsers_Index'),
  #  url(r'^group/(?P<gid>\d+)/users/add/new/$','txUser.Views_Group.AddUsersToGroup'),
  #  url(r'^group/(?P<gid>\d+)/users/edit/$','txUser.Views_Group.EditUsers_Index'),

    
    # admin
   # url(r'^admin/$','txUser.UserViews.ListUsers'),
)               
