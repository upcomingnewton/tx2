'''
Created on 26-Jul-2012

@author: jivjot
'''
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
                       
                       #temporary home
                       url(r'^UserProfile/UserHome/$','UserProfile.Views.UserProfile.StudentDetailsIndex'),

                       
                       # Board
                       
                       url(r'^Marks/Board/new$','UserProfile.Views.Marks.BoardInsert'),
                       url(r'^Marks/Board/View$','UserProfile.Views.Marks.BoardSelect'),
                       url(r'^Marks/Board/delete$','UserProfile.Views.Marks.BoardDelete'),
                       url(r'^Marks/Board/update$','UserProfile.Views.Marks.BoardUpdate'),
                       url(r'^Marks/Board/$','UserProfile.Views.Marks.BoardIndex'),
                       #DegreeType
                       url(r'^Marks/DegreeType/new$','UserProfile.Views.Marks.DegreeTypeInsert'),
                       url(r'^Marks/DegreeType/View$','UserProfile.Views.Marks.DegreeTypeSelect'),
                       url(r'^Marks/DegreeType/delete$','UserProfile.Views.Marks.DegreeTypeDelete'),
                       url(r'^Marks/DegreeType/update$','UserProfile.Views.Marks.DegreeTypeUpdate'),
                       url(r'^Marks/DegreeType/$','UserProfile.Views.Marks.DegreeTypeIndex'),
                       #Degree
                       url(r'^Marks/Degree/new$','UserProfile.Views.Marks.DegreeInsert'),
                       url(r'^Marks/Degree/View$','UserProfile.Views.Marks.DegreeSelect'),
                       url(r'^Marks/Degree/delete$','UserProfile.Views.Marks.DegreeDelete'),
                       url(r'^Marks/Degree/update$','UserProfile.Views.Marks.DegreeUpdate'),
                       url(r'^Marks/Degree/$','UserProfile.Views.Marks.DegreeIndex'),
                       #SessionType
                       url(r'^Marks/SessionType/new$','UserProfile.Views.Marks.SessionTypeInsert'),
                       url(r'^Marks/SessionType/View$','UserProfile.Views.Marks.SessionTypeSelect'),
                       url(r'^Marks/SessionType/delete$','UserProfile.Views.Marks.SessionTypeDelete'),
                       url(r'^Marks/SessionType/update$','UserProfile.Views.Marks.SessionTypeUpdate'),
                       url(r'^Marks/SessionType/$','UserProfile.Views.Marks.SessionTypeIndex'),
                       #Marks
                       url(r'^Marks/Marks/new$','UserProfile.Views.Marks.MarksInsert'),
                       url(r'^Marks/Marks/View$','UserProfile.Views.Marks.MarksSelect'),
                       url(r'^Marks/Marks/delete$','UserProfile.Views.Marks.MarksDelete'),
                       url(r'^Marks/Marks/update$','UserProfile.Views.Marks.MarksUpdate'),
                       url(r'^Marks/Marks/$','UserProfile.Views.Marks.MarksIndex'),
                       
                       #Branch
                       url(r'^UserProfile/Branch/new$','UserProfile.Views.UserProfile.BranchInsert'),
                       url(r'^UserProfile/Branch/View$','UserProfile.Views.UserProfile.BranchSelect'),
                       url(r'^UserProfile/Branch/delete$','UserProfile.Views.UserProfile.BranchDelete'),
                       url(r'^UserProfile/Branch/update$','UserProfile.Views.UserProfile.BranchUpdate'),
                       url(r'^UserProfile/Branch/$','UserProfile.Views.UserProfile.BranchIndex'),
                       #Category
                       url(r'^UserProfile/Category/new$','UserProfile.Views.UserProfile.CategoryInsert'),
                       url(r'^UserProfile/Category/View$','UserProfile.Views.UserProfile.CategorySelect'),
                       url(r'^UserProfile/Category/delete$','UserProfile.Views.UserProfile.CategoryDelete'),
                       url(r'^UserProfile/Category/update$','UserProfile.Views.UserProfile.CategoryUpdate'),
                       url(r'^UserProfile/Category/$','UserProfile.Views.UserProfile.CategoryIndex'),
                      #StudentDetails
                       url(r'^UserProfile/StudentDetails/new$','UserProfile.Views.UserProfile.StudentDetailsInsert'),
                       url(r'^UserProfile/StudentDetails/View$','UserProfile.Views.UserProfile.StudentDetailsSelect'),
                       url(r'^UserProfile/StudentDetails/delete$','UserProfile.Views.UserProfile.StudentDetailsDelete'),
                       url(r'^UserProfile/StudentDetails/update$','UserProfile.Views.UserProfile.StudentDetailsUpdate'),
                       url(r'^UserProfile/StudentDetails/$','UserProfile.Views.UserProfile.StudentDetailsIndex'),
                      #ExtraAcdemicInfo
                       url(r'^ExtraAcademicInfo/ExtraAcademicInfoType/new$','UserProfile.Views.ExtraAcademicInfo.ExtraAcdemicInfoTypeInsert'),
                       url(r'^ExtraAcademicInfo/ExtraAcademicInfoType/View$','UserProfile.Views.ExtraAcademicInfo.ExtraAcademicInfoTypeSelect'),
                       url(r'^ExtraAcademicInfo/ExtraAcademicInfoType/delete$','UserProfile.Views.ExtraAcademicInfo.ExtraAcademicInfoTypeDelete'),
                       url(r'^ExtraAcademicInfo/ExtraAcademicInfoType/update$','UserProfile.Views.ExtraAcademicInfo.ExtraAcademicInfoTypeUpdate'),
                       url(r'^ExtraAcademicInfo/ExtraAcademicInfoType/$','UserProfile.Views.ExtraAcademicInfo.ExtraAcdemicInfoTypeIndex'),
                      #ExtraAcdemicInf
                       url(r'^ExtraAcademicInfo/FunctionalAreaType/new$','UserProfile.Views.ExtraAcademicInfo.FunctionalAreaTypeInsert'),
                       url(r'^ExtraAcademicInfo/FunctionalAreaType/View$','UserProfile.Views.ExtraAcademicInfo.FunctionalAreaTypeSelect'),
                       url(r'^ExtraAcademicInfo/FunctionalAreaType/delete$','UserProfile.Views.ExtraAcademicInfo.FunctionalAreaTypeDelete'),
                       url(r'^ExtraAcademicInfo/FunctionalAreaType/update$','UserProfile.Views.ExtraAcademicInfo.FunctionalAreaTypeUpdate'),
                       url(r'^ExtraAcademicInfo/FunctionalAreaType/$','UserProfile.Views.ExtraAcademicInfo.FunctionalAreaTypeIndex'),
                      #ExtraAcademicInfoDetails
                       url(r'^ExtraAcademicInfo/ExtraAcademicInfoDetails/new$','UserProfile.Views.ExtraAcademicInfo.ExtraAcademicInfoDetailsInsert'),
                       url(r'^ExtraAcademicInfo/ExtraAcademicInfoDetails/View$','UserProfile.Views.ExtraAcademicInfo.ExtraAcademicInfoDetailsSelect'),
                       url(r'^ExtraAcademicInfo/ExtraAcademicInfoDetails/delete$','UserProfile.Views.ExtraAcademicInfo.ExtraAcademicInfoDetailsDelete'),
                       url(r'^ExtraAcademicInfo/ExtraAcademicInfoDetails/update$','UserProfile.Views.ExtraAcademicInfo.ExtraAcademicInfoDetailsUpdate'),
                       url(r'^ExtraAcademicInfo/ExtraAcademicInfoDetails/$','UserProfile.Views.ExtraAcademicInfo.ExtraAcademicInfoDetailsIndex'),
                      
                      #FunctionalAreaList
                       url(r'^ExtraAcademicInfo/FunctionalAreaList/new$','UserProfile.Views.ExtraAcademicInfo.FunctionalAreaListInsert'),
                       url(r'^ExtraAcademicInfo/FunctionalAreaList/View$','UserProfile.Views.ExtraAcademicInfo.FunctionalAreaListSelect'),
                       url(r'^ExtraAcademicInfo/FunctionalAreaList/delete$','UserProfile.Views.ExtraAcademicInfo.FunctionalAreaListDelete'),
                       url(r'^ExtraAcademicInfo/FunctionalAreaList/update$','UserProfile.Views.ExtraAcademicInfo.FunctionalAreaListUpdate'),
                       url(r'^ExtraAcademicInfo/FunctionalAreaList/$','UserProfile.Views.ExtraAcademicInfo.FunctionalAreaListIndex'),
                      #MedicalInfo
                       url(r'^UserProfileMisc/MedicalInfo/new$','UserProfile.Views.UserProfileMisc.MedicalInfoInsert'),
                       url(r'^UserProfileMisc/MedicalInfo/View$','UserProfile.Views.UserProfileMisc.MedicalInfoSelect'),
                       url(r'^UserProfileMisc/MedicalInfo/delete$','UserProfile.Views.UserProfileMisc.MedicalInfoDelete'),
                       url(r'^UserProfileMisc/MedicalInfo/update$','UserProfile.Views.UserProfileMisc.MedicalInfoUpdate'),
                       url(r'^UserProfileMisc/MedicalInfo/$','UserProfile.Views.UserProfileMisc.MedicalInfoIndex'),
                      
                      )