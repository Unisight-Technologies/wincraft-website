

function validateData(){
  var name = document.forms["query-form"]["name"].value;
  var phone = document.forms["query-form"]["phone"].value;
  var email = document.forms["query-form"]["email"].value;
  var query = document.forms["query-form"]["query"].value;

  if(phone.length == 10){
    if (!isNaN(phone)){
      return true;
    }
    else{
      alert("Please enter a valid phone number");
      return false;
    }
  }
  else{
    alert("Please enter a valid phone number");
    return false;
  }
}
