
$(document).ready(function() {
   
    let deleteBtn = $('.delete-btn');
    let searchBtn = $('#search-btn');
    let searchForm = $('#search-form');

    $(deleteBtn).on('click', function(e) {

        e.preventDefault();
        
        let delLink = $(this).attr('href');
        let result = confirm('Deseja realmente excluir esse usuário?');

        if (result) {
            window.location.href = delLink;
        }
    });

    $(searchBtn).on('click', function() {
        searchForm.submit();
    });
});
