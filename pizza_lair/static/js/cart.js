const addToCart = async (id) => {
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    await fetch("/cart/addToCart", {
        method: "POST",
        headers: {
            'X-CSRFToken': csrftoken,
            'Content-Type': 'application/json'},
        mode: 'same-origin', // Do not send CSRF token to another domain.
        body: JSON.stringify({ id })
    })
}

const getCookie = (name) => {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const clearSession = async() => {
    const csrftoken = getCookie("csrftoken");
    $.ajax('/cart/addToCart', {
        method: "DELETE",
        headers: {
         'X-CSRFToken': csrftoken,
        },
        success: ()=> {
            console.log("Cleared Session");
            $('.cart-items').html('<h3>Cart is empty</h3>');

        }
    })
}

const deleteItem = (itemID) => {

}

$('#clear-cart-btn').click(clearSession);