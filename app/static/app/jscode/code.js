
$.ajaxSetup({
    headers: {
        'X-CSRF-TOKEN': $('meta[name="csrf-token"]').attr('content')
    }
});

$(document).ready(function () {


    $('.catid').on('change', function () {
        var id  = $('.catid').val();
   

        $.ajax({

            url: "/fatch-subcatgeory/"+id,
            dataType: "json",
            success: function (data) {
                var select = $('.addSubCat');
                select.empty();

                // Populate the dropdown with the filtered data
                $.each(data.data, function (index, item) {
                    select.append('<option value="' + item.id + '">' + item.subcat_name + '</option>');
                });
                
            }
        });
    });


    $('.addSubCat').change(function() {
        var selectedValue = $(this).val();
        console.log('Selected Value:', selectedValue);
      });


});