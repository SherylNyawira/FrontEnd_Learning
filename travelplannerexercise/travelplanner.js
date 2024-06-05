document.getElementById('bookingForm').addEventListener('submit', function(e) {
    e.preventDefault();
    alert('Your travel has been booked!Thanks for booking with us.');
});

document.getElementById('contactForm').addEventListener('submit', function(e) {
    e.preventDefault();
    alert('Your message has been sent!');
});
document.getElementById('destination').addEventListener('change', function(e) {
    const destination = e.target.value;
    const detailsDiv = document.getElementById('details');

    let detailsHtml = '';

    switch(destination) {
        case 'mombasa':
            detailsHtml = `
                <label for="stay">Stay at:</label>
                <select id="stay" name="stay">
                    <option value="diani">Diani</option>
                    <option value="bamburi">Bamburi</option>
                </select>
                <p>Sceneries: Aquatic and Beaches</p>
            `;
            break;
        case 'nakuru':
            detailsHtml = `
                <p>Hotel: Sarova</p>
                <p>Activities: Seeing wild animals, Camping in the forest</p>
            `;
            break;
        case 'kisumu':
            detailsHtml = `
                <p>Activities: Viewing Lake Victoria, Eating fish</p>
            `;
            break;
        case 'nairobi':
            detailsHtml = `
                <p>Activities: Museum visit, Game park visit</p>
            `;
            break;
        case 'kirinyaga':
            detailsHtml = `
                <p>Activities: Viewing beautiful waterfalls, Hot air balloon rides</p>
            `;
            break;
        default:
            detailsHtml = '';
    }

    detailsDiv.innerHTML = detailsHtml;
});

function openModal(element) {
    var modal = document.getElementById("modal");
    var modalImg = document.getElementById("modalImage");
    var captionText = document.getElementById("caption");
    
    modal.style.display = "block";
    modalImg.src = element.querySelector("img").src;
    captionText.innerHTML = element.querySelector("p").innerHTML;
}

function closeModal() {
    var modal = document.getElementById("modal");
    modal.style.display = "none";
}
