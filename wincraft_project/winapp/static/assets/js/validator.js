

function validateData(){
  var name = document.forms["query-form"]["name"].value;
  var phone_email = document.forms["query-form"]["email_phone"].value;
  var query = document.forms["query-form"]["query"].value;
  var flag = 0;

  for (var i=0;i<phone_email.length;i++){
    if (phone_email[i] == '@' || phone_email[i] == '.'){
      flag++;
    }
  }
    // Check if email
    if (flag>0){
          if (flag == 2){
            document.getElementById('query-form-id').submit();
          }
          else{
            alert("Please enter a valid email!");
          }
    }
    // Check if phone number
    else{
          if(phone_email.length == 10){
            document.getElementById('query-form-id').submit();
          }
          else{
            alert("Please enter a valid phone number");
          }
    }
}
