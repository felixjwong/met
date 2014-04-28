<?php
    
    if( isset($_POST["sparkid"]) )
    {
        $sparkid = (string) $_POST["sparkid"];
        $accesscode = (string) $_POST["accesscode"];
        $avgrate = (string) $_POST["avgrate"];
        $floatavgrate = floatval($avgrate);
        if ($floatavgrate > 0)
        {
            if ($floatavgrate < 100)
            {
                $command = escapeshellcmd('python met.py '.$sparkid.' '.$accesscode.' '.$avgrate);
                $output = shell_exec($command);
            }
        }
    }
?>

<!doctype html>
<html>
<head>
	<meta charset="utf-8">
	<title>MET | My Endurance Trainer</title>
	<meta name="title" content="MET | My Endurance Trainer" />
	<meta name="description" content="Internet Portal for MET" />
	<link rel="shortcut icon" id="favicon" href="favicon.png"> 
	<meta name="author" content="Chih-Yu Liu, Tracy Lu, and Felix Wong">
	<link href='http://fonts.googleapis.com/css?family=Open+Sans:300,400,700 ' rel='stylesheet' type='text/css'>
	<link href='http://fonts.googleapis.com/css?family=Pacifico:400 'rel='stylesheet' type='text/css'>
	<script type="text/javascript" src="http://code.jquery.com/jquery-1.9.1.js"></script>
  <script type="text/javascript" src="jquery.onepage-scroll.js"></script>
  <link href='onepage-scroll.css' rel='stylesheet' type='text/css'>
  <meta name="viewport" content="initial-scale=1, width=device-width, maximum-scale=1, minimum-scale=1, user-scalable=no">

