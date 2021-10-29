

console.log("hello buddy");

var btn = document.getElementsByClassName("update-cart")

for(var i=0; i<btn.length; i++){
    btn[i].addEventListener("click", function () {
        var productId = this.dataset.product;
        var action = this.dataset.action;
        console.log(productId, action)        
        if(user=="AnonymousUser"){
        console.log("Go to login page bro...")
        }
        else{
            updatecart(productId, action)
        }
    })
}

function updatecart(productId, action) {     
    console.log("Thanks for click");
    console.log(productId, action);

    var url='/update_item/'
    fetch(url, {
        method:"POST",
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,

        },
        body:JSON.stringify({'productId':productId, 'action':action})
    })
    .then((response)=>{
        return response.json()
    })
    .then((data)=>{
        console.log(data);
        location.reload()
    });
}


