from django.urls import path

from . import views

urlpatterns = [path("index.html", views.index, name="index"),
               path("AdminLogin.html", views.AdminLogin, name="AdminLogin"),	      
               path("AdminLoginAction", views.AdminLoginAction, name="AdminLoginAction"),
               path("AddFacultyAction", views.AddFacultyAction, name="AddFacultyAction"),
               path("AddFaculty.html", views.AddFaculty, name="AddFaculty"),
               path("AddStudentAction", views.AddStudentAction, name="AddStudentAction"),
               path("AddStudent.html", views.AddStudent, name="AddStudent"),
	       path("StudentLogin.html", views.StudentLogin, name="StudentLogin"),
	       path("StudentLoginAction", views.StudentLoginAction, name="StudentLoginAction"),
	       path("FacultyLogin.html", views.FacultyLogin, name="FacultyLogin"),
               path("FacultyLoginAction", views.FacultyLoginAction, name="FacultyLoginAction"),
	       path("ViewFaculty", views.ViewFaculty, name="ViewFaculty"),
               path("ViewStudent", views.ViewStudent, name="ViewStudent"),	   
	       path("ResourceAllocation.html", views.ResourceAllocation, name="ResourceAllocation"),
	       path("ResourceAllocationAction", views.ResourceAllocationAction, name="ResourceAllocationAction"),
	       path("SchoolPerformance", views.SchoolPerformance, name="SchoolPerformance"),

	       path("AddAttendance.html", views.AddAttendance, name="AddAttendance"),
	       path("AddAttendanceAction", views.AddAttendanceAction, name="AddAttendanceAction"),

	       path("CreateAssignments.html", views.CreateAssignments, name="CreateAssignments"),
	       path("CreateAssignmentsAction", views.CreateAssignmentsAction, name="CreateAssignmentsAction"),

	       path("UploadMaterial.html", views.UploadMaterial, name="UploadMaterial"),
	       path("UploadMaterialAction", views.UploadMaterialAction, name="UploadMaterialAction"),
	       path("DownloadMaterials", views.DownloadMaterials, name="DownloadMaterials"),
	       path("DownloadMaterialAction", views.DownloadMaterialAction, name="DownloadMaterialAction"),

	       path("AddMarks.html", views.AddMarks, name="AddMarks"),
	       path("AddMarksAction", views.AddMarksAction, name="AddMarksAction"),

	       path("StudentMessaging.html", views.StudentMessaging, name="StudentMessaging"),
	       path("StudentMessagingAction", views.StudentMessagingAction, name="StudentMessagingAction"),

	       path("Messaging.html", views.Messaging, name="Messaging"),
	       path("MessagingAction", views.MessagingAction, name="MessagingAction"),

	       path("ViewMarks.html", views.ViewMarks, name="ViewMarks"),
	       path("ViewMarksAction", views.ViewMarksAction, name="ViewMarksAction"),

	       path("ViewProgressReport.html", views.ViewProgressReport, name="ViewProgressReport"),
	       path("ViewProgressReportAction", views.ViewProgressReportAction, name="ViewProgressReportAction"),
	       path("ViewStudentMessages", views.ViewStudentMessages, name="ViewStudentMessages"),
	       path("ViewAssignments", views.ViewAssignments, name="ViewAssignments"),
	       path("ViewMessages", views.ViewMessages, name="ViewMessages"),
]
