const parks = ['Acadia National Park', 'Arches National Park', 'Badlands National Park', 'Big Bend National Park', 'Biscayne National Park', 'Black Canyon of the Gunnison National Park', 'Bryce Canyon National Park', 'Canyonlands National Park', 'Capitol Reef National Park', 'Carlsbad Caverns National Park', 'Channel Islands National Park', 'Clayton Co International Park, Jonesboro GA', 'Congaree National Park', 'Congaree National Park Wilderness', 'Crater Lake National Park', 'Cuyahoga Valley National Park', 'Death Valley National Park', 'Denali National Park', 'Dry Tortugas National Park', 'Everglades National Park', 'Fort Hunt National Park', 'Fort Pickens National Park', 'Gateway Arch National Park', 'Glacier Bay National Park', 'Glacier National Park', 'Grand Canyon National Park', 'Grand Teton National Park', 'Great Basin National Park', 'Great Sand Dunes National Park and Preserve', 'Great Smoky Mountains National Park', 'Guadalupe Mountains National Park', 'Haleakala National Park', 'Hawaii Volcanoes National Park', 'Hot Springs National Park', 'Indiana Dunes National Park', 'Isle Royale National Park', 'Joshua Tree National Park', 'Katmai National Park', 'Kenai Fjords National Park', 'Kings Canyon National Park', 'Lassen Volcanic National Park', 'Mammoth Cave National Park', 'Mesa Verde National Park', 'Mount Rainier National Park', 'North Cascades National Park', 'Olympic National Park', 'Petrified Forest National Park', 'Pinnacles National Park', 'Redwood National Park', 'Rocky Mountain National Park', 'Saguaro National Park', 'Sequoia National Park', 'Shenandoah National Park', 'Theodore Roosevelt National Park', 'Voyageurs National Park', 'Wind Cave National Park', 'Wolf Trap National Park for the Performing Arts', 'Yellowstone National Park', 'Yosemite National Park', 'Zion National Park']

    const button = document.querySelector('#park-container');
    for (const park of parks) {
        button.insertAdjacentHTML('beforeend', `<li><a href="/parks/${park}">${park}</a></li>`);

    }

    function showParks(evt){
        evt.preventDefult();
        const state=document.querySelector('select[name="state]').value;
        fetch(`/parks_js?state=${state}`)
        .then(response => response.joson())
        .then(jsonData => {
            document.querySelector('#park-container').innerHTML=jsonData;
        });
    }
    document.querySelector('#state_form').addEventListener('submit', showParks)

