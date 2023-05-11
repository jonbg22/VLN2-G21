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
            $('.cart-item').each(function (ind) {
                if (parseInt($(this).attr("data-id")) === itemID) {
                    if (all) {
                        $(this).remove();
                    } else {
                        const counter = $(this).children('.product-counter').children('.product-count');
                        counter.text(parseInt(counter.text())-1);
                    }
                }
                if ($('.cart-items').html === "") {
                    $('.cart-items').html('<h3>Cart is empty</h3>');
                }
            })

        }
    })
}

const incrementItem = async (dir, itemID,prodID) => {
    if (dir === "+") {
        await addToCart(prodID);
        $('.cart-item').each(function (ind) {
            if (parseInt($(this).attr("data-id")) === itemID) {
                const counter = $(this).children('.product-counter').children('.product-count');
                counter.text(parseInt(counter.text())+1);
            }
        })

    } else if (dir === "-") {
        deleteItem(itemID,false);
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