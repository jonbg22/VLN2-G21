const addToCart = async (id) => {
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    await fetch("/menu/addToCart", {
        method: "POST",
        headers: {
            'X-CSRFToken': csrftoken,
            'Content-Type': 'application/json'},
        mode: 'same-origin', // Do not send CSRF token to another domain.
        body: JSON.stringify({ id })
    })
    console.log(sessionStorage.getItem("cart"))
}

const clearSession = async() => {
    await fetch("/menu/addToCart");
    console.log("Cleared Session");
}