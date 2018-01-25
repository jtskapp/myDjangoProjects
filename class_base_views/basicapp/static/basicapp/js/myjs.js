$(document).ready(function(){
  // alert('loaded');

  $('#modal-control').on('click',function() {
    div = document.getElementById("overlay");
    div.style.visibility = (div.style.visibility == "visible") ? "hidden" : "visible";
  });

  $('#close-modal-control').on('click',function() {
    div = document.getElementById("overlay");
    div.style.visibility = (div.style.visibility == "visible") ? "hidden" : "visible";
  });


  $(".add-school").click(function() {
      alert('click');
      opendialog(this.href, this.title);
  });

  function opendialog(page, dialog_title) {
      alert(page);
      alert(dialog_title);
      var viewportWidth = $(window).width();
      var viewportHeight = $(window).height();

      var $dialog = $('#somediv')
      .html('<iframe style="border: 0px; " src="' + page + '" width="100%" height="100%"></iframe>')
      .dialog({
          title: dialog_title,
          autoOpen: false,
          dialogClass: 'dialog_fixed,ui-widget-header',
          modal: true,
          height: viewportHeight * 0.75,
          minWidth: viewportWidth * 0.75,
          minHeight: viewportHeight * 0.75,
          draggable:true
          /*close: function () { $(this).remove(); },*/
          /*buttons: { "Ok": function () {         $(this).dialog("close"); } }*/
      });
        $dialog.dialog('open');
      }
      console.log( "ready!" );



      $(".addschool").click(function(ev) { // for each edit contact url
          alert('.addschool')
          ev.preventDefault(); // prevent navigation
          var url = $(this).data("form"); // get the contact form url
          alert(url);
          $("#schoolModal").load(url, function() { // load the url into the modal
              $(this).modal('show'); // display the modal on url load
          });
          return false; // prevent the click propagation
      });

      $('.modal-dialog').live('submit', function() {
          alert('.modal-dialog')
          $.ajax({
              type: $(this).attr('method'),
              url: this.action,
              data: $(this).serialize(),
              context: this,
              success: function(data, status) {
                  alert(data);
                  $('#schoolModal').html(data);
              }
          });
          return false;
      });















});