<link rel="shortcut icon" href='http://www.hcs.harvard.edu/met/favicon.ico' type="image/x-icon">
<link rel="icon" href='http://www.hcs.harvard.edu/met/favicon.ico' type="image/x-icon">


  <style>
    html {
      height: 100%;
    }
    body {
      background: #E2E4E7;
      padding: 0;
      text-align: center;
      font-family: 'open sans';
      position: relative;
      margin: 0;
      height: 100%;
      -webkit-font-smoothing: antialiased;
    }
    
    .wrapper {
    	height: 100% !important;
    	height: 100%;
    	margin: 0 auto; 
    	overflow: hidden;
    }
    
    a {
      text-decoration: none;
    }
    
    
    h1, h2 {
      width: 100%;
      float: left;
    }
    h1 {
      margin-top: 100px;
      color: #000;
      margin-bottom: 5px;
      font-size: 70px;
      letter-spacing: -4px;
      font-weight: 100;
    }
    h1 span {
      font-size: 26px;
      margin: 0 5px;
      text-transform: capitalize;
      background: rgba(0,0,0,0.85);
      display: inline-block;
      color: #6D461D;
      border-radius: 5px 5px;
      -webkit-border-radius: 5px 5px;
      -moz-border-radius: 5px 5px;
      text-shadow: 0 2px 8px rgba(0, 0, 0, 0.75);
      padding: 3px 10px;
    }
    h2 {
      color: #6D461D;
      font-weight: 100;
      margin-top: 0;
      margin-bottom: 10px;
    }
    
    .pointer {
      color: #9b59b6;
      font-family: 'Pacifico', cursive;
      font-size: 30px;
      margin-top: 15px;
    }
    code {
      margin: 20px 1%;
      float: left;
      width: 48%;
      height: 105px;
      background: rgba(0,0,0,0.1);
      border: rgba(0,0,0,0.05) 5px solid;
      border-radius: 5px;
      padding:5px;
      color: white;
      text-align: center;
      font-size: 15px;
      margin-top: 25px;
      display: block;
      box-sizing: border-box;
      -webkit-box-sizing: border-box;
      -moz-box-sizing: border-box;
    }
    code.html {
      color: #7EC9E6;
    }
    code.js {
      color: #FFAD00;
    }

    .main {
      float: left;
      width: 100%;
      margin: 0 auto;
    }
    
    .main h1 {
      padding:150px 50px;
      float: left;
      width: 100%;
      font-size: 45px;
      box-sizing: border-box;
      -webkit-box-sizing: border-box;
      -moz-box-sizing: border-box;
      font-weight: 100;
      color: white;
      margin: 0;
    }
   
    .main h1.demo1 {
      background: #1ABC9C;
    }
    
    .reload.bell {
      font-size: 12px;
      padding: 20px;
      width: 45px;
      text-align: center;
      height: 47px;
      border-radius: 50px;
      -webkit-border-radius: 50px;
      -moz-border-radius: 50px;
    }
    
    .reload.bell #notification {
      font-size: 25px;
      line-height: 140%;
    }
    
    .reload, .btn{
      display: inline-block;
      border: 4px solid #A2261E;
      border-radius: 5px;
      -moz-border-radius: 5px;
      -webkit-border-radius: 5px;
      background: #CC3126;
      display: inline-block;
      line-height: 100%;
      padding: 0.7em;
      text-decoration: none;
      color: #fff;
      width: 100px;
      line-height: 140%;
      font-size: 17px;
      font-family: open sans;
      font-weight: bold;
    }
    .reload:hover{
      background: #444;
    }
    .btn {
      width: 200px;
      color: rgb(255, 255, 255);
      border: 4px solid rgb(0, 0, 0);
      background: rgba(3, 3, 3, 0.75);
    }
    .clear {
      width: auto;
    }
    .btn:hover, .btn:hover {
      background: #444;
    }
    .btns {
      width: 410px;
      margin: 50px auto;
    }
    .credit {
      text-align: center;
      color: rgba(255,255,255,0.7);
      padding: 10px;
      width: 410px;
      clear: both;
    }
    .credit a {
      color: rgba(0,0,0,0.85);
      text-decoration: none;
      font-weight: bold;
      text-align: center;
    }
    
    .back {
      position: absolute;
      top: 0;
      left: 0;
      text-align: center;
      display: block;
      padding: 7px;
      width: 100%;
      box-sizing: border-box;
      -moz-box-sizing: border-box;
      -webkit-box-sizing: border-box;
      background: rgba(255, 255, 255, 0.25);
      font-weight: bold;
      font-size: 13px;
      color: #000;
      -webkit-transition: all 500ms ease-in-out;
      -moz-transition: all 500ms ease-in-out;
      -o-transition: all 500ms ease-in-out;
      transition: all 500ms ease-in-out;
    }
    .back:hover {
      color: black;
      background: rgba(255, 255, 255, 0.5);
    }
    
    header {
      position: relative;
      z-index: 10;
    }
    .main section .page_container {
      position: relative;
      top: 20%;
      margin: 0 auto 0;
      max-width: 950px;
      z-index: 3;
    }
    .main section  {
      overflow: hidden;
    }
    
    .main section > img {
      position: absolute;
      max-width: 100%;
      z-index: 1;
    }
    
    .main section.page1 {
        background:#d2efff url(run.jpg) ;
        min-height: 100%;
        min-width: 1024px;
      background-repeat:no-repeat;
      background-size: 100%;
    }
    .main section.page1 h1 {
      text-align: left;
      padding: 0;
      margin-bottom: 15px;
      font-size: 70px;
      color: white;
    }
    .main section.page1 h2 {
      color: rgba(255,255,255,0.85);
      text-align: center;
      width: 435px;
      line-height: 160%;
    }
    .main section .page_container .btns {
      clear: both;
      float: left;
      text-align: center;
      width: 435px;
    }
    .main section .page_container .btns a{
      text-align: center;
    }
    .main section.page2 {
      background: #d2efff url(harvard.jpg) no-repeat center -150px ;
    }
    .main section.page2 > img {
      position: absolute;
      top: -300px;
      left: 50%;
      margin-left: -1095px;
    }
    .main section.page2 .page_container {
      margin-top: -110px;
      overflow: hidden;
    }
    .main section.page2 h1 {
      text-align: center;
      padding: 0;
      margin-bottom: 15px;
      font-size: 50px;
      letter-spacing: -1px;
      color: black;
    }
    .main section.page2 h2 {
      color: rgba(255,255,255,0.85);
      text-align: center;
      line-height: 160%;
      font-weight: 100;
      color: black;

    }
    .viewing-page-2 .back{
      background: rgba(0, 0, 0, 0.25);
      color: #FFF;
      }
    .main section.page3 {
        background:url(hyard.png) #ffffff;
        min-height: 100%;
        min-width: 500px;
        background-repeat:no-repeat;
        background-size: 100%;
        background-position:100% 100%;
    }
    .main section.page3 .page_container {
      overflow: hidden;
      width: 80%;
      height: 75%;
      left: 0px;
      top: 5%;
    }
    .main section.page3 h1 {
      text-align: left;
      padding: 0;
      margin-bottom: 0;
      font-size: 50px;
      letter-spacing: -1px;
      color: black;
    }
    .main section.page3 h2 {
      color: rgba(0,0,0,0.85);
      text-align: left;
      line-height: 160%;
      font-weight: 100;
      font-size: 21px;
    }
  
  
  .main section.page4 {
      background:gray url(metwork.png) ;
              min-height: 100%;
              min-width: 500px;
              background-repeat:no-repeat;
              background-size: 50%;
              background-position:right;
  }
  .main section.page4 .page_container {
      overflow: hidden;
      width: 35%;
      left: -25%;
      top: 12%;
  }
  
  .main section.page4 h1 {
      text-align: left;
      padding: 0;
      margin-bottom: 0;
      font-size: 50px;
      letter-spacing: -1px;
      color: white;
  }
  .main section.page4 h2 {
      color: white;
      text-align: left;
      line-height: 160%;
      font-weight: 100;
      font-size: 21px;
  }
  
  
    body.disabled-onepage-scroll .onepage-wrapper  section {
      min-height: 100%;
      height: auto;
    }
    
    body.disabled-onepage-scroll .main section .page_container, body.disabled-onepage-scroll .main section.page3 .page_container  {
      padding: 20px;
      margin-top: 150px;
      -webkit-box-sizing: border-box;
      -moz-box-sizing: border-box;
      box-sizing: border-box;
    }
    
    body.disabled-onepage-scroll  section .page_container h1{
      text-align: center;
      font-size: 50px;
    }
    body.disabled-onepage-scroll section .page_container h2, body.disabled-onepage-scroll section .page_container .credit, body.disabled-onepage-scroll section .page_container .btns{
      text-align: center;
      width: 100%;
    }
    
    body.disabled-onepage-scroll .main section.page1 > img {
      position: absolute;
      width: 80%;
      left: 10%;
    }
    
    body.disabled-onepage-scroll .main section > img {
      position: relative;
      max-width: 80%;
      bottom: 0;
    }
    body.disabled-onepage-scroll code {
      width: 95%;
      margin: 0 auto 25px;
      float: none;
      overflow: hidden;
    }
    
    body.disabled-onepage-scroll .main section.page3 .page_container {
      width: 90%;
      margin-left: auto;
      margin-right: auto;
      right: 0;
    }
  
  
  
  .inputform {
      border-top-left-radius: 6px;
      border-top-right-radius: 6px;
      border-top: #0b0b0b solid 1px;
      background: rgba(20,20,20,0.6);
      width: 400px;
      height: 12px;
      display: block;
      padding-top: 14px;
      padding-bottom: 14px;
      border-radius: 6px;
      border: none;
      text-align: center;
      text-decoration: none;
      font-size: 15px;
      font-family: open sans;
      color: #FFF;
  }
  
  .inputform1 {
  border-top-left-radius: 6px;
  border-top-right-radius: 6px;
  border-top: #0b0b0b solid 1px;
  background: rgba(20,20,20,0.6);
  width: 100px;
  height: 12px;
  display: block;
  padding-top: 14px;
  padding-bottom: 14px;
  border-radius: 6px;
  border: none;
  text-align: center;
  text-decoration: none;
  font-size: 15px;
  font-family: open sans;
  color: #FFF;
  }
  .inputform:hover {
      background:  rgba(71,71,71,0.6);
  }
