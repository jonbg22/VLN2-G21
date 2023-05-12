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
    $.ajax('/cart/clearCart', {
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

const deleteItem = (itemID, all = true) => {
    const csrftoken = getCookie("csrftoken");
    $.ajax('/cart/delCart/'+itemID+"?all="+all, {
        method: "DELETE",
        headers: {
         'X-CSRFToken': csrftoken,
        },
        success: ()=> {
            console.log("Deleting Item");
            $('.cart-offer-wrapper').each(function () {
                if (parseInt($(this).children('.cart-item-offer').attr("data-id")) === itemID) {
                    $(this).remove()
                }
            })
            $('.cart-item').each(function (ind) {
                if (parseInt($(this).attr("data-id")) === itemID) {
                    if (all) {
                        $(this).remove();
                    } else {
                        const counter = $(this).children('.product-counter').children('.product-count');
                        if (parseInt(counter.text()) > 1) counter.text(parseInt(counter.text())-1);
                        else if (parseInt(counter.text()) === 1) $(this).remove();
                    }
                }
                if ($('.cart-item').length === 0 && $('.cart-item-offer').length === 0 ) {
                    $('.cart-items').html('<h3>Cart is empty</h3>');
                }
            })

        }
    })
}


const incrementPrice = (element, modifier) => {
    const totalPrice = $(element).children('.product-price-container').children('.product-total-price');
    const singlePrice = $(element).children('.product-price-container').children('.product-single-price');
    const cartPrice = $('.cart-total-price')
    console.log("TOTAL: " + parseFloat(totalPrice.text()))
    console.log("SINGLE: " + parseFloat(singlePrice.text()))
    if (modifier === "-") {
        totalPrice.text(parseFloat((totalPrice.text())) - parseFloat(singlePrice.text()));
        cartPrice.text(parseFloat(cartPrice.text()) - parseFloat(singlePrice.text()));

    }
    else if (modifier === "+") {
        totalPrice.text(parseFloat((totalPrice.text())) + parseFloat(singlePrice.text()));
        cartPrice.text(parseFloat(cartPrice.text()) + parseFloat(singlePrice.text()))
    }
}




const incrementItem = async (dir, itemID,prodID) => {
    if (dir === "+") {
        await addToCart(prodID);
        $('.cart-item').each(function (ind) {
            if (parseInt($(this).attr("data-id")) === itemID) {
                const counter = $(this).children('.product-counter').children('.product-count');
                counter.text(parseInt(counter.text())+1);
                incrementPrice(this, "+")
            }
        })

    } else if (dir === "-") {
        deleteItem(itemID,false);
        $('.cart-item').each(function (ind) {
            if (parseInt($(this).attr("data-id")) === itemID) {
                incrementPrice(this, "-")
            }
        })
    }
}

$('#clear-cart-btn').click(clearSession);


$('.expand-details').click(function () {
    $(this).toggleClass("active");

    if ($(this).hasClass("active")) {
        $(this).text("Details ▲")
    } else {
        $(this).text("Details ▼")
    }
    $(this).parent().next().toggle();
})