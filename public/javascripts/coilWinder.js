function setHomePosition(){
  console.log("made here");
  $(document).ready(function() {
    $('#homeForm').submit(function(event) {
        event.preventDefault();
        //jQuery post
        $.get("/api/home", {})
          .done(function(data) {
            alert(data);
          })
          .fail(function(err) {
            // $('#error').text(err.responseText);
            // setTimeout(clearError, 2000);
            // function clearError(){
            //   $('#error').text('')
            }
          );
    });
  });
}

// $(document).ready(function() {
//   $('#homeForm').submit(function(event) {
//       event.preventDefault();
//       //jQuery post
//       $.post("/api/home")
//         .done(function(data) {
//           alert(data);
//         })
//         .fail(function(err) {
//           // $('#error').text(err.responseText);
//           // setTimeout(clearError, 2000);
//           // function clearError(){
//           //   $('#error').text('')
//           }
//         );
//   });
// });
