fetch('http://127.0.0.1:8000/api/blog/')
    .then(res => res.json())
    .then(data => {
        data.filter(blog => !blog.is_deleted).map(blog => createCard(blog))
    });


const cards = document.querySelector('.row');

function createCard(blog){
    const cardDiv = 
    `<div class="col-lg-4 col-md-6 col-sm-12 mb-4">
        <div class="card" style="width: 100%;">
            <img src="${blog.banner}" class="card-img-top">
            <div class="card-body">
                <h5 class="card-title">${blog.title}</h5>
                <p class="card-text">${blog.description}</p>
                <a href="#" class="btn btn-primary">Detail</a>
            </div>
        </div>
    </div>`
    cards.innerHTML += cardDiv;
}