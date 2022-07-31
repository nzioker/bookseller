const addToCartBtns = document.getElementsByClassName("add_to_cart_button");

for(i = 0; i < addToCartBtns.length; i++){
    
    addToCartBtns[i].addEventListener('click', function(){
        const productId = this.dataset.product_id
        const action = this.dataset.action
        console.log('Product Id:', productId, 'Action:', action)
        console.log('User:', user)

        if(user === 'AnonymousUser'){
            console.log('Not logged in')
        }
        else{
            sendUserData(productId, action)
        }
        
        function sendUserData(productId, action){
            const url = '/update_item/'

            fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrftoken,
                },
                body: JSON.stringify({'productId':productId, 'action':action})
            })
            .then((response) =>{
                return response.json()
            })
            .then((data) =>{
                console.log('data:',data)
                location.reload()
            })
        }
        
    });
}