.inputform1:hover {
background:  rgba(71,71,71,0.6);
}



   table.equalDevide tr td { width:15%; }
  
  
  
  .unselectable {
      /* For Opera and <= IE9, we need to add unselectable="on" attribute onto each element */
      /* Check this site for more details: http://help.dottoro.com/lhwdpnva.php */
      -moz-user-select: none; /* These user-select properties are inheritable, used to prevent text selection */
      -webkit-user-select: none;
      -ms-user-select: none; /* From IE10 only */
      user-select: none; /* Not valid CSS yet, as of July 2012 */
      
      -webkit-user-drag: none; /* Prevents dragging of images/divs etc */
      user-drag: none;
  }

	</style>
	<script>
	  $(document).ready(function(){
      $(".main").onepage_scroll({
        sectionContainer: "section",
        responsiveFallback: 600,
        loop: true
      });
		});
        
        
        
		
	</script>
</head>
<body>
  <div class="wrapper">
	  <div class="main">
	    
      <section class="page1">
        <div class="page_container">
          <h1>have you <i>MET</i> your goal?</h1>
          <h2>Introducing MET: My Endurance Trainer.</h2>
          <p class="credit">Created by Andy Liu, Tracy Lu, and Felix Wong.</a></p>


  	    </div>
        
        
        <div class="btns" style="position:absolute;color:white; width:50%; bottom:5%; left:7%">
            
            <form id="myform" action="index.php" method="post">
                
                <table align="center">
                    <tr>
                        <td align="right" style="inputlabel"> spark id &nbsp; &nbsp; </td> <td> <input type="text" name="sparkid" class="inputform"></td>
                    </tr><tr>
                    
                        <td align="right" style="inputlabel"> access token &nbsp; &nbsp; </td> <td>  <input type="text" name="accesscode" class="inputform"></td>
                    </tr><tr>
                    
                    <td align="right" style="inputlabel"> goal avg rate &nbsp; &nbsp;
                    </td><td>
                    <input type="text" name="avgrate" class="inputform1" width="50px"></td>
                    </tr>
                </table>
