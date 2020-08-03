function showContent(brand){

  if (brand == 'aluk'){

      $('#simta').css('display', 'none');
      $('#firat').css('display', 'none');
      $('#aluk').slideToggle();

  }


  if (brand == 'simta'){

      $('#aluk').css('display', 'none');
      $('#firat').css('display', 'none');
      $('#simta').slideToggle();
  }


  if (brand == 'firat'){

      $('#simta').css('display', 'none');
      $('#aluk').css('display', 'none');
      $('#firat').slideToggle();
  }

}
