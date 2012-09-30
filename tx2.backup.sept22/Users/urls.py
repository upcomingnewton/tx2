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
        url(r'^list/$','Users.Views.SearchUserViews.ListUser'),
        url(r'^search/post/$','Users.Views.SearchUserViews.SearchUser'),
        url(r'^search/$','Users.Views.SearchUserViews.SearchUserIndex'),
        url(r'^edit/(?P<UserID>\d+)/post/$','Users.Views.UserViews.EditUser'),
        url(r'^edit/(?P<UserID>\d+)/group/(?P<GroupID>\d+)/post/$','Users.Views.UserViews.EditUser'),
        # MENU URLS
        url(r'^menu/list/$','Users.Views.MenuViews.ListAllMenu'),
        url(r'^menu/list/delete/$','Users.Views.MenuViews.ListDeletedMenu'),
        url(r'^menu/add/$','Users.Views.MenuViews.AddMenuIndex'),
        url(r'^menu/edit/(?P<MenuId>\d+)/$','Users.Views.MenuViews.EditMenuIndex'),
        url(r'^menu/delete/(?P<MenuId>\d+)/$','Users.Views.MenuViews.DeleteMenuIndex'),
        url(r'^menu/activate/(?P<MenuId>\d+)/$','Users.Views.MenuViews.ActivateMenuIndex'),
        # MENU URLS #TODO
        url(r'^menu/add/post/$','Users.Views.MenuViews.AddMenu'),
        url(r'^menu/edit/(?P<MenuId>\d+)/post/$','Users.Views.MenuViews.EditMenu'),
        url(r'^menu/delete/(?P<MenuId>\d+)/post/$','Users.Views.MenuViews.Delete'),
        url(r'^menu/activate/(?P<MenuId>\d+)/post/$','Users.Views.MenuViews.Activate'),
        url(r'^group/$','Users.Views.GroupViews.GroupIndex',{'options':'simple'}),
        url(r'^group/add/$','Users.Views.GroupViews.CreateNewGroupIndex'),
        url(r'^group/add/post/$','Users.Views.GroupViews.CreateNewGroup'),
        url(r'^group/select/$','Users.Views.GroupViews.GroupIndex',{'options':'select'}),
        url(r'^group/options/$','Users.Views.GroupViews.GroupIndex',{'options':'options'}),
        url(r'^group/select/post/$','Users.Views.GroupViews.GroupSelectToMemory'),
        url(r'^groupmenu/$','Users.Views.GroupMenuViews.GroupMenuViewIndex'),
        url(r'^groupmenu/(?P<GroupID>\d+)/details/$','Users.Views.GroupMenuViews.GroupMenuDetailsIndex'),
        url(r'^groupmenu/add/$','Users.Views.GroupMenuViews.GroupMenuAddIndex'),
        url(r'^groupmenu/add/post/$','Users.Views.GroupMenuViews.GroupMenuAdd'),
        url(r'^groupmenu/delete/$','Users.Views.GroupMenuViews.GroupMenuDeleteIndex'),
        url(r'^groupmenu/delete/post/$','Users.Views.GroupMenuViews.GroupMenuDelete'),
)
