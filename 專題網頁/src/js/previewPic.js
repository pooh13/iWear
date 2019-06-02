function readURL(input) {

  if (input.files && input.files[0]) {
    var reader = new FileReader();
    var pic = document.getElementById("blah");

    reader.onload = function(e) {
      $('#blah').attr('src', e.target.result);
    }

    reader.readAsDataURL(input.files[0]);
    pic.style.display='block';
  }

}

// $("#imgInp").change(function() {
//   readURL(this);
// });


// function setText(ob,name){  
//     document.getElementById(name).value=ob.value;;  
// }  