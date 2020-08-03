/*function close_socket()
{
    console.log("test");
    socket.disconnect();       
    return null
}

$(window).on('beforeunload ',function() {
    return close_socket();
});
*/
$(document).ready(function(){
    var socket = io.connect('http://' + document.domain + ':' + location.port + '/update');
    var numbers_received = [];
    socket.on('newnumber', function(msg) {
        console.log("Received status " + msg.number);
        //maintain a list of ten numbers
        if (numbers_received.length >= 5)
        {
            numbers_received.shift()
        }            
        numbers_received.push(msg.number);
        numbers_string1 = '';
        numbers_string2 = '';
        numbers_string3 = '';
        numbers_string4 = '';
        numbers_string5 = '';

        if (numbers_received.length >= 5)
        {       
        numbers_string1 = '<p>' + numbers_received[0].toString() + '</p>';
                
        numbers_string2 = '<p>' + numbers_received[1].toString() + '</p>';
        numbers_string3 = '<p>' + numbers_received[2].toString() + '</p>';
        numbers_string4 = '<p>' + numbers_received[3].toString() + '</p>';
        numbers_string5 = '<p>' + numbers_received[4].toString() + '</p>';
        }

            if(numbers_received[0].toString()==="Accident Detected")
                {
                            swal({text: "Accident Detected!",icon: "warning",});
                            req = $.ajax({
                    url : '/update-acc-table',
                    type : 'GET',
            });
                                    req.done(function(data) {

                    console.log(data)
                    $('#acc_table').html(data.s)
        });
    
                            //break;
                            //var con = "<thead><tr><th scope=\"col\">&nbsp;</th><th scope=\"col\">Vehicle No</th><th scope=\"col\">Date & Time</th>  <th scope=\"col\">Location</th><th scope=\"col\">Spot</th><th scope=\"col\">Mobile No</th><!--<th scope=\"col\">&nbsp;</th>--></tr></thead><tbody><tr><th scope=\"row\"><input type=\"checkbox\" /></th><td>TN 27 AC 5678</td><td>17:30, 12 FEB 2020</td><td>Four-Roads</td><td>Pole 15</td><td>9865445476</td></tr>";
                 // console.log(con);
                //$('#acc_table').html(con);
                  }             
        //console.log(numbers_string1)
        
        $('#log1').html(numbers_string1);
        $('#log2').html(numbers_string2);
        $('#log3').html(numbers_string3);
        $('#log4').html(numbers_string4);
        $('#log5').html(numbers_string5);

    });

});

/*
     if(s==='Accident Detected')
      {
        swal({
  text: "Accident Detected!",
  icon: "warning",
});
*/
/*$.ajax({
{
              var con = "<thead>
                  <tr>
                    <th scope=\"col\">&nbsp;</th>
                    <th scope=\"col\">Vehicle No</th>
                    <th scope=\"col\">Date & Time</th>  
                    <th scope=\"col\">Location</th>
                    <th scope=\"col\">Spot</th>
                    <th scope=\"col\">Mobile No</th>
                    <!--<th scope=\"col\">&nbsp;</th>-->
                  </tr>
                </thead>
                <tbody>
            
                  <tr>
                    <th scope=\"row\"><input type=\"checkbox\" /></th>
                     <td>TN 27 AC 5678</td>
                     <td>17:30, 12 FEB 2020</td>
                     <td>Four-Roads</td>
                     <td>Pole 15</td>
                     <td>9865445476</td>
                  </tr>
                  <tr>
                    <th scope=\"row\"><input type=\"checkbox\" /></th>
                     <td>TN 45 BZ 2658</td>
                     <td>17:20, 12 FEB 2020</td>
                     <td>Seelanayakanpatty</td>
                     <td>Pole 60</td>
                     <td>8865634728</td>
                  </tr>"

                $('#acc_table').html(con);
            }
        });*/