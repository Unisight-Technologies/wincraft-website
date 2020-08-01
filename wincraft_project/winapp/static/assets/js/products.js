var counter_aluk = 0;
var counter_firat = 0;
var counter_simta = 0;


function showContent(brand){

  if (brand == 'aluk'){
      counter_aluk++;
      if(counter_aluk % 2 == 0){
        $('#aluk').css('display', 'none');
      }
      else{
        $('#simta').css('display', 'none');
        $('#firat').css('display', 'none');
        $('#aluk').css('display', 'inherit');
      }
  }


  if (brand == 'simta'){
      counter_simta++;
      if(counter_simta % 2 == 0){
        $('#simta').css('display', 'none');
      }
      else{
        $('#aluk').css('display', 'none');
        $('#firat').css('display', 'none');
        $('#simta').css('display', 'inherit');
      }
  }


  if (brand == 'firat'){
      counter_firat++;
      if(counter_firat % 2 == 0){
        $('#firat').css('display', 'none');
      }
      else{
        $('#simta').css('display', 'none');
        $('#aluk').css('display', 'none');
        $('#firat').css('display', 'inherit');
      }
  }

}
