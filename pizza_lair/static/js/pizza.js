$(document).ready(function () {
    function updatePizzas() {
        console.log("FIRED");
        const searchInput = $('#pizza-search-input').val();
        const filterVal = $('input[name="category"]:checked').val();
        const orderByVal = $('#pizza-orderby-selector').find(':selected').val()
        const orderByDir = $('input[name="orderdir"]:checked').val();

        let url = `/menu/pizzas?search=${searchInput}&filter=${filterVal}&orderBy=${orderByVal}&orderDir=${orderByDir}`

        $.ajax({
            url: url,
            type: 'GET',
            success: function (resp) {
                const newHTML = resp.data.map(d => {
                    let prod = JSON.parse(d.prod)[0].fields;
                    return `<div class="pizza" data-id="${prod.id}">
                        <a href="/menu/pizzas/${prod.id}">
                        <img class="pizza-img" src="${prod.imgLink}">
                        <h2 class="pizza-name">${prod.name}</h2>
                        <hr class="pizza-line">
                        <p class="pizza-price">$${Math.round(prod.price)}</p>
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

    $('.filter').click(function(e) {
        console.log(e.target.value);
    })

});