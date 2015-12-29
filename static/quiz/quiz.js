function print1(elementId) {
   var ifr = document.getElementById(elementId);
   //alert('ok');

   //Wait until PDF is ready to print    
   if (typeof ifr.print === 'undefined') {  
	   alert('undefind');
       setTimeout(function(){print1(elementId);}, 1000);
   } else {
	   alert('print');
       ifr.print();
   }
   
   
   //getMyFrame.src=url;
   //getMyFrame.focus();
   //alert('focus');
   //getMyFrame.contentWindow.print();
   //alert(getMyFrame);
}


function saveBaiThi(){
	
	//alert(window.location.href);
	window.location.href = window.location.href+"save/";
}

function finishBaiThi(){
	
	//alert(window.location.href);
	var newURL = window.location.href + "finish/";
	alert(newURL);
	window.location.href = newURL;
}