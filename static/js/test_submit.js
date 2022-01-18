    document.querySelector('#rat').addEventListener('submit', (evt) => {
        evt.preventDefault();
        let rat=document.querySelector('#rat').value;
        document.querySelector('#rating_list').insertAdjacentHTML('beforeend', `<li>${rat}</li>`);
});