<span style="font-size:8pt; width=350; line-height: normal"><i> Please enter your goal avg rate in the form '##.#.' and disregard this field the first 5 times you retrain MET.</i>   </span>
<p>
                <a class="reload btn" href="javascript: submitform()">retrain MET</a></span>
                
                
                
            </form>
            
            
            
        </div>




        
        <?php
            if( isset($_POST["sparkid"]) )
            {
              //echo $output;
        
                print "<div id=\"mydiv11\" class=\"page_container\" style=\"background-color:rgba(255,255,255,0.8); border:45px solid rgba(255,255,255,0); border-radius:25px; width:20%; top:-100px;\">Your MET is good to go!<p> Access some of your running info <a href=\"infopage.php?sid=".$_POST["sparkid"]."\">here</a>.</div>";
            }
            ?>




        
  	    <!---<img src="phones.png" alt="phones">--->
      </section>
	    
        <script>
        var fade_out = function() {
        $("#mydiv11").fadeOut().empty();
        }
        
        setTimeout(fade_out, 10000);
        </script>
        
        
        
	    <section class="page2">
            
           <!-- <div style="position:absolute; left:100px; top:50px"><img height="100px" src="bracelet1.jpg" alt="phones">
                </div>-->
            
            <div style="position:absolute; right:-200px"><img class="unselectable" src="runner.png" alt="phones">
                </div>
	      <div class="page_container">
              
          <h1>What is MET?</h1>
          <h2>MET is <i>your</i> endurance trainer. It helps <i>you</i> optimize <i>your</i> endurance training.
              

              
           <p>
              
          </h2>
          
          
          <img class="unselectable" src="people.png" style="left:-300px" height="100px">
          
          
          <div align="center">
        
             
              
              <div style="font-family:'open sans';font-size:16px;color:rgba(0,0,0,0.7); width:50%">
                  
                  
                  <p>
              MET gives you feedback on your <b>heart rate</b> and <b>pace</b> while it monitors your running. This lets you know when to take it easy or work harder during your routine.
              <p>
              
          </div>


<div style="font-family:'open sans';font-size:10px;color:rgba(0,0,0,0.7); width:80%">
    &nbsp;
    </div>


</div>
          
          <div align="center">
          <div style="font-family:'open sans';font-size:14px;color:rgba(0,0,0,0.7); width:80%">

              <table  cellpadding="0" cellspacing="0" width="100%" border="0">
                  <tr>
                      <td align="center" width="200"><img class="unselectable" src="touch.png" height="100px"></td>
                      <td align="center" width="100">&nbsp;&nbsp;&nbsp;</td>
                      <td align="center" width="200"><img class="unselectable" src="laptop.png" height="100px"> </td>
                      <td align="center" width="100">&nbsp;&nbsp;&nbsp;</td>
                      <td align="center" width="200"><img class="unselectable" src="graph.png" height="100px"> </td>
                  </tr>
                  <tr height="10">
                      </tr>
                  <tr>
                      <td align="center"valign="top" >Touch MET when you start and stop your routine. MET will give you soft blinks while it's on.</td>
                      <td align="center" width="100">&nbsp;&nbsp;&nbsp;</td>
                      
                      
                      <td align="center" width="200" valign="top">Tell us to help you optimize or reoptimize your routine by entering your credentials here after your workout. </td>
                      
                      <td align="center" width="100">&nbsp;&nbsp;&nbsp;</td>
                      
                      <td align="center" width="200" height="100" valign="top" >While you look at some nice statistics, MET automatically updates itself with the new optimized routine.  </td>
                  </tr>
              </table>
          </div>
          

