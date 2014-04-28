<!doctype html>
<html>
<head>
<link href='http://fonts.googleapis.com/css?family=Open+Sans:300,400,700 ' rel='stylesheet' type='text/css'>
<style>
html {
    height: 100%;
    }
body {
    background: gray url(datatrans.png);
    min-height: 100%;
    min-width: 1024px;
    background-repeat:no-repeat;
    background-size: 100%;
    background-attachment: fixed;
    padding: 0;
    text-align: center;
    font-family: 'open sans';
    position: relative;
    margin: 0;
    height: 100%;
    -webkit-font-smoothing: antialiased;
    color: white
    }
.imcl {
    height:auto;
    width:auto; max-width:500px;
    z-index: 10;
  }
img {
    -webkit-filter: invert(100%);
}
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
</head>


<body>

<p>&nbsp;
<p>
<span style="font-size:20px; top:100px">Your MET is good to go! Here are some of the quantitative data we've taken:</span>
<p><p>
<img class="imcl" src="data/<?php echo $_GET["sid"]; ?>/histogram.png">
<img  class="imcl" src="data/51ff66065067545736270187/hrar_fit.png">
<img  class="imcl" src="data/51ff66065067545736270187/hrrr_fit.png">
<img  class="imcl" src="data/51ff66065067545736270187/rrar_fit.png">
<img  class="imcl" src="data/51ff66065067545736270187/tiar_fit.png">
<img  class="imcl" src="data/51ff66065067545736270187/tihr.png">


</body>
</html>