/*
Ben Weeks 3/12/16
JS Function to delete every file in an edX course
Use with extreme CAUTION from the Files & Uploads page in Studio.
*/
deleteAll = function() {
  var URLArray = document.URL.split("/");
  var domainName = URLArray[2];
  var org = URLArray[URLArray.length - 4];
  var course = URLArray[URLArray.length - 3]
  var term = URLArray[URLArray.length - 2];
  var baseURL = "https://" + domainName
                + "/assets/" + org
                + "/" + course
                + "/" + term + "/";
  var staticURL = baseURL + "%2Fc4x%2F"
                + org + "%2F"
                + course + "%2Fasset%2F";
  var listURL = baseURL + "?page=-1&page_size=600&sort=date_added&direction=desc&asset_type=&format=json";
  files = $.ajax( {
    "type": "GET",
    "url": listURL
  } );
  files = JSON.parse(files.responseText)["assets"];
  for(i = 0; i < files.length; i++) {
    deleteURL = files[i]["portable_url"].replace("/static/", staticURL);
    $.ajax( {
      "type": "DELETE",
      "url": deleteURL
    } );
  };
};

