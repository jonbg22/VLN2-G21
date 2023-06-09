$(document).ready(function () {
    function updatePizzas() {
        console.log("FIRED");
        const searchInput = $('#pizza-search-input').val();
        const filterVal = $('input[name="category"]:checked').val();
        const orderByVal = $('#pizza-orderby-selector').find(':selected').val()
        const orderByDir = $('input[name="orderdir"]:checked').val();
        console.log("Search = " + searchInput)
        console.log("Filter = " + filterVal)
        console.log("Order = " + orderByVal + " " + orderByDir)


        let url = `/menu/pizzas?search=${searchInput}&filter=${filterVal ? filterVal : ""}&orderBy=${orderByVal}&orderDir=${orderByDir}`
        console.log("URL = " + url)
        $.ajax({
            url: url,
            type: 'GET',
            success: function (resp) {
                const newHTML = resp.data.map(d => {
                    let prod = JSON.parse(d.prod)[0].fields;
                    console.log(prod);
                    return `<div class="product" data-id="${d.prod_id}">
                            <a href="/menu/pizzas/${d.prod_id}">
                                <img class="product-img" src="${prod.imgLink}">
                                <h2 class="product-name">${prod.name}</h2>
                                <hr class="product-line">
                                <p class="product-price">$${Math.round(prod.price)}</p>
                            </a>
                            </div>`
                });
                $('#pizzas').html(newHTML.join(''));
                console.log(newHTML);
                $('#pizza-search-input').val('');
            },
            error: function (xhr, status,error) {
                console.error(error);
            }

        });
    }


    $('#pizza-search-btn').click(updatePizzas)
    $('.filter').click(updatePizzas);
    $('.orderdir').click(updatePizzas);
    $('#pizza-orderby-selector').on('input',updatePizzas);


});