</div>
      </section>
        
        
        
        <section class="page4">
 <div class="page_container">
<!--     <div style="position:absolute;"><img src="metwork.png"></div>-->

     
                <h1>How does it work?</h1>
                <h2><p>MET combines the portability of an IoT device with the accessibility of a cloud-based webapp. We have gone great lengths (pun intended) to do your training homework for you.
                    <p>
                    Our METEOR algorithm combines state-of-the-art regression models with machine learning. It takes care of everything while running on our server, so you can just focus on what you do best: <i>running</i>.
                    
                   
                    
                </h2>
                
     
                
          </div>
            
            <div style="position:absolute; bottom:-10px;left:-10px;height:110%; width:110%"> <img class="unselectable" src="data.png" style="height:100%; width:100%; opacity:0.1;"></div>
            
        </section>
        
        
        <script>
            var makeUnselectable = function( $target ) {
                $target
                .addClass( 'unselectable' ) // All these attributes are inheritable
                .attr( 'unselectable', 'on' ) // For IE9 - This property is not inherited, needs to be placed onto everything
                .attr( 'draggable', 'false' ) // For moz and webkit, although Firefox 16 ignores this when -moz-user-select: none; is set, it's like these properties are mutually exclusive, seems to be a bug.
                .on( 'dragstart', function() { return false; } );  // Needed since Firefox 16 seems to ingore the 'draggable' attribute we just applied above when '-moz-user-select: none' is applied to the CSS
                
                $target // Apply non-inheritable properties to the child elements
                .find( '*' )
                .attr( 'draggable', 'false' )
                .attr( 'unselectable', 'on' ); 
            };
            </script>
        
        
        
	    
	    <section class="page3">
       
           
           
            
            <div class="page_container" style="background-color:rgba(255,255,255,0.0); border:45px solid rgba(255,255,255,0);
                border-radius:25px; ">
    <div style="position:absolute; top:0px;right:0px"> <img class="unselectable" src="hcollege.png" height="50px">&nbsp;&nbsp;&nbsp;<img class="unselectable" src="harvard.png" height="50px"></div>
              
          <h1>Who are we?</h1>
          <h2>We are a team of three Harvard students dedicated to helping you achieve your running goals.
          
          <p>
          <p>
          <p>
          
          TEAM MET = Andy Liu +
          
         Tracy Lu +
          
          Felix Wong
<br>
(with additional guidance from the great <a style="color: #1b8bba" href="https://en.wikipedia.org/wiki/H._T._Kung">H. T. Kung</a>)
          
          </h2>
          
          <div class="page_container" style="background-color:rgba(255,255,255,0.8); border:25px solid rgba(255,255,255,0);
  ">
          
          <div align="left"><span style="font-size:15px; font-family:'open sans'; font-weight:lighter; font-color: #375c6c" align="left">
              Andy Liu is a junior in <font color="#ce4413">Winthrop House</font> studying <a href="http://www.seas.harvard.edu/"><font color="#1b8bba">Electrical Engineering</font></a>.
              <br>
              Tracy Lu is a senior in <font color="#ce4413">Pforzheimer House</font> studying <a href="http://www.seas.harvard.edu/"><font color="#1b8bba">Computer Science</font></a>.
              <br>
              Felix Wong is a senior in <font color="#ce4413">Winthrop House</font> studying <a href="http://www.math.harvard.edu/"><font color="#1b8bba">Mathematics</font></a>.
              <p>
              Contact us <a style="color: #1b8bba" href="mailto:met@hcs.harvard.edu"><b>here</b></a>.
          </span>
      
      <div align="center">
      <div style="top:90%;left:100%"> &nbsp;&nbsp;&nbsp;&nbsp;<img class="unselectable" src="team.png" height="100px">
<p>
</div>
      </div>
      
      </div>
      
      
      </div>
          
          </div>
    
    
 
  	    </div>








      </section>
        
        
    </div>
  </div>
</body>

<script type="text/javascript">
    function submitform()
    {
        document.forms["myform"].submit();
    }
</script>


</html>