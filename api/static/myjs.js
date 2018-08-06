function myRequest(){
    document.getElementById('form1').style.display="block";       
}
function check_empty() {
  if (document.getElementById('name').value == "" || document.getElementById('email').value == "" || document.getElementById('message').value == "") {
        alert("Fill All Fields !");
    } else {
    document.getElementById('form').submit();
    alert("Form Submitted Successfully...");
    }
}
//Function to Hide Popup
function div_hide(){
    document.getElementById('form1').style.display = "none";  
} 
function div_hide1(){
    document.getElementById('content').style.display = "none";
}
/* content display */

function myContent(){
    document.getElementById('content').style.display="block";
    
}

/*---Searchbar--*/
function mySearch1(){
    document.getElementById('search').style.display = "none";
}
function mySearch(){
    document.getElementById('search').style.display = "block";
}
function myFunction(){
    var input, filter, ul, i, li;
    input = document.getElementById('search');
    filter = input.value.toUpperCase();
    ul= document.getElementById('notify');
    li = ul.getElementsByTagName('li')

    for(i =0; i<li.length; i++){
        a = li[i].getElementsByTagName("a")[0];
        if(a.innerHTML.toUpperCase().indexOf(filter)>-1){
            li[i].style.display = "";
        }
        else{
            li[i].style.display = "none";
        }
    }

}


/*make new request form*/







