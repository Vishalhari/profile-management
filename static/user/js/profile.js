
var newRowAdd = '';
var newedu = '';
var newcert ='';
var newexp ='';



$(document).ready(function(){
    $(".addskill").click(function () {
            newRowAdd = '<div class="skillrows"><div class="col-md-6">'+
           '<input type="text" class="form-control m-input" name="skill" placeholder="Enter Skills"></div>'+
           '<div class="col-md-3">'+
           '<div class="input-group-prepend">'+
           '<button class="btn btn-danger remove" id="DeleteRow" type="button"><i class="bi bi-trash"></i>Delete</button>'+
           '</div></div><br><br></div>';

            $('#skillsappend').append(newRowAdd);
    });


    $('.addedu').click(function(){
        newedu = '<div class="educationrows">'+
                  '<div class="col-md-3">'+
                  '<input type="text" class="form-control m-input" name="course" placeholder="Enter Course">'+
                  '</div>'+
                  '<div class="col-md-3">'+
                  '<input type="text" class="form-control m-input" name="academicyear" placeholder="Enter Academic Year">'+
                  '</div>'+
                  '<div class="col-md-3">'+
                  '<input type="text" class="form-control m-input" name="percentage" placeholder="Enter Percentage">'+
                  '</div>'+
                  '<div class="col-md-3">'+
                  '<div class="input-group-prepend">'+
                  '<button class="btn btn-danger remove-edu" type="button"><i class="bi bi-trash"></i>Delete</button>'+
                  '</div>'+
                  '</div><br><br>'+
                  '</div>';
        $('#educationappend').append(newedu);
    });

    $('.addcertification').click(function(){
        newcert = '<div class="certificationrows">'+
                 '<div class="col-md-3">'+
                 '<input type="text" class="form-control m-input" name="cerificatename" placeholder="Enter Certificate Name">'+
                 '</div>'+
                 '<div class="col-md-3">'+
                 '<input type="text" class="form-control m-input" name="institutename" placeholder="Enter Institution">'+
                 '</div>'+
                 '<div class="col-md-3">'+
                 '<input type="text" class="form-control m-input" name="year" placeholder="Enter Year">'+
                 '</div>'+
                 '<div class="col-md-3">'+
                 '<div class="input-group-prepend">'+
                 '<button class="btn btn-danger remove-cert" type="button"><i class="bi bi-trash"></i>Delete</button>'+
                 '</div>'+
                 '</div><br><br>'+
                 '</div>';
        $('#certificationappend').append(newcert);
    });

    $('.addexp').click(function(){
        newexp = '<div class="experiencerows">'+
                  '<div class="col-md-2">'+
                  '<input type="text" class="form-control m-input" name="company" placeholder="Enter Company name">'+
                  '</div>'+
                  '<div class="col-md-2">'+
                  '<input type="text" class="form-control m-input" name="location" placeholder="Enter Location">'+
                  '</div>'+
                  '<div class="col-md-2">'+
                  '<input type="text" class="form-control m-input" name="startyear"" placeholder="Enter Joined Year">'+
                  '</div>'+
                  '<div class="col-md-2">'+
                  '<input type="text" class="form-control m-input" name="endyear" placeholder="Enter Resigned year">'+
                  '</div>'+
                  '<div class="col-md-2">'+
                  '<div class="input-group-prepend">'+
                  '<button class="btn btn-danger remove-exp" type="button"><i class="bi bi-trash"></i>Delete</button>'+
                  '</div>'+
                  '</div><br><br>'+
                 '</div>';
        $('#experienceappend').append(newexp);
    });

    $(document).on('click','.remove-edu',function(){
        $(this).closest('.educationrows').remove();
    });

    $(document).on('click', '.remove', function(){
        $(this).closest('.skillrows').remove();
    });

    $(document).on('click', '.remove-cert', function(){
        $(this).closest('.certificationrows').remove();
    });

     $(document).on('click', '.remove-exp', function(){
        $(this).closest('.experiencerows').remove();
    });

});



