var chatBody = document.getElementById("chat-body");
var sendMsg=document.getElementById("send-msg");
var inputField=document.getElementById("msg");

function  onEnter(){
	
	 if(event.which == 13 || event.keyCode == 13)
	 	createReply();
};

function createReply(){

	var msg = document.getElementById("msg").value;
	if (msg.length>0){
		document.getElementById("msg").value="";

		var request = new XMLHttpRequest();
		renderUserMsg(msg);
		var url='http://127.0.0.1:8000/chat'+'?q='+encodeURIComponent(msg);
		request.open('GET',url,);
		request.onload=function(){
			var reply=request.responseText;
			/*console.log(reply);*/
		renderBotMsg(reply);

		}

		request.send(); 	
	}
}

sendMsg.addEventListener("click",createReply);



function renderBotMsg(msg){

		htmlString="";
		htmlString+="<div id='kk' class=\"chat-box-left\">";
		htmlString+=msg+"</div>";
		htmlString+="<div class=\"chat-box-name-left\">"+" -  StackExchange Bot"+"</div>";
		htmlString+=" <hr class=\"hr-clas\" />";

	chatBody.insertAdjacentHTML('beforeend',htmlString);
	chatBody.scrollTop = chatBody.scrollHeight;

}


function renderUserMsg(msg){

	htmlString="";
		htmlString+="<div class=\"chat-box-right\">";
		htmlString+=msg+"</div>";
		htmlString+="<div class=\"chat-box-name-right\">"+"- you"+"</div>";
		htmlString+=" <hr class=\"hr-clas\" />";

	chatBody.insertAdjacentHTML('beforeend',htmlString);
	chatBody.scrollTop = chatBody.scrollHeight;
}




