'use strict';

document.querySelector('#id').style.display = 'none';

function submitRating (evt) {
    evt.preventDefault();
    
    const ratings = document.querySelector('#rating').value;
    if (!ratings) {
        alert("Please select a rating.")
    }else{

    const data = {        
        rating: document.querySelector('#rating').value,
        comment: document.querySelector('#comment').value,
        trail_id: document.querySelector('#id').innerText
    };

    fetch('/rating.json', {
        method: 'POST',
        body: JSON.stringify(data),
        headers: {
            'Content-Type': 'application/json'
        },
    })
    .then(response => response.json())
    .then(jsonData => {
        document.querySelector('#user_rating')
        .insertAdjacentHTML('beforebegin', `<li>User Rating: ${jsonData.rating}</li> <li>User Comment: ${jsonData.comment}</li>`);

        alert(`You rate this trail ${jsonData.rating} out of 5.0!`);
    });

    }     

}
document.querySelector('#rating_form').addEventListener('submit', submitRating);
        
