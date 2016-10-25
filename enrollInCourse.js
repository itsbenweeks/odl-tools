/* Ben Weeks
JS Function to enroll a student in a course without having to go to the instructor dashboard.
Make sure you have an open session first, and grab the CSRF Token from the X-CSRFToken header.
*/

enroll_in_course = function( course_url, username, csrf_token ) {
  $.ajax( {
    url: course_url + "instructor/api/students_update_enrollment",
    data: "action=enroll&identifiers=" + username + "&auto_enroll=true&email_students=false",
    type: "POST",
    headers: { "X-CSRFToken": csrf_token}
  } );
}

