from django.conf.urls.defaults import patterns,  url


urlpatterns = patterns('',
                         
    # USER REGISTRATION , LOGIN AND RELATED STUFF
        #INDEX PAGES
        url(r'^login/$','Users.Views.UserViews.Login_index'),
        url(r'^logout/$','Users.Views.UserViews.log_out'),
        # post-back for logging in 
        url(r'^login/log_in/$','Users.Views.UserViews.log_in'),
        url(r'^dashboard/$','Users.Views.UserViews.view_dashboard'),
        
    
    ###########################################################################################
        url(r'^register/$','txUser.views.Views_User.CreateUserIndex'),
        url(r'^register/new/$','txUser.views.Views_User.CreateUserFromSite'),
    
  #  url(r'^forgetpassword/$','txUser.UserViews.Forget_Pass_index'),
  #  url(r'^forget_pass/$','txUser.UserViews.forget_pass'),
    url(r'^authenticate/email/(?P<token>\S+)/(?P<refs>\d+)/$','txUser.views.Views_User.AuthenticateUserFromEmail'),
    
    
    # USER GROUP MENU STUFF

    
    
    # GROUP 

   url(r'^group/create/$','txUser.views.Views_Group.CreateGroup_Index'),
   url(r'^group/create/new/$','txUser.views.Views_Group.CreateGroup'),
   url(r'^group/list/(?P<req_type>\S+)/$','txUser.views.Views_Group.ListGroups'),
    
    
   url(r'^grouptype/$','Users.Views.GroupTypeViews.GroupTypeIndex'),
   url(r'^grouptype/create/$','Users.Views.GroupTypeViews.CreateNewGroupTypeIndex'),
   url(r'^grouptype/create/new/$','Users.Views.GroupTypeViews.CreateNewGroup'), 
   url(r'^grouptype/list/$','Users.Views.GroupTypeViews.ListAllGroupTypes'), 
 #   url(r'^group/(?P<gid>\d+)/users/add/$','txUser.Views_Group.AddUsers_Index'),
  #  url(r'^group/(?P<gid>\d+)/users/add/new/$','txUser.Views_Group.AddUsersToGroup'),
  #  url(r'^group/(?P<gid>\d+)/users/edit/$','txUser.Views_Group.EditUsers_Index'),

    
    # admin
   # url(r'^admin/$','txUser.UserViews.ListUsers'),
)               