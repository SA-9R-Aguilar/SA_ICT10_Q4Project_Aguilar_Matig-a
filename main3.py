from pyscript import document

#photo content to be used in the loop below
photos = [
    {
        "image": "images/TEACHER.jpg",
        "caption": "10-Ruby Teacher's Day Celebration"
    },

    {
        "image": "images/FOOD.jpg",
        "caption": "10-Ruby Food Fair"
    },

    {
        "image": "images/CHRISTMAS.jpg",
        "caption": "10-Ruby Christmas Party"
    },

    {
        "image": "images/PEACE.jpg",
        "caption": "Peace Project Presentation"
    },

    {
        "image": "images/INTRAMS.jpg",
        "caption": "Intramurals"
    },

    {
        "image": "images/CAT.jpg",
        "caption": "CAT Graduation"
    }
    
]

gallery = document.getElementById("gallery")

#HTML code in Python to be sent to HTML to display contents
for photo in photos:

    gallery.innerHTML += f"""

    <div class="col-md-4">

        <div class="card h-100 shadow">

            <img src="{photo['image']}" 
                 class="card-img-top img-fluid"
                 style="height:250px; object-fit:cover;">

            <div class="card-body">

                <p class="card-text text-center">
                    {photo['caption']}
                </p>

            </div>

        </div>

    </div>
    """

    # for project